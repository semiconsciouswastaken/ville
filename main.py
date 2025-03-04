import pyglet

# Create a window
window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()

# Run the application
pyglet.app.run()