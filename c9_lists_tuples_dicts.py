# Lists
# create a simple list
randomlist = ['apple', 'banana', True, 10, 'Mango']
# access list elements
print(randomlist[0])
print(randomlist[4])
# assign new list elements
randomlist[0] = 'Peach'
print(randomlist[0])
# add list elements
randomlist.append(0)
print(randomlist)
# delete list elements
del randomlist[1]
print(randomlist)


# Tuples
# 'tuple' object does not support item assignment.
# 'tuple' object doesn't support item deletion.
randomtuple = ('apple', 'banana', True, '10', 'Mango')
print(randomtuple[1])
print(randomtuple[4])
# del randomtuple
# print(randomtuple)


# Dictionaries
# access ditionary elements
randomdict = {'Make': 'Honda', 'Model': 'Civic', 'Year': 2010, 'Color': 'Black'}
print(randomdict['Make'])
print(randomdict['Model'])
# assign values to dictionary elements
randomdict['Make'] = 'Audi'
print(randomdict['Make'])
# delete dictionary elements
del randomdict['Make']
print(randomdict)
# clear whole dictionary
randomdict.clear()
print(randomdict)


cars = []

add_inventory = input('Add inventory? [y/n] ')

while add_inventory == 'y':  
    # Get car data from user
    make = input('Make: ')
    model = input('Model: ')
    year = input('Year: ')
    miles = input('Miles: ')

    # Create car dictionary object and save it to list
    car = {'Make': make, 'Model': model, 'Year': year, 'Miles': miles}
    cars.append(car)

    # Ask user if we should keep going
    add_inventory = input('Add inventory? [y/n] ')

print('')  
print('Here are your cars:')

# Display all of our cars
for c in cars:  
    print('Make: ' + c['Make'])
    print('Model: ' + c['Model'])
    print('Year: ' + c['Year'])
    print('Miles: ' + c['Miles'])
    print('')
