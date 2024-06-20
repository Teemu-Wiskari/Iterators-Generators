class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list  # основной список

    def __iter__(self):
        self.iters_stack = [iter(self.main_list)]  # стек итераторов
        return self

    def __next__(self):
        while self.iters_stack:  # пока стек не пустой
            try:
                next_item = next(self.iters_stack[-1])  # получаем следующий элемент
            except StopIteration:
                self.iters_stack.pop()  # если не получилось, значит итератор пустой
                continue  # и переходим к следующему элементу

            if isinstance(next_item, list):  # если следующий элемент оказался списком
                self.iters_stack.append(iter(next_item))  # добавляем его итератор в стек
            else:
                return next_item  # возвращаем следующий элемент
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()

list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

for item in FlatIterator(list_of_lists_2):
    print(item)
