# Backdoor for Windows using Python

This project is a Python-based backdoor script that establishes a reverse shell connection to a target Windows machine, allowing remote command execution. It facilitates file transfers, keylogging, and screenshot capture, making it a comprehensive tool for remote administration and security testing.

## Features

- **Reverse Shell Access** – Execute commands on the target Windows machine remotely.
- **File Transfer** – Upload and download files between the attacker and target machines.
- **Keylogger** – Capture keystrokes on the target machine to monitor user activity.
- **Screenshot Capture** – Take screenshots of the target system's desktop environment.

## Disclaimer

**This project is intended for educational purposes and authorized security testing only.** Unauthorized use of this tool on systems without explicit permission is illegal and unethical. The author is not responsible for any misuse or damage caused by this project.

## Prerequisites

- **Python 3.x** – Ensure Python is installed on both the attacker and target machines.
- **Required Libraries** – Install necessary Python libraries:
  ```bash
  pip install -r requirements.txt
  ```

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/pranav9087/backdoor-for-windows-using-python.git
cd backdoor-for-windows-using-python
```

### 2. Configure the Backdoor
- Modify the `backdoor.py` script to include the attacker's IP address and desired port number.

### 3. Deploy the Backdoor on Target Machine
- Transfer the `backdoor.py` script to the target Windows machine.
- Optionally, compile the Python script into an executable using PyInstaller:
  ```bash
  pyinstaller --onefile backdoor.py
  ```

### 4. Start the Server on Attacker Machine
- Run the `server.py` script to listen for incoming connections:
  ```bash
  python server.py
  ```

### 5. Execute the Backdoor on Target Machine
- Run the `backdoor.py` script (or the compiled executable) on the target machine to establish the connection.

### 6. Available Commands
- Once connected, type `help` in the attacker's terminal to view all available commands, including:
  - **File Transfer** – Upload or download files.
  - **Keylogging** – Start or stop the keylogger.
  - **Screenshot** – Capture screenshots.

## Security Considerations

- **Antivirus Detection** – Antivirus software may detect and block the backdoor. Use obfuscation techniques if necessary and ensure you have authorization to test the target system.
- **Network Configuration** – Make sure firewalls and network configurations allow the reverse shell connection on the specified port.

## Contributing

Contributions to enhance the functionality or security of this project are welcome. Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request for review.

