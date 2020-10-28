import glob
import shutil
import os

folders = glob.glob('*/*')

for folder in folders:
    # print(files)
    for file in os.listdir(folder):
        if file.endswith('.wav'):
            shutil.move(folder+'/'+file, 'wav_files/' + file)