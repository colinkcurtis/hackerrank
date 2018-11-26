import fileinput
import time
import math

class HeighweyDragon():
    def __init__(self):
        pass
    
    def getinput(self, input):
        #input_list = [line.rstrip() for line in input]
        input_list = [line.rstrip() for line in open(input)]
        #print(input_list)
        return input_list
    
    def make_query_list(self, inputs):
        num_queries_in_file = int(inputs[0])
        query_list = [(inputs[i], inputs[i+1]) for i in range(1, 2*num_queries_in_file, 2)]
        return query_list
            
    def decimal_query_list(self, query_list):
        decimal_query_list = [(x[0], int(x[1], base=16)) for x in query_list]
        return decimal_query_list

    # def make_heighwey_dragon(self, pair):
    #     h_start = time.time()
    #     a_map = 'aRbFR'
    #     b_map = 'LFaLb'
    #     d_o = 'Fa'
    #     n = pair[0]
    #     heighwey_dragon = []
    #     heighwey_dragon.append(d_o)
    #     for i in range(int(n)):
    #         d_list = []
    #         seq_list = []
    #         for index, x in enumerate(d_o):
    #             if x in ('a'):
    #                 d_list.append(a_map)
    #             elif x in ('b'):
    #                 d_list.append(b_map)
    #             else:
    #                 d_list.append(x)
    #                 if index < 200:
    #                     if x in ('L'):
    #                         seq_list.append(index)
    #         d_list = ''.join(d_list)
    #         heighwey_dragon.append(d_list)
    #         d_o = d_list
    #         #if i == 3:
    #             #print(heighwey_dragon)
    #     h_end = time.time()
    #     #print('old method time:', h_end-h_start)
    #     return(heighwey_dragon[-1], seq_list)
    
    def make_heighwey_dragon_by_sequences(self, pair):
        #STILL THE SLOWEST PART
        h_start = time.time()
        d_o = 'Fa'
        n = pair[0]
        steps = pair[1]
        needed_steps = math.ceil(math.sqrt(steps))
        print(steps, needed_steps, n)
        for i in range(int(needed_steps)):
            string_0_mod = d_o[::-1]
            flipped_reversed_string_0 = string_0_mod.translate({ord("a"): "b", ord("b"): "a", ord("L"): "R", ord("R"): "L"})
            d_n = d_o+'R'+flipped_reversed_string_0+'R'
            d_o = d_n
        h_end = time.time()
        print('new method time:', h_end-h_start)
        return d_n

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
        theta_L = math.pi/2
        theta_R = -math.pi/2
        j=1
        for pair in decimal_query_list:
            j+=1
            heighwey_dragon_seq = self.make_heighwey_dragon_by_sequences(pair)
            position = (0,0)
            orientation = (0,1)
            steps = pair[1]
            i = 0
            while i < steps:
                for x in heighwey_dragon_seq:
                    if i >= steps:
                        break
                    if x in ('F'):
                        position = self.new_position(position, orientation)
                        i += 1
                    elif x in ('a'):
                        continue
                    elif x in ('b'):
                        continue
                    elif x in ('L'):
                        orientation = self.rotate_orientation(theta_L, orientation)
                    else:
                        orientation = self.rotate_orientation(theta_R, orientation)  
            output.append(position)
            end = time.time()
        return output
              
# if fileinput.input():
#     HeighweyDragonObject = HeighweyDragon()
#     inputs = HeighweyDragonObject.getinput(fileinput.input())
#     query_list = HeighweyDragonObject.make_query_list(inputs)
#     decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
#     moved_cursor = HeighweyDragonObject.move_cursor(decimal_query_list)
#     for x in moved_cursor:
#         for y in x:
#             print(hex(y).replace('0x','').upper())

if __name__ == '__main__':
    HeighweyDragonObject = HeighweyDragon()
    inputs = HeighweyDragonObject.getinput('test_input.txt')
    query_list = HeighweyDragonObject.make_query_list(inputs)
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    moved_cursor = HeighweyDragonObject.move_cursor(decimal_query_list)
    
    for x in moved_cursor:
        for y in x:
            print(hex(y).replace('0x','').upper())