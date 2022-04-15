import os
import pandas as pd



data = []


path = os.path.join(os.getcwd(),'..','data','accents')

words       = ['heed','hid','head']
arpabet     = ['IY1' ,'IH1','EH1' ]
class_label = [  1   ,  2  ,  3   ]

for accent in os.listdir(path): 
    for gender in os.listdir(os.path.join(path,accent)):
        for speaker in os.listdir(os.path.join(path,accent,gender)):
            
            data_speaker = speaker[:len(speaker)-4]
            data_gender = 'M' if gender == 'male' else 'F'
            
            for i in range(3):
                data.append([data_speaker,data_gender,words[i],arpabet[i],class_label[i],None,None,None])

pd.DataFrame(data,columns=['Speaker','Gender','Word','Phoneme','Class','F1','F2','F3']).to_csv(os.path.join(os.getcwd(),'..','data','data.csv'), index=False)
            

print('Finished!')