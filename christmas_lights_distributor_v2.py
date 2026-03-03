import math
import itertools
import copy


#Converts a dictionary of values to a list of perfectly distributed values.
#Ex: {'A':2, 'B:4'} -> [[A, X, X, A, X, X], [B, X, B, B, X, B]]
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


#This is a recursive function that iterates through every permutation of mainList.
#To do this, it uses a copy of mainList, "iterList."
#Visual representation with one 'A' 'B' and 'C':

#[['A', '-', '-'], ['B', '-', '-'], ['C', '-', '-']]
#[['A', '-', '-'], ['B', '-', '-'], ['-', 'C', '-']]
#[['A', '-', '-'], ['B', '-', '-'], ['-', '-', 'C']]
#[['A', '-', '-'], ['-', 'B', '-'], ['C', '-', '-']]
#[['A', '-', '-'], ['-', 'B', '-'], ['-', 'C', '-']] ... and so on.

#NOTES:
#The first sublist ('A' in the example) does not iterate to prevent duplicate solutions that are just shifted by 1.
#A solution check is only performed while on the final sublist ('C' in the example)
#The iteration for a particular sublist is stopped early to prevent multiples of the same solution:
#Example: ['A', '-', '-','A', '-', '-'] will appear twice, so we stop 3 iterations in.
def generate(mainList, iterList, placeholder, index = 1):

    #iterate through iterList (length of iterList) times
    for i in range(len(iterList[0])):

        #if there are deeper sublists, recursively call the function
        if index + 2 <= len(iterList):
            generate(mainList, iterList, placeholder, index + 1)
        #else, we're on the final sublist, check the solution
        else:
            solution_check(iterList, placeholder)

        #insert the last element into the first slot
        iterList[index].insert(0,iterList[index].pop())

        #stop early if the current sublist matches same mainList sublist
        if iterList[index] == mainList[index]:
            return()


#Checks if all of the sublists in a list have exactly one value, throughout all of the sublists, for each index
#Success exmple: [['A', '-', '-'], ['-', 'B', '-'], ['-', '-', 'C']]
#Fail exmple: [['A', '-', '-'], ['B', '-', '-'], ['-', '-', 'C']]
def solution_check(candidate, placeholder):
    #iterates len(iterlist) times
    for i in range (len(candidate[0])):
        sum = 0
        #calculates how many elements are present throughout all sublists at index [i]
        for subList in candidate:
            if subList[i] != placeholder:
                sum += 1
        #if sum > 1, the check fails and ends
        if sum > 1:
            return()

    #solution found!
    solution_formatting(candidate, placeholder)


#formats the solution (in this case, into a print statement)
def solution_formatting(solution, placeholder):

    #compile the solution into a single list, going one index at a time
    compiledSolution = []
    for i in range (len(solution[0])):
        for subList in solution:
            if subList[i] != placeholder:
                compiledSolution.append(subList[i])
    
    #print the compiled solution (formatting avoids bugs with emojis)
    formatting = ''
    for i in compiledSolution:
        formatting += i
    print(f'Solution Found: {formatting} {formatting}')


def main():
    placeholder = 'x' #the character used for empty space in the sublists
    mainDict = {'🔴':3, '🟢':3, '🔵':2, '🟡':2} #items to be sorted

    print('Your items:', mainDict)
    mainList = distribute(mainDict, placeholder)
    mainList = generate(mainList, copy.deepcopy(mainList), placeholder)


if __name__ == "__main__":
    main()