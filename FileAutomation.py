#*Eriosakhare Joshua Omoruyi

#This project will feature an algorithm that automates file organization for the user
import os, shutil

#copied path directories to automate files within
path =r"C:/Users/Eriosakhare(joshua)/Documents/notes/"
path1 =r"C:/Users/Eriosakhare(joshua)/Downloads/"

filename = os.listdir(path)
filename2 = os.listdir(path1)


#Premise*
#* Verify if there are already folders within the directory/Create folders
folder_names = ['Textbook Pdfs', 'images', 'notes']
for track in range(0,3):
    if not os.path.exists(path+ folder_names[track]):
           print(path+ folder_names[track])
           os.makedirs((path+ folder_names[track]))

folder_names2 =['Misc Beats - Samples', 'Flps']
for item in range(0,2):
      if not os.path.exists(path1+ folder_names2[item]):
            print((path1+ folder_names2[item]))
            os.makedirs((path1+ folder_names2[item]))
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
for file in filename2:
      if ".mp3" in file and not os.path.exists(path1 +"Misc Beats - Samples/" + file):
           shutil.move(path1 + file,path1 +"Misc Beats - Samples/" + file)
      elif ".flp" in file and not os.path.exists(path1 +"Flps/" + file):
            shutil.move(path1 + file,path1 + "Flps/" + file)
      
      else:
            print("Files were not relocated.")


