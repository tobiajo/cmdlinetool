from cmdlinetool import util


def run():
    print('x + y = ?')
    try:
        x = int(input('x = '))
        y = int(input('y = '))
    except Exception as e:
        print('error: %s' % e)
        return 1
    print('=> x + y = %s' % util.adder(x, y))
