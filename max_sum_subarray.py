# [1,2,3, -1, -3, 4, -20, 5, 6]
# the sub array will start with +ve and end with +ve as well
# when encountered with -ve numbers, keep on moving fwd even untill the cumulative sum becomes zero.
# also when encoutered with a -ve number store the last possible max sum subarray
# after -ve numbers if you encounter +ve number, then that +ve number should be worth the trip over -ve numbers
# otherwise no need to include the -ve numbers. start a new sub array option from the +ve number just encountered
# edge case: all -ve numbers - return max number from array

class Solution:
    last_array_end = -1
    last_array_start = -1
    last_max_sum = None

    def run_solve(self, numbers):
        start_index = 0
        total_nums = len(numbers)
        while(numbers[start_index] <= 0 and start_index < total_nums):
            start_index += 1
        
        if (start_index == total_nums):
            return None

        _, end_index, max_sum = self.find_next_postivies(numbers, start_index)
        while(start_index < total_nums and end_index < total_nums):
            _, neg_end_index, neg_sum = self.find_next_negatives(numbers, end_index + 1)
            _, recover_end_index, neg_recover_sum = self.find_next_postivies(numbers, neg_end_index + 1)
            # print("----------")
            # print(neg_end_index, neg_sum)
            # print(recover_end_index, neg_recover_sum)
            # print("----------")
            if neg_sum + neg_recover_sum < 1:
                self.new_subarray_discovered(start_index, recover_end_index, max_sum)
                start_index = neg_end_index + 1
                end_index = recover_end_index
                max_sum = neg_recover_sum
            else:
                end_index = recover_end_index
                max_sum += neg_sum
                max_sum += neg_recover_sum
            if (recover_end_index == total_nums - 1 or recover_end_index == -1):
                break

        self.new_subarray_discovered(start_index, end_index, max_sum)
        return self.last_array_start, self.last_array_end, self.last_max_sum
        



        # end_index = 0
        # max_sum = None
        # move_start = True
        # prev_index_neg = False
        # neg_sum = 0
        # last_positive_index = None
        # while end_index + 1 < len(numbers) and start_index + 1 < len(numbers):
        #     if move_start:
        #         if numbers[start_index] < 1:
        #             start_index += 1
        #         else:
        #             move_start = False
        #             end_index = start_index + 1
        #             max_sum = numbers[start_index]
        #     else:
        #         if numbers[end_index] < 0 
        #             if last_positive_index is None:
        #                 last_positive_index = end_index - 1
        #             prev_index_neg = True
        #             neg_sum += numbers[end_index]
        #             if neg_sum + max_sum < 1:
        #                 self.new_subarray_discovered(start_index, last_positive_index, max_sum - neg_sum)
        #                 start_index = end_index + 1
        #                 end_index = None
        #                 max_sum = None
        #                 prev_index_neg = None
        #                 neg_sum = None
        #                 move_start = True
        #                 start_index = end_index + 1
        #         elif numbers[end_index] >= 0:
        #             if prev_index_neg:
        #                 prev_index_neg = False
        #                 if (neg_sum > numbers[end_index]):
                            
        #             else:
        #                 end_index += 1

    def find_next_postivies(self, numbers, start_index):
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^")
        # print(start_index)
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^")
        if start_index > len(numbers) - 1:
            return start_index, start_index, 0
        end_index = start_index
        max_sum = 0
        while end_index < len(numbers) and numbers[end_index] > 0:
            max_sum += numbers[end_index]
            end_index += 1

        return start_index, end_index - 1 if end_index > start_index else start_index, max_sum

    def find_next_negatives(self, numbers, start_index):
        # print("###############")
        # print(start_index)
        # print("###############")
        if start_index > len(numbers) - 1:
            return start_index, start_index, 0
        end_index = start_index
        max_sum = 0
        while end_index < len(numbers) and numbers[end_index] < 0:
            max_sum += numbers[end_index]
            end_index += 1

        return start_index, end_index - 1 if end_index > start_index else start_index, max_sum

    def new_subarray_discovered(self, start, end, max_sum):
        # print(start, end, max_sum)
        if max_sum > self.last_max_sum:
            self.last_array_start = start
            self.last_array_end = end
            self.last_max_sum = max_sum


print(Solution().run_solve([1,2,3, -1, -3, 4, -20, 5, 6])) # 7,8,11
print(Solution().run_solve([1,2,3, -1, -3, 4, -20, -5, 6])) # 0,2,6
print(Solution().run_solve([1,20,3, -1, -3, 4, -20, -5, 6])) # 0,2,24
print(Solution().run_solve([1,2,3, -1, -3, 4, -2, 5, 6])) # 5,8,13