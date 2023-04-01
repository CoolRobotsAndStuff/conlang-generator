from collections import OrderedDict

class Stack():
    def __init__(self) -> None:
        self.members = OrderedDict()

    def insert_item(self, index, key, value):
        member_list = list(self.members.items())
        member_list.insert(index, (key, value))
        self.members = OrderedDict(member_list)

    def get_item(self, key):
        return self.members[key]
    
    def insert_stack(self, index, stack):
        member_list = list(self.members.items())
        other_memeber_list = list(stack.members)
        final_list = member_list[:index] + other_memeber_list + member_list[index:]
        self.members = OrderedDict(final_list)