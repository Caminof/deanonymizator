# DEANONYMIZATOR

DEANONYMIZATOR is an AI-powered tool designed to compare statements from an anonymous user with a list of suspects. It performs linguistic analysis and information mapping to help identify potential matches. The tool leverages free access to Large Language Models (LLMs) provided by Groq.

### Inspiration
This project is inspired by the real-life story of "OxyMonster," where linguistic analysis of statements made on deep web forums and Twitter was instrumental in confirming an individual's identity.

---

### Requirements
To run DEANONYMIZATOR, ensure you have the following dependencies installed:

- **Python 3.8 or later**
- **Required Libraries** (installable via `pip`):
  - `argparse`: For parsing command-line arguments
  - `asyncio`: To manage asynchronous operations
  - `pathlib`: For handling file paths
  - `datetime`: To generate timestamped output filenames
  - `groq`: To interact with the Groq API

---

### Setup and Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/DEANONYMIZATOR.git
   cd DEANONYMIZATOR
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key for Groq:
   - Add your Groq API key to your environment variables or configure it in the script directly.

---

### Usage
DEANONYMIZATOR can be run directly from the command line. The script requires the following inputs:

1. A text file containing the statements of the anonymous user.
2. One or more text files containing statements from the suspects.

#### Example Command:
```bash
python deanonymizator.py anonymous.txt suspect1.txt suspect2.txt
```

#### Output:
The tool generates an output file named with a timestamp, such as `output_20241222_130000.txt`, containing the results of the comparisons.

---

### Contributing
Contributions are welcome! Please create an issue or pull request to suggest changes or report bugs.

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

