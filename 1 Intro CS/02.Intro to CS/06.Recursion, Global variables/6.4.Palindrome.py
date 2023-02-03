def is_palindrome(st:str):
    '''
    :param st: String
    :return: Bool
    '''

    def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if ord(c) in range(ord('a'), ord('z') + 1):
                letters += c
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(st))


print(is_palindrome('Anna'))
print(is_palindrome('Annabd'))
