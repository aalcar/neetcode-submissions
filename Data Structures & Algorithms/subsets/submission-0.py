class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we can just add and remove 
        # in O(1) because they're unique
        # integers (w/ a set)
        
        # set of sets?
        # if its already there...go back?
        # 
        # either add it
        # or dont
        # for num in nums:
        # go on a branch where we add or dont add
        # 
        # pass in index and array of nums?
        #
        res = set()
        
        def add_next_value(do_add, index, arr, subset):
            if index >= len(arr):
                res.add(tuple(subset[:]))
                return

            if do_add:
                subset.append(arr[index])

            add_next_value(True, index + 1, arr, subset[:])
            add_next_value(False, index + 1, arr, subset[:])
        
        add_next_value(True, 0, nums, [])
        add_next_value(False, 0, nums, [])
        return [list(subset) for subset in res]