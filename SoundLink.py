from dslink.DSLink import Configuration, DSLink
from dslink.Node import Node
import pyglet


class SoundLink(DSLink):
    def __init__(self):
        self.player = pyglet.media.Player()
        super().__init__(Configuration("sound", responder=True))

        self.play_sound = Node("playSound", self.super_root)
        self.play_sound.set_config("$name", "Play Sound")
        self.play_sound.set_invokable("write")
        self.play_sound.set_invoke_callback(self.play_sound_callback)
        self.super_root.add_child(self.play_sound)

        self.pause_sound = Node("pauseSound", self.super_root)
        self.pause_sound.set_config("$name", "Pause Sound")
        self.pause_sound.set_invokable("write")
        self.pause_sound.set_invoke_callback(self.pause_sound_callback)
        self.super_root.add_child(self.pause_sound)

        self.queue_sound = Node("queueSound", self.super_root)
        self.queue_sound.set_config("$name", "Queue Sound")
        self.queue_sound.set_invokable("write")
        self.queue_sound.set_invoke_callback(self.queue_sound_callback)
        self.queue_sound.set_parameters([
            {
                "name": "Sound Path",
                "type": "string"
            },
            {
                "name": "Play on Invoke",
                "type": "bool",
                "default": True
            }
        ])
        self.super_root.add_child(self.queue_sound)

    def play_sound_callback(self, params):
        self.player.play()

    def pause_sound_callback(self, params):
        self.player.pause()

    def queue_sound_callback(self, params):
        self.player.queue(pyglet.media.load(params["Sound Path"]))
        if "Play on Invoke" in params and params["Play on Invoke"]:
            self.player.play()

if __name__ == "__main__":
    SoundLink()
