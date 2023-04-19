def get_input(input_file: str='Inputs/Day1_Inputs.txt') -> list:
    """
    Parse an input file to extract a list of movement instructions.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day1_Inputs.txt'.

    Returns
    -------
    instructions : list(str)
        List of instructions.

    """
    # Parse input file and split instructions into list
    with open(input_file) as f:
        instructions = [line.strip().split(', ') for line in f.readlines()][0]

    return instructions

def Day1_Part1(input_file: str='Inputs/Day1_Inputs.txt') -> int:
    """
    Find the Manhattan distance reached from the starting position after following all the movement
    instructions given in an input file. Instructions are in the form 'R3' where the letter ('R' or
    'L') means you should turn right or left, and the number of the number of spaces you should
    then move.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day1_Inputs.txt'.

    Returns
    -------
    total_distance : int
        Manhattan distance from the starting position of the position reached at the end of the
        instructions.

    """
    # Parse input file and extract instructions
    instructions = get_input(input_file)

    # Begin facing North (0) and at the starting position [0, 0]
    facing, position = 0, [0, 0]

    # Follow every instuction
    for instruction in instructions:
        # Rotate the facing accordingly, with North, East, South and West denoted as 0, 1, 2 and 3
        if instruction[0] == 'L':
            facing = (facing - 1)%4
        else:
            facing = (facing + 1)%4
        # If facing North or East, add to the corresponding coordinate
        if facing < 2:
            position[facing] += int(instruction[1:])
        # Else subtract from the corresponding coordinate
        else:
            position[facing - 2] -= int(instruction[1:])

    # Finally, calculate absolute sum of movements in each axis from starting position
    total_distance = sum(abs(p) for p in position)

    return total_distance

def Day1_Part2(input_file: str='Inputs/Day1_Inputs.txt') -> int:
    """
    Find the Manhattan distance from the starting position of the first location visited twice,
    after following all the movement instructions given in an input file. Instructions are in the
    form 'R3' where the letter ('R' or 'L') means you should turn right or left, and the number of
    the number of spaces you should then move.

    Parameters
    ----------
    input_file : str, optional
        Input file containing the instructions.
        The default is 'Inputs/Day1_Inputs.txt'.

    Returns
    -------
    total_distance : int
        Manhattan distance from the starting position of the first location visited twice.

    """
    # Parse input file and extract instructions
    instructions = get_input(input_file)
        
    # Begin facing North (0) and at the starting position [0, 0]
    facing, position = 0, [0, 0]

    # Create set of all positions visited
    all_positions = set()

    # Follow every instruction
    for instruction in instructions:
        # Rotate the facing accordingly, with North, East, South and West denoted as 0, 1, 2 and 3
        if instruction[0] == 'L':
            facing = (facing - 1)%4
        else:
            facing = (facing + 1)%4
        # Perform movements one step at a time in order to record every coordinate visited
        for i in range(int(instruction[1:])):
            # If facing North or East, add 1 to the corresponding coordinate
            if facing < 2:
                position[facing] += 1
                # Else subtract 1 from the corresponding coordinate
            else:
                position[facing - 2] -= 1
            # If this position is already in the set of all positions, it has been visited before
            if (position_tuple := tuple(position)) in all_positions:
                # Return absolute sum of movements in each axis from starting position
                total_distance = sum(abs(p) for p in position)
                return total_distance
            # Else add coordinates to the set
            else:
                all_positions.add(position_tuple)
