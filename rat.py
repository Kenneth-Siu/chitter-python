from reply import Reply
from dm import DM
from squeak import Squeak


def is_valid_squeak(squeak, types_of_squeak):
    for squeak_type in types_of_squeak:
        if isinstance(squeak, squeak_type):
            return True
    return False

class Rat:
    def __init__(self, handle):
        self.handle = handle
        self.squeaks = []
        self.profile_types_of_squeaks_displayed = []
    
    def update_types_of_squeak_displayed(self, types):
        self.profile_types_of_squeaks_displayed = types
    
    def squeak(self, message):
        squeak = Squeak(message)
        self.squeaks.append(squeak)
        return squeak
    
    def dm(self, message, at):
        dm = DM(message, at)
        self.squeaks.append(dm)
        return dm
    
    def reply(self, message, to):
        reply = Reply(message, to)
        self.squeaks.append(reply)
        return reply

    def get_display_squeaks(self):
        return filter(lambda squeak: is_valid_squeak(squeak, self.profile_types_of_squeaks_displayed), self.squeaks)
