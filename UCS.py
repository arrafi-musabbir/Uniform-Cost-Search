
'''
Created on Fri Jul 17 23:13:02 2020
@author: ARRAFI
'''

'''
the following section reads from a text file that contains a graph of cities
and cost between cities
'''

with open('Uniform-Cost-Search/Weighted graph(cities).txt', 'r') as f:
    wd = dict()
    for i in f:
        ltemp = i.split()
        if len(ltemp) == 1:
            wd[ltemp[0]] = None
        else:
            wd[ltemp[0]] = dict()
            for i in range(0, len(ltemp)):
                if 2 * i + 1 < len(ltemp) and 2 * i + 2 < len(ltemp):
                    wd[ltemp[0]][ltemp[2 * i + 1]] = int(ltemp[2 * i + 2])

'''
read from a text file and initialized the graph in a dictionary
'''
# this part of commented out code is used to display the initialized dictionary
# for i in wd:
#     print(i, ">:>", wd[i])

'''
priorityQueue method takes dictionary,queue,current cost and return a queue
that is sorted based on min priority as well as the current cost running
'''
def priorityQueue(d, que, cost):
    keys = list()
    values = list()
# the dictionary is initialized into two list
    for i in d:
        keys.append(i)
        values.append(d[i])
    # heapsort method sorts the values list

    def heapSort(l):
        l1 = list()

        def minHeapify(l):
            for i in range(len(l)):
                left = 2 * i + 1
                right = 2 * i + 2
                if (left < len(l) and l[left] < l[i]):
                    l[left], l[i] = l[i], l[left]
                    minHeapify(l)
                if (right < len(l) and l[right] < l[i]):
                    l[right], l[i] = l[i], l[right]
                    minHeapify(l)
            return l
        while len(l) > 0:
            minHeapify(l)
            l[0], l[len(l) - 1] = l[len(l) - 1], l[0]
            l1.append(l.pop())
        l.clear()
        for i in l1:
            l.append(i)
        return l

    heapSort(values)  # sorts values based on min priority
    que.clear()
    # the following section sorts the keys list based on values
    for i in values:
        for key, value in d.items():
            if len(que) == len(keys):
                break
            if value == i:
                que.append(key)
    # poping out the visited node
    if len(que) > 0:
        d.pop(que[0])
    # poping out the cost of visited node
    if len(values) > 0:
        cost = values[0]
    return cost


def ucs(d, S, G):
    print("Running Uniform Cost Search")
    visited = list()
    dtemp = dict()
    que = list()
    # path = dict()  # path keeps track of cost at every visited node
    cost = 0
    temp = S
    que.append(S)
    while len(que) > 0:
        temp = que.pop(0)
        if temp == G:  # checking if goal has been reached
            visited.append(temp)
            # path[temp] = cost
            break
        if visited.count(temp) == 0:  # checking if node has already been visited
            if d[temp] is not None:
                for i in d[temp]:
                    dtemp[i] = d[temp][i] + cost
                    que.append(i)
                visited.append(temp)
            else:
                visited.append(temp)
            # path[temp] = cost
            cost = priorityQueue(dtemp, que, cost)

    if temp == G:
        print("starting search-->", end=" ")
        for i in visited:
            print(i, "-->", end=" ")
        print("reached GOAL")
        print("UCS sol: ", cost)
    else:
        print("No path exist")
    # print(path)
    return None


ucs(wd, "s", "g")
