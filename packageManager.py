# from datetime import timedelta, datetime
# class packageManager:
    
#     def __init__(self):
        
#         self.timeTable = {}
        
#     time = datetime.now()    
        
        
#     def addToTimeTable(self,time, packageDict):
#         self.timeTable[time] = packageDict
#     def initTimeTable(self, time, hashTable):
#         self.timeTable[time] = hashTable
#     def lookupTimeTable(self,time):
#         if self.time.time.strftime("%H:%M:%S") in self.timeTable.keys():
#             self.timeTable[time.strftime("%H:%M:%S")]
            
#         else:
#             self.time = self.time - timedelta(seconds=1)
    
        
        

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

# pm = PackageManager()
# pm.add_to_time_table("08:31:09", {"some_key": "some_value"})
# pm.add_to_time_table("09:01:24", {"some_other_key": "some_other_value"})

# result = pm.lookup_time_table("09:00")
# print(result)  # prints: {'some_key': 'some_value'}
    