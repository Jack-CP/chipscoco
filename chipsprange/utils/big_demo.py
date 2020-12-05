# __author__ = chengpeng
# __email__ =1176383558@qq.com
# __date__ = 2020.11.8
# # __desc__ = git another demo

class Cat:
    pass

class Babby(Cat):
    def cry(self):
        print("babby never cry like a baby")


class WildCat(Cat):
    def cry(self):
        print("wild cat almost cry like a baby")

class Kitty(Babby, WildCat):
    def cry(self):
        print("kitty and xiaoliang cry like a baby")


print(Kitty.__mro__)
kitty = Kitty()
kitty.cry()













