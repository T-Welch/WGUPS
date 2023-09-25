
from datetime import datetime, timedelta
from bisect import bisect_left

class packageManager:
    
    def __init__(self):
        self.timeTable = {}
        self.sortedTimes = []
        
    def addToTimeTable(self, time_str, package_dict):
        time = datetime.strptime(time_str, "%H:%M:%S").time()
        index = bisect_left(self.sortedTimes, time)
        self.sortedTimes.insert(index, time)
        self.timeTable[time] = package_dict
        
    def lookupTimeTable(self, time_str):
        time = datetime.strptime(time_str, "%H:%M:%S").time()
        index = bisect_left(self.sortedTimes, time)
        if index == 0:
            return None
        closest_time = self.sortedTimes[index - 1]
        return self.timeTable[closest_time]

    