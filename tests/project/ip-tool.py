# N4Tools version:1.7.1
from N4Tools.Design import ThreadAnimation,Square,Color,Animation
from requests import get

@ThreadAnimation()
def MyIpInfo(Thread):
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
    Thread.kill()
    print (Sq.style([end]))

MyIpInfo()
