#*Eriosakhare Joshua Omoruyi

#This project will feature an algorithm that automates file organization for the user
import os, shutil

#copied path directory to automate files within
path =r"C:/Users/Eriosakhare(joshua)/Documents/notes/"

filename = os.listdir(path)


#Premise*
#* Verify if there are already folders within the directory/Create folders
folder_names = ['Textbook Pdfs', 'images', 'notes']
for track in range(0,3):
    if not os.path.exists(path+ folder_names[track]):
           print(path+ folder_names[track])
           os.makedirs((path+ folder_names[track]))
#* Identify files based on their types
#* Correctly reorganize files using their types
for file in filename:
      if ".pdf" in file and not os.path.exists(path +"Textbook Pdfs/" + file):
            shutil.move(path + file,path +"Textbook Pdfs/" + file)
      elif ".jpg" in file and not os.path.exists(path +"images/" + file):
            shutil.move(path + file,path +"images/" + file)
      elif ".docx" in file and not os.path.exists(path +"notes/" + file):
            shutil.move(path + file,path +"notes/" + file)
      else:
            print("Files were not relocated.")


