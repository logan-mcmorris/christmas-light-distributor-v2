import copy


#Converts a dictionary of values to a list of perfectly distributed values.
#Ex: {'A':2, 'B:4'} -> [[A, X, X, A, X, X], [B, X, B, B, X, B]]
def distribute(mainDict, placeholder):
    mainList = [] #will contain a list of lists, one list for each key
    total = sum(mainDict.values())

    #distribute each item into a list
    firstIteration = True

    for key in mainDict:

        #get the spacing between the key
        spacing = total / mainDict[key]
        step = spacing

        #create a list with one item of the key
        subList = [key]

        #generate the rest of the list based off of the spacing
        for i in range(total - 1):
            if  (i + 1) >= step:
                subList.append(key)
                step += spacing
            else:
                subList.append(placeholder)

        mainList.append(subList)
    return(mainList)


#Finds and returns solutions given a list of distributed lists.
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
#A solution check is only performed while on the final (deepest) sublist ('C' in the example)
#The iteration for a particular sublist is stopped early to prevent multiples of the same solution:
#Example: ['A', '-', '-','A', '-', '-'] will appear twice, so we stop 3 iterations in.
def generate(mainList, iterList, placeholder, index = 1, solutionList = []):

    #iterate through iterList (length of iterList) times
    for i in range(len(iterList[0])):

        #if there are deeper sublists, recursively call the function
        if index + 2 <= len(iterList):
            generate(mainList, iterList, placeholder, index + 1, solutionList)
        #else, we're on the final sublist, check the solution
        else:
            compiledCandidate = solution_check(iterList, placeholder)
            if compiledCandidate != 0:
                solutionList.append(compiledCandidate)

        #insert the last element into the first slot
        iterList[index].insert(0,iterList[index].pop())

        #stop early if the current sublist matches same mainList sublist
        if iterList[index] == mainList[index]:
            return(solutionList)


#Returns 0 if the candidate isn't a solution, and the formatted candidate if it is.
#Prints the formatted solution
#Checks if all of the sublists in a list have exactly one value, throughout all of the sublists, for each index
#Success exmple: [['A', '-', '-'], ['-', 'B', '-'], ['-', '-', 'C']]
#Fail exmple: [['A', '-', '-'], ['B', '-', '-'], ['-', '-', 'C']]
def solution_check(candidate, placeholder):
    compiledCandidate = []

    #iterates len(iterlist) times
    for i in range (len(candidate[0])):
        sum = 0
        #calculates how many elements are present throughout all sublists at index [i]
        for subList in candidate:
            if subList[i] != placeholder:
                sum += 1
                compiledCandidate.append(subList[i])
        #if sum > 1, the check fails and ends
        if sum > 1:
            return(0)

    #solution found, print and return the solution
    print('Solution found:',' '.join(compiledCandidate))
    return(compiledCandidate)


#Original problem: {'🔴':3, '🟢':3, '🔵':2, '🟡':2}
def main():
    placeholder = None #the value used for empty space in the sublists
    mainDict = {'🔴':3, '🟢':3, '🔵':2, '🟡':2} #items to be sorted
    print('Your items:', mainDict)
    print('Searching for solutions...')

    mainList = distribute(mainDict, placeholder)
    solutionList = generate(mainList, copy.deepcopy(mainList), placeholder)

    #print solution number
    if solutionList:
        print(f'{len(solutionList)} solutions found!')
    else:
        print('No solutions found.')


if __name__ == "__main__":
    main()