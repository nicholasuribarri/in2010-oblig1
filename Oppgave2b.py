import heapq
import sys
def algoritme(array):
    high = len(array)-1
    if 0 <= high:
        v = []
        h = []
        mid = round(high/2)
        for count in range(len(array)):
            if count < mid:
                heapq.heappush(v, heapq.heappop(array))
            else: #count >= mid:
                heapq.heappush(h, heapq.heappop(array))  
        print(heapq.heappop(h))
        algoritme(h)
        algoritme(v)
    return 

#nput = [0,10,20,30,40,50,60,70,80,90,100, 110, 150, 167, 123451]
#algoritme(input)

read = sys.stdin.read().splitlines() # en liste med 1 element for hver linje
input = []
for i in read:
    input.append(i)

algoritme(input)
