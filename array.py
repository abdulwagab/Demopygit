import array as arr  #import an array model

def create(a, b):  # creating a function
    a = arr.array('i', [1, 2, 3, 4, 5])  #function deceleration 'a'
    a.append(6)  #append function used to add any value in middle, last, are first

    a.insert(8, 9) # insert function used to pass two arguments in that function

    a.extend([10, 11, 12]) # extend function used to continue that above function normally

    b = arr.array('i', [21, 22, 23])  # creating another function array

    b.remove(23)  #remove the value 23 in 2nd function 'b'


    print(a + b)  # At last print the 'a' and 'b' function

create('a', 'b')  # call the function

