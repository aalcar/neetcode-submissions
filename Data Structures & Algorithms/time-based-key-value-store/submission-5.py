class TimeMap:
    def __init__(self):
        self.key_to_ts_arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_ts_arr:
            self.key_to_ts_arr[key] = [[timestamp, value]]
        else:
            self.key_to_ts_arr[key].append([timestamp, value])
    """
    map: {
        alice: {
            1: "happy",
            3: "sad"
        }
    }
    """
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_ts_arr:
            return ""
        """
        [1:bar, 4:bar2]
        [1,4] timestamp=5, l=0,r=1, mid = 0, save 1,
        [4]  l=1,r=1, mid = 1+0/2=1
        """
        timestamps = self.key_to_ts_arr[key]
        l, r = 0, len(timestamps) - 1
        saved_timestamp = float('-inf')
        saved_val = ""
        while l <= r:
            mid = l + (r - l) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            elif timestamps[mid][0] > timestamp:
                r = mid - 1 
            else:
                saved_timestamp = max(saved_timestamp, timestamps[mid][0])
                saved_val = timestamps[mid][1]
                l = mid + 1

        if saved_timestamp == float('-inf'):
            return ""

        return saved_val

"""
1. How do we store them?
2. Seems like we can use a binary search for .get()

1.
a. Could have a map in a map?
That seems like the best way ngl

map: key -> map[timestamp]: value

map[key]->map[timestamp]:value

-- getting all of the timestamps is an O(n) operation

I could just aggregate them and do a bin. search on that?

2. 
so we do map[key] and we have the timestamp:value map

that's gonna have a ton of timestamps, which one do we grab?
aggregate into array in O(n)
now we have timestamps[]
do bin search? target is biggest value <= timestamp

we have timestamp=10
BIG--all times are strictly increasing
so we DONT have to sort it
[] len=10, mid=4, nums[mid]=7
7 IS smaller
so it could be 7, but we want the biggest val possible, so we search the right

our binary search:
-- calculate mid = l + (r - l) // 2
-- if nums[mid] < target:
----- SAVE IT
----- l = mid + 1 (search right)
-- else if nums[mid] > target:
----- don't save
----- r = mid - 1 (search left)
--- else 
------ early return value

--- literally just normal binary search lol? but we save values that
--- are less than target and keep looking for more.
--- == is the biggest val possible, so we can early return it
"""

