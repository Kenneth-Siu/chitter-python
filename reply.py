from squeak import Squeak


class Reply(Squeak):
    def __init__(self, message, to):
        super().__init__(message)
        self.to = to