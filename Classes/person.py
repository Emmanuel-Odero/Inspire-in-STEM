class Person:
  def __init__(self, _name, _age):
    self.name = _name
    self.age = _age

  def sayHi(self):
    print('Hello, my name is ' + str(self.name) + ' and I am ' + str(self.age) + ' years old!')

p1 = Person('Bob', 25)
p1.sayHi() # Prints: Hello, my name is Bob and I am 25 years old!
