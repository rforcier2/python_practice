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
