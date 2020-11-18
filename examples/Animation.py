from N4Tools.Design import Animation,ThreadAnimation
import time

Anim = Animation()

def MyLoadingAnimation(timer=1,end_msg='DONE!'):
    TA = ThreadAnimation()
    TA.set_animation(
        Anim.Loading(),
        END=end_msg,
    )
    with TA:
        time.sleep(timer)

def MyProInput(text):
    Anim.SlowText(text)
    return input()


if __name__ == '__main__':
    MyLoadingAnimation(timer=2,end_msg='DONE!')

    name = MyProInput('Enter name: ')
    print (name)

    Anim.SlowLine(('text '*10+'\n')*10,timer=0.1)

