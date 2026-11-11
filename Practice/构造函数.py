# class FooBar:
#     def __init__(self, value=42):
#         self.somevar = value
#
#
# f = FooBar("This is a constructor argument")
# print(f.somevar)


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = "Squawk!"

    def sing(self):
        print(self.sound)


# b = Bird()
# b.eat()
# b.eat()

sb = SongBird()
print(sb.sing())
print(sb.eat())
print(sb.eat())



