import fileinput

class HeighweyDragon():
    def __init__(self):
        pass
    
    def getinput(self, input):
        input_list = []
        for line in input:
            input_list.append(line.rstrip())
        return input_list
    
    def make_query_list(self, inputs):
        num_queries_in_file = int(inputs[0])
        query_list = [(inputs[i], inputs[i+1]) for i in range(1, 2*num_queries_in_file, 2)]
        return query_list
            
    def decimal_query_list(self, query_list):
        decimal_query_list = [(x[0], int(x[1], base=16)) for x in query_list]
        return decimal_query_list
        
if fileinput.input():
    HeighweyDragonObject = HeighweyDragon()
    inputs = HeighweyDragonObject.getinput(fileinput.input())
    query_list = HeighweyDragonObject.make_query_list(inputs)
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    print(decimal_query_list)