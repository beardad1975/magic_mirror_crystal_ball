from ursina import *
app = Ursina()

window.borderless = False

e = Entity(model='quad')
s = Sequence(
    2,
    Func(print, 'one'),
    Func(e.fade_out, duration=1),
    2,
    Func(print, 'two'),
    Func(e.fade_in, duration=1),
    2,
    Func(print, 'three'),
    loop=True
    )

s.append(
    Func(print, 'appended to sequence')
    )

def input(key):
    actions = {'s' : s.start, 'f' : s.finish, 'p' : s.pause, 'r' : s.resume, 'k': s.kill}
    if key in actions:
        actions[key]()

app.run()
