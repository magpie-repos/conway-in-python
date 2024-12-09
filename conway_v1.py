'''Crummy implementation fo Conway's Game of Life in Python.I swear there has to be a more 
elegant way to check the neighboring cells than the if/else abomination I've got here.
Also the way output is handled is pretty ass.
'''

import time
import random


rows = 50
cols = 100
cycles = 80
living_weight = 0.3 #Percent of cells to be spawned as living initially

def create_cel_array():
    cel_array = [] 
    for r in range(0, rows):
        cel_array.append([" "] * cols)
    return cel_array

def randomize_cel_array(cel_array):
    for r in range(0, rows):
        for c in range(0, cols):
            if random.random() < living_weight:
                cel_array[r][c] = "0"
            else:
                cel_array[r][c] = " "
            
    return cel_array

def display_cels(cel_array):
    for r in range(0, rows):
        row_str = ''
        for c in range(0, cols):
            row_str += cel_array[r][c]
        print(row_str)

def process_cels(cel_array):
    new_cel_array = cel_array 
    for r in range(0, rows):
        for c in range(0, cols):
            num_nbrs = 0
            
            if cel_array[r - 1][c - 1] != " ": 
                num_nbrs += 1
            if cel_array[r - 1][c] !=  " ":
                num_nbrs += 1
            if c == cols - 1:
                if cel_array[r - 1][0] != " ":
                    num_nbrs += 1
            else:
                if cel_array[r - 1][c + 1] != " ":
                    num_nbrs += 1
            if cel_array[r][c - 1] != " ":
                num_nbrs += 1
            if c == cols - 1:
                if cel_array[r][0] != " ":
                    num_nbrs += 1
            else:
                if cel_array[r][c + 1] != " ":
                    num_nbrs += 1
            if r == rows - 1:
                if cel_array[0][c - 1] != " ":
                    num_nbrs += 1
                if cel_array[0][c] != " ":
                    num_nbrs += 1
                if c == cols - 1:
                    if cel_array[0][0] != " ":
                        num_nbrs += 1
                else:
                    if cel_array[0][c + 1] != " ":
                        num_nbrs += 1
            else:
                 if cel_array[r + 1][c - 1] != " ":
                     num_nbrs += 1
                 if cel_array[r + 1][c] != " ":
                     num_nbrs += 1
                 if c == cols - 1:
                     if cel_array[r + 1][0] != " ":
                         num_nbrs += 1
                 else:
                     if cel_array[r + 1][c + 1] != " ":
                         num_nbrs += 1
            
            #Total num of neighbors and determine actions on cell
            if 2 < num_nbrs < 4:
                new_cel_array[r][c] = "O"
            else:
                new_cel_array[r][c] = " "
    return new_cel_array

cel_array = create_cel_array()
cel_array = randomize_cel_array(cel_array)

cycle_count = 0
while cycles > cycle_count:
    display_cels(cel_array)
    time.sleep(1/30)
    cel_array = process_cels(cel_array)
    cycle_count += 1













