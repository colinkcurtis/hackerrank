import fileinput
import asyncio

class HeighweyDragon():
    def __init__(self):
        pass
    
    def getinput(self, input):
        input_list = [line.rstrip() for line in input]
        return input_list
    
    def make_query_list(self, inputs):
        num_queries_in_file = int(inputs[0])
        query_list = [(inputs[i], inputs[i+1]) for i in range(1, 2*num_queries_in_file, 2)]
        return query_list
            
    def decimal_query_list(self, query_list):
        decimal_query_list = [(x[0], int(x[1], base=16)) for x in query_list]
        return decimal_query_list

    def make_heighwey_dragon(self, pair):
        a_map = 'aRbFR'
        b_map = 'LFaLb'
        d_o = 'Fa'
        n = pair[0]
        heighwey_dragon = []
        heighwey_dragon.append(d_o)
        for i in range(int(n)):
            d_i = d_o.replace('a',a_map).replace('b', b_map)
            heighwey_dragon.append(d_i)
            d_o = d_i
        return(heighwey_dragon)
    
if fileinput.input():
    HeighweyDragonObject = HeighweyDragon()
    
    inputs = HeighweyDragonObject.getinput(fileinput.input())
    
    query_list = HeighweyDragonObject.make_query_list(inputs)
    
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    
    make_heighwey_dragon = HeighweyDragonObject.make_heighwey_dragon(decimal_query_list[0])
    
    print(make_heighwey_dragon)