# Function that finds the number of chickens and dogs

def test_function(numHeads, numLegs):
    for numChick in range (0, numHeads + 1):
        numDogs = numHeads - numChick
        totLegs = 4 *  numDogs + 2* numChick
        if totLegs == numLegs:
            return [numChick, numDogs]
    return None












