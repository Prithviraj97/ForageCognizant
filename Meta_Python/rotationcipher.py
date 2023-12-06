'''
Rotational Cipher
    One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
    Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
    For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". 
    Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced 
    with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
'''

#function for roatation cipher.
# def rotation_cipher(string):
#     result = ""
#     #iterate through each char in the string
#     for i in range(len(string)):
#         #check if it's an alphabet or number
#         if (ord('a') <= ord(string[i]) and ord(string[i]) <= ord('z')):
#             #calculate new position of letter after rotation
#             newPos = ((ord(string[i]) - ord('a') + 3) % 26 ) + ord('a')
#             #convert back to chr() and add to result
#             result += chr(newPos)
#         elif (ord('A') <= ord(string[i]) and ord(string[i]) <= ord('Z')):
#             #calculate new position of letter after rotation
#             newPos = ((ord(string[i]) - ord('A') + 3) % 26 ) + ord('A')
#             #convert back to chr() and add to result
#             result += chr(newPos)
#         elif (ord('0') <= ord(string[i]) and ord(string[i]) <= ord('9')):
#             #calculate new position of digit after rotation
#             newPos = ((ord(string[i]) - ord('0') + 3) % 10 ) + ord('0')
#             #convert back to chr() and add to result
#             result += chr(newPos)
#         else:
#             #if not a letter or digit just copy over
#             result += string[i]
#             return result
# print(rotation_cipher("Zebra-493?"))

#Facebook + own solution for test cases.
import math
# Add any extra import statements you may need here
import string

# Add any helper functions you may need here
def rotation(char, rotation):
  if char.isalpha():
      # Determine the case (upper or lower)
      is_upper = char.isupper()

      # Apply rotation to the character
      rotated_char = chr((ord(char) - ord('A' if is_upper else 'a') + rotation) % 26 + ord('A' if is_upper else 'a'))

      return rotated_char
  elif char.isdigit():
      # Apply rotation to digits
      return str((int(char) + rotation) % 10)
  else:
      # Return non-alphanumeric characters unchanged
      return char

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  rotated = ""
  for char in input_str:
    rotated += rotation(char, rotation_factor)  
  return rotated


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  