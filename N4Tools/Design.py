import time ,sys ,threading

__all__ = ['Color','Text','Square','Animation','ThreadAnimation']

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
            return self.__class__(self.colors[item])
        else: raise AttributeError(f"type object '{__class__.__name__}' has no attribute '{item}'")

    def __add__(self, other):
        return super().__add__(other)+self.NORMAL

    def reader(self,text:str) -> str:
        '''Read the Colors from string'''
        if type(text) != str:
            raise TypeError(f'reader function accept only string not ({type(text).__name__}: {text})')
        for name,color in self.colors.items():
            text = text.replace('[$'+name+']',color)
        text = text.replace('[$/]',self.colors['NORMAL'])
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

    def rgb(self,rgb:int,type='FG') -> str:
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
        return self.__class__(f'\033[{38 if type=="FG" else 48};5;{rgb}m')

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
            try: return '\n'.join([string[sorted(left_space)[0]:] for string in text])
            except IndexError: return '\n'.join(text)
        return delete_left( delete_bottom( delete_top(text) ) )

    def pos(self,text:str,x=0,y=0) -> str:
        '''Change text postion'''
        if type(text) != str:
            raise TypeError(f'pos function accept only string not ({type(text).__name__}: {text})')
        text = text.split('\n')
        style = '\n'*y
        for i in text:
            style = style+(' '*x)+i+'\n'
        return Color().reader(style[:-1])

    def CentreAlign(self,text:str) -> str:
        '''Put the Text in the Middle'''
        if type(text) != str:
            raise TypeError(f'CentreAlign function accept only string not ({type(text).__name__}: {text})')
        text_size = self.get_size(text)['width']
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
        return Color().reader('\n'.join(result))

    def CentreAlignPro(self, ListTexts: list) -> str:
        '''Put the big Texts in the Middle'''
        if type(ListTexts) != list:
            raise TypeError(f'CentreAlign function accept only list not ({type(ListTexts).__name__}: {ListTexts})')
        width = 0
        for text in ListTexts:
            text = Color().del_colors(text)
            temp_width = self.get_size(text)
            width = temp_width['width'] if width < temp_width['width'] else width

        result = []
        for t in ListTexts:
            if self.get_size(t)['width'] == width:
                result.append(t)
            else:
                result.append(
                    self.pos(
                        t,
                        x=(width // 2) - (self.get_size(t)['width'] // 2)
                    )
                )
        return Color().reader('\n'.join(result))

    def Figlet(self,text:str,font='epic') -> str:
        try:
            import pyfiglet
        except ModuleNotFoundError or ImportError:
            sys.exit(ModuleNotFoundError('ModuleNotFoundError: No module named figlet\n\t"pip3 install pyfiglet"'))
        if font not in pyfiglet.FigletFont.getFonts():
            raise TypeError(f'Figlet not support this font! ({font})')
        FIG = pyfiglet.Figlet(font=font)
        output = FIG.renderText(text)
        output = self.del_padding(str(output))
        return output

    def FigletFonts(self) -> list:
        try:
            import pyfiglet
        except ModuleNotFoundError or ImportError:
            sys.exit(ModuleNotFoundError('ModuleNotFoundError: No module named figlet\n\t"pip3 install pyfiglet"'))
        return pyfiglet.FigletFont.getFonts()

    def mix(self,List:list,spacing=0) -> str:
        '''Mix texts together'''
        height ,output = [] ,''
        for text in List:height += [self.get_size(text)['height']]
        temp = [
            self.full(self.pos(t,x=spacing).split('\n'))+
            ([' '*(self.get_size(t)['width']+spacing)]*
             (sorted(height)[-1]-sorted(height)[0]))
            for t in List
        ]
        for text in zip(*temp):
            output += ''.join(text)+'\n'
        return Color().reader(self.del_padding(output))

    def full(self,text):
        tmp = []
        for i in text:
            tmp += [self.get_size(i)['width']]
        Len = sorted(tmp)[-1]
        tmp = []
        for i in text:
            tmp += [f'{i}{" " * (Len - self.get_size(i)["width"])}']
        return tmp

    def equal(self, text):
        tmp = []
        for i in text:
            tmp += [self.get_size(i)['width']]
        Len = sorted(tmp)[-1]
        tmp = []
        for i in text:
            i = f"{' ' * ((Len - self.get_size(i)['width']) // 2)}{i}"
            tmp += [f'{i}{" " * (Len - self.get_size(i)["width"])}']
        return tmp

    def arabic(self,text):
        try:
            import arabic_reshaper
            from bidi.algorithm import get_display
        except ModuleNotFoundError:
            raise ModuleNotFoundError('''To fix this error install this libs\n"pip install arabic_reshaper"\n"pip install python-bidi"''')

        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)

class Square:
    def __init__(self):
        self.SETTINGS = {
            'square':['╔', '║', '╚', '═', '╝', '║', '╗', '═'],
            'spacing':0,
            'padding':[0,0,0,0],
            'color':'',
            'cols':0,
            'equal':True,
            'center':False,
        }

    def __setattr__(self, key, value):
        super(Square, self).__setattr__(key,value)
        if key in self.SETTINGS:
            self.set_settings({key:value})

    def __dir__(self):
        return list(set(dir(__class__)+[attr for attr in self.SETTINGS.keys()]))

    def style(self,List:list) -> str:
        if type(List) != list:
            raise TypeError(f'style function accept only list not {List.__class__.__name__}')

        if self.SETTINGS['equal']:
            if self.SETTINGS['center']:
                List = Text().equal(List)
            else:
                List = Text().full(List)

        if self.SETTINGS['cols'] == 0:
            output = Text().mix([self.base(sq) for sq in List],spacing=self.SETTINGS['spacing'])

        else:
            output = ''
            cols = self.SETTINGS['cols']
            temp1 = 0
            temp2 = cols
            while True:
                try:
                    output += Text().mix([self.base(sq) for sq in List[temp1:temp2]],spacing=self.SETTINGS['spacing'])+'\n'
                    temp1 = temp2
                    temp2 += cols
                    if len(List) <= temp1:
                        output = output[:-1]
                        break
                except IndexError:
                    output = output[:-1]
                    break
        return output

    def set_settings(self,settings:dict) -> dict:
        for key,item in settings.items():
            if key == 'square':
                if type(item) == list and len(item) == 8:
                    self.SETTINGS[key] = item
                else: raise TypeError('square accept only list and len list should be 8')

            elif key == 'spacing':
                if type(item) == int:
                    self.SETTINGS[key] = item
                else: raise TypeError('spacing accept only (int)')

            elif key == 'padding':
                if type(item) == list and len(item) == 4:
                    self.SETTINGS[key] = item
                else: raise TypeError('padding accept only (list) and 4 items')

            elif key == 'color':
                if type(item) == str or type(item) == Color:
                    if item.replace('[$','').replace(']','') in Color().colors.keys() or item in [_color[1] for _color in Color().colors.items()]:
                        self.SETTINGS[key] = str(item)
                    else: raise TypeError(f'color accept only {["[$"+c+"]" for c in Color().colors.keys()]}')
                else: raise TypeError('color accept only (str)')

            elif key == 'cols':
                if type(item) == int:
                    self.SETTINGS[key] = item
                else: raise TypeError('cols accept only (int)')

            elif key == 'equal':
                if type(item) == bool:
                    self.SETTINGS[key] = item
                else: raise TypeError('equal accept only (bool)')

            elif key == 'center':
                if type(item) == bool:
                    self.SETTINGS[key] = item
                else: raise TypeError('center accept only (bool)')

            else: raise TypeError(f"'{key}' is not in settings, use only {[key for key in self.SETTINGS.keys()]}")

        return self.SETTINGS

    def base(self,text):
        PADDING = self.SETTINGS['padding']

        '''set padding and text size'''
        text = Text().pos(text,x=PADDING[0])
        text = ('\n'*PADDING[1]) + text + ('\n'*PADDING[3])
        text_size = Text().get_size(text)
        text_size = {'width':text_size['width']+PADDING[2]}

        SQUARE = self.SETTINGS['square']
        COLOR = self.SETTINGS['color']

        CO = (COLOR if COLOR else '[$NORMAL]')
        output = CO+SQUARE[0]+CO+(SQUARE[7]*text_size['width'])+CO+SQUARE[6]+'[$NORMAL]' # .......... ╔═════╗
        for t in text.split('\n'):
            t_size = Text().get_size(t)
            output += '\n'+CO+(SQUARE[1]+'[$NORMAL]'+t) # ........................................... ║
            output += ' '*(text_size['width']-t_size['width'])+CO+SQUARE[5]+'[$NORMAL]' # ................. ║

        output += '\n'+CO+SQUARE[2]+CO+(SQUARE[3]*text_size['width'])+CO+SQUARE[4]+'[$NORMAL]' # .... ╚═════╝
        return Color().reader(output)

class Animation:
    def Loading(self,text='Loading...',anim=['/','-','\\','|']):
        while True:
            for i in anim:
                yield text+i

    def SlowText(self,text,timer=0.1):
        '''to write text by Index(System) slow motion'''
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(timer)

    def SlowLine(self,text,timer=0.5):
        '''to write text by Line as slow motion'''
        for i in text.split('\n'):
            print(i)
            time.sleep(timer)

class ThreadAnimation:
    def __init__(self):
        self.kill = False
        self.timer = .2
        self.END = 'DONE...!'
        self.ANIMATION = None

    def set_animation(self,ANIMATION,END=None):
        '''
        to set Animation.
        example:
        ... def MyAnimation():
        ...     while True:
        ...         for i in 'Loading':
        ...             yield f'Loading...( {i} )'
        ...
        ... TA = ThreadAnimation()
        ... TA.set_animation( MyAnimation(), END='DONE...!' )
        ...
        ... with TA:
        ...     for i in range(10000000):
        ...         pass
        ... print (i)
        '''
        self.ANIMATION = ANIMATION
        self.END = END if END != None else self.END

    def thread(self,func):
        '''
        function thread.
        example:
        ... TA = ThreadAnimation()
        ... TA.set_animation( MyAnimation() )
        ...
        ... @TA.thread
        ... def my_function():
        ...     for i in range(10000000):
        ...         pass
        ...     return i
        ...
        ... print( my_function() )

        '''
        def wrapper(*args,**kwargs):
            self.__enter__()
            rv = func(*args,**kwargs)
            self.kill = True
            self.THREAD_ANIM.join()
            return rv
        return wrapper

    def __enter__(self):
        '''
        example:
        ... TA = ThreadAnimation()
        ... TA.set_animation( MyAnimation(), END='DONE...!' )
        ...
        ... with TA as thread:
        ...     for i in range(10000000):
        ...         pass
        ...     print(thread.is_alive())
        ...
        ... print (thread.is_alive())
        ... print (i)
        '''
        self.kill = False
        def anim():
            size = 0
            for text in self.ANIMATION:
                text = Color().reader(text+'[$NORMAL]')
                if self.kill:
                    print('\r'+self.END+' '*(size-len(self.END) if len(self.END) < size else 0))
                    break

                sys.stdout.write('\r'+text)
                size = len(Color().del_colors(text))
                time.sleep(self.timer)

        self.THREAD_ANIM = threading.Thread(target=anim)
        self.THREAD_ANIM.daemon = True
        self.THREAD_ANIM.start()

        return self.THREAD_ANIM

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.kill = True
        self.THREAD_ANIM.join()