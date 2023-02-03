class IntDict(object):
    '''A dictionary with integer keys'''

    def __init__(self, num_buckets):
        '''Create an empty dictionary'''
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])

    def add_entry(self, key, dict_val):
        '''Assumes key an int. Adds an entry'''
        hash_bucket = self.buckets[key % self.num_buckets]
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        hash_bucket.append((key, dict_val))

    def get_value(self, key):
        '''Assumes key an int
           Returns value associated with key'''
        hash_bucket = self.buckets[key % self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result += f'{e[0]}:{e[1]},'
        return result[:-1] + '}'


if __name__ == '__main__':
    import random

    D = IntDict(17)
    for i in range(20):
        key = random.choice(range(10 ** 5))
        D.add_entry(key, i)
    print(f'The value of the Int_dict is: {D}')

    print('The buckets are:')
    for hash_bucket in D.buckets:
        print(hash_bucket)
