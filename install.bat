@echo off
setlocal enabledelayedexpansion

:: Test emoji support by printing a smiley and reading the output
:: (Note: This is limited in batch, so we'll simulate fallback with a simple user prompt)

:: Define emoji symbols (default)
set "CHECK=✅"
set "CROSS=❌"
set "INFO=ℹ️"
set "STAR=✨"

:: Define ASCII fallback symbols
set "CHECK_ASC=OK"
set "CROSS_ASC=ERR"
set "INFO_ASC=INFO"
set "STAR_ASC=*"

:: Function to check if console font supports emoji
:: Batch can't easily do this, so we ask user or assume modern Windows
set "EMOJIS_SUPPORTED=1"

:: If you want to be super safe, uncomment the next lines to ask user
:: echo Are emojis displaying correctly? (y/n)
:: set /p emojians=
:: if /i NOT "%emojians%"=="y" set "EMOJIS_SUPPORTED=0"

:: Choose symbols depending on support
if "%EMOJIS_SUPPORTED%"=="1" (
    set "SYM_CHECK=%CHECK%"
    set "SYM_CROSS=%CROSS%"
    set "SYM_INFO=%INFO%"
    set "SYM_STAR=%STAR%"
) else (
    set "SYM_CHECK=%CHECK_ASC%"
    set "SYM_CROSS=%CROSS_ASC%"
    set "SYM_INFO=%INFO_ASC%"
    set "SYM_STAR=%STAR_ASC%"
)

:: Color support (Windows 10+ supports ANSI codes in cmd with ENABLE_VIRTUAL_TERMINAL_PROCESSING)
:: Try to enable ANSI colors
>nul 2>&1 reg query "HKCU\Console" /v VirtualTerminalLevel && (
    :: Windows 10+ with VT support
    set "GREEN=\033[0;32m"
    set "RED=\033[0;31m"
    set "YELLOW=\033[1;33m"
    set "CYAN=\033[0;36m"
    set "RESET=\033[0m"
) || (
    :: No color support, empty codes
    set "GREEN="
    set "RED="
    set "YELLOW="
    set "CYAN="
    set "RESET="
)

echo %SYM_STAR% %GREEN%Starting YTConverter™ universal installer...%RESET%

:: Your install commands here...
:: Example messages:
echo %SYM_INFO% %CYAN%Checking environment...%RESET%
:: Simulate install
echo %SYM_CHECK% %GREEN%Installation complete!%RESET%
echo %SYM_INFO% %CYAN%Run 'python ytconverter.py' to start.%RESET%

pause
endlocal
exit /b 0
