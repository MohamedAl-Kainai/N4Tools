import time ,sys ,os

class Color:
    Colors = {
            # Dark
            "W#":"\033[0;37m", # Wihte
            "R#":"\033[0;31m", # Red
            "G#":"\033[0;32m", # Green
            "Y#":"\033[0;33m", # Yellow
            "B#":"\033[0;34m", # Blue
            "P#":"\033[0;35m", # Pink
            "C#":"\033[0;36m", # Cyan
            "g#":"\033[1;30m", # Gray

            # Light
            "WL#":"\033[1;37m", # Wihte
            "RL#":"\033[1;31m", # Red
            "GL#":"\033[1;32m", # Green
            "YL#":"\033[1;33m", # Yellow
            "BL#":"\033[1;34m", # Blue
            "PL#":"\033[1;35m", # Pink
            "CL#":"\033[1;36m", # Cyan

            # Dark
            "W@":"\033[7m", # bg Wihte
            "R@":"\033[41m", # bg Red
            "G@":"\033[42m", # bg Green
            "Y@":"\033[43m", # bg Yellow
            "B@":"\033[44m", # bg Blue
            "P@":"\033[45m", # bg Pink
            "C@":"\033[46m", # bg Cyan
            "g@":"\033[47m", # bg Light gray

            # Light
            "RL@":"\033[101m", # bg Light Red
            "GL@":"\033[102m", # bg Light Green
            "YL@":"\033[103m", # bg Light Yellow
            "BL@":"\033[104m", # bg Light Blue
            "PL@":"\033[105m", # bg Light Pink
            "CL@":"\033[106m", # bg Light Cyan
            "gL@":"\033[100m", # bg Light Light gray

            "##":"\033[0m", # Normal
            "BB#":"\033[1m", # Bold/Bright
            "UL#":"\033[4m", # Underlined
            "B*#":"\033[5m", # Blink
    }
    @classmethod
    def reader(cls,text):
        for name,color in cls.Colors.items():
            text = text.replace(name,color)
        return text

    @classmethod
    def del_colors(cls,text):
        for name,color in cls.Colors.items():
            text = text.replace(name,'')
            text = text.replace(color,'')
        return text

    @classmethod
    def add(cls,Dict):
        for name,color in Dict.items():
            if name in cls.Colors:
                raise TypeError(f'{name} is already in use by Class Color...\n\
                To fix Error change the {name} to another name')
            for i in cls.Colors:
                if i in name:
                    raise TypeError(f'{i} is already in {name}...\n\
                    \rTo fix Error change the {name} to another name')
            cls.Colors[name] = color

    @classmethod
    def show_all_fgbg(cls):
        temp = 0
        text = 'type : Foreground...\n'
        for type in [38,48]: # Foreground / Background
            text += '\n\ntype : Background...\n' if type==48 else ''
            for i in range(255):
                temp += 1
                _txt = '{}{:4d} \033[0m'.format(f'\033[{type};5;{i+1}m',i+1)
                if temp > 8:
                    text += _txt+'\n'
                    temp = 0
                else:
                    text += _txt
                temp += 1
        print (text)

    @classmethod
    def fgbg_color(cls,type='FG',fgbg=7):
        '''
        type :
            FG : Foreground
            BG : Background
        fgbg : (int)
        '''
        if type not in ['FG','BG']:
            raise TypeError('please choose BG or FG')
        return f'\033[{38 if type=="FG" else 48};5;{fgbg}m'

# fix AttributeError (str) [Color funciton crash with Color Class]
Color_ = Color
#-------------

class ProFunctions:
    def Measure_Sides_text(self,text):
        text = Color.del_colors(text)
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
            L = len(Color.del_colors(i))
            style += '\n'+Colors+SQ[1]+'\033[0m'+i+' '*(Width-L)+Colors+SQ[5]
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
            tmp += [len(Color.del_colors(i))]
        Len = sorted(tmp)[-1]
        tmp = []
        for i in text:
            i = f"{' '*((Len-len(Color.del_colors(i)))//2)}{i}"
            tmp += [f'{i}{" "*(Len-len(Color.del_colors(i)))}']
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

    # to write text by Line as slow motion
    def SlowLine(text,t=0.5,end=False):
        for i in text.split('\n'):
            print(i,end='\n' if end == False else end if text.split('\n')[-1] == i else '\n')
            time.sleep(t)

    # python for ever...-
    def Text(CLT='G#',CUT='W#',t=0.2,text='C#tB#eG#xP#t',AT='Animation',Loading=False,repeat=2,end=False):
        CUT = Color.reader(CUT)
        CLT = Color.reader(CLT)
        AT=AT+' '
        text = Color.reader(str(text))
        temp = 0
        def Anim():
            temp1 = text+CLT
            temp2 = AT[:i].lower()+CUT
            temp3 = AT[i].upper()+CLT
            temp4 = AT[i+1:].lower()
            text_AT = '\r'+temp1+temp2+temp3+temp4
            if Loading:text_AT = '\r'+temp1+temp2+temp3+temp4+Loading[temp]
            sys.stdout.write(text_AT)
            time.sleep(t)
        print(text+CLT+AT,end='\r')
        for i in range(repeat):
            for i in range(0,len(AT)):
                if Loading:
                    if temp < len(Loading)-1:
                        temp += 1
                        Anim()
                    else:
                        temp = 0
                        Anim()
                else:
                    Anim()
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # Loading animation...
    def Loading(AT=['|','/','-','\\'],text='W#text...',t=0.1,repeat=10,end=False):
        text = Color.reader(str(text))
        W = Color.reader('W#')
        for i in range(repeat):
            for i in range(0,len(AT)):
                ASA = Color.reader(str(AT[i]))
                sys.stdout.write('\r'+text+ASA+' ')
                time.sleep(t)
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    # Downloading animation...
    # Animation should be list
    def DL(AT=['B#│','G#█','C#▒','B#│'],text='W#Loading',t=0.2,width=25,end=False):
        text = Color.reader(str(text))
        AT = [Color.reader(str(i)) for i in AT]
        y = width+1
        for i in range(width+1):
            sys.stdout.write('\r'+text+AT[0]+(i*AT[1])+(AT[2]*(y-1))+AT[3]+' ')
            time.sleep(t)
            y -= 1
        if end:
            print(Color.reader(end),end='')
        elif end == False:
            print('')

    def DWeb(self):
        pass
