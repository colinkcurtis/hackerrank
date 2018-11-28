import fileinput
import time
import math
import sys
import memory_profiler
import os
import zlib
import gc

class HeighweyDragon():
    def __init__(self):
        pass
    
    def getinput(self, input):
        #input_list = [line.rstrip() for line in input]
        #import pdb; pdb.set_trace()
        input_list = []
        input_list = [line.rstrip() for line in open(input) if line]
        return input_list
    
    def make_query_list(self, inputs):
        num_queries_in_file = int(inputs[0])
        query_list = [(inputs[i], inputs[i+1]) for i in range(1, 2*num_queries_in_file, 2)]
        return query_list
            
    def decimal_query_list(self, query_list):
        decimal_query_list = [(x[0], int(x[1], base=16)) for x in query_list]
        return decimal_query_list

    def flipped_reversed_string_0(self, string_0_mod):
        flipped_reversed_string_0 = string_0_mod.translate({ord("a"): "b", ord("b"): "a", ord("L"): "R", ord("R"): "L"})
        return flipped_reversed_string_0

    def string_flip(self, d_o):
        string_0_mod = d_o[::-1]
        return string_0_mod
    #
    @profile
    def make_heighwey_dragon_by_sequences(self, pair):
        time1 = time.time()
        d_o = str()
        d_o = 'Fa'.encode('utf-8')
        d_o_compressed = zlib.compress(d_o, 1)
        d_o_list = []
        d_o_list.append(d_o_compressed)
        steps = pair[1]
        sqrt_steps = math.ceil(math.sqrt(steps))
        for i in range(int(sqrt_steps)):
            #previous_string = zlib.decompress(d_o_list[i-1]).decode()
            #flipped_string = self.string_flip(previous_string)
            #flipped_reversed_string_0 = self.flipped_reversed_string_0(flipped_string)
            flipped_reversed_string_0 = self.flipped_reversed_string_0(self.string_flip(zlib.decompress(d_o_list[i-1]).decode()))
            #compressed_new_string = zlib.compress((previous_string+'R'+flipped_reversed_string_0+'R').encode('utf-8'),1)
            compressed_new_string = zlib.compress((zlib.decompress(d_o_list[i-1]).decode()+'R'+flipped_reversed_string_0+'R').encode('utf-8'), 1)
            flipped_reversed_string_0 = None
            d_o_list.append(compressed_new_string)
            compressed_new_string = None
        time2 = time.time()
        heighwey_time = time2-time1
        print('time:', heighwey_time)
        last_string = zlib.decompress(d_o_list[-1]).decode()
        return last_string

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
    gc.collect()
    inputs = HeighweyDragonObject.getinput('test_input.txt')
    query_list = HeighweyDragonObject.make_query_list(inputs)
    decimal_query_list = HeighweyDragonObject.decimal_query_list(query_list)
    moved_cursor = HeighweyDragonObject.move_cursor(decimal_query_list)
    
    for x in moved_cursor:
        for y in x:
            print(hex(y).replace('0x','').upper())