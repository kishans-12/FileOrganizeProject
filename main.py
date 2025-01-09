import os ,shutil
path = input()
print(f"The given path is {path}")

replace = path.replace("\\","/")
print(replace)

if(os.path.exists(replace) == True):
    print("correct")
else:
    print("False")

    exit()

if (os.path.isdir(replace) == True):
    print("Correct")

else:
    print("Please provide correct folder path")
    exit()

if(os.path.exists(replace+"/images")== True):
   shutil.rmtree(replace+"/images")
if(os.path.exists(replace+"/audios")== True):
   shutil.rmtree(replace+"/audios")
if(os.path.exists(replace+"/videos")== True):
   shutil.rmtree(replace+"/videos")
if(os.path.exists(replace+"/docs")== True):
   shutil.rmtree(replace+"/docs")

   

# Creating empty folders
os.makedirs(replace+"/images")
os.makedirs(replace+"/audios")
os.makedirs(replace+"/videos")
os.makedirs(replace+"/docs")


# Store all files and sub-folders present in the given path in the list "filelist"
filelist=[]
filelist = os.listdir(replace)

# fileDictionary = {"images":[],"videos":[],"Audios":[],"docs":[]}

for fileName in filelist:
    
    #check for file or folder
    if os.path.isdir(replace+'/'+fileName):
        continue

    #Get the file extention
    extension=fileName.split('.')[-1]

    # for images
    if extension in ('jpg','jpeg','png','gif'):
        shutil.move(replace+'/'+fileName,replace+'/images/'+fileName)
    # for videos
    elif extension in ('mp4','mkv','avi','flv'):
        shutil.move(replace+'/'+fileName,replace+'/videos/'+fileName)
    # for audios
    elif extension in ('mp3','wav','flac'):
        shutil.move(replace+'/'+fileName,replace+'/audios/'+fileName)
    # for docs
    elif extension in ('doc','docx','pdf','txt'):
        shutil.move(replace+'/'+fileName,replace+'/docs/'+fileName)
    else:
        print(f"File {fileName} is not moved to any folder")

