import logging

from dslink.DSLink import Configuration, DSLink
from dslink.Node import Node
from dslink.Profile import Profile
import pyglet


class SoundLink(DSLink):
    def __init__(self):
        self.player = pyglet.media.Player()
        self.sound_logger = self.create_logger("Sound", logging.DEBUG)
        DSLink.__init__(self, Configuration("sound", responder=True))

        self.profile_manager.create_profile(Profile("playSound"))
        self.profile_manager.register_callback("playSound", self.play_sound)

        self.profile_manager.create_profile(Profile("pauseSound"))
        self.profile_manager.register_callback("pauseSound", self.pause_sound)

        self.profile_manager.create_profile(Profile("queueSound"))
        self.profile_manager.register_callback("queueSound", self.queue_sound)

    def get_default_nodes(self):
        root = self.get_root_node()

        play_sound = Node("playSound", root)
        play_sound.set_name("Play Sound")
        play_sound.set_config("$is", "playSound")
        play_sound.set_invokable("write")
        root.add_child(play_sound)

        pause_sound = Node("pauseSound", root)
        pause_sound.set_name("Pause Sound")
        pause_sound.set_config("$is", "pauseSound")
        pause_sound.set_invokable("write")
        root.add_child(pause_sound)

        queue_sound = Node("queueSound", root)
        queue_sound.set_name("Queue Sound")
        queue_sound.set_config("$is", "queueSound")
        queue_sound.set_invokable("write")
        queue_sound.set_parameters([
            {
                "name": "Sound Path",
                "type": "string"
            }
        ])
        root.add_child(queue_sound)

        return root

    def play_sound(self, params):
        self.player.play()

    def pause_sound(self, params):
        self.player.pause()

    def queue_sound(self, obj):
        try:
            self.player.queue(pyglet.media.load(obj.params["Sound Path"]))
        except pyglet.media.avbin.AVbinException:
            self.sound_logger.warning("Could not find file: %s" % obj["Sound Path"])

if __name__ == "__main__":
    SoundLink()
