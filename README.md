## YTConverter™
<p align="center">
  <img src="https://img.shields.io/badge/Version-4.0.1-blueviolet?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/forks/kaifcodec/ytconverter?style=for-the-badge&logo=git" />
  <img src="https://img.shields.io/github/stars/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/github/issues/kaifcodec/ytconverter?style=for-the-badge&logo=github" />
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/pypi/dm/ytconverter?label=PyPI%20Downloads&color=blue&logo=pypi" />
  <img src="https://static.pepy.tech/badge/ytconverter?left_color=black&right_color=brightgreen" />
</p>

---
> **Preface (optional):** A subtle reflection before diving into the technical details, feel free to skip to main content.

|                                                                 |
|-----------------------------------------------------------------|
| **❓ Born from silent hands, shaping what they cannot fully feel.** |
| **❓ Weighted and left alone, with no hand to guide through the quiet.** |
| **❓ Moving the world’s sound, while never feeling its pulse.** |
| <sub>— Author: 401</sub> |
---
`YTConverter™` is a Python-based project developed by [kaifcodec](https://github.com/kaifcodec) designed to provide a robust tool for converting YouTube videos into various formats. This tool simplifies the process of downloading and converting videos from YouTube.


---
![file_000000006dfc61fb9c9a2cb865da0157](https://github.com/user-attachments/assets/eadca26f-79a7-4233-90dd-1c850f50a8cc)
---

Check the screenshots below👇


<!--- <p align="centre">
  
  <img src="https://github.com/user-attachments/assets/3f50727f-0927-4b3b-82fa-729c346e66d1" width="600" height ="500" />
</p> --->

---

## Requirements
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)
- ffmpeg & yt-dlp binary

## Install pypi Package (For Any)
---
- You can clone the repository or manually install `ffmpeg` by following no.2 commands 👇 
1. Clone the repository and auto-setup the required binaries by running `install.sh`

   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   cd ytconverter/standalone/
   ./install.sh
   ```
- Or else you can manually install `ffmpeg` by following below commands and ignore the repository cloning.
<!--- 1. Or manually instll ffmpeg
   ```bash
   sudo apt install ffmpeg # For Linux
   ```
   ```bash
   pkg install ffmpeg # For Termux
   ``` 
- After installing ffmpeg binary follow the below instructions
   ```bash
   ./standalone/install.sh # Only for Linux-like & Termux users
   ``` --->
  2. If `install.sh` fails try installing ffmpeg manually by following below commands

      ```bash
      sudo apt install ffmpeg # For Linux
      ```
      ```bash
      pkg install ffmpeg # For Termux
      ```
3. After completion of setup install ytconverter pypi package and run

   ```bash
   pip install ytconverter
   ytconverter -S
   ```
- ⚠️ You need to manually install ffmpeg for windows or you can try `standalone/install.bat`

---   
- ⚠️ However usage of standalone ytconverter.py is recommended⚠️
- Pypi package still in beta, Follow the below process 👇👇
---
### Installation For Linux (Ubuntu/Debian/Fedora/Arch):
1. Install Python:
   ```bash
   sudo apt update && sudo apt install python3 python3-pip -y  # For Debian/Ubuntu
  
   sudo dnf install python3 python3-pip  # For Fedora
  
   sudo pacman -S python python-pip  # For Arch
   ```
2. Install Git and Curl:
   ```bash
   sudo apt install git -y  # Debian/Ubuntu
   ```
3. Clone the repository:
   ```bash
   git clone https://github.com/kaifcodec/ytconverter.git
   cd ytconverter/standalone/
   ```
4. Install required Python libraries:
   ```bash
   pip3 install -r requirements.txt
   ```
## Installation (Termux/Linux-distros)
```bash
# Update Termux and install Python
pkg update -y && pkg upgrade -y && pkg install python

# Install Git and Curl
pkg install git

# Clone the repository
git clone https://github.com/kaifcodec/ytconverter.git

# Grant storage permission
termux-setup-storage

# Navigate to the project directory
cd ytconverter/standalone/

# Install dependencies
pip install -r requirements.txt
```

## Installation (Windows)

1. Download or clone the repository:

   ```powershell
   git clone https://github.com/kaifcodec/ytconverter.git
   cd ytconverter/standalone/
2. Open Command Prompt and run the installer batch file `ytconverter/standalone/` directory:
```powershell
install.bat
```
3. After installation move installed yt-dlp.exe and ffmpeg binaries to your `PATH` directory, so that the script can access it globally.

4. After installation, start the program:
```powershell
python3 ytconverter.py
```
## Usage
1. Run the main script to start the conversion process:
   ```bash
   python3 ytconverter.py
   ```
2. Follow the on-screen instructions to input the YouTube URL and choose the desired output format.

## Update In Linux & Termux (Recommended frequently)
1. To update the `ytconverter` repository, run:
   ```bash
   ./standalone/update.sh # It also keeps your yt-dlp up-to-date 
   ```
2. To update the `ytconverter` binary just simply run the below command on your terminal:
   ```bash
   ytconverter -U
   ```
## Tested on
- Linux
- Termux
- Ubuntu
- MacOs
- Windows 10/11

---
## Screenshots
<p align= "left">
 <img width="1004" height="469" alt="1000122247" src="https://github.com/user-attachments/assets/80269ce0-1443-4dc4-836f-3bf63905879b" />
</p>
<p align="left">
<img src= "https://github.com/user-attachments/assets/8e9d00ce-b698-4b1f-8870-badd5d274442" width="600" height="600"/>
</p>
---



## Contact for any error or issue:
- kaifcodec@gmail.com

## Features
- **Video Downloading**: Fetch videos directly from YouTube.
- **Audio Downloading**: Downloads audio of any video with wide range of bitrate selection.
- **Multiple video download**: Now you can download multiple videos using the tool, just paste the urls one by one
- **Format Conversion**: Convert downloaded videos into different formats such as MP3, MP4, etc.
- **Metadata Handling**: Extract and manage metadata associated with YouTube videos.

---



## Contributing

Contributions, issues, and feature requests are welcome!

Please take a moment to read our [CONTRIBUTING.md](CONTRIBUTING.md) guide for details on how to help make **YTConverter™** better.

Feel free to open a pull request or submit an issue.

## Disclaimer ⚠⚠
 - **We do ask you for your Name and Contact information at the beginning of the tool for update-related notices, but if you don't want to disclose those creds, you can leave those fields blank**
 - **We also collect some basic information about the usage statistics and the user's Public IP, but we assure you that this data is not kept more than 48 hours**
 - **We respect your privacy. Any basic info this tool collects (like usage data) is handled securely and never shared. No creepy tracking—just good software.**
 - Thank you 🌹 and Keep supporting ❤

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please open an issue or contact [kaifcodec](https://github.com/kaifcodec).

# If you found this tool helpful leave a star that will motivate me to maintain this project and add new features 
---
## Stars ⭐ 
[![Star History Chart](https://api.star-history.com/svg?repos=kaifcodec/ytconverter&type=Date)](https://star-history.com/#kaifcodec/ytconverter&Date)
---
