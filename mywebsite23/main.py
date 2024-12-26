import os

class Test:
    def __init__(self):
        f = open("temp.csv","w")
        f.write("data,more data,testing")
        f.close()

    def __del__(self):
        os.remove('temp.csv')
        print("CleanUp done!")

firstItem = Test()