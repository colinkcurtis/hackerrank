import fileinput
import asyncio
import math

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
        return(heighwey_dragon[-1])
    
    def rotation_matrix(self, theta):
        A = round(math.cos(theta))
        B = round(-math.sin(theta))
        C = round(math.sin(theta))
        D = round(math.cos(theta))
        rotation_matrix=[(A,B),(C,D)]
        return rotation_matrix
    
    def rotate_orientation(self, theta, orientation):
        rotation_matrix = self.rotation_matrix(theta)
        new_x = rotation_matrix[0][0]*orientation[0]+rotation_matrix[0][1]*orientation[1]
        new_y = rotation_matrix[1][0]*orientation[0]+rotation_matrix[1][1]*orientation[1]
        new_orientation = (new_x, new_y)
        return new_orientation
    
    def new_position(self, position, orientation):
        new_position = ((position[0]+orientation[0]), (position[1]+orientation[1]))
        return new_position
                        
    def move_cursor(self, decimal_query_list):
        output = []
        for pair in decimal_query_list:
            heighwey_dragon = self.make_heighwey_dragon(pair[0])
            theta_L = math.pi/2
            theta_R = -math.pi/2
            position = (0,0)
            orientation = (0,1)
            rotation_matrix = ()
            steps = pair[1]
            for i in range(steps):
                for char in heighwey_dragon:
                    if char == 'a':
                        continue
                    elif char == 'b':
                        continue
                    elif char == 'L':
                        orientation = self.rotate_orientation(theta_L, orientation)
                        
                    elif char == 'R':
                        orientation = self.rotate_orientation(theta_R, orientation)
                        
                    else:
                        position = self.new_position(position, orientation)
                        break
            output.append(position)
        return output
              
if fileinput.input():
    
    HeighweyDragonObject = HeighweyDragon()
    
    inputs = HeighweyDragonObject.getinput(fileinput.input())
    
    query_list = HeighweyDragonObject.make_query_list(inputs)
    
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    
    moved_cursor = HeighweyDragonObject.move_cursor(decimal_query_list)
    
    print(moved_cursor)