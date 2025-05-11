
## YTConverter™
---
`YTConverter™` is a Python-based project developed by [kaifcodec](https://github.com/kaifcodec) designed to provide a robust tool for converting YouTube videos into various formats. This tool simplifies the process of downloading and converting videos from YouTube.

---
![IMG-20250423-WA0001](https://github.com/user-attachments/assets/ef43f4b4-0afa-4682-8c4d-7d19200a40f7)

<p align="centre">
  
  <img src="https://github.com/user-attachments/assets/3f50727f-0927-4b3b-82fa-729c346e66d1" width="600" height ="500" />
</p>

---

## Requirements
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation (Termux/LinuxOs)

### For Termux:
1. Install Python and update Termux:
   ```bash
   pkg update -y && pkg upgrade -y && pkg install python
   ```
2. Install Git:
   ```bash
   pkg install git
   ```
3. Install Curl:
   ```bash
   pkg install curl
   ```
4. Clone the repository:
   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   ```
5. Give storage permission:
   ```bash
   termux-setup-storage
   ```
6. Navigate to the project directory:
   ```bash
   cd ytconverter
   ```
7. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### For Linux (Ubuntu/Debian/Fedora/Arch):
1. Install Python:
   ```bash
   sudo apt update && sudo apt install python3 python3-pip -y  # For Debian/Ubuntu
   # OR
   sudo dnf install python3 python3-pip  # For Fedora
   # OR
   sudo pacman -S python python-pip  # For Arch
   ```
2. Install Git and Curl:
   ```bash
   sudo apt install git curl -y  # Debian/Ubuntu
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   cd ytconverter
   ```
4. Install required Python libraries:
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage
1. Run the main script to start the conversion process:
   ```bash
   python ytconverter.py
   ```
2. Follow the on-screen instructions to input the YouTube URL and choose the desired output format.

## Tested on
- Linux
- Termux
- Ubuntu
- MacOs

---
 <p align="left">
<img src= "https://github.com/user-attachments/assets/8e9d00ce-b698-4b1f-8870-badd5d274442" width="600" height="600"/>
</p>

---

<p align="center">
  <b>Click on the image below to Watch the demo and installation on YouTube</b>
  <a href="https://youtu.be/W2Evqs3fqHs" target="_blank">
    <img src="https://img.youtube.com/vi/W2Evqs3fqHs/hqdefault.jpg" alt="Watch the demo" style="max-width: 100%;">
  </a>
</p>

<p align="center">
  
</p>


---

## Contact for any error or issue:
- kaifcodec@gmail.com

## Features
- **Video Downloading**: Fetch videos directly from YouTube.
- **Format Conversion**: Convert downloaded videos into different formats such as MP3, MP4, etc.
- **Metadata Handling**: Extract and manage metadata associated with YouTube videos.

---



## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## Disclaimer ⚠⚠
 - **We do ask you for your Name and Contact information in the beginning of the tool for update related notices but if you don't want to disclose those creds you can leave those fields blank**
 - **We also collect some basic informations about the usage statistics and user Public IP but we assure you that these datas are not kept more than 48 hours**
 - **We respect your privacy. Any basic info this tool collects (like usage data) is handled securely and never shared. No creepy tracking—just good software.**
 - _Thank you 🌹🌹_ _Keep supporting ❤❤_

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please open an issue or contact [kaifcodec](https://github.com/kaifcodec).


---
