import typing

class Room(typing.NamedTuple):
    """
    Class describing a room with an encrypted name, sector ID and checksum.
    """
    encrypted_name: str
    sector_ID: int
    checksum: str

def get_input(input_file: str='Inputs/Day4_Inputs.txt') -> list:
    """
    Parse an input file to extract the properties of a set of rooms. Each room consists of an
    encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a
    checksum in square brackets.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the room properties.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    rooms : list(Room)
        Extracted list of rooms formatted as Room objects.

    """
    rooms = []
    # Parse input file
    with open(input_file) as f:
        for line in f.readlines():
            # Split lines by dashes
            line = line.strip().split('-')
            # Seperate and format room properties
            rooms.append(Room('-'.join(line[:-1]),
                              int(line[-1].split('[')[0]),
                              line[-1].split('[')[1][:-1]))

    return rooms

def room_is_real(room):
    """
    Determines whether or not a room is real by checking if the checksum of the room consists of
    the five most common letters in the encrypted name of the room, in order, with ties broken by
    alphabetization.

    Parameters
    ----------
    room : Room
        Properties of the room to test, formatted as a Room object.

    Returns
    -------
    room_is_real : bool
        Whether or not the room is real.

    """
    # Find the counts of each letter in the encrypted room name
    letter_counts = {l: room.encrypted_name.count(l) for l in room.encrypted_name if l != '-'}

    # Find all the letters corresponding to each count value found, sorted alphabetically
    letters_per_count = {count: sorted(l for l, c in letter_counts.items() if c == count) \
                         for count in letter_counts.values()}

    # Sort each found count number in descending order
    descending_counts = sorted(letters_per_count.keys())[::-1]

    # Starting with blank correct checksum
    correct_checksum = ''
    # While the correct checksum is shorter than 5 characters
    while len(correct_checksum) < 5:
        # Find the letters corresponding to the next highest occurance in the encrypted name
        curr_letters = letters_per_count[descending_counts.pop(0)]
        # Add letters in alphabetical order to the end of the correct checksum up to a maximum
        # length of 5
        correct_checksum += ''.join(curr_letters[:5 - len(correct_checksum)])

    # Return the result of comparing the correct checksum to the given checksum for the room
    return room.checksum == correct_checksum

def Day4_Part1(input_file: str='Inputs/Day4_Inputs.txt') -> int:
    """
    Finds the sum of the sector IDs of the real rooms out a set of rooms given in an input file.
    Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a
    dash, a sector ID, and a checksum in square brackets.A room is real if the checksum of the room
    consists of the five most common letters in the encrypted name of the room, in order, with ties
    broken by alphabetization.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the room properties.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    real_room_ID_sum : int
        The sum of the sector IDs of all real rooms from the list.

    """
    # Parse input file and extract room properties
    rooms = get_input(input_file)

    # Sum up sector IDs of rooms passing room_is_real requirement
    real_room_ID_sum = sum(room.sector_ID for room in rooms if room_is_real(room))
    
    return real_room_ID_sum

def decrypt_name(room):
    """
    Apply a decryption procedure based on a Caesar cipher to the encrypted name of a room. To 
    decrypt a room name, each letter is rotated forward through the alphabet a number of times
    equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become
    spaces.

    Parameters
    ----------
    room : Room
        The room whose name should be decrypted.

    Returns
    -------
    decrypted_name : str
        The decrypted name.

    """
    # Starting with blank name
    decrypted_name = ''
    # For each character in the encrypted name of the room
    for char in room.encrypted_name:
        # Replace dashes with spaces
        if char == '-':
            decrypted_name += ' '
        # Rotate all other letters around by the sector ID, wrapping from 'z' back to 'a'
        else:
            # Use ord() to convert letter to corresponding integer, transform with -97 so that 'a'
            # goes to zero, then add sector ID and mod 26 to wrap around, adding back 97 and
            # converting back to correpsonding decrypted letter with chr()
            decrypted_name += chr((ord(char)-97+room.sector_ID)%26 + 97)

    return decrypted_name

def Day4_Part2(input_file: str='Inputs/Day4_Inputs.txt') -> int:
    """
    Finds the sector ID of the room in an information kiosk where the North Pole objects are stored,
    where room properties are given in an input file, but room names are encrypted. Room names are
    decrypted using a Caesar cipher, where the key is the room's sector ID, so each letter is
    rotated forward through the alphabet a number of times equal to the room's sector ID. A becomes
    B, B becomes C, Z becomes A, and so on. Dashes become spaces.

    Parameters
    ----------
    input_file : str, optional
        Input file giving the room properties.
        The default is 'Inputs/Day4_Inputs.txt'.

    Returns
    -------
    northpole_object_storage_ID : int
        Sector ID of the room for North Pole object storage.

    """
    # Parse input file and extract room properties
    rooms = get_input(input_file)

    # Decrypt each room's name and map to sector ID in dictionary
    decrypted_name_IDs = {decrypt_name(room): room.sector_ID for room in rooms}

    # Find the sector ID of the North Pole object storage room designated 'northpole object storage'
    northpole_object_storage_ID = decrypted_name_IDs['northpole object storage']
    
    return northpole_object_storage_ID
