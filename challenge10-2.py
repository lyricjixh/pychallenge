#!/usr/bin/env python
# challenge level 10

def number_to_list(number):
    n = 0
    str_number = str(number)
    length = len(str_number)
    number_list=[]
    while n <= length-1:
        number_list.append(str_number[n])
        n += 1
    return number_list;
        
type_in = raw_input('input your number: ')
try:
    number=int(type_in)
except:
    print "please re-type number in digital"

num_list=[1]  # initial start number as list
print "num_list is: ", number_to_list(number)
rounds = 5   #total round
run = 1       #initial run count
list_wip = [] #work in process number list for each round
count = 1     #initials same digits count in the list
n = 0         #initial list index

while run <= rounds:
    print "now run round: ", run
    length = len(num_list)
    while n < length-1:         #for list length greater than 2, looping
        if num_list[n] == num_list[n+1]:
            count += 1
        else:
            list_wip.append(count)
            list_wip.append(num_list[n])
            count = 1
        n += 1
    list_wip.append(count)      #for list length equal 1, append the count first then the number
    list_wip.append(num_list[n])  
    num_list = list_wip           #save the wip list to number list
    print "current number list: ", "".join(str(digit) for digit in num_list)
    # reset values to start new round
    n = 0                       #reset initial list index
    count = 1                   #reset digit count to 1
    list_wip = []               #reset wip list to null
    run += 1
print "final number: ", "".join(str(digit) for digit in num_list)
print "length of final number: ", len(num_list)
        
