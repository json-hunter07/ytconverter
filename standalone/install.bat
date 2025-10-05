@echo off
setlocal enabledelayedexpansion

set "TEMP_DIR=%cd%\installer_temp"
set "FFMPEG_ZIP=%TEMP_DIR%\ffmpeg.zip"
set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
set "TOOLS_DIR=%LocalAppData%\Programs\YTConverter"

mkdir "%TEMP_DIR%" >nul 2>&1
mkdir "%TOOLS_DIR%" >nul 2>&1

echo Checking Python...
where python >nul 2>&1 || (
    echo Python not found. Install it from https://www.python.org/downloads/
    exit /b 1
)

echo Installing yt-dlp...
python -m pip install -U yt-dlp >nul 2>&1 || (
    echo Failed to install yt-dlp.
    exit /b 1
)

echo Checking ffmpeg...
where ffmpeg >nul 2>&1
if %errorlevel%==0 (
    echo ffmpeg already installed.
) else (
    echo Downloading ffmpeg...
    powershell -Command "Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'"
    powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%TEMP_DIR%' -Force"
    for /d %%I in (%TEMP_DIR%\ffmpeg-*) do set "FFMPEG_EXTRACTED=%%I"
    xcopy /E /I /Y "%FFMPEG_EXTRACTED%\bin" "%TOOLS_DIR%\ffmpeg" >nul
    echo ffmpeg installed.
)

echo Updating PATH...
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "OLD_PATH=%%b"
if not defined OLD_PATH set "OLD_PATH=%PATH%"
setx PATH "%TOOLS_DIR%\ffmpeg;%OLD_PATH%" >nul

rmdir /S /Q "%TEMP_DIR%" >nul 2>&1

echo Installation complete.
echo Open a new Command Prompt and run:
echo yt-dlp --version
echo ffmpeg -version
pause
exit /b 0
