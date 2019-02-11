import time

# Time to start making a web crawler:
page = '''
<div id="top_bin"> 
  <div id="top_content" class="width960">
    <div class="udacity float-left">
    <a href="http://udacity.com">Udacity</a>
    <a href="http://youtube.com">youtube</a>
    <a href="http://codepen.io">Codepen</a>
    <a href="http://github.com">Github</a> 
     '''
#second Link
start_link = page.find("<a href=")
# This will find the first link on the page
#get the first quote and second quote after html link tag
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)

def getNextLink(pageString):
  #second Link
  start_link = pageString.find("<a href=")
  # This will find the first link on the page
  #get the first quote and second quote after html link tag
  start_quote = pageString.find('"', start_link)
  end_quote = pageString.find('"', start_quote+1)

  #get the string inbetween those quotes, the second link on the page
  url = pageString[start_quote+1:end_quote]
  print (url)
  return url, end_quote

getNextLink(page)

string = "Hello my name is Ronnie Hello my name is Ronnie"

def find_second(string, target):
  first_target = string.find(target)
  return string.find(target, first_target+1)

  

print ( find_second(string, "Hello") )

def bigger(a, b):
  return a if a > b else b

print ( bigger(5,2))

def is_friend(friends_name):
  # a function that tells if a another name is a friends'
  # All of your friend's names start with the letter D
  if friends_name == "" or friends_name == None:
    print("That's not a name!")

  if friends_name != "":
    return friends_name[0] == 'D' or friends_name[0] == 'd'

print(is_friend("dave"))
print(is_friend("Freddie"))

#changed rule to d or n

def is_friend(friends_name):
  # a function that tells if a another name is a friends'
  # All of your friend's names start with the letter D
  if friends_name == "" or friends_name == None:
    print("That's not a name!")

  if friends_name != "":
    return friends_name[0] == 'D' or friends_name[0] == 'd' or friends_name[0] == 'N' or friends_name[0] == 'n'
print(is_friend("Nancy"))


def biggest(a,b,c):
  return max(a,b,c)

print( biggest(5,2,3) )

def print_numbers(n):
  i = 0
  while i < n:
    i += 1
    print (i)

print(print_numbers(4))

def factorial(n):
  result = 1
  while n >= 1:
    result = result * n
    n = n-1
  return result   
print(factorial(5))




def get_page(link):
  from urllib.request import urlopen
  web_page = urlopen(link)
  web_page_text = web_page.read()
  page_content = web_page_text.decode('UTF-8')
  return page_content

def get_next_link(page_string):
  start_link = page_string.find("<a href=")
  if start_link == -1:
    return None, 0
  start_quote = page_string.find('"', start_link)
  end_quote = page_string.find('"', start_quote+1)
  url = page_string[start_quote+1:end_quote]
  return url, end_quote


# This function will retrieve all links while there are
# links and print them to the console.
def print_all_links(valid_page):
  while valid_page:
    url, endpos = get_next_link(valid_page)  
    if url:
      print (url)
      valid_page = valid_page[endpos:]
    else: 
      break

#print_all_links(get_page('https://youtube.com'))

#collatz conjecture
def collatz(n):
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
            print(n)
        else:
            n = 3*n + 1
            print(n)

collatz(4)



# finds the last target string occurance in a string 

def find_last(string, target):
  last_pos = -1
  while True:
    pos = string.find(target, last_pos+1)
    if pos == -1:
      return last_pos
    last_pos = pos
print(find_last('hello my name is hello there', 'hello'))

def stamps(target):
    current = 0
    fives = 0
    twos = 0
    ones = 0

    while target - current >= 5:
        fives += 1
        current += 5

    while target - current >= 2:
        twos += 1
        current += 2

    while target - current >= 1:
        ones += 1
        current += 1

    return fives, twos, ones

print (stamps(28))

def set_range(a,b,c):
    return max(a,b,c) - min(a,b,c) 

print(set_range(3,5,7))



def count_spaces(string):
  if string.find(' '):
    print(string.count(' '))

count_spaces('The Lions nest is near, and it can smell you')


#Given your birthday and a set date, calculate age in days:


#first define leap year to have the correct days for February
def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            return year%400==0
        else:
            return True
    else:
        return False
    
   
# Next, a function to get how many days are in each month
def daysInMonth(year,month):
    if month==2:
        if isLeapYear(year):
            return 29
        return 28
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        return 30
        
# Function to get the next day and calculate the next correct date.
def nextDay(year, month, day):
    """Use our Days in month function to determine next day"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# AFDHEJK

# Ensures the second date(year2, month2, day2) is AFTER our
# first date(year1, month1, day1). 
# We cannot time travel, therefore counting 
# days backwards will not be considered valid.
def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False        

 
# Final step, This will count the number of days between dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # Program defensively and ensure the dates are actually valid
    assert dateIsAfter(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days




# Test routine
def days_between_dates_test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1993,3,7,2019,2,4), 9465),
                  ((1997,1,21,2019,2,4), 5)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print (":( Failed... Test with data:", args, "Ans: ", answer, "Res: ", result,"days")
        else:
            print ("PASSED. Test case with data:", args, "Ans:", answer, "days")

days_between_dates_test()

print ("\nI am :", daysBetweenDates(1993, 3, 7, 2019, 2, 4), "days old")
print("Sydney is:", daysBetweenDates(1997,1,21,2019,2,4), "days old.")

def print_abacus(value):
   #line code 1
   numbers= ["|00000*****   |",
            "|00000****   *|",
            "|00000***   **|",
            "|00000**   ***|",
            "|00000*   ****|",
            "|00000   *****|",
            "|0000   0*****|",
            "|000   00*****|",
            "|00   000*****|",
            "|0   0000*****|",]
   #line code 2 and 3        
   for n in ("0"*(10-len(str(value)))+str(value)):
       print (numbers[int(n)])

###  TEST CASES
print ("\nAbacus showing 123456789:")
print_abacus(123456789)

print('\n Abacus Showing 2313608:')
print_abacus(2313601)


print('\n')
print("This demonstrates Leap Year Babies. If they were born on the day and year of a Leap Year: \n")
def is_leap_baby(day,month,year):
    # Write your code after this line.
    if day is 29 and month is 2:
        if year%4 is 0:
            if year%100 is 0:
                return year%400 is 0
            return True
        return False
    return False

# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status, name):
    if status:
        print (name, "is a leap year baby!")
    else:
        print (name, "is NOT a leap year baby!")

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Born 2/29/1996, Calvin')
#>>>Born {birthday}, Calvin is a leap year baby

output(is_leap_baby(29, 2, 1900), 'Born 2/29/1900, Charlie')
#>>>Born {birthday}, Charlie is NOT a leap year baby



print("/n")

#Function to check if string is a palindrome:
def checkPalindrome(inputString):
    return inputString == inputString[::-1]

def testPalindrome():
    test_cases = [(("aabbaa"), True), 
                  (('racecar'), True),
                  (('hammertime'), False),
                  (('timmy ymmit'), True ),
                  (('DammItImmaD'), True),
                  (('HelolleH'), False),
                  (('Hello World!'), False)]
    for (args, answer) in test_cases:
        result = checkPalindrome(args)
        if result != answer:
            print (":( Failed... Test with data:", args, "Ans: ", answer, "Res: ", result)
        else:
            print ("PASSED. Test case with data:", args, "Ans:", answer)

testPalindrome();



print("\nCURRENT # OF DAYS SINCE \nDATE: 1997,1,22 \nFORMAT: YYYY,MM,DD")

# Another iteration of this to give you the current age in days where your
# date of birth is a parameter.

def currentDaysFromBirth(year1,month1,day1):
  import datetime
  now = datetime.datetime.now()  

  # These vars are just for a more readable output
  year2, month2, day2 = year1, month1, day1

  # Ensure the date is not in the future
  assert dateIsAfter(now.year, now.month, now.day, year1, month1, day1)

  days=0
  while dateIsAfter(now.year, now.month, now.day, year1, month1, day1):
    days +=1
    (year1,month1,day1) = nextDay(year1,month1,day1)
  print (days, "days since", year2,month2,day2)
  return days


# will print and return
currentDaysFromBirth(1997,1,21)

print ("\nDATE: 1,1,1990")
currentDaysFromBirth(1990,1,1)

print('\n\nCOUNTRY TEST:')
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington DC', 307]]

def getCapital(countryName):
  for country in countries:
    targetName = country[0]
    capital = country[1]
    if targetName == countryName:
      print (capital)
      return capital
  print("Cannot find that capital")
    


getCapital("Romania")
  
