import argparse
import asyncio
from pathlib import Path
from groq import AsyncGroq
from datetime import datetime

# Argument Parser for CLI Usage
parser = argparse.ArgumentParser(description="A linguistic comparison and information mapping tool for text files.")
parser.add_argument("anonymous", type=str, help="Text file containing the anonymous statements.")
parser.add_argument("suspects", type=str, nargs="+", help="Text files containing the suspects' statements.")
args = parser.parse_args()

# File Paths
anonymous_file = Path(args.anonymous)
suspect_files = [Path(suspect) for suspect in args.suspects]

# Generate an output file name based on the current date and time
output_filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
output_file = Path(output_filename)

# Load system message from a file
def load_system_message(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

#//////////////////////////////////// API CONFIGURATION ///////////////////////////////////////

# Initialize the API Client
client = AsyncGroq(api_key="None")  # Replace `None` with your API key or fetch from an environment variable.

# Asynchronous function to interact with the API
async def fetch_chat_completion(system_message: str, user_message: str, model: str) -> str:
    chat_completion = await client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},  
            {"role": "user", "content": user_message}       
        ],
        model=model,
        temperature=0 
    )
    return chat_completion.choices[0].message.content

# Compare texts using the system message
async def compare_texts(anonymous_content: str, suspect_content: str, system_message: str) -> str:
    user_message = f"Anonymous: {anonymous_content}\nSuspect: {suspect_content}"
    return await fetch_chat_completion(system_message, user_message, "llama3-8b-8192")

#//////////////////////////////////////////////////////////////////////////////////////////////////

async def main() -> None:
    # Load the system message
    system_message = load_system_message("system_message.txt")

    # Read the contents of the anonymous file
    with open(anonymous_file, "r", encoding="utf-8") as file:
        anonymous_content = file.read()

    # Read the contents of each suspect file
    suspect_contents = []
    for suspect_file in suspect_files:
        with open(suspect_file, "r", encoding="utf-8") as file:
            suspect_contents.append(file.read())

    # Compare the anonymous file with each suspect file asynchronously
    comparison_results = await asyncio.gather(
        *[compare_texts(anonymous_content, suspect_content, system_message) 
          for suspect_content in suspect_contents]
    )

    # Write results to the output file
    with open(output_file, "w", encoding="utf-8") as output:
        for i, result in enumerate(comparison_results, 1):
            output.write(f"Comparison with suspect {i}: {result.strip()}\n")

    print(f"Results saved to {output_file}")

#//////////////////////////////////////////////////////////////////////////////////////////////////

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
