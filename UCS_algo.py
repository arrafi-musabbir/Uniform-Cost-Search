
class UCS:

    def __init__(self, dic, start, goal):
        self.dic = dic
        self.start = start
        self.goal = goal
        self.ucs()

    '''
    priorityQueue method takes dictionary,queue,current cost and return a queue
    that is sorted based on min priority as well as the current cost running
    '''

    def priorityQueue(self, d, que, cost):
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

    def ucs(self):
        print("Running Uniform Cost Search")
        d = self.dic
        start = self.start
        goal = self.goal
        visited = list()
        dtemp = dict()
        que = list()
        # path = dict()  # path keeps track of cost at every visited node
        cost = 0
        temp = start
        que.append(temp)
        while len(que) > 0:
            temp = que.pop(0)
            if temp == goal:  # checking if goal has been reached
                visited.append(temp)
                # path[temp] = cost
                break
            if visited.count(temp) == 0:  # checking if node has already been
                                          # visited
                if d[temp] is not None:
                    for i in d[temp]:
                        dtemp[i] = d[temp][i] + cost
                        que.append(i)
                    visited.append(temp)
                else:
                    visited.append(temp)
                # path[temp] = cost
                # will sort the nodes based on min priority
                cost = self.priorityQueue(dtemp, que, cost)

        if temp == self.goal:
            print("starting search-->", end=" ")
            for i in visited:
                print(i, "-->", end=" ")
            print("reached GOAL")
            print("UCS sol: ", cost)
        else:
            print("No path exist")
        # print(path)
        return None
