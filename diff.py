from os import listdir
import os.path

#Working similaly to diff -y bin_dump_helloStriped_FUN_00118890 bin_dump_tcp_sever__print

array={}
path="./bytecode_comp/"
for e in listdir(path): #load all byte code strings in the path
    if os.path.isfile(os.path.join(path,e)):
        with open(os.path.join(path,e),"r") as file:
            array[e] = file.read()


str = ""
for i in range(0, min([len(slicing) for slicing in array.values()])): #Compare the sings and set * if they differ
    vgl=None
    for source in array.values():
        if vgl == None:
            vgl = source[i]
        elif vgl != "*" and source[i] != vgl:
            vgl = "*"
    str += vgl.strip()

print(str) #Print the output and write in into output file 
with open("diff_print", "w") as file:
    file.write(str)


    
    
