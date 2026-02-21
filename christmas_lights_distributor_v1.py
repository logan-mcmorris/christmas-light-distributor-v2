import math
import itertools
        
def list_comparison(lights):
    global deviationWinner
    global winnerList
    
    if lights in winnerList:
        return
    
    #accounts for the lights looping
    lights2 = lights + lights
    deviationChallenger = []
    
    #iterate through each UNIQUE character
    seen = []
    for color in (lights):
        if color in seen:
            continue
        seen.append(color)
        
        distance = 0
        distanceValues = []
        firstInstanceHit = 0
        
        #check each distance between characters and put them in a list
        for spot, i in enumerate(lights2):
            
            #make sure the color has appeared at least once before comparing
            if color != i and firstInstanceHit == 0:
                continue
            
            if color == i and firstInstanceHit == 0:
                firstInstanceHit = 1
                continue
            
            if color != i:
                distance += 1
                continue
            
            else:
                distanceValues.append(distance)
                distance = 0
            
            #stop after 50% (accuracy reasons)
            if spot + 1 > len(lights2) // 2:
                break
        
        #print(distanceValues)
        average = sum(distanceValues) / len(distanceValues)
        #print(average)
        deviation = abs(max([max(distanceValues) - average, min(distanceValues) - average]))
        #print(deviation)
        deviationChallenger.append(deviation)
    
    
    #information saved per iteration
    info = {'Pattern':lights, 'Deviation':max(deviationChallenger)}

    if max(deviationChallenger) < max(deviationWinner):
        deviationWinner = deviationChallenger
        print('new winner!', info)
        winnerList.append(lights[:])
    elif max(deviationChallenger) == max(deviationWinner):
        print('new tie!:', info)
        winnerList.append(lights[:])


lightsDict = {'R': 3, 'G': 3, 'B': 2, 'Y': 2}
deviationWinner = [999]
winnerList = []

#convert dict to list
lights = []
for i, j in lightsDict.items():
    #print(i, j)
    
    while j > 0:
        lights.append(i)
        j -= 1

#call permutation function
print('Generating permutations...')
final = set(itertools.permutations(lights))
print(f'Generation done. {len(final)} permutations to compare.')
for i in final:
    list_comparison(i)
