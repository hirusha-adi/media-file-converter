import os
import platform
from time import sleep as t_sleep


def clear_screen():
    if platform.system().lower().startswith('win'):
        os.system("cls")
    else:
        os.system("clear")


def show_logo():
    clear_screen()
    print("""
  __  __ _____ ____ 
 |  \/  |  ___/ ___|
 | |\/| | |_ | |    
 | |  | |  _|| |___ 
 |_|  |_|_|   \____|
Media File Converter
   by ZeaCeR#5641

Only have media files in
the current working dir!
    """)


def convert_to_mp3():
    for file in os.listdir(os.getcwd()):
        if file == "convert.py":
            continue
        try:
            os.system(
                f'''ffmpeg -i "{file}" "{''.join(file.split('.')[:-1])}.mp3"''')
        except:
            continue


def convert_to_mp4():
    for file in os.listdir(os.getcwd()):
        if file == "convert.py":
            continue
        try:
            os.system(
                f'''ffmpeg -i "{file}" "{''.join(file.split('.')[:-1])}.mp4"''')
        except:
            pass


def convert_to_cust(cust_file_ex):
    for file in os.listdir(os.getcwd()):
        if file == "convert.py":
            continue
        try:
            os.system(
                f'''ffmpeg -i "{file}" "{''.join(file.split('.')[:-1])}.{cust_file_ex}"''')
        except:
            pass


def MAIN_PROGRAM():
    show_logo()
    print("""
[1] .* to mp3
[2] .* to mp4
[3] .* to custom
    """)
    main_opt = input("[+] Please select an option: ")
    if main_opt == "1":
        convert_to_mp3()
    elif main_opt == "2":
        convert_to_mp4()
    elif main_opt == "3":
        cfext = input("[+] Enter the custom file format: ")
        convert_to_cust(cfext)
    else:
        print("[!!] Please enter a valid option")
        t_sleep(3)
        MAIN_PROGRAM()


if __name__ == "__main__":
    MAIN_PROGRAM()
