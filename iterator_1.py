class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list  # основной список

    def __iter__(self):
        self.main_cursor = 0  # курсор основного списка
        self.nest_cursor = 0  # курсор вложенного списка
        return self

    def __next__(self):
        while self.main_cursor < len(self.main_list):
            if self.nest_cursor < len(self.main_list[self.main_cursor]):  # если вложенный список не пустой
                list_element = self.main_list[self.main_cursor][self.nest_cursor]  # берем элемент из вложенного списка
                self.nest_cursor += 1  # увеличиваем курсор вложенного списка
                return list_element
            self.main_cursor += 1  # увеличиваем курсор основного списка
            self.nest_cursor = 0  # обнуляем курсор вложенного списка
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

for item in FlatIterator(list_of_lists):
    print(item)
