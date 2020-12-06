
nums = []
with open('input.txt') as fp:
       for cnt, line in enumerate(fp):
           nums.append(int(line.strip('\n')))

# part 1
def part_1():
    for i in range(len(nums)-1):
        for j in range(len(nums)):
            a, b = nums[i], nums[j]

            if a + b == 2020:
                print(a * b)
                exit(0)

# part 2
def part_2():
    for i in range(len(nums)-2):
        for j in range(len(nums)-1):
            for k in range(len(nums)):
                        a, b, c = nums[i], nums[j], nums[k]

                        if a + b + c == 2020:
                            print(a*b*c)
                            exit(0)


part_2()
