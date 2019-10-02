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
            return self.pair[0] == other.pair[0]

    def __init__(self, bucket_num=64):
        """
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        """
        self.map = [[]] * bucket_num
        self.bucket_num = bucket_num
        self.entries_num = 0
        # raise NotImplementedError

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        hash_ = self._get_hash(key)
        idx = self._get_index(hash_)
        if self.map[idx] != []:
            for entry in self.map[idx]:
                if entry.get_key() == key:
                    return entry.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        #  raise NotImplementedError
        hash_ = self._get_hash(key)
        idx = self._get_index(hash_)
        for i in range(len(self.map[idx])):
            if self.map[idx][i].get_key() == key:
                del self.map[idx][i]
                self.entries_num -= 1
                break
        self.map[idx].append(HashMap.Entry(key, value))
        self.entries_num += 1

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        # raise NotImplementedError
        return self.entries_num

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        # raise NotImplementedError
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        # raise NotImplementedError
        return hash_value % self.bucket_num

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
        if self.entries_num > len(self.map) - 3:
            new_map = [[]] * len(self.map) * 2
            self.bucket_num = len(self.map) * 2
            for lst in self.map:
                for entry in lst:
                    hash_ = self._get_hash(entry.get_key())
                    idx = self._get_index(hash_)
                    new_map[idx].append(entry)
            self.map = new_map
            return
        if self.entries_num < len(self.map) // 2 - 1:
            new_map = [[]] * (len(self.map) // 2)
            self.prime_number = len(self.map) // 2
            for lst in self.map:
                for entry in lst:
                    hash_ = self._get_hash(entry.get_key())
                    idx = self._get_index(hash_)
                    new_map[idx].append(entry)
            self.map = new_map
            return

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        # raise NotImplementedError
        bucket = ''
        item = ''
        for i, lst in enumerate(self.map):
            for entry in lst:
                bucket += str(i) + ', '
                item += entry.get_value() + ', '
        bucket = bucket[:len(bucket)-2]
        return f'buckets: {bucket}, items: {item}'

    def __contains__(self, item):
        # TODO Метод проверяющий есть ли объект (через in)
        # raise NotImplementedError
        for lst in self.map:
            for entry in lst:
                if item == entry.get_key():
                    return True
        return False
