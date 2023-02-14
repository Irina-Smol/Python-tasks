#Считайте цифру, выведите её название на английском (zero, one, ..., nine).
#Sample Input:
#8
#Sample Output:
#eight

the_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

a = int(input())
if a in the_dict:
   print(the_dict[a])
