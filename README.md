## About
This Python script:

- Continuously monitors the clipboard.
- Detects cryptocurrency wallet addresses in the clipboard.
- Replaces any detected wallet address with a fake one, mimicking the method used by malicious clipboard hijackers.

## Setup

To run PoC, follow the steps below:

### 1. Clone the Repository

`git clone https://github.com/koseogluemre/clipboard-hijacking.git`

`cd clipboard-hijacking`

### 2. Install Required Lib.

Before running the script, you need to install the required Python libraries. Use the following command to install the dependencies:

`pip install pywin32`

### 3. Run the Script

`python clip.py`

## [?]How to Stay Safe

- Regularly check your clipboard before pasting sensitive information.
- Use security tools or clipboard monitoring software to detect unexpected changes.
- Keep your systems updated and use trusted antivirus programs.

## [!]Educational Focus

This example is meant to teach cybersecurity enthusiasts and developers about how clipboard hijacking works. It focuses on the importance of checking input and staying alert.
