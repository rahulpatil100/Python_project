##TUPLES:- tuple is collection of python object much like list
#creating empty tuple
tuple1 = ()
print("\nInitial Empty tuple: ")
print(tuple1)

#creating tuple using string
tuple1 = ("Rahul", "Patil")
print("\nTuple with the using string")
print(tuple1)

#creating tuple using list
list = [1,2,3,4,5,6]
print("\nTuple using list ")
print(tuple(list))

#creating tuple mix datta type with using loop
tuple1 = ("Rahul","Patil")
n = 3
print("\nTuple with loop")
for i in range(int(n)):
    tuple1 = (tuple1)
    print(tuple1)