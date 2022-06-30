from baum import *

def main():
    b = Baum("")
    b.show()
    b.insert("felix")
    b.show()
    b.insert("fel*x")
    b.show()
    b.insert("felix123")
    b.show()

if __name__ == "__main__":
    main()
