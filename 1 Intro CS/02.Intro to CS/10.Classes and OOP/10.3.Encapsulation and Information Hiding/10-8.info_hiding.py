class info_hiding(object):
    def __init__(self):
        self.visible = 'look at me'
        self.__also_visible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'

    def print_visible(self):
        print(self.visible)

    def print_invisible(self):
        print(self.__invisible)

    def __print_invisible(self):
        print(self.__invisible)

    def __print__invisible__(self):
        print(self.__invisible)


test = info_hiding()
print(test.visible)
print(test.__also_visible__)
# error
print(test.__invisible)