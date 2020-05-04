import numpy as np 
import os
import string
import random 

def randomString(stringLength=10):
    """
    Generates a random string

    Arguments
    stringLength -- the path to write all the files
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def write_files(path):
    """
    Writes files randomly into a folder

    Arguments
    path -- the path to write all the files
    """
    number_files= int(random.uniform(10, 25))
    for j in range(number_files):
        f = open(path+"file_"+randomString(int(random.uniform(8, 25)))
            +".txt", "a")
        f.write(perm[i])
        f.close()
    return number_files


#**************************
#Helper script to write files
#***************************

#Reads sentences from extract and
#creates a randomly permuted array 
#with each of them
f = open("text.txt", "r")
arr=f.read().split("\n")
print(len(arr))
perm = np.random.permutation(arr)
f.close()

#Creates folders ans file randomly with at most
#4 levels of depth
path="./files/"
os.system("mkdir "+ path )
i=0
while i < 8700:
    path="./files/"
    if random.uniform(0, 1)>0.20:
        folder_name="folder_"+randomString()
        path+=folder_name+"/"
        os.system("mkdir "+ path )
        i+=write_files(path)
        if random.uniform(0, 1)>0.20:
            folder_name="folder_"+randomString()
            path+=folder_name+"/"
            os.system("mkdir "+ path )
            i+=write_files(path)
            if random.uniform(0, 1)>0.20:
                folder_name="folder_"+randomString()
                path+=folder_name+"/"
                os.system("mkdir "+ path )
                i+=write_files(path)
                if random.uniform(0, 1)>0.20:
                    folder_name="folder_"+randomString()
                    path+=folder_name+"/"
                    os.system("mkdir "+ path )
                    i+=write_files(path)
   
    number_files= int(random.uniform(10, 25))
    for j in range(number_files):
        f = open(path+randomString(int(random.uniform(8, 25)))
            +".txt", "a")
        f.write(perm[i])
        f.close()
        i+=1

print(randomString())
#os.system("mkdir e")


