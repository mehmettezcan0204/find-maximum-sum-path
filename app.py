data = """1
          8 4
          2 6 9
          8 5 9 3"""


# check given number is prime number
def is_prime(num):
    # if num=1 return True. because 1 is not prime number
    if num >= 2:
        # divide each number which is smaller than 
        # the given 'num'
        # if one of the division remainder equals 0 
        # return True (that proves number is not prime)
        # else return False (because number is prime)
        for y in range(2,num):
            if ( num % y ) == 0:
                return False
        return True        
    else:
        return False


# for given pyramid array 
# start from bottom to top
# on each element find the max NON PRIME number and 
# add to current number
# ex:
# line-1    1
# line-2    4 6
# line-3    7 8 9


# we start from the bottom two line (line-3, line-2 )
# check each line for prime number
# line-3 =  7(prime) 8 9 >> [0, 8, 9] 
# line-2 = 4 6 >> [4, 6]

# now we sum the each corresponding lines
# and take the max sum
# line-2 + line-3 >> [max(4+0=4 ,4+8=12 ), max(6+8=14, 6+9=15)]
# >> [12, 15]

# now current pyramid is
# 1
# 12 15

# do this process recursively unless the pyrmid lenght becomes 1
# [max(12+1=13, 1+15=16 )] >> [16]

# max sum path will be >> 16 

def findMaxSumPath(pyramid):
    while len(pyramid) > 1:
        # get last two line of the pyramid
        t0 = pyramid.pop() # [8, 5, 9 , 3]
        t1 = pyramid.pop() #  [2, 6, 9],
        
        newPyramidLine =[]
        for i,t in enumerate(t1):
            # push the max sum NON PRIME numbers the new array
            if(is_prime(t)):
                newPyramidLine.append(0)
            else:
                newPyramidLine.append(max(t0[i], t0[i+1]) + t)    
        pyramid.append(newPyramidLine)
    return pyramid[0][0]



# convert pyramid string to array for calculation
def formatStringToArray(pyramitData):
    mainPyramid = []
    for row in pyramitData.splitlines():
        pyramidStep = []
        for eachNum in row.split():
            # convert each value to integer
            pyramidStep.append(int(eachNum))
        mainPyramid.append(pyramidStep)
    return 

print(findMaxSumPath(formatStringToArray(data)))

