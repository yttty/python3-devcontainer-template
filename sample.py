import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("Hello {}!".format(sys.argv[1]))
    else:
        print("Hello dev-container!")
