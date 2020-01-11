import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = sorted(f.read().split("\n"))  # List containing 10000 names
f.close()

def get_mid(arr):
    return int((len(arr)-1)/2)

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
DONE = False
CHECKING = True
i = 0
m = get_mid(names_2)
m_item = names_2[m]
l,r = names_2[:m], names_2[m:]
while DONE is False: #O(n) 9xFaster
    #check if we are at end
    if i > len(names_1)-1:
        DONE = True
        break
    #create checking loop per item of array 1
    while CHECKING: #O(log(n))
        #left side
        if names_1[i] < m_item:
            # check if have dwindled down to nothing
            if len(l) > 2:
                m = get_mid(l)
                m_item = l[m]
                l,r = l[:m], l[m:]
            #if only 1 item
            else: 
                if l[0] == names_1[i]:
                    duplicates.append(l[0])
                elif len(l) > 1 and l[1] == names_1[i]:
                    duplicates.append(l[1])
                CHECKING = False
                
        #right side
        else:
            if len(r) > 2:
                m = get_mid(r)
                m_item = r[m]
                l,r = r[:m], r[m:]
            else: #if only 1 item
                if r[0] == names_1[i]:
                    duplicates.append(r[0])
                elif len(r) > 1 and r[1] == names_1[i]:
                    duplicates.append(r[1])
                CHECKING = False
                

    i += 1 # incriment up array1
    m = get_mid(names_2) #reset to middle of array2
    m_item = names_2[m] #reset to middle item of array2
    l,r = names_2[:m], names_2[m:] #reset l&r to array2
    CHECKING = True #reset checking




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
