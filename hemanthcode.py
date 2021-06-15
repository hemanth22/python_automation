import os,sys,glob;


def searchfile(user):
    files = glob.glob('home/'+user+'/*.py')
    for file in files:
        abc_file = os.path.basename(file)
        return abc_file

def fullsearchfile(user):
    files = glob.glob('home/'+user+'/*.py',recursive=True)
    for file in files:
        return file

username = 'vagrant'

abc = searchfile(username)
xyz = fullsearchfile(username)

print(abc)
print(xyz)
