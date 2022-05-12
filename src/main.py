from ursina import *
from ursina.shaders.basic_lighting_shader import basic_lighting_shader
from lib.player import Player

app = Ursina()
# window.borderless = False
window.fullscreen = True
window.exit_button.visible = False

Entity.default_shader = basic_lighting_shader


sky = Sky(
    texture="assets/bg/hexagon.png",
    color=color.rgb(0, 0, 120)
)
map = Entity(model="assets/levels/1/map.obj", scale=0.8)
map.collider = MeshCollider(map)
player = Player(position=(-10,0,0))

def input(key):
    if key == 'r':
        player.respawn()

app.run()