from collections import namedtuple


class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')


class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


class BabbingBlock():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


brook = BabbingBlock()


def who_says(obj):
    print(obj.who(), 'says', obj.says())


class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
#print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up doc")
#print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
#print(hunted2.who(), 'says:', hunted2.says())

first = Word('ha')
second = Word('HA')
third = Word('eh')
#print(first == second)
#print(third == first)

'''
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)
'''

'''
easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
'''
# CoyoteWeapon.commercial()


class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length


class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description,
              'bill and a', self.tail.length, 'tail')


class Thing():
    pass


'''
#6-pr1
example = Thing()

print(Thing())
print(example)
'''

# 6-pr2

'''
class Thing2():
    def __init__(self, letters):
        self.letters = letters


print(Thing2('abc').letters)
'''

'''
#6-pr3
class Thing3():
    def __init__(self, letters):
        self.letters = letters


letters = Thing3('xyz')
print(letters.letters)
'''


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

    def __str__(self):
        return ('name=%s, symbol=%s,number=%s' % self.name, self.symbol, self.number)


# 6-pr4,5
obj = Element('Hydrogen', 'H', '1')

dict_element = {'name': 'Hydrogen', 'symbol': 'H', 'number': '1'}

obj2 = Element(**dict_element)

print(obj2.name, obj2.symbol, obj2.number)

obj.dump()

print(obj)
