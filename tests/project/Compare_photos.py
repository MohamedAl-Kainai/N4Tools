# N4Tools version 1.7.1
import random, os, time
from N4Tools.Design import Square,Text
size = 12
Sq = Square()
Sq.padding = [1,0,1,0]

def SquareList():
    return [[random.choice([1,0]) for i in range(size)] for i in range(size//2)]

def percentage(part, whole):
    return 100 * float(part)/float(whole)

os.system('clear')
while True:
    equal = 0
    allX = 0
    allY = 0
    x = SquareList()
    y = SquareList()
    dataX = ''
    dataY = ''
    for x,y in zip(x,y):
        for rowX,rowY in zip(x,y):
            if rowX:
                allX += 1
                if rowY:
                    dataX += '[$GREEN]#[$/]'
                    equal += 1
                else: dataX += '#'
            else:dataX += ' '
            if rowY:
                allY += 1
                if rowX:
                    dataY += '[$GREEN]#[$/]'
                    equal += 1
                else: dataY += '#'
            else:dataY += ' '
        dataX += '\n'
        dataY += '\n'

    x = Sq.base(dataX[:-1])
    y = Sq.base(dataY[:-1])
    print (Text().mix([x,y],spacing=2))
    print (f'[x:{allX}, y:{allY}] [equal:{equal}] [{round(percentage(equal,allX+allY))} % 100]        ')
    time.sleep(.5)
    print(chr(27)+'[H',end='')
