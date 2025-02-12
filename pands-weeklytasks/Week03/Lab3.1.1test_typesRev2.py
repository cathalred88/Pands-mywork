#test_types    
# Author: Andrew Beaty
# this is copied from onedrive lab to see the format function running. 
# i like how the format function is distributive in that it can call functions defined earlier in the program and assign them into the code we are working on, in sequence. 
# i see there are three {} locations that we will be calling data for, and there are then three variables called to fill these. I will proceed to test what happens when there is a difference in the number required (say 3) and the number called (say 2). Answer - this breaks the code as expected- tuple index out of range. 


i = 3
fl = 3.5
isa = True
memo = 'how now Brown Cow'
lots = []
print('variable {} is of type:{} and value:{}'.format('i', type(i), i))
print('variable {} is of type:{} and value:{}'.format('fl', type(fl), fl))
print('variable {} is of type:{} and value:{}'.format('is', type(isa), isa))
print('variable {} is of type:{} and value:{}'.format('memo', type(memo), memo))

# print('variable {} is of type:{} and value:{}'.format('lots', type(lots), lots))
print('variable {} is of type:{} and value:{}'.format('lots', type(lots), ))