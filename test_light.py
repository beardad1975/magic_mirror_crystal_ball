from ursina import *

app = Ursina()
from ursina.shaders import lit_with_shadows_shader, normals_shader, matcap_shader
# you have to apply this shader to enties for them to recieve shadows.
EditorCamera()
#Entity(model='plane', scale=10, color=color.gray, shader=lit_with_shadows_shader)

#heart = Entity(model='模型/愛心.obj', y=1, color=color.red, shader=lit_with_shadows_shader)
heart = Entity(model='模型/愛心.obj', y=1, color=color.red, shader=normals_shader)
#heart.texture = '圖片/魔鏡角色.png'
pivot = Entity()
#PointLight(parent=pivot, y=2, z=3)
#PointLight(y=-5, )
#PointLight( y=-5, )
window.color = color.rgb(255, 200 ,200)



#pivot.animate_rotation_y(720, duration=4, curve=curve.linear, loop=True)


def input(key):
    if key == 'space':
        heart.shake()
    elif key == 'n':
        heart.shader = normals_shader
    elif key == 'l':
        heart.shader = lit_with_shadows_shader

def update():
    heart.rotation_y += 1
    #heart.rotation_z += 0.2

app.run()
