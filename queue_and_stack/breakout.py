# find middle item of list

# UPER

# U - Understand

# 1 for each item to find length of list, then / 2
# 2 loops second 2x where the second ends, will be answer

class LinkList:
    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, value):
        self.length += 1
        if self.head is None:
            self.head = {'value': value}
        else:
            self.head = {'value': value, 'tail': self.head}


    def remove(self):
        if self.head is None:
            return None
        else:
            self.length -= 1
            value = self.head['value']
            if self.length == 0:
                self.head = None
            else:
               self.head = self.head['tail']

            return value

    def reverse(self):
        temp_head = LinkList()
        for n in self.length:
            temp_head.insert(self.remove())
        self.head = temp_head.head


test_list = LinkList()
for item in [1,2,3]:
    test_list.insert(item)

print(test_list.remove())
print(test_list.remove())
print(test_list.remove())


# reverse in linklist


