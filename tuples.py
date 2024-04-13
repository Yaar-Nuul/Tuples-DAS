
numbers_parenthesis = (1, 2, -5)
print(numbers_parenthesis)

tuple_constructor = tuple(('Yaar', 'Adut', 'Akuang'))
print(tuple_constructor)

#Type
empty_tuple = ()
print(empty_tuple)


single_value_tuple = ('a',)
print(single_value_tuple)


mixed_tuple = (2, 'Hello', 'Python')
print(mixed_tuple)

# Accessing items in a tuple
mixed_tuple = (2, 'Hello', 'Python', True)
print(mixed_tuple)

print(mixed_tuple[0])
print(mixed_tuple[-1])
print(mixed_tuple[0:])
print(mixed_tuple[:-1])



#Length of a Tuple
cars = ('BMW', 'Tesla', 'Ford', 'Toyota', 'Honda')
print('Total Items:', len(cars))


# iterating through a tuple
fruits = ('apple','banana','orange')
for fruit in fruits:
    print(fruit)


# Checking if an item exist in a Tuple
colors = ('red', 'orange', 'blue')
print('yellow' in colors)  
print('red' in colors) 