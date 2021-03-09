from time import perf_counter
t = perf_counter()
from ursina import *
app = Ursina()
Entity(model='cube', shader=Shader())
EditorCamera()
print('ttttttttttttt', perf_counter() - t)
def input(key):
    if key == 'r':
        reload_shaders()

def reload_shaders():
    for e in scene.entities:
        if hasattr(e, '_shader'):
            print('-------', e.shader)
            # e._shader = Panda3dShader.make(language, vertex, fragment, geometry)

app.run()
