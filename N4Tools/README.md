# N4Tools
##### What is N4Tools?
It is a library that contains a set of ready-made codes that enable you to create the most wonderful designs on the terminal.
#### example:
```python
from N4Tools.Design import Text, Square, Color

class MyToolDesign:
    T = Text()
    SQ = Square()
    CO = Color()
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
        return self.T.Figlet('vairus7x',font='big')

    def Tools(self):
        tools = self.tools
        tools = [f'- [$LYELLOW]{t.upper()} [$LGREEN][[$RED]{num+1}[$LGREEN]]' for num ,t in enumerate(tools)]
        tools = self.T.equal(tools)
        output = ''
        design1 = '\n\n[$RED]--[[$LYELLOW]v7x[$RED]]--'
        design2 = self.SQ.color+( ' '+('|-'*10)+'|-   V7X-Team   -|'+('-|'*10) )
        temp = -1
        while True:
            try:
                item = '\n'+self.T.mix([
                    self.SQ.style([tools[temp+1]]),
                    design1,
                    self.SQ.style([tools[temp+2]]),
                ]).replace('══','╧╤')
                temp += 2
                if len(tools)-1 != temp:
                    item = self.T.CentreAlignPro([item,design2])
                output += item
            except IndexError:break
        return output

    def print_style(self):
        output = self.T.CentreAlignPro([self.Title(),self.Tools()])
        print (output+'\n')
        while True:
            user = input(self.CO.RED+'Enter number: ')
            try:
                print (self.tools[int(user)-1].upper())
                break
            except IndexError:
                print ('Not Found!')

if __name__ == '__main__':
    MyToolDesign().print_style()
```
output:
![Screenshot 2020-11-18 124019](https://user-images.githubusercontent.com/56244233/99526680-e3982200-299b-11eb-871d-41c799e63454.png)