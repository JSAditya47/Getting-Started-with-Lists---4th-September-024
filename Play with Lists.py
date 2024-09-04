L = [4, 5, 1, 2, 9, 7, 10, 8  ]
print(f"Original List: {L}")

count = 0

for i in L:
    count = count + i
    
avg = count/len(L)

print(f"Sum = {count}")
print(f"Average = {avg}")

L.sort()
print(L)

print("\nSmallest Element is: ", L[0])
print("\nLargest Element is: ", L[-1])
