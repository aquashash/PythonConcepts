# Generators - another example to understand how to use and benefits
import random
import memory_profiler as mem_profile
import time

names= ['Robert', 'Eddy',' Praniel', 'Peter', 'John', 'Bill', 'David']
major =['computers', 'electrical', 'mechanical', 'statistics', 'history', 'economics']
print('Memory (Before): {} MB'.format(mem_profile.memory_usage()))


# list
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = { "id" : i,
                   "name":random.choice(names),
                   "major": random.choice(major)
                }
        result.append(person)
    return result


# generator
def people_generator(num_people):
    for i in range(num_people):
        person = { "id" : i,
                   "name":random.choice(names),
                   "major": random.choice(major)
                }
        yield person

# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print('Memory (After): {} Mb'.format(mem_profile.memory_usage()))
print('Took {} seconds'.format(t2-t1))
