import time ,sys ,os

# color...
BL,Bl,R,G,Y,B,P,C,W = [
    '\033[0;30m', # black
    '\033[1;30m', # grey
    '\033[0;31m', # red
    '\033[0;32m', # green
    '\033[0;33m', # yellow
    '\033[0;34m', # blue
    '\033[0;35m', # purple
    '\033[0;36m', # cyan
    '\033[0;37m', # white
]
class Color:
    clm = []
    clb = [BL,Bl,R,G,Y,B,P,C,W]
    def reader(text):
        text = text.replace('Bl#',Color.clb[1])
        text = text.replace('R#',Color.clb[2])
        text = text.replace('G#',Color.clb[3])
        text = text.replace('Y#',Color.clb[4])
        text = text.replace('B#',Color.clb[5])
        text = text.replace('P#',Color.clb[6])
        text = text.replace('C#',Color.clb[7])
        text = text.replace('W#',Color.clb[8])
        return text

    def remove_c(self,text):
        remove_c = [BL,Bl,R,G,Y,B,P,C,W]+self.clm+[
            '\033[1;30m', # grey
            '\033[1;31m', # red
            '\033[1;32m', # green
            '\033[1;33m', # yellow
            '\033[1;34m', # blue
            '\033[1;35m', # purple
            '\033[1;36m', # cyan
            '\033[1;37m', # white
        ]
        for i in remove_c:
            text = text.replace(i,'')
        return text

    @classmethod
    def Theme(cls,type):
        if type == 'dark':
            cls.clb = [BL,Bl,R,G,Y,B,P,C,W]
        elif type == 'light':
            cls.clb = [
                '\033[0;30m', # black
                '\033[1;30m', # grey
                '\033[1;31m', # red
                '\033[1;32m', # green
                '\033[1;33m', # yellow
                '\033[1;34m', # blue
                '\033[1;35m', # purple
                '\033[1;36m', # cyan
                '\033[1;37m', # white
            ]
        else:
            raise NameError(['dark','light'])

    @classmethod
    def add(cls,*args):
        for i in args:
            cls.clm.append(i)

# fix AttributeError (str) [Color funciton crash with Color Class]
Color_ = Color
#-------------

class ProFunctions:
    def Measure_Sides_text(self,text):
        text = Color().remove_c(text)
        text = text.split('\n')
        top = 0
        right = 0
        down = 0
        width = 0

        # height
        temp2 = []
        height = []
        temp = False
        for i in text:
            if i == '' and temp is False:
                pass
            else:
                temp = True
                temp2.append(i)
        temp = False
        for i in temp2[::-1]:
            if i == '' and temp is False:
                pass
            else:
                temp = True
                height.append(i)

        check_up = []
        # to git the top
        for i in text:
            if i == '':
                top += 1
            else:
                break
        # to git the down
        for i in range(1,len(text)):
            i = int('-'+str(i))
            if text[i] == '':
                down += 1
            else:
                break
        # to git the right
        text = text[top:len(text)]
        text = text[0:len(text)-down]
        for i in text:
            if i == '':
                check_up.append(999) # if text is None it will take 999
            else:
                for space in i:
                    if space == ' ':
                        right += 1
                    else:
                        break
                check_up.append(right)
                right = 0
        try:
            right = sorted(check_up)[0]
        except IndexError:
            raise TypeError('The text must not be empty')
        check_up.clear()
        # to git the width
        for i in text:
            for Width in i:
                width += 1
            check_up.append(width)
            width = 0
        width = sorted(check_up)[-1]-right
        check_up.clear()
        return [top,right,down,width,len(height)]

    # text position...
    def CTL2(self,text,top,right,down):
        style = ''
        text = text.split('\n')
        # spaces top
        style = style+('\n'*top)
        # spaces right
        for i in text:
            style = style+(' '*right)+i+'\n'
        # spaces down
        style = style+'\n'*(down)
        return style[0:-2]

    def square(self,text,SQ,Colors):
        Width = self.Measure_Sides_text(text)
        Width = Width[3]+Width[1]
        height = len(text.split('\n'))
        Sides = text.split('\n')
        style = ''
        style += Colors+SQ[0]+SQ[7]*Width+SQ[6]
        for i in Sides:
            L = len(Color().remove_c(i))
            style += '\n'+Colors+SQ[1]+W+i+' '*(Width-L)+Colors+SQ[5]
        style += '\n'+Colors+SQ[2]+SQ[3]*Width+SQ[4]
        return Text(True).DS(style)

    def Mix_Squares_text(self,text,space):
        how_many_squars = len(text)
        style = ''
        check_up = []
        check_up_int = 0
        # to delete spaces and put evre square in list alone
        for txt in text:
            txt = Text(True).DS(txt)
            txt = txt.split('\n')
            check_up.append(txt)
        # to put squares to gather and delete spaces...
        for i in range(0,len(check_up[0])):
            for Square in range(0,how_many_squars):
                try:
                    style +=  check_up[Square][i]+' '*space
                except IndexError:
                    raise TypeError('The text must be Equal (\\n)')
            style += '\n'
        style = Text(True).DS(style)
        return style

    def Equal(self,*text):
        tmp = []
        for Int,Str in enumerate(text):
            tmp += [f'{Str}']
        text = tmp
        tmp = []
        for i in text:
            tmp += [len(Color().remove_c(i))]
        Len = sorted(tmp)[-1]
        tmp = []
        for i in text:
            i = f"{' '*((Len-len(Color().remove_c(i)))//2)}{i}"
            tmp += [f'{i}{" "*(Len-len(Color().remove_c(i)))}']
        text = tmp
        return text

class Text(ProFunctions):
    def __init__(self,text):
        self.TEXT = Color.reader(str(text))

    # figlet ...
    def Figlet(self):
        text = self.TEXT
        text = os.popen('figlet "%s"'%text).read()
        _text = ''
        for i in text.split('\n')[0:-2]:
            _text += i+'\n'
        return _text[0:-1]

    # toilet ...
    def Toilet(self):
        text = self.TEXT
        text = os.popen('toilet -f mono12 "%s"'%text).read()
        _text = ''
        for i in text.split('\n')[2:-3]:
            _text += i+'\n'
        return _text[0:-1]

    # Measure the Text and get the Spaces ...
    def GS(self):
        text = self.TEXT
        MST = self.Measure_Sides_text(text)
        return {
        'top':MST[0],
        'right':MST[1],
        'down':MST[2],
        'Size':{'height':MST[3],'width':MST[4]},
        }

    # Change text location ...
    def CTL(self,top=0,right=0,down=0):
        text = self.TEXT
        style = ''
        text = text.split('\n')
        # spaces top
        style = style+('\n'*top)
        # spaces right
        for i in text:
            style = style+(' '*right)+i+'\n'
        # spaces down
        style = style+'\n'*(down)
        return style[0:-2]

    # delete Spaces pro(sprit)...
    def DS(self,text):
        sides = self.Measure_Sides_text(text)
        text = text.split('\n')
        style = ''
        check_up = 0
        # delete top spaces [\n]
        for i in range(sides[0]):
            text.remove(text[0])
        for i in text:
            if i == '':
                style += '\n'
                text.remove(text[0])
            else:
                break
        # delete right spaces
        for i in text:
            check_up = sides[1]
            for x in i:
                if check_up>0:
                    check_up -= 1
                else:
                    style += x
            style += '\n'
        check_up = 0
        # delete down spaces
        text = style[0:len(style)-sides[2]-1]
        # delete left space
        text_x = ''
        text_y = ''
        style = ''
        for i in text.split('\n'):
            text_x += i[::-1]+'\n'
        text_x = text_x[0:-1]
        sides = self.Measure_Sides_text(text_x)
        check_up = 0
        for i in text_x.split('\n'):
            check_up = sides[1]
            for x in i:
                if check_up>0:
                    check_up -= 1
                else:
                    style += x
            style += '\n'
        for i in style[0:-1].split('\n'):
            text_y += i[::-1]+'\n'
        return text_y[0:-1]

class Style(ProFunctions):
    def __init__(self,*args):
        self.args = [Color.reader(str(i)) for i in args]

    # text in Square ...
    def Square(self,Square=['╔','║','╚','═','╝','║','╗','═'],space=0,padding_x=0,padding_y=0,Color='R#',cols=False,Equal=True):
        Square = [Color_.reader(i) for i in Square]
        Color = Color_.reader(Color)
        text = self.args
        if Equal:
            text = self.Equal(*self.args)
        Style = []
        xs = []
        STYLE = ''
        if not cols:
            cols = len(text)
        for i in text:
            _i = ''
            for x in i.split('\n'):
                _i += (' '*padding_x)+x+(' '*padding_x)+'\n'
            _i = _i[0:-1]
            Style.append(self.square(str( ('\n'*padding_y)+_i+('\n'*padding_y)),Square,Color))
        cols = cols
        temp = 0
        for i in range(0,len(Style),cols):
            temp += cols
            xs.append(Style[i:temp])
        for i in xs:
            STYLE += self.Mix_Squares_text(i,space)+'\n'
        return STYLE[0:-1]

    # Texts in the Middle ...
    def Center(self):
        args = self.args
        style = ''
        temp = [self.Measure_Sides_text(i)[3] for i in args]
        temp2 = sorted(temp)[-1]
        bigest = self.Measure_Sides_text(args[temp.index(temp2)])
        for i in args:
            i += ' '
            width = self.Measure_Sides_text(i)[3]
            right = self.Measure_Sides_text(i)[1]
            style += self.CTL2(i,0,(((temp2+1)//2)-(width//2)),0)+'\n'
        return style[0:-1]

class Animation:
    # to write text by Index(System) slow motion
    def SlowText(text,t=0.1,end=False):
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(t)
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # to write text by line(Index) as slow motion
    def SlowIndex(text,t=0.01,end=False):
        for i in range(0,len(text)):
            time.sleep(t)
            print(text[i],end='')
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # to write text by Line as slow motion
    def SlowLine(text,t=0.5,end=False):
        for i in text.split('\n'):
            print(i,end='\n' if end == False else end if text.split('\n')[-1] == i else '\n')
            time.sleep(t)

    # python for ever...-
    def Text(CLT=G,CUT=W,t=0.2,text='C#tB#eG#xP#t',AT='Animation',repeat=2,end=False):
        CUT = Color.reader(CUT)
        CLT = Color.reader(CLT)
        AT=' '+AT+' '
        text = Color.reader(str(text))
        print(W+text+CLT+AT,end='\r')
        for i in range(repeat):
            for i in range(0,len(AT)):
                print(W+text+CLT+AT[:i].lower()+CUT+AT[i].upper(),end='\r')
                time.sleep(t)
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # Loading animation...
    def Loading(AT=['|','/','-','\\'],text='text...',t=0.1,repeat=10,end=False):
        text = Color.reader(str(text))
        W = Color.reader('W#')
        for i in range(repeat):
            for i in range(0,len(AT)):
                ASA = Color.reader(str(AT[i]))
                print(W+text+ASA,end='\r')
                time.sleep(t)
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # Downloading animation...
    # Animation should be list
    def DL(AT=['B#│','G#█','C#▒','B#│'],text='Loading',t=0.2,width=25,end=False):
        text = Color.reader(str(text))
        AT = [Color.reader(str(i)) for i in AT]
        y = width+1
        for i in range(width+1):
            print('\r'+W+text+AT[0]+(i*AT[1])+(AT[2]*(y-1))+AT[3]+' ',end='')
            time.sleep(t)
            y -= 1
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    def DWeb(self):
        pass
