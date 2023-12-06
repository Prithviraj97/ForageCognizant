'''Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.
Matching Pairs
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def swap_char(string, i,j):
  charlist = list(string)
  if 0<=i<len(charlist) and 0<=j<len(charlist):
    charlist[i], charlist[j] = charlist[j], charlist[i]
    return ''.join(charlist)
  else:
    print("Invalid Indices")
    return string

def matching_pairs(s, t):
  # Write your code here
  match = 0
  n = len(s)
  initialmatch = sum(1 for i in range(n) if s[i]==t[i])
  max_matching = initialmatch
  for i in range(n):
    for j in range(i+1,n):
      swapped_s = swap_char(s,i,j)
      current_match = sum(1 for k in range(n) if swapped_s[k]==t[k])
      max_matching = max(max_matching, current_match)
  return max_matching
    

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)


  