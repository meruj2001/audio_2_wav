import os
import glob

folders = glob.glob('*/*')

print(folders)

for folder in folders:
    print(folder)
    for file in os.listdir(folder):
        if (file.endswith(".mp4")): #or .avi, .mpeg, whatever.
            print(file)
            print(file.split('.')[0])
            print("ffmpeg -i " + folder + "/" + file + " " + folder + "/" + file.split('.')[0] + ".wav")
            os.system("ffmpeg -i " + folder + "/" + file + " " + folder + "/" + file.split('.')[0] + ".wav")
        else:
            continue