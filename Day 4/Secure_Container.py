PUZZLE_INPUT = "264360-746325" # its a range of digits

def check_decrease(password: str) -> bool:
    if ''.join(sorted(password)) == password:
        return True
    return False

def check_adjacents_digits(password: str) -> bool:
    if len(set(password)) != len(password):
        return True
    return False

def check_adjacents_digits_not_part_of_larger_group(password: str) -> bool:
    pwd_length = len(password)
    pwd_set_length = len(set(password))

    if pwd_length == pwd_set_length:
        return False

    elif pwd_length - pwd_set_length == 1:
        return True
    
    elif pwd_length - pwd_set_length > 1:
        char = password[0]
        count = 1
        count_occurence = []

        for i in range(1, pwd_length):
            
            if password[i] == char:
                count += 1
                if i == pwd_length-1:
                    count_occurence.append(count)
            else:
                count_occurence.append(count)
                count = 1
                char = password[i]

        if 2 in count_occurence:
            return True

    return False

def is_valid(password: str) -> bool:
    # The digits never decrease
    if not check_decrease(password):
        return False
    # Two adjacents digits
    # elif not check_adjacents_digits_not_part_of_larger_group(password):
    elif not check_adjacents_digits(password):
        return False

    return True

if __name__ == "__main__":

    valid_password = 0
    for digit in range(264360, 746325 + 1, 1):
        password = str(digit)

        if is_valid(password):
            valid_password += 1
            
    print(valid_password)