grades = ['A', 'B', 'C', 'D', 'F']
cutoffs = [90, 80, 70, 65, 0]



def assigngrade(score, grades = ['A', 'B', 'C', 'D', 'F'], cutoffs = [90, 80, 70, 65, 0]):
    for x in range(len(cutoffs)):
        if score >= cutoffs[x]:
            return grades[x]

def droplowest(L):
    min = 2000
    for x in L:
        if x < min:
            min = x
    L.remove(min)
    return L

def average(L):
    sum = 0
    for x in L:
        sum += x
    return sum / len(L)



