# lists
# insert
employee = ['Peter', 'John ', 'Smith' , 'Andrew']
print(employee)
print(employee[2])
employee[0] = "Alex"
print(employee)
employee.insert(1, 'Jack')
print(employee)

# tuples
students = ('Esther', 'Susan', 'Angela', 'Juliana')
print(students)
print(students[3])
# sets not indexed, not ordered add
products = {'Apple' ,  'Banana' ,'Orange' , 'Pineapple'}
products.add('Cherry')
print(products)
if 'Banana' in products:
    print('Banana')
if 'Pineapple' in products:
    print('Pineapple')
if 'Apple' in products:
    print('Apple')
if 'Car' in products:
        print('Car')
else:
    print('Not found')


# dictionary
book = {'Name': 'The code',
        'Price': 1000,
        'Date Published': 1999
}
print(book)
if 'Name' in book:
    print('Yes it exists')
else:
    print('No it does not exist')
book['Publisher'] = 'Speed'
print(book)
# in pairs of keys and values

