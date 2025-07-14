import logging
from todo import ToDo

def main():
    logging.basicConfig(level=logging.INFO)

    lst = ToDo()
    lst.show()
    lst.add("Постирать левый носок")
    lst.show()
    lst.show_completed()
    
    lst.add("Погладить правый носок")
    lst.show()
    lst.complete(1)
    lst.complete(2)

    lst.show()
    lst.show_completed()
    lst.remove(1)
    lst.show_completed()

if __name__ == "__main__":
    main()