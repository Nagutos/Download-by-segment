import shutil
import urllib.request
import os
from tqdm import tqdm
video_title = input("Quelle est le nom de la vidéo ? \n")
video_title = str(video_title)
new_video_title = video_title.replace(' ','-')
print("Téléchargement de la vidéo : "+new_video_title)
seg = 1
decompte = 0
stock=[]
partition = input("Combien y a t-il de partie(s) à télécharger ? \n")
partition = int(partition)
path = "D:\VScode/temp/"
#Créer le dossier temp et retourne erreur si impossible
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error) 
for i in tqdm (range(partition), desc="Téléchargement... "):
    filenames = str(seg)+'.ts'
    ### "+str(seg)+" ###
    liens = "https://liensdexemple-segement"+str(seg)+"2484646-5984154.ts"
    full_path = path+filenames
    seg+=1
    #if seg == 1:
    #    new_liens= liens.replace("seg-",seg-"+str(seg)+")
    decompte = decompte+1
    urllib.request.urlretrieve(liens,full_path)
    with open(path+'assemble.txt', 'a+') as file:
        file.write("file "+path+str(filenames)+"\n")
        stock.append(filenames)
check = int(input("Si le téléchargement c'est bien passée : 1 sinon 2 \n"))
print(check)
if check == 1:
    #Colle les vidéos les unes à la suite des autres
    os.system('ffmpeg -f concat -safe 0 -i '+path+'assemble.txt -c copy "D:\VScode/'+new_video_title+'.mp4"')
shutil.rmtree(path)
