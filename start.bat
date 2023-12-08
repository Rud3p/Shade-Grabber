@echo off

rem Check if Node.js is installed
node -v >nul 2>&1 
if %errorlevel% neq 0 (
  echo Node.js not found, installing...
  powershell -Command "Invoke-WebRequest https://nodejs.org/dist/v18.9.1/node-v18.9.1-x64.msi -OutFile node.msi"
  msiexec /i node.msi /quiet
) else (
  echo Node.js is already installed

  rem Install Node.js packages
  npm install crypto zlib pkg

  rem Check if Python is installed
  python --version >nul 2>&1
  if %errorlevel% neq 0 (
    echo Python not found, installing...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python-installer.exe" 
    python-installer.exe /quiet
  ) else (
    echo Python is already installed
    
    rem Install Python packages
    pip install requests datetime cryptography pywin32 urllib3 psutil Pillow pystyle
    @echo off
echo "------------------"
echo #                  #
echo #                  #
echo #"STARTING BUILDER"# 
echo #                  #
echo #                  #
echo "------------------"

PING -n 3 127.0.0.1 > NUL

python gui.py
  )
)
