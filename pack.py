from squeak import Squeak


def filter_function(squeak):
    return isinstance(squeak, Squeak)

def flatten(list_of_lists):
    return [list for sub_list in list_of_lists for list in sub_list]

class Pack():
    def __init__(self, monarch, max_rats):
        self.rats = []
        self.monarch = monarch
        self.max_rats = max_rats
    
    def change_max_rats(self, max_rats):
        self.max_rats = max_rats

    def add_rat(self, rat):
        if (len(self.rats) >= self.max_rats):
            raise Exception("Too many rats ewww")
        if (rat in self.rats):
            raise Exception("No rat clones")
        self.rats.append(rat)
    
    def get_available_spaces(self):
        return self.max_rats - len(self.rats)
    
    def get_member_squeaks(self):
        list_of_squeaks_by_member = []
        for rat in self.rats:
            list_of_squeaks_by_member.append(filter(filter_function, rat.squeaks))
        return flatten(list_of_squeaks_by_member)
