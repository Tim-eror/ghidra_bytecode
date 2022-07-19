from baum import *
from os import listdir
import os.path

def mokup():
    b = Baum("")
    b.insert("felix","1")
    b.insert("fe23lopi","2")
    b.insert("re*ee","3")
    b.insert("fe2opop","4")
    b.insert("reeop","5")
    b.insert("fel*x","6")
    b.insert("felix123","7")
    b.insert("fefufumm","8")
    dump = b.dump()
    print("tree dumped\n")
    print(dump)
    b2 = Baum.pmud(dump)
    print("\n\n\ntree parsed\n")
    print(b2)


def main():
    b = Baum()
    path="./bytecode_dump/"
    for e in listdir(path): #load all byte code strings in the path
        if os.path.isfile(os.path.join(path,e)) and e.endswith(".diff"):
            with open(os.path.join(path,e),"r") as file:

                b.insert(file.read(),e)
            
    with open("bytecode_dump/tcp_relase__print.bin") as o:
        print(b.search(o.read()))
    b.show()

if __name__ == "__main__":
    # main()
    mokup()
