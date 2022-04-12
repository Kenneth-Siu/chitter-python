from squeak import Squeak


class DM(Squeak):
    def __init__(self, message, at):
        super().__init__(message)
        self.at = at