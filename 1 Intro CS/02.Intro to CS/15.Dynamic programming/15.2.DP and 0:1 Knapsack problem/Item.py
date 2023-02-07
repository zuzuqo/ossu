class Item(object):
    def __init__(self, name, value, weight):
        self._name = name
        self._value = value
        self._weight = weight

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight

    def __str__(self):
        return f"<{self._name}, {self._value}, {self._weight}>"