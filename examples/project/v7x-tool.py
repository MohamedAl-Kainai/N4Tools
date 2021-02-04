# N4Tools version 1.7.1
from N4Tools.Design import (
    Text,
    Square,
    Color,
    Animation,
    ThreadAnimation
)

T = Text()
CO = Color()
A = Animation()

class MyToolDesign:
    SQ = Square()
    def __init__(self):
        self.SQ.color = '[$LRED]'
        self.SQ.padding = [1,1,1,1]

        self.tools = [
            'Texmux tools', 'Linux on android',
            'DOS,DDOS Attacks', 'Info gathering',
            'Scan everything', 'Social engner',
            'Info about us', 'Exit the v7x',
            'adfsds', 'Name',
        ]

    def Title(self):
        return T.Figlet('vairus7x',font='big')

    def Tools(self):
        tools = self.tools
        tools = [f'- [$LYELLOW]{t.upper()} [$LGREEN][[$RED]{num+1}[$LGREEN]]' for num ,t in enumerate(tools)]
        tools = T.equal(tools)
        output = ''
        design1 = '\n\n[$RED]--[[$LYELLOW]v7x[$RED]]--'
        design2 = self.SQ.color+( ' '+('|-'*10)+'|-   V7X-Team   -|'+('-|'*10) )
        temp = -1
        while True:
            try:
                item = '\n'+T.mix([
                    self.SQ.style([tools[temp+1]]),
                    design1,
                    self.SQ.style([tools[temp+2]]),
                ]).replace('══','╧╤')
                temp += 2
                if len(tools)-1 != temp:
                    item = T.CentreAlignPro([item,design2])
                output += item
            except IndexError:break
        return output

    def main(self):
        @ThreadAnimation(Animation=A.Loading,kwargs={'text':'Loading [style]...'})
        def load_style(Thread):
            output = T.CentreAlignPro([self.Title(),self.Tools()])
            Thread.kill()
            print (output+'\n')
        load_style()
        while True:
            user = T.CInput(CO.RED+'Enter number: ')
            try:
                print (self.tools[int(user)-1].upper())
                break
            except :
                print ('Not Found!')

if __name__ == '__main__':
    MyToolDesign().main()