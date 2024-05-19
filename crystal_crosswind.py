import sys
import numpy as np
from concurrent.futures import ThreadPoolExecutor
from io import StringIO

def parse_input(input_data=None):
    if input_data is not None:
        input_stream = StringIO(input_data)
    else:
        input_stream = sys.stdin

    input = input_stream.read().strip().split()
    idx = 0
    
    d_x = int(input[idx])
    d_y = int(input[idx+1])
    k = int(input[idx+2])
    idx += 3
    
    winds = []
    for _ in range(k):
        w_x = int(input[idx])
        w_y = int(input[idx+1])
        b = int(input[idx+2])
        boundaries = [(int(input[idx+3 + 2*i]), int(input[idx+4 + 2*i])) for i in range(b)]
        winds.append((w_x, w_y, boundaries))
        idx += 3 + 2 * b
        
    return d_x, d_y, winds

def process_wind(wind, d_x, d_y):
    w_x, w_y, boundaries = wind
    must_have = np.zeros((d_y, d_x), dtype=bool)
    possible = np.ones((d_y, d_x), dtype=bool)
    
    for x, y in boundaries:
        must_have[y-1][x-1] = True
        
        cur_x, cur_y = x, y
        while 1 <= cur_x <= d_x and 1 <= cur_y <= d_y:
            possible[cur_y-1][cur_x-1] = False
            cur_x -= w_x
            cur_y -= w_y
            
    return must_have, possible

def main(input_data=None):
    d_x, d_y, winds = parse_input(input_data)
    
    must_have_grid = np.zeros((d_y, d_x), dtype=bool)
    possible_grid = np.ones((d_y, d_x), dtype=bool)
    
    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda wind: process_wind(wind, d_x, d_y), winds)
        
        for must_have, possible in results:
            must_have_grid |= must_have
            possible_grid &= possible
            
    minimal_structure = must_have_grid
    maximal_structure = must_have_grid | possible_grid
    
    for structure in [minimal_structure, maximal_structure]:
        for row in structure:
            print(''.join('#' if cell else '.' for cell in row))
        print()

if __name__ == "__main__":
    main()
