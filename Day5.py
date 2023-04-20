from hashlib import md5
import numpy as np

def Day5_Part1(door_ID: str='uqwqemis') -> str:
    """
    Finds the password for a door of a given ID. The eight-character password for the door is
    generated one character at a time by finding the MD5 hash of the Door ID and an increasing
    integer index (starting with 0). A hash indicates the next character in the password if its
    hexadecimal representation starts with five zeroes. If it does, the sixth character in the hash
    is the next character of the password.

    Parameters
    ----------
    door_ID : str, optional
        ID of the door to be opened.
        The default is 'uqwqemis'.

    Returns
    -------
    password : str
        Password of the door with the given ID.

    """
    # Starting with index of 0, empty password (all _'s) and password index of 0
    i, password, index = 0, ['_']*8, 0

    # While the password is less than 8 characters
    while index < 8:
        # Find MD5 hash of door ID + current index with hashlib library, check if it starts with
        # five zeros
        if (id_hash := md5((door_ID + str(i)).encode('utf-8')).hexdigest()).startswith('00000'):
            # Add sixth character to password
            password[index] = id_hash[5]
            # Increment password index
            index += 1
            # Display password with random characters for undetermined characters
            display_password = ''
            for c in password:
                if c == '_':
                    display_password += hex(np.random.randint(0, 16))[2]
                else:
                    display_password += c
            print('\r' + display_password, end='', flush=True)
            
        # Display password with random characters for undetermined characters for effect
        elif i % 10000 == 0:
            display_password = ''
            for c in password:
                if c == '_':
                    display_password += hex(np.random.randint(0, 16))[2]
                else:
                    display_password += c
            print('\r' + display_password, end='', flush=True)
        # Increment index
        i += 1

    # Join characters of final password
    print('\r' + (password := ''.join(password)), flush=True)
    
    return password

def Day5_Part2(door_ID: str='uqwqemis') -> str:
    """
    Finds the password for a door of a given ID. The eight-character password for the door is
    generated one character at a time by finding the MD5 hash of the Door ID and an increasing
    integer index (starting with 0). A hash indicates the next character in the password if its
    hexadecimal representation starts with five zeroes. If it does, the sixth character represents
    the position (0-7) of this new character in the password, and the seventh character is the
    character to put in that position. Use only the first result for each position, and ignore
    invalid positions (>8).

    Parameters
    ----------
    door_ID : str, optional
        ID of the door to be opened.
        The default is 'uqwqemis'.

    Returns
    -------
    password : str
        Password of the door with the given ID.

    """
    # Starting with index of 0 and empty password (all _'s)
    i, password = 0, ['_']*8

    # While some characters are undetermined
    while '_' in password:
        # Find MD5 hash of door ID + current index with hashlib library, check if it starts with
        # five zeros and the corresponding password index is valid and has not already been found
        if (id_hash := md5((door_ID + str(i)).encode('utf-8')).hexdigest()).startswith('00000') \
            and (index := int(id_hash[5], 16)) < 8 and password[index] == '_':
            # Set corresponding position in password to seventh character
            password[index] = id_hash[6]
            # Display password with random characters for undetermined characters
            display_password = ''
            for c in password:
                if c == '_':
                    display_password += hex(np.random.randint(0, 16))[2]
                else:
                    display_password += c
            print('\r' + display_password, end='', flush=True)
        # Display password with random characters for undetermined characters for effect
        elif i % 10000 == 0:
            display_password = ''
            for c in password:
                if c == '_':
                    display_password += hex(np.random.randint(0, 16))[2]
                else:
                    display_password += c
            print('\r' + display_password, end='', flush=True)
            # Increment index
        i += 1

    # Join characters of final password
    print('\r' + (password := ''.join(password)), flush=True)
    
    return password
