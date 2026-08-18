class TimeMap:

    """
    Given:
        0<= timestamp <=
        1 <= key.length, value.length <= 100
        key, value are lower english and digits
        unique key, unique timestamps, multiple values
        set operations are in ascending sorted order

    Result:
        __init__: create the class object
        set: store the key and value at timestamp
        get: 
            return the value associated with the largest timestamp_prev
            Otherwise, return ""

    Approach:



    """

    def __init__(self):
        self.key_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_map:
            self.key_map[key] = []

        self.key_map[key].append([value, timestamp])
    

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_map:
            return ""

        values = self.key_map.get(key)

        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        
        return res
