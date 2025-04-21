import time
import os
import random
import subprocess as s
import re
import json
import shutil
try:
    from colored import fg, attr
    f_colored = fg(117)  # Use a distinct alias for colored foreground
    r = fg(1)
    b = attr(0)
    import fontstyle as fs  # Use 'fs' as alias for fontstyle
    import requests
    import yt_dlp
    from yt_dlp import YoutubeDL
    from yt_dlp.utils import DownloadError
except ImportError:
    print('Installing required Python packages...\n')
    os.system("pip install fontstyle")
    os.system("pip install yt_dlp")
    os.system("pip install colored")
    os.system("pip install requests")
    print('\nInstalling required system packages...\n')
    os.system("pkg install -y ffmpeg yt-dlp") # Install both ffmpeg and yt-dlp using pkg
    print('\nRun the code again')
    exit()

tname = fs.apply('WHAT IS YOUR NAME?', '/yellow/bold')
warning = fs.apply(
    "(DON'T TRY TO ENTER WRONG DATA,YOU WILL NOT BE ABLE TO CHANGE IT AGAIN)", '/red/bold')
tnum = fs.apply('ENTER YOU PHONE NUMBER OR EMAIL TO STAY UPDATED ABOUT NEW RELEASES', '/cyan/bold')
f1 = '''                   ▄▀▄     ▄▀▄
                  ▄█░░▀▀▀▀▀░░█▄
              ▄▄  █░░░░░░░░░░░█  ▄▄
             █▄▄█ █░░█░░┬░░█░░█ █▄▄█'''
f2 = '''      ╔════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™          ║
      ║ ♚ Author : KAIF_CODEC                  ║
      ║ ♚ Github : github.com/kaifcodec        ║
      ║ ♚ Email  : kaif.repo.official@gmail.com║
      ╠═════════════════════════════════════════ '''
f3 = '''      ╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁]  ➳
      ╠═▶ 1. Music Mp3 🎶
      ╠═▶ 2. Video🎥
      ╠═▶ 3. Exit YTConverter'''
f4 = '      ╚═:➤ '

des1 = fs.apply(f1, '/red')
des2 = fs.apply(f2, '/yellow')
des3 = fs.apply(f3, '/cyan')
des4 = fs.apply(f4, '/cyan')

burl = fs.apply('Bad url check the url first', '/red/bold')
error = fs.apply('AN ERROR OCCURRED, RUN THE CODE AGAIN', '/red/bold')


def main_title():
    pass


def bio():
    print(des1)
    print(des2)
    print(des3)


text1 = fs.apply("Enter the url of the video you want \nto download  ", "/green/bold")
text2 = fs.apply(
    "Enter the destination path where you want to save this mp3  ", "/yellow/bold")
text3 = fs.apply("(Or leave blank to save in current directory)", "/yellow/bold")
text4 = fs.apply("Taken time to download =", "/cyan/bold")


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
        fg(117) + "Enter download path (or press Enter for default): " + attr(0)).strip()
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
    print(fs.apply("\nFetching available video formats (this process could take 5-10s)...\n", "/cyan/bold"))

  
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


    title_test=info.get("title","Unknown title")

###############
    log_usage(name, num, url, title_test, 'video')
###############

    
    video_formats = [f for f in formats if f.get('vcodec') != 'none']
    audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

    # Display available formats
    print(fs.apply("\nAvailable Formats:\n", "/cyan/bold"))
    for i, fmt in enumerate(formats):
        res = fmt.get('resolution', 'Audio Only') if fmt.get(
            'vcodec') != 'none' else 'Audio Only'
        ext = fmt.get('ext', 'Unknown')
        acodec = fmt.get('acodec', 'None')
        vcodec = fmt.get('vcodec', 'None')
        print(
            f"{fs.apply(f'[{i + 1}]', '/yellow/bold')} {fs.apply(res, '/cyan')} ({fs.apply(ext, '/magenta')}) - Format ID: {fs.apply(fmt['format_id'], '/green')} - Audio: {fs.apply(acodec, '/magenta')} - Video: {fs.apply(vcodec, '/magenta')}")

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
    log_usage(name, num, url, info_json.get("title", "Unknown Title"), 'audio')
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


def filesize_format(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"
################



def log_usage(name, num, video_url, video_title, action):
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
        "action": action
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


def dat_collect():
    file = open('data.py', 'w')
    print("THIS IS COMPULSORY FOR THE FIRST TIME\n")
    mm = input(tname + warning + '⚠⚠ : ')
    print('  ')
    nn = input(tnum + warning + '⚠⚠ : ')
    print('   ')
    file.write(f"Name='{mm}' \nNum='{nn}' ")
    file.close()
    return


try:
    import data
    name = data.Name
    num = data.Num
except:
    dat_collect()
    import data
    name = data.Name
    num = data.Num
    pass 
try: 
    os.system("clear")
    os.system(f"rm -r -f __pycache__ ")
except:
 pass


bio()
option = input(des4)

if (option == "1" or option == "1 "):
    main_title()
    print('''\n\n''')
    main_mp3()
elif (option == "2" or option == "2 "):
    main_title()
    print('''\n\n''')
    main_mp4()
elif (option == "3" or option == "3 "):
    print('Have a nice day Bye!')
    exit()
else:
    print('Have a nice day Bye!')
    exit()

exitc = fs.apply(
    "Press [ENTER] to continue downloading another content  ", "/green/bold")
print(exitc)
choice = input(">>")
while (choice == "" or choice == " "):
    bio()
    option = input(des4)

    if (option == "1" or option == "1 "):
        main_title()
        print('''\n\n''')
        main_mp3()
    elif (option == "2" or option == "2 "):
        main_title()
        print('''\n\n''')
        main_mp4()
    elif (option == '3' or option == '3 '):
        print('''\nHave a nice day Bye!''')
        exit()
    else:
        print('''\nHave a nice day Bye!''')
        exit()
   
