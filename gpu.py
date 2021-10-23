import os

print("""
[1] mkv to mp4
[2] mp4 to mp3
[3] webm to mp4
[4] webm to mp3
[5] custom
""")

mmo = input("? Select: ")
if mmo == "1":
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(".mkv"):
            newfilename = f"{'.'.join(file.split('.')[:-1])}.mp4"
            os.system(
                f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{file}" -c:v h264_nvenc -preset slow "{newfilename}" """)

elif mmo == "2":
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(".mp4"):
            newfilename = f"{'.'.join(file.split('.')[:-1])}.mp3"
            os.system(
                f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{file}" -c:v h264_nvenc -preset slow "{newfilename}" """)

elif mmo == "3":
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(".webm"):
            newfilename = f"{'.'.join(file.split('.')[:-1])}.mp3"
            os.system(
                f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{file}" -c:v h264_nvenc -preset slow "{newfilename}" """)

elif mmo == "4":
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(".webm"):
            newfilename = f"{'.'.join(file.split('.')[:-1])}.mp4"
            os.system(
                f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{file}" -c:v h264_nvenc -preset slow "{newfilename}" """)

else:
    fromv = input("? from:")
    tov = input("? to: ")
    for file in os.listdir(os.getcwd()):
        if file.lower().endswith(f".{fromv}"):
            newfilename = f"{'.'.join(file.split('.')[:-1])}.{tov}"
            os.system(
                f"""ffmpeg -hwaccel_device 0 -hwaccel cuda -i "{file}" -c:v h264_nvenc -preset slow "{newfilename}" """)
