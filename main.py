def Select_Three(mas):
    res = [el for el in mas if len(el) <=3]

    return res


in_mas = ['Hello', '2', 'world', ':-)']
# in_mas = ['1234', '1567', '-2', 'computer science']
# in_mas = ['Russia', 'Denmark', 'Kazan']

print(Select_Three(in_mas))