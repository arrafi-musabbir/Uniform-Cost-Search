
'''
the following section reads from a text file that contains a graph of cities
and cost between cities
'''


class FileRead:
    # this class takes a weighted txt file and initilizes it in a dictionary
    def __init__(self):
        self.wd = dict()

    def readFile(self, path):
        # this method read a weighted file and initializes it to a dictionary
        with open(path, 'r') as f:
            for i in f:
                ltemp = i.split()
                if len(ltemp) == 1:
                    self.wd[ltemp[0]] = None
                else:
                    self.wd[ltemp[0]] = dict()
                    for i in range(0, len(ltemp)):
                        if 2 * i + 1 < len(ltemp) and 2 * i + 2 < len(ltemp):
                            self.wd[ltemp[0]][ltemp[2 * i + 1]] = \
                             int(ltemp[2 * i + 2])
        return self.wd

    def showDict(self):
        for i in self.wd:
            print(i, ':', self.wd[i])
        return None
