import fileinput

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
            d_list = []
            for x in d_o:
                if x in ('a'):
                    d_list.append(a_map)
                elif x in ('b'):
                    d_list.append(b_map)
                else:
                    d_list.append(x)
            d_list = ''.join(d_list)
            heighwey_dragon.append(d_list)
            d_o = d_list
        return(heighwey_dragon[-1])
    
    # def rotation_matrix(self, theta):
        #         A = round(math.cos(theta))
        #         B = round(-math.sin(theta))
        #         C = round(math.sin(theta))
        #         D = round(math.cos(theta))
        # if theta == 'left':
        #     A = 0
        #     B = -1
        #     C = 1
        #     D = 0
        # elif theta == 'right':
        #     A = 0
        #     B = 1
        #     C = -1
        #     D = 0
        # rotation_matrix=[(A,B),(C,D)]
        # return rotation_matrix
    
    def rotate_orientation(self, theta, orientation):
        # rotation_matrix = self.rotation_matrix(theta)
        # new_x = rotation_matrix[0][0]*orientation[0]+rotation_matrix[0][1]*orientation[1]
        # new_y = rotation_matrix[1][0]*orientation[0]+rotation_matrix[1][1]*orientation[1]
        # new_orientation = (new_x, new_y)
        if theta in ('left'):
            if orientation == (0,1):
                new_orientation = (-1,0)
            elif orientation == (-1,0):
                new_orientation = (0,-1)
            elif orientation == (0,-1):
                new_orientation = (1,0)
            elif orientation == (1,0):
                new_orientation = (0,1)
        else:
            if orientation == (0,1):
                new_orientation = (1,0)
            elif orientation == (1,0):
                new_orientation = (0,-1)
            elif orientation == (0,-1):
                new_orientation = (-1,0)
            elif orientation == (-1,0):
                new_orientation = (0,1) 
        return new_orientation
    
    def new_position(self, position, orientation):
        new_position = ((position[0]+orientation[0]), (position[1]+orientation[1]))
        return new_position
                        
    def move_cursor(self, decimal_query_list):
        output = []
        theta_L = 'left'
        theta_R = 'right'
        for pair in decimal_query_list:
            heighwey_dragon = self.make_heighwey_dragon(pair)
            position = (0,0)
            orientation = (0,1)
            steps = pair[1]
            i = 0
            while i < steps:
                for x in heighwey_dragon:
                    if i >= steps:
                        break
                    if x in ('F'):
                        new_position = self.new_position(position, orientation)
                        position = new_position
                        i += 1
                    elif x in ('a'):
                        continue
                    elif x in ('b'):
                        continue
                    elif x in ('L'):
                        new_orientation = self.rotate_orientation(theta_L, orientation)
                        orientation = new_orientation
                    else:
                        new_orientation = self.rotate_orientation(theta_R, orientation)  
                        orientation = new_orientation
            output.append(position)
        return output
              
if fileinput.input():
    HeighweyDragonObject = HeighweyDragon()
    inputs = HeighweyDragonObject.getinput(fileinput.input())
    query_list = HeighweyDragonObject.make_query_list(inputs)
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    moved_cursor = HeighweyDragonObject.move_cursor(decimal_query_list)
    for x in moved_cursor:
        for y in x:
            print(hex(y).replace('0x','').upper())