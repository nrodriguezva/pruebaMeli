import database.connection_db as dbconnetion
from model.file import File
import os

def readPath(f_path):
    if f_path.find("txt") == -1:
        contents = os.listdir(f_path)
        for u in contents:
            listName = u.split('.')
            newFile = File(listName[0],listName[1])
            print(newFile.getNameFile() + ' ' + newFile.getExtentionFile())
            dbconnetion.read_file(newFile,  f_path+'\\'+u)
    else:
        f_pathAux = f_path.replace('//', '\\')
        print(f_pathAux)
        listpath = f_pathAux.split('\\')
        num = len(listpath)
        aux = listpath[num-1]
        listName = aux.split('.')
        newFile = File(listName[0],listName[1])
        print(newFile.getNameFile() + ' ' + newFile.getExtentionFile())
        dbconnetion.read_file(newFile,  f_path)