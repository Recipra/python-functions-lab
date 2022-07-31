# Challenge 1

def sum_to(n):
  sum = 0

  while n > 0 and n < n + 1:
    sum += n
    n -= 1
  
  return sum

# Challenge 2

def largest(number_list):
  number_list.sort()
  return number_list[-1]

# Challenge 3

def occurrences(string1, string2):
  return string1.count(string2)

# Challenge 4

def product(*args):
  number = 1

  for arg in args:
    number *= arg
  
  return number
