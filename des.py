def hex2bin(s):


mp = {'0': "0000",
      '1': "0001",
      '2': "0010",
      '3': "0011",
      '4': "0100",
      '5': "0101",
      '6': "0110",
      '7': "0111",
      '8': "1000",
      '9': "1001",
      'A': "1010",
      'B': "1011",
      'C': "1100",
      'D': "1101",
      'E': "1110",
      'F': "1111"}
bin = ""
for i in range(len(s)):
bin = bin + mp[s[i]]
return bin
# Binary to hexadecimal conversion
def bin2hex(s):


mp = {"0000": '0',
      "0001": '1',
      "0010": '2',
      "0011": '3',
      "0100": '4',
      "0101": '5',
      "0110": '6',
      "0111": '7',
      "1000": '8',
      "1001": '9',
      "1010": 'A',
      "1011": 'B',
      "1100": 'C',
      "1101": 'D',
      "1110": 'E',
      "1111": 'F'}
hex = ""
for i in range(0, len(s), 4):
ch = ""
ch = ch + s[i]
ch = ch + s[i + 1]
ch = ch + s[i + 2]
ch = ch + s[i + 3]
hex = hex + mp[ch]
return hex
# Binary to decimal conversion
def bin2dec(binary):


binary1 = binary
decimal, i, n = 0, 0, 0
while(binary != 0):
dec = binary % 10
decimal = decimal + dec * pow(2, i)
binary = binary//10
i += 1
return decimal
# Decimal to binary conversion
def dec2bin(num):


res = bin(num).replace("0b", "")
if(len(res) % 4 != 0):
div = len(res) / 4
div = int(div)
counter = (4 * (div + 1)) - len(res)
for i in range(0, counter):
res = '0' + res
return res
# Permute function to rearrange the bits
def permute(k, arr, n):


permutation = ""
for i in range(0, n):
permutation = permutation + k[arr[i] - 1]
return permutation
# shifting the bits towards left by nth shifts
def shift_left(k, nth_shifts):


s = ""
for i in range(nth_shifts):
for j in range(1, len(k)):
s = s + k[j]
s = s + k[0]
k = s
s = ""
return k
# calculating xow of two strings of binary number a and b
def xor(a, b):


    ans = ""
    for i in range(len(a)):
    if a[i] == b[i]:
    ans = ans + "0"
    else:
    ans = ans + "1"
    return ans
# Table of Position of 64 bits at initial level: Initial Permutation Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
