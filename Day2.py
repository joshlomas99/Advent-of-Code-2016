def get_input(input_file: str='Inputs/Day2_Inputs.txt') -> list:
    """
    Parses an input file to extract a series of lines of instructions.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day2_Inputs.txt'.

    Returns
    -------
    instructions : list
        Extracted list of instructions.

    """
    # Parse input file and split instructions into list
    with open(input_file) as f:
        instructions = [line.strip() for line in f.readlines()]

    return instructions

# Set up dictionary for key coordinates on the keypad
keypad = {(0, 0): '1',
          (0, 1): '2',
          (0, 2): '3',
          (1, 0): '4',
          (1, 1): '5',
          (1, 2): '6',
          (2, 0): '7',
          (2, 1): '8',
          (2, 2): '9'}

import operator

def add_tuples(a, b):
    """
    Adds two tuples together elementwise using map.

    Parameters
    ----------
    a : tuple(int)
        First tuple.
    b : tuple(int)
        Second tuple.

    Returns
    -------
    out : tuple(int)
        Elementwise addition of the input tuples.

    """
    return tuple(map(operator.add, a, b))

# Set up lambda functions for movement by one space in any direction
# forcing the coordinates to stay within the bounds of the keypad
move_up = lambda a : add_tuples(a, (-1, 0)) if a[0] > 0 else a
move_down = lambda a : add_tuples(a, (1, 0)) if a[0] < 2 else a
move_left = lambda a : add_tuples(a, (0, -1)) if a[1] > 0 else a
move_right = lambda a : add_tuples(a, (0, 1)) if a[1] < 2 else a

# Dictionary mapping instruction to corresponding lambda function
moves = {'U': move_up,
         'D': move_down,
         'L': move_left,
         'R': move_right}

def Day2_Part1(input_file: str='Inputs/Day2_Inputs.txt') -> str:
    """
    Find the code to unlock a bathroom, by following a set of instructions to move around a keypad
    of the form:

    1 2 3
    4 5 6
    7 8 9

    Each line of instructions gives the movements on the keypad required to locate a corresponding
    value of the correct code, starting initially at the number 5 for the first line, and then 
    starting at the value of the previous line for the next line. Movements which would take you
    out of the bounds of the keypad do not occur.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the movement instructions on the keypad.
        The default is 'Inputs/Day2_Inputs.txt'.

    Returns
    -------
    code : str
        The code to unlock the bathroom.

    """
    # Parse input file and extract each line of instructions
    instructions = get_input(input_file)

    # Starting at the number 5 with a blank code
    coords, code = (1, 1), ''
    # For each line of instructions
    for instruction in instructions:
        # For each character in the line
        for step in instruction:
            # Perform a movement according to the instruction character
            coords = moves[step](coords)
        # At the end of each line, add the current key to the end of the code
        code += keypad[coords]
    
    return code

# Set up dictionary for key coordinates on the new keypad
new_keypad = {(-2, 0): '1',
              (-1, -1): '2',
              (-1, 0): '3',
              (-1, 1): '4',
              (0, -2): '5',
              (0, -1): '6',
              (0, 0): '7',
              (0, 1): '8',
              (0, 2): '9',
              (1, -1): 'A',
              (1, 0): 'B',
              (1, 1): 'C',
              (2, 0): 'D'}

# Set up lambda functions for movement by one space in any direction
# forcing the coordinates to stay within the bounds of the new keypad
new_move_up = lambda a : add_tuples(a, (-1, 0)) \
                if sum(abs(i) for i in add_tuples(a, (-1, 0))) < 3 else a
new_move_down = lambda a : add_tuples(a, (1, 0)) \
                if sum(abs(i) for i in add_tuples(a, (1, 0))) < 3 else a
new_move_left = lambda a : add_tuples(a, (0, -1)) \
                if sum(abs(i) for i in add_tuples(a, (0, -1))) < 3 else a
new_move_right = lambda a : add_tuples(a, (0, 1)) \
                if sum(abs(i) for i in add_tuples(a, (0, 1))) < 3 else a

# Dictionary mapping instruction to corresponding lambda function
new_moves = {'U': new_move_up,
             'D': new_move_down,
             'L': new_move_left,
             'R': new_move_right}

def Day2_Part2(input_file: str='Inputs/Day2_Inputs.txt') -> str:
    """
    Find the code to unlock a bathroom, by following a set of instructions to move around a keypad
    of the form:

        1
      2 3 4
    5 6 7 8 9
      A B C
        D

    Each line of instructions gives the movements on the keypad required to locate a corresponding
    value of the correct code, starting initially at the number 5 for the first line, and then 
    starting at the value of the previous line for the next line. Movements which would take you
    out of the bounds of the keypad do not occur.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the movement instructions on the keypad.
        The default is 'Inputs/Day2_Inputs.txt'.

    Returns
    -------
    code : str
        The code to unlock the bathroom.

    """
    # Parse input file and extract each line of instructions
    instructions = get_input(input_file)

    # Starting at the number 5 with a blank code
    coords, code = (0, -2), ''
    # For each line of instructions
    for instruction in instructions:
        # For each character in the line
        for step in instruction:
            # Perform a movement according to the instruction character
            coords = new_moves[step](coords)
        # At the end of each line, add the current key to the end of the code
        code += new_keypad[coords]
    
    return code
