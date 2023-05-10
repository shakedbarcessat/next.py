import string


class UsernameContainsIllegalCharacter(Exception):
    def __str__(self):
        return "The username contains an illegal character"

class UsernameTooShort (Exception):
    def __str__(self):
        return "The username is too short"

class UsernameTooLong (Exception):
    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter (Exception):
    def __str__(self):
        return "The password is missing a character"

class PasswordTooShort (Exception):
    def __str__(self):
        return "The password is too short"

class PasswordTooLong (Exception):
    def __str__(self):
        return "The password is too long"

class UpperPassword(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Uppercase)"

class LowerPassword(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Lowercase)"

class DigitPassword(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Digit)"

class SpecialPassword(PasswordMissingCharacter):
    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Special)"

def check_input(username, password):
    try:
        for char in username:
            if (char not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                             'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z', \
                             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't',
                             'u', 'v', 'w', 'x', 'y', 'z', \
                             '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                raise UsernameContainsIllegalCharacter
        if len(username)<3:
            raise UsernameTooShort
        elif len(username)>16:
            raise UsernameTooLong
        elif len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong
        elif any(char in password for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])==False:
            raise UpperPassword
        elif any(char in password for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])==False:
            raise LowerPassword
        elif any(char.isdigit() for char in password)==False:
            raise DigitPassword
        elif any(char in password for char in string.punctuation)==False:
            raise SpecialPassword
        else:
            print("OK")
    except UsernameTooShort as e:
        print(UsernameTooShort.__str__(e))
    except UsernameTooLong as e:
        print(UsernameTooLong.__str__(e))
    except UsernameContainsIllegalCharacter as e:
        print(UsernameContainsIllegalCharacter.__str__(e) + ' "' + char + '" at index ' + str(username.index(char)))
    except SpecialPassword as e:
        print(SpecialPassword.__str__(e))
    except LowerPassword as e:
        print(LowerPassword.__str__(e))
    except UpperPassword as e:
        print(UpperPassword.__str__(e))
    except DigitPassword as e:
        print(DigitPassword.__str__(e))
    except PasswordTooShort as e:
        print(PasswordTooShort.__str__(e))
    except PasswordTooLong as e:
        print(PasswordTooLong.__str__(e))

def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")

if __name__ == '__main__':
    main()

