import os
from pathlib import Path
import setup

DOWNLOADS = Path.home() / 'Downloads'
# Should set the current directory to downloads!

os.chdir(DOWNLOADS)
# Testing shows we're now in the downloads directory
setup.generateArchives(DOWNLOADS)

# Now all the downloads should be setup
# Create our list of filetypes

folder_names = {'Code':{'js','jsp','html','ipynb','py','java','css'},'Documents':{'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub'},'Images':{'bmp','gif .ico','jpeg','jpg','png','jfif','svg','tif','tiff'},'Executables':{'apk','bat','bin', 'exe','jar','msi','py'},"Archives":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'}}
fkey_list = list(folder_names.keys())
fval_list = list(folder_names.values())

pos = fval_list.index('pptx')
print(fkey_list[pos])


old_files = [f for f in os.listdir(DOWNLOADS) if os.path.isfile(os.path.join(DOWNLOADS,f))]

print(f'There are {len(old_files)} files in your downloads folder!')

print() 
