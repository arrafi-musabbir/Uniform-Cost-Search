
'''
the following section reads from a text file that contains a graph of cities
and cost between cities
'''


class FileRead:
    # this class takes a weighted txt file and initilizes it in a dictionary
    def __init__(self, path):
        self.path = path
        self.readFile()

    def readFile(self):
        wd = dict()
        with open(self.path, 'r') as f:
            for i in f:
                ltemp = i.split()
                if len(ltemp) == 1:
                    wd[ltemp[0]] = None
                else:
                    wd[ltemp[0]] = dict()
                    for i in range(0, len(ltemp)):
                        if 2 * i + 1 < len(ltemp) and 2 * i + 2 < len(ltemp):
                            wd[ltemp[0]][ltemp[2 * i + 1]] = \
                             int(ltemp[2 * i + 2])
        print("here")
        return wd
