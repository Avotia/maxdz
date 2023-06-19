word = input("Введите слово ")
count_sym = len(word)//2
if list(word[:count_sym]) == list(reversed(word[-count_sym:])):
    print(True)
else:
    print(False)
