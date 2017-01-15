import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
    def emit_intermediate(self, key, value):
      self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)
    def emit(self, value):
        self.result.append(value) 
    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)
        for key in self.intermediate:
            reducer(key, self.intermediate[key])
        self.result.sort()
        for item in self.result:
            print "{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}"

mr = MapReduce()

def mapper(record):
    #Start writing the Map code here
    key = record[0]
    value = record[1]
    for friend in value:
        if not mr.intermediate:
            mr.emit_intermediate(1,(key, friend))
        else:
            mr.emit_intermediate(max(mr.intermediate.keys())+1, (key, friend))
            
def reducer(key, list_of_values):
    #Start writing the Reduce code here
    for v in list_of_values:
        if ((v[1],v[0]) in [x for v in mr.intermediate.values() for x in v]) and ((v[1], v[0]) not in mr.result and (v[0], v[1]) not in mr.result):
            if v[1] > v[0]:
                mr.emit((v[0], v[1]))
            else:
                mr.emit((v[1], v[0]))
    mr.result.sort()
    
if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mr.execute(inputData, mapper, reducer)
