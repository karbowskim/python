class ClassA:
    def __init__(self,text):
        self.text = text

    def geText(self):
        print("Fetching class A variable using access method: " + self.text)


class ClassB:
    def __init__(self,text):
        self.text = text

    def geText(self):
        print("Fetching class B variable using access method: " + self.text)


class ClassC:
    def __init__(self,text):
        self.text = text

    def geText(self):
        print("Fetching class C variable using access method: " + self.text)


class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def count(self):
        while(self.start <= self.stop):
            print(self.start)
            self.start = self.start + 1
        print("Count finished!")


# Using classess example:

classAObject = ClassA('Hello world!')
classBObject = ClassB('Hello Kitty!')
classCObject = ClassC('Hello Cthulhu!')

print(classAObject.text)
print(classBObject.text)
print(classCObject.text)

classAObject.geText()
classBObject.geText()
classCObject.geText()

counter = Counter(1,10)
counter.count()
