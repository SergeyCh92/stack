class Stack:

    def __init__(self):
        self.list_data = []

    def __str__(self):
        return f'{self.list_data}'

    def is_empty(self):
        if len(self.list_data) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.list_data.append(item)

    def pop(self):
        last_item = self.list_data[-1]
        del self.list_data[-1]
        return last_item

    def peek(self):
        last_item = self.list_data[-1]
        return last_item

    def size(self):
        quantity = len(self.list_data)
        return quantity


def check_str(data):
    response_wrong = 'Несбалансированно'
    response_ok = 'Сбалансированно'
    my_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for item in data:
        if item in my_dict:
            my_stack.push(item)
        elif item in my_dict.values() and not my_stack.is_empty():
            if item == my_dict[my_stack.peek()]:
                my_stack.pop()
            else:
                print(response_wrong)
                return response_wrong
        else:
            print(response_wrong)
            return response_wrong
    if my_stack.is_empty():
        print(response_ok)
        return response_ok
    else:
        print(response_wrong)
        return response_wrong


start = True
while start:
    my_str = input('Введите строку, содержащую только следующие символы: "({[]})":\n')
    my_stack = Stack()
    check_str(my_str)
    answer = input('Желаете продолжить (да/нет)?\n')
    if not answer.lower().startswith('д'):
        start = False
