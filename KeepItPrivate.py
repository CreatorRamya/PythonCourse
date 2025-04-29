class myClass:

    __privateVar = 28;
    def __priveMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Privaate Variable value:", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateVar