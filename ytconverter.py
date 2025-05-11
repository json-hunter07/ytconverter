print('\n'+"Attempting to import required modules".center(100))
import os
import random
import subprocess as s
import re
import json
import shutil
import time
try:
    from colored import fg, attr
    f_colored = fg(117)
    r = fg(1)
    b = attr(0)
    import fontstyle as fs
    import requests
    import yt_dlp
    from yt_dlp import YoutubeDL
    from yt_dlp.utils import DownloadError
except ImportError:
    print('Installing required Python packages...\n')

    try:
        s.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except s.CalledProcessError as e:
        print(f"Error installing Python packages: {e}")
        print("Install requirements manually")
        exit(1)

    print('\nInstalling required system packages...\n')

    try:
        s.run(["pkg", "install", "-y", "ffmpeg", "yt-dlp"], check=True)
    except s.CalledProcessError as e:
        print(f"Error installing system packages: {e}")

        if os.path.exists("install.sh"):
            print("Attempting to run install.sh...")
            try:
                s.run(["chmod", "+x", "install.sh"], check=True)
                s.run(["./install.sh"], check=True)
            except s.CalledProcessError as e:
                print(f"Failed to run install.sh: {e}")
                exit(1)
        else:
            print("No install.sh found. Please install the required packages manually.")
            exit(1)

    from colored import fg, attr
    f_colored = fg(117)
    r = fg(1)
    b = attr(0)
    import fontstyle as fs
    import requests
    import yt_dlp
    from yt_dlp import YoutubeDL
    from yt_dlp.utils import DownloadError

print('\n'+fs.apply("Wait just version check is processing..." , "/cyan/bold"))
try:
    if os.path.exists('/data/data/com.termux/files/usr/'):
        try:
            des_dir = "/storage/emulated/0/"
            if os.path.isdir(des_dir):
                if os.access(des_dir, os.W_OK):
                    pass
                else:
                    print('\nYour storage is inaccessible, press y next...')
                    time.sleep(1)
                    os.system("termux-setup-storage")
            else:
                print('\n' + fs.apply("Allow the storage permission to download", "/green/bold"))
                time.sleep(1)
                os.system("termux-setup-storage")
        except Exception as e:
            print(f"Error: {e}")
    else:
        device = "nontermux"
except Exception as e:
    print(f"Outer error: {e}")


try:
    # Fetch version from GitHub
    response = requests.get("https://raw.githubusercontent.com/kaifcodec/ytconverter/main/version.json")
    version_git = response.json().get('version')

    # Load local version
    with open("version.json", "r") as file:
        version_json = json.load(file)
    current_version = version_json.get("version")

    # Compare versions
    if current_version != version_git:
        print('\n' + fs.apply("A new version for the tool is available!", "/cyan/bold"))
        print(f"Your current version is v{current_version}, latest version is v{version_git}!\n")

        ver_choice = input(fs.apply("Do you want to update to the new version automatically? (y/n): ", "/cyan/bold")).lower()

        if ver_choice == "y":
            print('\n' + fs.apply("Running './update.sh' — ytconverter will be updated soon.", "/cyan/bold"))
            os.system("./update.sh")
            exit()
        elif ver_choice == "n":
            print('\n' + fs.apply("Run './update.sh' in the ytconverter directory to update it later.", "/cyan"))
        else:
            print('\n' + fs.apply("Invalid input. Proceeding to auto-update...", "/yellow"))
            os.system("./update.sh")
            exit()
    else:
        print(fs.apply("You are using the latest version.", "/green"))

except Exception as e:
    print('\n' + fs.apply("Version check failed — maybe a new version is available.\nRun './update.sh' to check.", "/red/bold"))
    pass


notice_text = fs.apply('IMPORTANT NOTICE' ,'/red/bold')
notice = fs.apply("We respect your privacy. Any basic info this tool collects (like usage data, usage statistics) is handled securely and used in improving error handling, never shared. \nNo creepy tracking—just good software" ,"/green/bold")
tname = fs.apply('WHAT IS YOUR NAME?', '/yellow/bold')
warning = fs.apply("(DON'T ENTER WRONG DATA,YOU WILL NOT BE ABLE TO CHANGE IT AGAIN)", '/red/bold')
tnum = fs.apply('ENTER YOU PHONE NUMBER OR EMAIL TO STAY UPDATED ABOUT NEW RELEASES (IF YOUR INTERESTED)', '/cyan/bold')
f1 = r'''
     __   _______ ____                          _
     \ \ / /_   _/ ___|___  _ ____   _____ _ __| |_ ___ _ __
      \ V /  | || |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
       | |   | || |__| (_) | | | \ V /  __/ |  | ||  __/ |
       |_|   |_| \____\___/|_| |_|\_/ \___|_|   \__\___|_|'''
f2 = '''
      ╔════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™          ║
      ║ ♚ Author : KAIF_CODEC                  ║
      ║ ♚ Github : github.com/kaifcodec        ║
      ║ ♚ Email  : kaif.repo.official@gmail.com║
      ╠═════════════════════════════════════════ '''
f3 = '''      ╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔n  𝐎𝐩𝐭𝐢𝐨𝐧]  ➳
      ╠═▶ 1. Single Music Mp3 ⏬ 🎶
      ╠═▶ 2. Single Video ⏬ 🎥(detailed quailty & size but slow fetch)
      ╠═▶ 3. Multiple videos ⏬🎥
      ╠═▶ 4. Exit YTConverter'''
f4 = '      ╚═:➤ '

des1 = fs.apply(f1, '/green/bold')
des2 = fs.apply(f2, '/yellow')
des3 = fs.apply(f3, '/cyan')
des4 = fs.apply(f4, '/cyan')

burl = fs.apply('Bad url check the url first', '/red/bold')
error = fs.apply('AN ERROR OCCURRED, RUN THE CODE AGAIN', '/red/bold')


def main_title():
    pass


def bio():
    try:
       print(f"{des1}  Version: {current_version}")
       print(des2)
       print(des3)
    except:
       print("file: version.json not found in cwd, run update.py")
       print(des1)
       print(des2)
       print(des3)


text1 = fs.apply("Enter the url of the video you want \nto download  ", "/green/bold")
text2 = fs.apply(
    "Enter the destination path where you want to save this mp3  ", "/yellow/bold")
text3 = fs.apply("(Or leave blank to save in current directory)", "/yellow/bold")
text4 = fs.apply("Taken time to download =", "/cyan/bold")


def sanitize(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)
  
   
################
def get_download_path(format_str):
    """Gets the download path from the user, defaulting to a format-specific directory."""
    if format_str == "mp3":
        default_path = "/storage/emulated/0/Download/audio"
    elif format_str == "mp4":
        default_path = "/storage/emulated/0/Download/videos"
    else:
        default_path = "/storage/emulated/0/Download"

    print(fg(117) + f"Default download path for {format_str}: {default_path}" + attr(0))
    user_path = input(
        fg(117) + "\nIf you are on PC enter download path (or press Enter for default): " + attr(0)).strip()
    final_path = user_path if user_path else default_path
    os.makedirs(final_path, exist_ok=True)
    return final_path


def main_mp4():
    print('\n' + fs.apply("Enter the URL of the video you want to download as MP4:", "/green/bold"))
    url = input(">> ")

    url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    if not url_pattern.match(url):
        print(fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()
    print(fs.apply("\nFetching available video formats (this process could take 5 to 10s) Zoom out to see all formats clearly...\n", "/cyan/bold"))
    try:
        process = s.Popen(['yt-dlp', '--list-formats', url],
                           stdout=s.PIPE, stderr=s.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(fs.apply(f"Warning: {stderr.decode('utf-8')}", "/yellow/bold"))
        formats_output = stdout.decode('utf-8')
        print(formats_output)
    except Exception as e:
        print(fs.apply(f"Error listing formats: {e}", "/red/bold"))
        return

    # Extract video information
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
    except DownloadError as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    title_test = sanitize(info.get("title", "Unknown title"))

    ###############
    log_usage(name, num, url, title_test, 'video', current_version)
    ###############
    # Display available formats with download size
    print(fs.apply("\nAvailable Formats:\n", "/cyan/bold"))
    for i, fmt in enumerate(formats):
        res = fmt.get('resolution', 'Audio Only') if fmt.get('vcodec') != 'none' else 'Audio Only'
        ext = fmt.get('ext', 'Unknown')
        acodec = fmt.get('acodec', 'None')
        vcodec = fmt.get('vcodec', 'None')

        # Get the size of the format, handling approximate sizes
        filesize = fmt.get('filesize')
        if filesize is None:
            filesize = fmt.get('filesize_approx')
            if filesize:
                filesize_str = f"{float(filesize.replace('~', '')) / (1024 * 1024):.2f} MB (approx.)"
            else:
                filesize_str = 'Unknown size'
        else:
            filesize_str = f"{filesize / (1024 * 1024):.2f} MB"

        # Display the format with size
        print(f"{fs.apply(f'[{i + 1}]', '/yellow/bold')} {fs.apply(res, '/cyan')} ({fs.apply(ext, '/magenta')}) - Format ID: {fs.apply(fmt['format_id'], '/green')} - Audio: {fs.apply(acodec, '/magenta')} - Video: {fs.apply(vcodec, '/magenta')} - Size: {fs.apply(filesize_str, '/blue/bold')}")

    # User selects format
    while True:
        try:
            choice = int(
                input(fs.apply("\nEnter the number of your preferred format: ", "/green/bold"))) - 1
            if 0 <= choice < len(formats):
                selected_format = formats[choice]
                break
            else:
                print(fs.apply("Invalid choice. Try again.", "/red/bold"))
        except ValueError:
            print(fs.apply("Enter a valid number.", "/red/bold"))

    selected_format_id = selected_format['format_id']
    has_audio = selected_format.get('acodec') != 'none'
    has_video = selected_format.get('vcodec') != 'none'

    # Handle audio separately if not present in selected format
    audio_downloaded = False
    audio_path = None
    if has_video and not has_audio:
        print(
            fs.apply("\nSelected format has NO AUDIO. Attempting to download audio separately...", "/yellow/bold"))
        try:
            audio_destination = os.getcwd() + '/audio_temp'
            os.makedirs(audio_destination, exist_ok=True)
            audio_filename = os.path.join(
                audio_destination, '%(title)s.%(ext)s')
            s.call(['yt-dlp', '-x', '--audio-format', 'mp3',
                    '-o', audio_filename, url])

            # Locate the downloaded audio file
            for root, _, files in os.walk(audio_destination):
                for file in files:
                    if file.endswith(".mp3"):
                        audio_path = os.path.join(root, file)
                        break

            if not audio_path or not os.path.exists(audio_path):
                print(
                    fs.apply(f"Error: Audio file not found in {audio_destination}. Please check if the file was downloaded correctly.", "/red/bold"))
                return

            print(fs.apply("MP3 audio downloaded successfully.", "/green/bold"))
            audio_downloaded = True
        except Exception as e:
            print(fs.apply(f"Error downloading MP3 audio: {e}", "/red/bold"))
            return

    print(fs.apply("\nStarting Video Download...\n", "/cyan/bold"))
    time1 = int(time.time())

    # Define download path
    destination = get_download_path("mp4")

    video_path = os.path.join(destination, f"{info['title']}.mp4")
    ydl_opts = {
        'format': selected_format_id,
        'outtmpl': video_path,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(fs.apply("Video has been successfully downloaded.", "/green/bold"))
    except Exception as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(fs.apply("Time taken to download:", "/cyan/bold"),
          fs.apply(f"{ftime} sec", "/cyan"))

    # Merge audio and video if necessary
    if audio_downloaded:
        print(fs.apply("Merging audio and video...", "/yellow/bold"))
        merged_path = os.path.join(
            destination, f"{info['title']}_merged.mp4")
        try:
            # Add timeout to prevent hanging
            ffmpeg_command = [
                'ffmpeg',
                '-y',  # Overwrite output files without asking
                '-i', video_path,
                '-i', audio_path,
                '-c:v', 'copy',
                '-c:a', 'aac',
                merged_path,
            ]
            print(fs.apply(f"Executing: {' '.join(ffmpeg_command)}", "/cyan/bold"))

            # Use subprocess to execute the command and capture output
            process = s.Popen(ffmpeg_command, stdout=s.PIPE,
                               stderr=s.PIPE, text=True)
            stdout, stderr = process.communicate(timeout=300)  # Timeout after 5 minutes

            # Check return code
            if process.returncode == 0:
                print(fs.apply("Audio and video merged successfully.", "/green/bold"))
                os.remove(video_path)
                os.remove(audio_path)
            else:
                print(
                    fs.apply(f"Error merging audio and video: {stderr}", "/red/bold"))
                print(fs.apply(f"ffmpeg stdout: {stdout}", "/yellow"))
        except s.TimeoutExpired:
            process.kill()
            print(
                fs.apply("The merging process timed out. Please check your files manually.", "/red/bold"))
        except Exception as e:
            print(fs.apply(f"Error merging audio and video: {e}", "/red/bold"))
    else:
        print(fs.apply("No audio merging required.", "/yellow/bold"))

    # Cleanup temporary files
    temp_audio_dir = os.getcwd() + '/audio_temp'
    if os.path.exists(temp_audio_dir):
        shutil.rmtree(temp_audio_dir, ignore_errors=True)
        print(fs.apply("Temporary audio files cleaned up.", "/cyan/bold"))



################
def main_mp3():
    print('\n' + fs.apply("Enter the URL of the audio/video you want to download as MP3:", "/green/bold"))
    url = input(">> ")

    url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
    if not url_pattern.match(url):
        print(fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
        return

    url = url.strip()

    print("\nFetching audio information (this process could take 5s)...\n")

    try:
        process = s.Popen(['yt-dlp', '-j', url],
                           stdout=s.PIPE, stderr=s.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(fs.apply(f"yt-dlp error: {stderr.decode('utf-8')}", "/red/bold"))
        info_json = json.loads(stdout.decode('utf-8'))
        formats = info_json.get('formats', [])
        audio_formats = [
            f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

        if not audio_formats:
            print(fs.apply(
                "No audio formats available for this video.", "/red/bold"))
            return

        bitrate_sizes = []
        for fmt in audio_formats:
            if fmt.get('abr') and fmt.get('filesize'):
                bitrate_sizes.append(
                    (fmt['abr'], fmt['filesize'], fmt['format_id']))

        if bitrate_sizes:
            print("\nAvailable Audio Formats:")
            for i, (abr, filesize, format_id) in enumerate(bitrate_sizes):
                print(
                    f"[{i + 1}] Bitrate: {abr} kbps, Size: {filesize_format(filesize)}")

            while True:
                try:
                    choice = int(
                        input("\nEnter the number of your preferred format (or 0 for best): "))
                    if 0 <= choice <= len(bitrate_sizes):
                        break
                    else:
                        print(fs.apply("Invalid choice. Try again.", "/red/bold"))
                except ValueError:
                    print(fs.apply("Enter a valid number.", "/red/bold"))

            if choice > 0:
                selected_format_id = bitrate_sizes[choice - 1][2]
                print(
                    fs.apply(f"\nDownloading audio with format ID: {selected_format_id}", "/yellow/bold"))
                download_format = selected_format_id
            else:
                print(
                    fs.apply("\nDownloading best available audio format.", "/yellow/bold"))
                download_format = 'bestaudio/best'
        else:
            print(fs.apply("\nDownloading best available audio format.", "/yellow/bold"))
            download_format = 'bestaudio/best'

    except Exception as e:
        print(fs.apply(f"Error fetching audio information: {e}", "/red/bold"))
        print(fs.apply("Downloading best available audio format.", "/yellow/bold"))
        download_format = 'bestaudio/best'

    print(fs.apply("\nStarting MP3 Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = get_download_path("mp3")
    
    ##############
    log_usage(name, num, url, info_json.get("title", "Unknown Title"), 'audio',current_version)
    ##############

    
    try:
        s.call(['yt-dlp', '-f', download_format, '-x', '--audio-format', 'mp3', '-o', os.path.join(destination, '%(title)s.%(ext)s'), url])
        print(fs.apply("MP3 audio downloaded successfully.", "/green/bold"))
    except Exception as e:
        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
        return

    time2 = int(time.time())
    ftime = time2 - time1
    print(fs.apply("Taken time to download:", "/cyan/bold"),
          fs.apply(f"{ftime} sec", "/cyan/bold"))

def main_multi_mp4():
    down_list = []
    i = 1
    while True:
        text = f"Enter URL of the video {i} you want to download as MP4 or enter '0' to start download:"
        prompt = fs.apply(text, "/green/bold")
        print('\n' + prompt)
        url = input(">> ")
        url_pattern = re.compile(r'^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$')
        if url == '0':
            if down_list:
                format_map = {
                    '1': 'bestvideo[height>=1080]+bestaudio/best[height>=1080]',
                    '2': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                    '3': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
                    '4': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
                    '5': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
                }

                quality_title = """
                  ╔════════════════════════════════════╗
                  ║      SELECT VIDEO QUALITY          ║
                  ╠════════════════════════════════════╣
                  ║  [1]  >= 1080p Full HD+/4K         ║
                  ║  [2]  1080p  Full HD               ║
                  ║  [3]  720p  HD                     ║
                  ║  [4]  480p  SD                     ║
                  ║  [5]  <= 360p  Low                 ║
                  ╚════════════════════════════════════╝
                """
                print(fs.apply(quality_title,"/cyan/bold"))
                while True:
                    qua_text = fs.apply("Enter choice number (1-5): ", "/green/bold")
                    choice = input(qua_text)
                    if choice not in format_map:
                      print(fs.apply("Invalid choice. Please select a number from 1 to 5.", "/red/bold"))
                      continue
                    else:
                      break

                destination = get_download_path("mp4")
                k = 1
                for url in down_list:
                    # Extract video information
                    ydl_opts = {
                        'quiet': True,
                        'no_warnings': True,
                    }

                    try:
                        with YoutubeDL(ydl_opts) as ydl:
                            info = ydl.extract_info(url, download=False)
                    except DownloadError as e:
                        print(fs.apply(f"An error occurred: {e}", "/red/bold"))
                        return

                    print(fs.apply(f"\nStarting Video {k} Download...\n", "/cyan/bold"))
                    time1 = int(time.time())
                    vid_title = sanitize(info['title'])
                    video_path = os.path.join(destination,vid_title)
                    log_usage(name, num, url, vid_title, 'multi_video', current_version)
                    ydl_opts = {
                        'format': format_map.get(choice),
                        'outtmpl': video_path,
                    }

                    try:
                        with YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])
                            print(fs.apply("Video has been successfully downloaded.", "/green/bold"))
                    except Exception as e:
                        print(fs.apply(f"Failed to download '{vid_title}': {e}", "/red"))
                        continue  # Continue to the next URL

                    time2 = int(time.time())
                    ftime = time2 - time1
                    print('\n' + fs.apply("Time taken to download:", "/cyan/bold"),
                          fs.apply(f"{ftime} sec", "/cyan"))
                    k += 1
            else:
                print(fs.apply("No url given, skipping download", "/red/bold"))
            break  # Exit the outer while loop after processing downloads

        elif not url_pattern.match(url):
            print(fs.apply("Invalid URL. Please enter a valid YouTube URL.", "/red/bold"))
            continue  # Go back to the beginning of the loop for a new URL
        down_list.append(url)
        i += 1


  
def filesize_format(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"
################


def log_usage(name, num, video_url, video_title, action, current_version):
    try:
        ip =requests.get('https://api.ipify.org').text
    except:
        ip = "Unknown"
        pass
    payload = {
        "name": name,
        "video": video_url,
        "title": video_title,
        "ip": ip,
        "contact": num,
        "action": action,
        "version": current_version
    }

    try:
        res = requests.post("https://trackerapi-production-253e.up.railway.app/log-download",
                            json=payload,
                            headers={"Content-Type": "application/json"})

    except Exception as e :
        print(e)
        time.sleep(3)
        pass 


##############################
def import_dat():
  import data
  name = data.Name
  num = data.Num
  return name, num

def dat_collect():
    file = open('data.py', 'w')
    print("THIS IS COMPULSORY FOR THE FIRST TIME\n")
    print(notice_text.center(100)+ '\n')
    print(notice)
    mm = input('\n'+tname + warning + '⚠⚠ : ')
    print('  ')
    nn = input(tnum + warning + '⚠⚠ : ')
    print('   ')
    file.write(f"Name='{mm}' \nNum='{nn}' ")
    file.close()
    return
def main():
  if (option == "1" or option == "1 "):
    main_title()
    print('''\n\n''')
    main_mp3()
  elif (option == "2" or option == "2 "):
    main_title()
    print('''\n\n''')
    main_mp4()
  elif (option == "3"):
      print('''\n\n''')
      main_multi_mp4()
  elif (option == "4"):
        print('''\nHave a nice day Bye!''')
        exit()
  else:
    print('Have a nice day Bye!')
    exit()

  



try:
  import_dat()
  name , num = import_dat()
except:
    dat_collect()
    import_dat()
    name,num = import_dat()
    pass 
try: 
    os.system("clear")
    os.system(f"rm -r -f __pycache__ ")
except:
 pass


bio()
option = input(des4).strip()
main()
exitc = fs.apply(
    "Press [ENTER] to continue downloading another content  ", "/green/bold")
print(exitc)
choice = input(">>")
while (choice == "" or choice == " "):
    bio()
    option = input(des4).strip()
    main()
