# takes two numbers and return their sum
def sum_two_numbers(x, y):
    total =  x + y
    return total


# takes a list and returns the sum of the list
def sum_a_list(l):
    total = 0
    for i in l:
        total += i
    
    return total

# takes a list and returns if the list has duplicate numbers
def has_duplicates(l):
    print("Starting loop")
    for i1 in range(0,len(l)):
        print("iteration", i1)
        for i2 in range(i1 + 1, len(l)):
            print("nested iteration", i2)
            n1 = l[i1]
            n2 = l[i2]
            print("n1=", n1)
            print("n2=", n2)
            if n1 == n2:
                return True

    return False


assert sum_two_numbers(10, 12) == 22

assert sum_a_list([1,2,3]) == 6

print("has duplicates case 1")
assert has_duplicates([1,4,5,2,3, 2]) == True
print("SUCCESS")

print("has duplicates case 2")
assert has_duplicates([1,2,3]) == False
print("SUCCESS")





print("All tests succeeded")