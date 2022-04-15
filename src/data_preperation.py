import os
from shutil import rmtree

path = os.path.join(os.getcwd(),'..','data','accents')
sound_file = 'cwa_CT.wav'

for filename in os.listdir(path):
    for gender in os.listdir(os.path.join(path,filename)):
        for speaker in os.listdir(os.path.join(path,filename,gender)):
            
            speaker_path = os.path.join(path,filename,gender,speaker)

            os.rename(os.path.join(speaker_path,sound_file),os.path.join(speaker_path,'..',speaker+'.wav'))
            rmtree(speaker_path)
            

print('Finished!')