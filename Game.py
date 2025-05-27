import pyglet

from Enums.ELayer import ELayer

window = pyglet.window.Window()
window.set_size(800, 1200)
# image_map = pyglet.image.load('tile_map.jpg')
# sprites = []
# x = 25
# y = 85
# for i in range(6):
#     x = 25
#     for j in range(4):
#         region = image_map.get_region(x, y, 64, 64)
#         print(image_map)
#         sprites.append(pyglet.sprite.Sprite(region, x=j*64, y=i*64))
#         x += 64 + 9
#     y += 64 + 9
# #ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)
#
# print(sprites[0])

sprite = pyglet.sprite.Sprite(pyglet.image.load('images/Grass_1.png'))


"""
Quick mental thoughts 
- have one batch
- have one group for each layer for that batch which priority matches layer level
- use sprite visibility for sprites that are either on screen or off screen (this optimizes the batch.draw call)
"""
batch = pyglet.graphics.Batch()
layers = []
for i in range(len([e.value for e in ELayer])):
    layers.append(pyglet.graphics.Group(order=i))

#sprite.
#sprite.delete()

batch = pyglet.graphics.Batch()
batch.

ball_sprites = []
for i in range(100):
    x, y = i * 10, 50
    ball_sprites.append(pyglet.sprite.Sprite(ball_image, x, y, batch=batch))

@window.event
def on_draw():
    window.clear()
    sprite.update(x=50, y=50)
    sprite.draw()
    # image_map.blit(0, 0)
    # for i in range(6):
    #     for j in range(4):
    #         new_x = 64*j
    #         new_y = 64*i
    #         print(new_x, new_y, i*4 + j)
    #         #sprites[i*4 + j].update(x=new_x, y=new_y)
    #         sprites[i*4 + j].draw()
    #sprites[1].draw()

pyglet.app.run()