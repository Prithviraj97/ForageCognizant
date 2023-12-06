import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
  # Count the frequency of characters in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    # Initialize variables for sliding window
    start = 0
    end = 0
    min_length = float('inf')
    required_chars = len(t)

    while end < len(s):
        # Check if the current character is part of t
        if s[end] in t_count:
            if t_count[s[end]] > 0:
                required_chars -= 1
            t_count[s[end]] -= 1

        # Try to minimize the substring by moving the start index
        while required_chars == 0:
            # Update the minimum length
            min_length = min(min_length, end - start + 1)

            # Move the start index and restore the character count
            if s[start] in t_count:
                t_count[s[start]] += 1
                if t_count[s[start]] > 0:
                    required_chars += 1
            start += 1

        # Move the end index to expand the substring
        end += 1

    return min_length if min_length != float('inf') else -1
  

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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  