def num_translate(a):
    if a != 'one' and a!='two' and a != 'three' and a != 'four' and a != 'five' and a != 'six' and a != 'seven' and \
            a != 'eight' and a != 'nine' and a != 'ten':
        print ('None')
    else:
        num = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
        print(f'{num[a]} ')

num_translate("ten")
