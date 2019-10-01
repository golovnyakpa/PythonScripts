#!/usr/bin/env python
# coding: utf-8


class HashMap:
    """
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    """
    class Entry:
        def __init__(self, key, value):
            """
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            """
            self.pair = (key, value)

        def get_key(self):
            # TODO возвращаем ключ
            # raise NotImplementedError
            return self.pair[0]

        def get_value(self):
            # TODO возвращаем значение
            # raise NotImplementedError
            return self.pair[1]

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            # raise NotImplementedError
            return self.pair[0] == other.pair[0] and self.pair[1] == \
                                                     other.pair[1]

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """
        self.map = [[]] * bucket_num
        self.prime_number = bucket_num
        self.entries_num = 0
        # raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        # raise NotImplementedError
        hash_ = self._get_hash(key)
        if self.map[hash_]:
            for entry in self.map[hash_]:
                if entry.get_key() == key:
                    return entry.get_value()
        else:
            return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        #  raise NotImplementedError
        self._resize()
        hash_ = self._get_hash(key)
        for i in range(len(self.map[hash_])):
            if self.map[hash_][i].get_key() == key:
                del self.map[hash_][i]
                self.entries_num -= 1
                break
        self.map[hash_].append(HashMap.Entry(key, value))
        self.entries_num += 1

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        # raise NotImplementedError
        '''
        len_ = 0
        for lst in self.map:
            for entry in lst:
                len_ += 1
        return len_
        '''
        return self.entries_num

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        # raise NotImplementedError
        num = self.str_to_num(key)
        return num % self.prime_number

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        # raise NotImplementedError
        return hash_value
        
    def values(self):
        # TODO Должен возвращать итератор значений
        # raise NotImplementedError
        all_values = []
        for lst in self.map:
            for entry in lst:
                all_values.append(entry.get_value())
        return iter(all_values)

    def keys(self):
        # TODO Должен возвращать итератор ключей
        # raise NotImplementedError
        all_keys = []
        for lst in self.map:
            for entry in lst:
                all_keys.append(entry.get_key())
        return iter(all_keys)

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        # raise NotImplementedError
        all_entries = []
        for lst in self.map:
            for entry in lst:
                all_entries.append((entry.get_key(), entry.get_value()))
        return iter(all_entries)

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        # raise NotImplementedError
        '''
        num = 0
        for lst in self.map():
            if lst:
                num += 1
        if num > len(self.map) // 2 + 1:
            new_map = [[]] * len(self.map) * 2
            self.prime_number = len(self.map) * 2
            for lst in self.map:
                for entry in lst:
                    n = self.str_to_num(entry.get_key())
                    hash_ = n % prime_number
                    new_map[hash_].append(entry)
        self.map = new_map'''
        if self.entries_num > len(self.map) - 3:
            new_map = [[]] * len(self.map) * 2
            self.prime_number = len(self.map) * 2
            for lst in self.map:
                for entry in lst:
                    hash_ = self._get_hash(entry.get_key())
                    new_map[hash_].append(entry)
            self.map = new_map
        return
        if self.entries_num < len(self.map) // 2 - 1:
            new_map = [[]] * (len(self.map) // 2)
            self.prime_number = len(self.map) // 2
            for lst in self.map:
                for entry in lst:
                    hash_ = self._get_hash(entry.get_key())
                    new_map[hash_].append(entry)
            self.map = new_map
        return
                     

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        # raise NotImplementedError
        bucket = ''
        item = ''
        for i, lst in enumerate(self.map):
            for entry in lst:
                bucket +=  str(i) + ', '
                item += entry.get_value() + ', '
        return f'buckets: {bucket}, items: {item}'

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        # raise NotImplementedError
        for lst in self.map:
            for entry in lst:
                if item == entry.get_value():
                    return True
        return False
        
    def str_to_num(self, str_):
        sum_ = 0
        for i in str(str_):
            sum_ += ord(i)
        return sum_
    def values(self):
90
        # TODO Должен возвращать итератор значений
91
        # raise NotImplementedError
92
        all_values = []
93
        for lst in self.map:
94
            for entry in lst:
95
                all_values.append(entry.get_value())
96
        return iter(all_values)
97
​
98
    def keys(self):
99
        # TODO Должен возвращать итератор ключей
100
        # raise NotImplementedError
101
        all_keys = []
102
        for lst in self.map:
103
            for entry in lst:
104
                all_keys.append(entry.get_key())
105
        return iter(all_keys)
106
​
107
    def items(self):
108
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
109
        # raise NotImplementedError
110
        all_entries = []
111
        for lst in self.map:
112
            all_entries += lst
113
        return iter(all_entries)
114
​
115
    def _resize(self):
116
        # TODO Время от времени нужно ресайзить нашу хешмапу
117
        # raise NotImplementedError
118
        num = 0
119
        for lst in self.map():
120
            if lst:
121
                num += 1
122
        if num > len(self.map) // 2 + 1:
123
            new_map = [[]] * len(self.map) * 2
124
            self.prime_number = len(self.map) * 2
125
            for lst in self.map:
126
                for entry in lst:
127
                    n = self.str_to_num(entry.get_key())
128
                    hash_ = n % prime_number
129
                    new_map[hash_].append(entry)
130
        self.map = new_map
131
                     
132
​
133
    def __str__(self):
134
        # TODO Метод выводит "buckets: {}, items: {}"
135
        # raise NotImplementedError
136
        bucket = ''
137
        item = ''
138
        for i, lst in enumerate(self.map):
139
            for entry in lst:
140
                bucket +=  str(i) + ', '
141
                item += entry.get_value() + ', '
142
        return f'buckets: {bucket}, items: {item}'
143
​
144
    def __contains__(self, item):
145
        # TODO Метод проверяющий есть ли объект (через in)
146
        # raise NotImplementedError
147
        for lst in self.map:
148
            for entry in lst:
149
                if item == entry.get_value():
150
                    return True
151
        return False
152
        
153
    def str_to_num(self, str_):
154
        sum_ = 0
155
        for i in str(str_):
156
            sum_ += ord(i)
157
        return sum_
