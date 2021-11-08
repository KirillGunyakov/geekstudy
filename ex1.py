def num_tranlate(number):
    for eng , rus in nums.items():
        if number==eng:
            return rus


nums = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'дясять'}

print(num_tranlate('one'))

