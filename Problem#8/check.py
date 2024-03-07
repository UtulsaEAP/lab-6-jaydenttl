'''
Name: Jayden Ly
Lab Time: 3/7/24 1:01 PM
'''
def in_order(nums):
    # Type your code here.
    for n in range(len(nums) -1):          #for index in the range 4
        if nums[n] >nums[n +1]:           # if 0>1    1>2 etc.
            return False                    #false
    else:
        return True

if __name__ == '__main__':
    # Test out-of-order example 
    nums1 = [5, 6, 7, 8, 3] #THIS IS NOT IN OREDR GANG
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10] #THIS IS IN OREDER GANG!!
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
