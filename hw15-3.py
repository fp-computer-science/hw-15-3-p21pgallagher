# Author: PJG (AMDG) 2/8/2021

# Question 1
library = {'Harry Potter':'J.K. Rowling', 'The Lord of the Rings':'J.R.R Tolkien', 'The Hunger Games':'Suzanne Collins', 'The Chronicles of Narnia':'C.S. Lewis'}

# Question 2
print(list(library.values()))

# Question 3
print(list(library.keys()))

# Question 4
print('Harry Potter' in library)

# Question 5
print('Star Wars' not in library)

# Question 6
print(library, {'Into the Wild':'Jon Krakauer'})

# Question 7
print(len(library))

# Question 8
print(library["The Chronicles of Narnia"])

# Question 9
print(list(library.items()))

# Question 10
del library['The Hunger Games']

print(library) 
'''just to check'''
