#!/usr/bin/env python

def get_wire_paths(filename: str):
    '''
    Extract the two wire paths from the given file name.
    Returns a list with the two paths.
    '''
    with open(filename, 'r') as f:
        path1 = f.readline().strip('\n').split(',')
        path2 = f.readline().strip('\n').split(',')

    return [path1, path2]

def parse_wire_path(path: list):
    '''
    Gets the visited points from the given wire path.
    '''
    path_arr = [] # list to store every position that the wire goes through
    current_pos = [0, 0]
    for move in path:
        magnitude = int(move[1:])
        for _ in range(magnitude):
            current_pos[0 if move[0] in ('L', 'R') else 1] += -1 if move[0] in ('L', 'D') else 1
            path_arr.append(tuple(current_pos[:]))

    
    return path_arr



path1, path2 = get_wire_paths('day3input.txt')
_path1 = parse_wire_path(path1)
_path2 = parse_wire_path(path2)

intersections = set(_path1) & set(_path2)
print('intersections:', intersections)
part1 = min([abs(x) + abs(y) for (x, y) in intersections])
print('part 1: ', part1)
part2 = 2 + min(sum(wire.index(intersect) for wire in (_path1, _path2)) for intersect in intersections)
print('part 2: ', part2)

