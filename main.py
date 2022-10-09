class TreeStore:
    def __init__(self, items):
        self.items = items

    def get_all(self):
        return self.items

    def get_item(self, id):

        return self.items[id - 1]

    def get_children(self, id):

        elements = []

        for item in self.items:
            if id == item['parent']:
                elements.append(item)

        return elements

    def get_all_parents(self, id):

        elements = []

        for number in range(id):
            elements.append(self.items[number])

        return list(reversed(elements))


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None},
    ]
    ts = TreeStore(items)

    print(ts.get_all())
    print(ts.get_item(7))
    print(ts.get_children(4))
    print(ts.get_children(5))
    print(ts.get_all_parents(7))
