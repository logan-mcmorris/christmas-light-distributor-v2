import math
import itertools

#converts a dictionary of values to a list of perfectly distributed values
#ex: {'A':2, 'B:4'} -> [[A, X, X, A, X, X], [B, X, B, B, X, B]]
def distribute(mainDict, placeholder):
    mainList = []
    total = sum(mainDict.values())

    #distribute each item into a list
    firstIteration = True
    for key in mainDict:
        subList = [key]
        quotient = total / mainDict[key]
        step = quotient
        for i in range(total - 1):
            if  (i + 1) >= step:
                subList.append(key)
                step += quotient
            else:
                subList.append(placeholder)
        mainList.append(subList)
    return(mainList)

#generate every possible looping configuration of a list while keeping order
#ex: [A, A, x, x] -> [[A, A, x, x], [x, A, A, x], [x, x, A, A], [A, x, x, A]]
#then finds the cartesian product
def generate(mainList):
    newList = []

    firstIteration = True
    for subList in mainList:

        #prevent first sublist from iterating
        #prevents duplicate solutions that are shifted over by one
        if firstIteration == True:
            firstIteration = False
            newList.append([subList])
            continue

        generations = []
        while True:
            #add generation
            generations.append(subList.copy())

            #move the back value to the front
            cut = subList.pop()
            subList.insert(0, cut)
            
            #if it exists in generations, break
            if subList in generations:
                break

        newList.append(generations)
    newList = list(itertools.product(*newList))
    print(newList)
    return(newList)

#returns a list of the combinations with the least max slide
def slide(mainList, placeholder):
    winner = []
    #get length of all of the itmes
    length = len(mainList[0][0])

    #for each combination contender
    for contender in mainList:

        #create "addList" that shows amount entries per slot when overlapped
        #for each value (like "A") in the combination contender, add 1 to each slot
        #ex: [A, X, A] and [B, X, X] -> [2, 0, 1]
        addList = [0] * length
        for item in contender:
            for index, value in enumerate(item):
                #if a value exists in the index, add 1 to the index of addList
                if value != placeholder:
                    addList[index] += 1
        #temporary code to find any semi-perfect solutions (this does not do subgroup calculations) (repeats code)
        if not (any(weight != 1 for weight in addList)):
            #compile solution
            perfectSolution = [placeholder] * length
            for item in contender:
                for index, value in enumerate(item):
                    if value != placeholder:
                        perfectSolution[index] = value
            #formatting
            formatting = ''
            for i in perfectSolution:
                formatting += i
            formatting += formatting
            print('Semi-perfect solution found:', formatting)
            


#SCORE CALCULATION PRIORITY (INCOMPLETE, NOT IMPLEMENTED):

#1) lowest maximum slide (sliding over 1 BEATS sliding over 2)
#2) Fewest slides (sliding one item BEATS sliding over two)
#Example: (two slides of 1) BEATS (one slide of 2)

#3) Highest minimum gap (gaps of [5, 3] BEATS gaps of [2, 6]
#4) Fewest gaps (gaps of [3] BEATS gaps of [3, 3, 3])
#Example: gaps of [5, 5, 3, 3] BEATS gaps of [2, 4]

#UPDATE: subgroups may not be needed
#5) Highest minimum subgroup gap
#6) Fewest subgroup gaps
placeholder = 'X'
mainList = distribute({'🔴':3, '🟢':3, '🔵':2, '🟡':2}, placeholder)
mainList = generate(mainList)
mainlist = slide(mainList, placeholder)