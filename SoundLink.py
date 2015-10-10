from dslink.DSLink import Configuration, DSLink
from dslink.Node import Node
import pyglet


class SoundLink(DSLink):
    def __init__(self):
        self.player = pyglet.media.Player()
        super().__init__(Configuration("sound", responder=True))

        self.play_sound = Node("playSound", self.super_root)
        self.play_sound.set_invokable("write")
        self.play_sound.set_invoke_callback(self.play_sound_callback)
        self.play_sound.set_parameters([
            {
                "name": "Sound Path",
                "type": "string"
            }
        ])
        self.super_root.add_child(self.play_sound)

    def play_sound_callback(self, params):
        self.player.queue(pyglet.media.load(params["Sound Path"]))
        self.player.play()

if __name__ == "__main__":
    SoundLink()
