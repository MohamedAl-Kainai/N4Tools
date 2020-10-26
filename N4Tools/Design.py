import time ,sys ,os

class Color(str):
    colors = {
        "BOLD":"\033[1m",
        "UNDERLINE": "\033[4m",
        "BLINK": "\033[5m",
        "NORMAL": "\033[0m",

        "WIHTEBG": "\033[7m",
        "REDBG": "\033[41m",
        "GREENBG": "\033[42m",
        "YELLOWBG": "\033[43m",
        "BLUEBG": "\033[44m",
        "PINKBG": "\033[45m",
        "CYANBG": "\033[46m",
        "GRAYBG": "\033[100m",

        "LREDBG": "\033[101m",
        "LGREENBG": "\033[102m",
        "LYELLOWBG": "\033[103m",
        "LBLUEBG": "\033[104m",
        "LPINKBG": "\033[105m",
        "LCYANBG": "\033[106m",
        "LGRAYBG": "\033[47m",

        "WIHTE": "\033[0;37m",
        "RED": "\033[0;31m",
        "GREEN": "\033[0;32m",
        "YELLOW": "\033[0;33m",
        "BLUE": "\033[0;34m",
        "PINK": "\033[0;35m",
        "CYAN": "\033[0;36m",
        "GRAY": "\033[1;30m",

        "LWIHTE": "\033[1;37m",
        "LRED": "\033[1;31m",
        "LGREEN": "\033[1;32m",
        "LYELLOW": "\033[1;33m",
        "LBLUE": "\033[1;34m",
        "LPINK": "\033[1;35m",
        "LCYAN": "\033[1;36m",
    }
    def __dir__(self):
        return list(set(dir(__class__)+[attr for attr in self.colors.keys()]))

    def __getattr__(self, item):
        if item in self.colors:
            COLOR = self
            return COLOR.__class__(self.colors[item])
        else: raise AttributeError(f"type object '{__class__.__name__}' has no attribute '{item}'")

    def __add__(self, other):
        return super().__add__(other)+self.NORMAL

    def reader(self,text:str) -> str:
        '''Read the Colors from string'''
        if type(text) != str:
            raise TypeError(f'reader function accept only string not ({type(text).__name__}: {text})')
        for name,color in self.colors.items():
            text = text.replace('[$'+name+']',color)
        return text

    def del_colors(self,text:str) -> str:
        '''Remove colors from string'''
        if type(text) != str:
            raise TypeError(f'del_colors function accept only string not ({type(text).__name__}: {text})')
        for name,color in self.colors.items():
            text = text.replace('[$'+name+']','')
            text = text.replace(color,'')
        return text

    def show_all_rgb_colors(self):
        '''Simple example to show all rgb colors'''
        temp = 0
        text = 'type : Foreground...\n'
        for type in [38,48]:
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

    def rgb(cls,rgb:int,type='FG') -> str:
        '''
        type :
            FG : Foreground
            BG : Background
        rgb : (int)
        '''
        if type not in ['FG','BG']:
            raise TypeError('please choose BG or FG')
        if rgb > 255 or rgb < 1:
            raise Exception("rgb max '255' ")
        return f'\033[{38 if type=="FG" else 48};5;{rgb}m'

class Text:
    def get_size(self,text:str) -> dict:
        '''Get the text size [width,height]'''
        if type(text) != str:
            raise TypeError(f'get_size function accept only string not ({type(text).__name__}: {text})')
        text = Color().del_colors(text)
        width = sorted([len(i) for i in text.split('\n')])[-1]
        height = len(text.split('\n'))
        return {'width':width,'height':height}

    def del_padding(self,text:str) -> str:
        '''Delete text padding'''
        if type(text) != str:
            raise TypeError(f'del_padding function accept only string not ({type(text).__name__}: {text})')
        def delete_top(text:str) -> str:
            text = text.split('\n')
            result = []
            top_space = True
            for t in text:
                if (list(Color().del_colors(t)) == [] or list(set(list(Color().del_colors(t)))) == [' ']) and top_space:
                    pass
                else:
                    top_space = False
                    result.append(t)
            return '\n'.join(result)

        def delete_bottom(text:str) -> str:
            text = text.split('\n')[::-1]
            result = []
            bottom_space = True
            for t in text:
                if (list(Color().del_colors(t)) == [] or list(set(list(Color().del_colors(t)))) == [' ']) and bottom_space:
                    pass
                else:
                    bottom_space = False
                    result.append(t)
            return '\n'.join(result[::-1])

        def delete_left(text:str) -> str:
            text = text.split('\n')
            left_space = []
            temp = None
            for t in text:
                for space in list(t):
                    if space == ' ': temp = 1 if temp == None else temp+1
                    else: break
                if temp != None:left_space.append(temp)
                temp = 0
            return '\n'.join([string[sorted(left_space)[0]:] for string in text])
        return delete_left( delete_bottom( delete_top(text) ) )

    def pos(self,text:str,x=0,y=0) -> str:
        '''Change text postion'''
        '''Change text postion'''
        if type(text) != str:
            raise TypeError(f'pos function accept only string not ({type(text).__name__}: {text})')
        text = text.split('\n')
        style = '\n'*y
        for i in text:
            style = style+(' '*x)+i+'\n'
        return style[:-1]

    def CentreAlign(self,text:str) -> str:
        '''Put the Text in the Middle'''
        if type(text) != str:
            raise TypeError(f'CentreAlign function accept only string not ({type(text).__name__}: {text})')
        text_size = self.get_size( Color().del_colors(text) )['width']
        result = []
        for t in text.split('\n'):
            if len(Color().del_colors(t)) == text_size:
                result.append(t)
            else:
                result.append(
                    self.pos(
                        t,
                        x=(text_size//2)-(len(Color().del_colors(t))//2)
                    )
                )
        return '\n'.join(result)

class Square:
    def __init__(self):
        self.SETTINGS = {
            'square':['╔', '║', '╚', '═', '╝', '║', '╗', '═'],
            'space':0,
            'padding':[0,0,0,0],
            'color':'[$GREEN]',
            'cols':False,
            'equal':True,
        }

    def style(self,text:str) -> str:
        text = self._square_base(text)
        return text

    def set_settings(self,settings:dict) -> dict:
        for key,item in settings.items():
            if key == 'square':
                if type(item) == list and len(item) == 8:
                    self.SETTINGS[key] = item
                else: raise TypeError('square accept only list and len list should be 8')

            elif key == 'space':
                if type(item) == int:
                    self.SETTINGS[key] = item
                else: raise TypeError('space accept only (int)')

            elif key == 'padding':
                if type(item) == list and len(item) == 4:
                    self.SETTINGS[key] = item
                else: raise TypeError('padding accept only (list) and 4 items')

            elif key == 'color':
                if type(item) == str:
                    if item.replace('[$','').replace(']','') in Color().colors.keys() or item in [_color[1] for _color in Color().colors.items()]:
                        self.SETTINGS[key] = item
                    else: raise TypeError(f'color accept only {["[$"+c+"]" for c in Color().colors.keys()]}')
                else: raise TypeError('color accept only (str)')

            elif key == 'cols':
                if type(item) == bool:
                    self.SETTINGS[key] = item
                else: raise TypeError('cols accept only (bool)')

            elif key == 'equal':
                if type(item) == bool:
                    self.SETTINGS[key] = item
                else: raise TypeError('equal accept only (bool)')

            else: raise TypeError(f"'{key}' is not in settings, use only {[key for key in self.SETTINGS.keys()]}")

        return self.SETTINGS

    def _square_base(self,text):
        PADDING = self.SETTINGS['padding']
        text = Text().pos(text,x=PADDING[0])
        text = ('\n'*PADDING[1]) + text + ('\n'*PADDING[3])
        text_size = Text().get_size(Color().del_colors(text))
        text_size = {'width':text_size['width']+PADDING[2]}
        SQUARE = self.SETTINGS['square']
        COLOR = self.SETTINGS['color']

        output = (COLOR if COLOR else '[$NORMAL]')+SQUARE[0]+(SQUARE[7]*text_size['width'])+SQUARE[6]+'[$NORMAL]' # .......... ╔═════╗
        for t in text.split('\n'):
            t_size = Text().get_size(Color().del_colors(t))
            output += '\n'+(COLOR if COLOR else '[$NORMAL]')+(SQUARE[1]+'[$NORMAL]'+t) # ..................................... ║
            output += (
                (
                    (COLOR if COLOR else '[$NORMAL]')+SQUARE[5] # .................................................................. ║
                ) if t_size['width'] == text_size['width'] else (
                    ' '*(text_size['width']-t_size['width'])+
                    (COLOR if COLOR else '[$NORMAL]')+SQUARE[5]+'[$NORMAL]' # space space space space space space space space space  ║
                )
            )
        output += '\n'+(COLOR if COLOR else '[$NORMAL]')+SQUARE[2]+(SQUARE[3]*text_size['width'])+SQUARE[4]+'[$NORMAL]' # .... ╚═════╝
        return Color().reader(output)

if __name__ == '__main__':
    def text_in_square(text):
        SQ = Square()
        SQ.set_settings({
            'padding':[1,0,1,0],
            'color':'\033[0;36m',
        })
        return SQ.style(text)

    text = 'Mohamed'
    print (text_in_square(text))

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
