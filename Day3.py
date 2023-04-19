def get_input(input_file: str='Inputs/Day3_Inputs.txt', vertical: bool=False) -> list:
    """
    Parses an input file to extract the side length of a series of triangles. By default each row
    is taken as a different triangle, but if the vertical parameter is set to True, then triangles
    are instead specified in groups of three vertically, i.e. each set of three numbers in a column
    specifies a triangle and rows are unrelated.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the triangle parameters.
        The default is 'Inputs/Day3_Inputs.txt'.
    vertical : bool, optional
        Whether the triangles side lengths are grouped vertically or not.
        The default is False.

    Returns
    -------
    triangles : list(tuple(int))
        List of the side length of triangles in tuples, sorted in ascending order.

    """
    # Parse input file and split instructions into list
    with open(input_file) as f:
        # If side lengths are vertically grouped
        if vertical:
            triangles = []
            # Parse through sets of 3 rows
            for i in range(len(lines := [[int(i) for i in line.strip().split()] \
                                         for line in f.readlines()])//3):
                # Extract each column from the current 3 rows as a new triangle, sort the values
                for j in range(3):
                    triangles.append(tuple(sorted(lines[3*i+k][j] for k in range(3))))

        # If the side lengths are horizontally grouped
        else:
            # Extract and sort the values on each row as a new triangle
            triangles = [tuple(sorted(int(i) for i in line.strip().split())) \
                         for line in f.readlines()]

    return triangles

def Day3_Part1(input_file: str='Inputs/Day3_Inputs.txt') -> int:
    """
    Determines how many of a set of triangles, whose side lengths are given in an input file
    arranged such that the side lengths of each triangle are grouped horizontally by row, are valid
    triangles, i.e. the sum of any two sides must be larger than the remaining side.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the triangle side lengths.
        The default is 'Inputs/Day3_Inputs.txt'.

    Returns
    -------
    num_valid : int
        The number of valid triangles in the set.

    """
    # Extract triangle side lengths from input file
    triangles = get_input(input_file)

    # Find how many have the sum of the smaller two sides as larger than the length of the longest
    # side - these are valid triangles
    num_valid = sum(t[0] + t[1] > t[2] for t in triangles)

    return num_valid

def Day3_Part2(input_file: str='Inputs/Day3_Inputs.txt') -> int:
    """
    Determines how many of a set of triangles, whose side lengths are given in an input file
    arranged such that the side lengths of each triangle are in groups of three vertically, i.e.
    each set of three numbers in a column specifies a triangle and rows are unrelated, are valid
    triangles, i.e. the sum of any two sides must be larger than the remaining side.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the triangle side lengths.
        The default is 'Inputs/Day3_Inputs.txt'.

    Returns
    -------
    num_valid : int
        The number of valid triangles in the set.

    """
    # Extract triangle side lengths from input file, with triangle side lengths grouped vertically
    triangles = get_input(input_file, True)

    # Find how many have the sum of the smaller two sides as larger than the length of the longest
    # side - these are valid triangles
    num_valid = sum(t[0] + t[1] > t[2] for t in triangles)

    return num_valid
