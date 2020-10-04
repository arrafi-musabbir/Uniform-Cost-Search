
'''
Created on Sat Oct 02 17:13:02 2020
@author: ARRAFI
'''

import UCS_algo as UC
import FileRead

f = FileRead.FileRead('D:/github/Uniform-Cost-Search/Weighted graph(cities).txt')

print()
#w = f.readFile()

u = UC.UCS(dic=f, start='s', goal='g')

#u.ucs()
