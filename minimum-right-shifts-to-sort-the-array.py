def checkIfArrayIsSorted(nums):
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            return False
    return True
def minimumRightShifts( nums):
    shifts=0
    while(nums[-1]<nums[0]):
        storeValue=nums[-1]
        nums.pop()
        nums.insert(0,storeValue)
        shifts+=1
        
    if(checkIfArrayIsSorted(nums)==False):
        return -1
    return shifts
        

print(minimumRightShifts([2,1,4]))

