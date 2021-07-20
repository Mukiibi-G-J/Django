import calendar 
import datetime
import time
from typing import Union
print(calendar.weekheader(3))
#givea the index of the first day of the week
print(calendar.firstweekday())
 
#u can also use the month (2021)for year and 4 for the month 
print(calendar.month(2021,4))

#give you the calender in an array 
print(calendar.monthcalendar(2019,3))

#gives you the whole year
print(calendar.calendar(2021))

day_of_the_week=calendar.weekday(2021,5,1)
print(day_of_the_week)

#use to find out if a year is a  leap year
Is_leap=calendar.isleap(2020)
print(Is_leap) 
how_many_leap_days= calendar.leapdays(2000,2005)
print(how_many_leap_days)


# Data Type
    # intergers
    # floats
    # boolens
    # strings
# Casting
    # float(1)
# data type
    # list
        # methods on list
            # append
            # insert(1>index,'name')
            # remove
            # reverse
            # sort
            # slicing
            # primt(_diigits[4:5]) 
                   
digits= [0,1,2,3,4,5,6,7,8,9]
# print(digits[::])
#striding
print(digits[0:7:2])
print(digits[::2]) 
print(digits[::-1])
print(digits[::-2])

for i in digits:
    print(digits[0:i])
# spliting and joining 
problems='broke, pale, short, nerdy'
list=problems.split(", ")
print(list)
joined=' and '.join(list)    #' and ' is called a delimiter
print(joined)
csv=','.join(list)
print(csv)

# tuples can't be changed
credit_card=(232323232323232, 'Joe', '11/20')
credit_card2=(232323232323232, 'Joe', '11/20')


#un packing a tuple

person=('Nacy-pants', 35, 'Pizza')
# (name, age, fav_food)= person
name, age, fav_food = person
print(name)
print(age)
print(fav_food)



person1=('Nacy-pants', 35, 'Pizza')
person2=('Nacy-pants', 35, 'Pizza')
people= [person1, person2]

for name, age, favourfood in people:
    print(name)
    print(age)
    print(fav_food)
    print()
    
#SETS 
    #1 aset is unorder
    #2 Does not have duplicates
    #function
        # .Union             set = a.union(b)
        # .intersection       set= a.intersection(b)
        # ,difference         set= a.difference(b)
s = {'bluberry', 'rasbery'}
s.add('strawbery')
print(s)

list1=[2,2,3,4,3,5,5,6,7]
new=set(list1)
# print(new)
# # new_list = list(new)
# print( list(new))  


# DIctionaries   
dictionary = {'bananas':56, 'friuts':76}
print(dictionary['bananas'])
print(dictionary.get('manago'))  #use to aviod an error if the keys is not de
 
  
contants={
    'john': ['0750440865', 'mukiibijoseph19@gmail.com'],
    'mike': ['0750440865']
    }




