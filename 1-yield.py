# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

# Es un return que hace paso a paso, deteniendo el proceso una unica vez por donde fue llado y al "llamarse" nuevamente ejecuta la siguite seccion despues de el yield anterior
