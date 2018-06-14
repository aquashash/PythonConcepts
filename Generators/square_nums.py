# square numbers function is returning a list

def square_numers_list(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_numers_list([1,2,3,4,5,6])
print(my_nums)


# converting above function to generator

def square_numers_gen(nums):
    for i in nums:
        yield(i*i)


my_nums = square_numers_gen([1,2,3,4,5,6])
print(my_nums)

for num in my_nums:
    print(num)


# same function with list comprehension
my_num = [i*i for i in [1,2,3,4,5,6]]
print(my_num)
for num in my_num:
    print (num)


## converting list comprehension to generator
my_num = (i*i for i in [1,2,3,4,5,6])

print(my_num)
print(list(my_num))

for num in my_num:
    print (num)


