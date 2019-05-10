from random import randint

def exchange(list: list, index: int, change_index:int):
    list[index], list[change_index] = list[change_index], list[index]

def show(list: list):
    [print(i) for i in list]

def is_sorted(list: list):
    list_is_sorted = True
    for index, e in enumerate(list):
        if index:
            if list[index - 1] > e:
                list_is_sorted = False
                break
        continue
    return list_is_sorted

def create_random_numbers(count = 10000):
    return [randint(0, 1000000) for x in range(0, count)]

def shell(numbers: list):
    length = len(numbers)
    h = int(1)
    while h < length / 3:
        h = int(3 * h + 1)
    while h > 1:
        for i in range(h, length):
            j = i
            while j >= h and numbers[j] < numbers[j - h]:
                exchange(numbers, j, j - h)
                j -= h
        h = int(h / 3)

if __name__ == "__main__":
    numbers = create_random_numbers(10)
    print(numbers)
    shell(numbers)
    print(numbers)

    # text = '该产品下设备编号[61123434535 ]已存在'
    # import re
    # s = re.sub('\D+', "", text)
    # print(s)

