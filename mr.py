import sys
from collections import OrderedDict

class MapReduce:
    def __init__(self):
        # initialize dictionary for intermediate values from Map task
        self.intermediate = OrderedDict()
        # initialize list for results of Reduce task
        self.result = []

    def emitIntermediate(self, key, value):
        # if key not already in dictionary, set value to empty list
        self.intermediate.setdefault(key, [])
        # add value to list associated with key
        self.intermediate[key].append(value)

    def emit(self, value):
        # append value to list of results
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        # read each line from input file; call Map function on each record
        for record in data:
            mapper(record)

        # for each key:valuelist in intermediate dictionary, call Reduce task
        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        # print each result in result list
        for item in self.result:
            person = item[0]
            person = person[1:]
            line = "{\"Person\":\""+person+"\",\"Number of friends\":\"" + str(item[1]) + "\"}" + '\n'
            print line
            finalresults = open("results1.txt","a")
            finalresults.write(line)

mapReducer = MapReduce()

def mapper(record):
    # key: PersonA
    # value: PersonB
    a=record.split()
    mapReducer.emitIntermediate(a[0],a[1])
    mapReducer.emitIntermediate(a[1],a[0])

def reducer(key, list_of_values):
    # key: document identifier
    # value: list of friends
    mapReducer.emit((key,len(list_of_values)))
    
if __name__ == '__main__':
    inputData = []
    f = file('af.txt', 'r')
    if f:
        inf = open('af.txt', 'r')
    else:
        inf = sys.stdin
    for line in inf:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)
    f.close()