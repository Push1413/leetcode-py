def longestConsecutive(nums)-> int:
    num_set = set(nums)
    longest_streak = 0
    for i in num_set:
        if i-1 not in num_set:
            current_streak =1
            current_num = i
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak+=1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


if __name__ == '__main__':
    num = [0,3,7,2,5,8,4,6,0,1];
    print(longestConsecutive(num));

