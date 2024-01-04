#binary search algorithm
#for a given list and number, find the index of the number using binary search
def bsearch(l, x):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (high+low)//2
        if l[mid] == x:
            return mid 
        elif l[mid] < x:
            low = mid + 1
        else: 
            high = mid -1
    return -1
# k=bsearch([1,2,3,4,5], 6)
# print('The value of k is: ',k)


##index of the first occurense of the element an array

def firstoccurense(l, x):
    low=0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]<x:
            low = mid + 1
        elif l[mid]>x:
            high = mid - 1
        else:
            if mid==0 or l[mid-1]!=l[mid]:
                return mid 
            else:
                high = mid-1
    return -1

# k=firstoccurense([1,2,3,3,4,4,4,5], 4)
# print(k)

##index of last occurense of the element
def lastoccurense(l, x):
    low=0
    high=len(l)-1 # 5
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low = mid+1 ## low 3
        elif l[mid]>x:
            high = mid-1
        else:
            if mid==len(l)-1 or l[mid+1]!=l[mid]:
                return mid 
            else:
                low = mid+1 #low 5
    return -1

k=lastoccurense([1,2,3,3,4,4,4,4,4], 4)
print(k)


##Count occurences in a sorted array
def countoccurenses(l, x):

    return


##square root of and
def squareroot(l, x):

    return