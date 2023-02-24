import statistics, random

def mean_colour(colour):
  meanColour = statistics.mean(colour)
  print(meanColour)


def mode_colour(clothes):
  most_colour = {}
  for colours in clothes.values():
    for colour in colours:
      most_colour.setdefault(colour, 0)
      most_colour[colour] += 1

  max_clothe = max(most_colour.values())
  for k,v in most_colour.items():
   return k, v if v == max_clothe else print()


def median_colour(colour):
  n = len(colour)
  mid = n//2

  if n%2 == 0:
    return (colour[mid], colour[mid-1])
  return colour[mid]


def probabilty_red(colours):
  redProbability = colours.count('red')/len(colours)
  print(f'{int(redProbability*100)}%')


def recursive_number(listOfNumber, number):
  if number == listOfNumber[0]:
    return True 
  return recursive_number(listOfNumber[1:], number)


def binary_to_base10():
  numbers = ''
  for _ in range(4):
    numbers += str(random.randint(0,1))
  print(numbers)
  return int(numbers, base=2)


def sum_of_fibonacci(number=50):
  if number <= 2:
    return 1
  return sum_of_fibonacci(number-1) + sum_of_fibonacci(number-2)
