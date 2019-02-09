# Time to start testing strings and manipulating them
page = '''
<div id="top_bin">
  <div id="top_content" class="width960">
    <div class="udacity float-left"><a href="http://udacity.com">Udacity</a><a href="http://youtube.com">youtube</a><a href="http://codepen.io">Codepen</a><a href="http://starlimeweb.com">starlime</a>
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


def print_numbers(n):
  i = 0
  while i < n:
    i += 1
    print (i)

print(print_numbers(4))


#small mathy section. Making functions to return comparisons of numbers
def factorial(n):
  result = 1
  while n >= 1:
    result = result * n
    n = n-1
  return result
print(factorial(5))


def bigger(a,b):
  return max(a,b)  

def biggest(a,b,c):
  return max(a,b,c)   

def median(a,b,c):
  big = biggest(a,b,c) 
  if big == a:
    return  bigger(b,c)
  if big == b:
    return bigger(a,c)
  else:
    return bigger(a,b)
  
print(median(9,4,7))

#collatz conjecture
def collatz(n):
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
            print(n)
        else:
            n = 3*n + 1
            print(n)
#returns 16/8/4/2/1
collatz(5)

#More string manipulation
#
# finds the last target string occurance in a string 

def find_last(string, target):
  last_pos = -1
  while True:
    pos = string.find(target, last_pos+1)
    if pos == -1:
      return last_pos
    last_pos = pos
print(find_last('hello my name is hello there', 'hello'))



def count_spaces(string):
  if string.find(' '):
    print(string.count(' '))

count_spaces('The Lions nest is near, and it can smell you')

#Given your birthday and a set date, calculate age in days:
def isLeapYear(year):
    if year%4==0:
        if year%100==0:
            return year%400==0
        else:
            return True
    else:
        return False
    
def daysInMonth(year,month):
    if month==2:
        if isLeapYear(year):
            return 29
        else: return 28
    if month==1 or month==3 or month==5 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        return 30
        
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
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

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert dateIsAfter(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        days += 1
        (year1, month1, day1) = nextDay(year1, month1, day1)
    return days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1993,3,7,2019,2,4), 9465)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, ":( Failed")
        else:
            print ("PASSED. Test case with data:", args, "Answer:", answer, "days")

test()

print ("I am :", daysBetweenDates(1993, 3, 7, 2019, 2, 4), "days old")
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
print ("\nAbacus showing 0:\n")
print_abacus(0)

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
        print ("%s is a leap year baby!" % name)
    else:
        print ("%s NOT a leap year baby!" % name)

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Born 2/29/1996, Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Born 2/29/1900, Charlie')
#>>>There's nothing special about Charlie's birthday. He is not a leap year baby!

#Check if string is a palindrome:
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

def currentDaysFromBirth(year1,month1,day1):
  import datetime
  now = datetime.datetime.now()  

  assert dateIsAfter(now.year, now.month, now.day, year1, month1, day1)

  days=0
  while dateIsAfter(now.year, now.month, now.day, year1, month1, day1):
    days +=1
    (year1,month1,day1) = nextDay(year1,month1,day1)
  return days



print(currentDaysFromBirth(1995,1,22))
