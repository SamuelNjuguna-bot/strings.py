#Sep 25/2024
#The below program check if a String is a palindrome or symmetrical
is_symmetrical = 'Kenya'
is_symmetrical2 = 'Mum'
S1 = is_symmetrical.lower()
S2 = is_symmetrical2.lower()
if S1[::-1] == S1:
    print("True")
else:
    print("False")

if S2[::-1] ==  S2:
    print("true")
else:
    print("false")

# Ways to remove the i'th character from a String
stringExample = "String"
ith = "S"
indx = stringExample.index(ith)
print(stringExample.replace(stringExample[indx], ' '))
#finding String Length in python
length = "Length"
print(len(length))
#Avoiding Spaces in String
example = "list example"
splited = example.strip(' ').replace(' ', '')
print(splited)
#Program to print even length words in a String
def even(ListtL):
    even_list = []
    print(listL)
    x = ''
    for item in listL:
         x = item[:2]
         even_list.append(x)
    return even_list
even_length_string = 'This is a python script'
listL = list(even_length_string.split(' '))
print(str(even(ListtL=listL)).strip(']['))
