import os.path as path
def getOutImagePath(file):
    dir, filename =  path.split(file)
    return path.normpath(path.join(dir, "..\img", path.splitext(filename)[0]+".png"))
#unit test
if __name__ == "__main__":
    print getOutImagePath(__file__)
