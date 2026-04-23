def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body  tally: total,num = (4,4), (13,9), (15,2), (16,1)
    return total

result = tally([4, 9, 2, 1])
def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. new_list,idx = ([4],0), ([4,9],1), ([4,9,2],2), ([4,9,2,1],3)
    return new_list                    # How does this loop differ from that above? differs because this loop uses indexes, while the one above uses values directly # increment_all

result = copy([4, 9, 2, 1])
def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. new_list,value = ([5],4), ([5,10],9), ([5,10,3],2), ([5,10,3,2],1)
    return new_list

result = increment_all([4, 9, 2, 1])