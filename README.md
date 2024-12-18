## About
This Python Script:

- Continuously observes the clipboard to identify cryptocurrency wallet addresses.
- Substitutes any found wallet addresses with a fabricated one.
- Emulates the approach clipboard hijackers use to manipulate clipboard content.
- Note: Actual malware in real scenarios is far more intricate and elusive. This serves only as a simplified example.

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

- Consistently review what’s on your clipboard before inserting sensitive information.
- Employ security utilities or clipboard monitoring tools that alert you to unanticipated modifications.
- Maintain updated systems and rely on reputable antivirus solutions.

## [!]Educational Focus

This proof of concept aims to educate cybersecurity enthusiasts and developers about clipboard hijacking techniques. It highlights the critical importance of input validation and promoting user vigilance.
