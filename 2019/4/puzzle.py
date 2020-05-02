input = "138307-654504"

[lower, upper] = input.split('-')

def does_repeat(num):
    seen = []
    for digit in str(num):
        if digit in seen:
            return True
        seen.append(digit)
    return False

def always_increments(num):
    prev = -1 
    for digit in str(num):
        if int(digit) < prev:
            return False
        else:
            prev = int(digit)
    return True

def one_group_of_two(num):
    num = str(num)
    start = end = 0

    while end < len(num):
        while end < len(num) and num[start] == num[end]:
            end += 1
        if end - start - 1 == 1:
            return True
        else:
            start = end
            end += 1
    return False

count = 0
for i in range(int(lower), int(upper)):
    if len(str(i)) != 6:
       continue
   #make sure there is at least one repeating digit
    if not does_repeat(i):
       continue
   #make sure digits are always incrementing throughout num
    if not always_increments(i):
       continue
   #make sure there is at least one group of exactly 2 adjacent digits
    if not one_group_of_two(i):
       continue
    count += 1
print(count)

    
   


