from N4Tools.Design import ThreadAnimation,Square,Color,Animation
from requests import get

TA = ThreadAnimation()
TA.set_animation(
    Animation().Loading(
        text='[$GREEN]Loading...',
        anim=['/','-','\\','|'],
    )
)

@TA.thread
def MyIpInfo():
    r = get('http://ipinfo.io/json')
    end = ''
    for key,val in r.json().items():
        if key not in ['hostname','readme','org']:
            end += f'[$LYELLOW]{key}[$WIHTE]: [$LGREEN]{val}\n'
    end = end[:-1]

    Sq = Square()
    Sq.cols = 1
    Sq.padding = [1,0,10,0]
    Sq.color = Color().LRED
    Sq.center = True
    Sq.square = [
        '[$LBLUE][[$LGREEN]+[$LBLUE]]',
        ' |',
        '[$LBLUE][[$LGREEN]+[$LBLUE]]',
        '-',
        '[$LBLUE][[$LGREEN]+[$LBLUE]]',
        '  |',
        '[$LBLUE][[$LGREEN]+[$LBLUE]]',
        '-']
    TA.END = Sq.style([end])

MyIpInfo()
