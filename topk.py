array = []

def readFile(name): #reads the file into an array
    file = open(name)  # opens file and reads it
    file = file.read()
    var = file.splitlines()
    for line in var:
        word = line.split(':') #take the colon out
        word[0], word[1] = int(word[0]), int(word[1])
        array.append(word)  # appends each line to the array
    return array

readFile('timeSpent.txt')


def swap(minheap, i, j): #swap values
    minheap[i], minheap[j] = minheap[j], minheap[i]

#O(n-k)
def buildHeap(minheap, array): #builds a min heap of k values
    for i in range(len(minheap), len(array)):
        if minheap[0][1] < array[i][1]: #if minheap's root is less than the main list's
            minheap[0] = array[i] #update minheap's root
            sink(0) #sink it to the correct position
        elif minheap[0][1] == array[i][1] and minheap[0][0] > array[i][0]: #if minheap's & arrays time are equal &  minheap's ID > main list's ID
            minheap[0] = array[i]
            sink(0)


def smallest_child(i):
    if (2 * i) + 2 == len(minheap): #if only left child
        return 2 * i + 1  # left child
    elif minheap[2 * i + 1][1] < minheap[2 * i + 2][1]: #if left is less than right child
        return 2 * i + 1  # left child
    elif minheap[2 * i + 1][1] == minheap[2 * i + 2][1] and minheap[2 * i + 1][0] > minheap[2 * i + 2][0]: #if the time is equal for left & right,& left chillds user ID is greater than the rights
        return 2 * i + 1 # left child
    else:
        return 2 * i + 2  # right child

def sink(i): #O(lgk)
    swapped = False
    while (i * 2 + 1) < len(minheap) and swapped == False:
        mc = smallest_child(i)
        if minheap[i][1] >= minheap[mc][1]:
            swap(minheap, i, mc)
            i = mc
        else:
            swapped = True



#get the minimum element and add it to a new list
def getMin(minheap, new):
    new.append(minheap[0])
    swap(minheap, 0, len(minheap) - 1)
    minheap.pop()
    sink(0)


minheap = []

k = int(input("Enter k: "))

for i in range(k):
    minheap.append(array[i])
buildHeap(minheap, array)


new = []
for i in range(k):
    getMin(minheap, new)

for i in range(len(new)-1, -1, -1):
    print('User ID: ' + str(new[i][0]) + ' Time Spent: ' + str(new[i][1]))