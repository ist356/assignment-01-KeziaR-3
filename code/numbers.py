'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''


odd = {}
even = {}

i = 1 
while True:
    vals = int(input("Enter integer values "))

    if vals == 0:
        print(f" {{'odd': {list(odd.values())}, 'even': {list(even.values())}}}")
        break
    
    elif vals % 2 == 0:
        even[i] = vals

    else:
        odd[i] = vals

    i += 1


  
        