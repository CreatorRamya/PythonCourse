class fruit:
    taste = 'sweet'

    def __init__(self, name, color):
        self.name = name
        self.color = color
        
grapes = fruit('Grapes', 'Purple')
guava = fruit('Guava', 'Green')
banana = fruit('Banana', 'Yellow')

print(grapes.taste)
print(grapes.name, grapes.color)
print(guava.name, guava.color)
print(banana.name, banana.color)
