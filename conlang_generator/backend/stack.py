from collections import OrderedDict

class Stack():
    def __init__(self) -> None:
        self.members = OrderedDict()

    def insert_item(self, index: int, key, value):
        member_list = list(self.members.items())
        member_list.insert(index, (key, value))
        self.members = OrderedDict(member_list)

    def delete_item(self, index: int):
        member_list = list(self.members.items())
        del member_list[index]
        self.members = OrderedDict(member_list)

    def delete_item(self, key):
        del OrderedDict[key]

    def move_item(self, item, target_index):
        if isinstance(item, int):
            return self.__move_item_by_index(item, target_index)
        else:
            return self.__move_item_by_key(item, target_index)

    def __move_item_by_index(self, item_index: int, target_index: int):
        member_list = list(self.members.items())
        item = member_list.pop(item_index)
        member_list.insert(target_index, item)
        self.members = OrderedDict(member_list)

    def __move_item_by_key(self, key, target_index: int):
        item = self.members.pop(key)
        member_list = list(self.members.items())
        member_list.insert(target_index, (key, item))
        self.members = OrderedDict(member_list)



    def get_item(self, key):
        return self.members[key]
    
    def insert_stack(self, index, stack):
        member_list = list(self.members.items())
        other_memeber_list = list(stack.members)
        final_list = member_list[:index] + other_memeber_list + member_list[index:]
        self.members = OrderedDict(final_list)