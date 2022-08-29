from colorama import Fore
Green = Fore.GREEN
Reset = Fore.RESET

#encrypt
def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char == " ":
            result += " "
        else:
            # encrypt text
            if char.isupper():
                Uchar_cipher = chr((ord(char) - 65 + shift) % 26 + 65)
                result += Uchar_cipher
            else:
                Lchar_cipher = chr((ord(char) - 97 + shift) % 26 + 97)
                result += Lchar_cipher

    print(result)
    print("-" * 100)
    main()

#decrypt
def decrypt(cipher_text, shift):
    result = ""

    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char == " ":
            result += " "
        else:
            if char.isupper():
                #decrypt text
                Uchar_text = chr((ord(char) - 65 - shift) % 26 + 65)
                result += Uchar_text
            else:
                Lchar_text = chr((ord(char) - 97 - shift) % 26 + 97)
                result += Lchar_text
    print(result)
    print("-" * 100)
    main()

def main():
    #banner display
    banner_display = """"
  ****************************************************************************************************** 
  *   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗    *
  *  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗   *
  *  ██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝   *
  *  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗   *
  *  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║   *
  *   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   *
  * Caesar Cipher Encryption                                                                           *
  * Coded By PhoeNix                                                                                   *
  * Github : @PhoneMyatPyaeSone                                                                        *                           *            
  ******************************************************************************************************
    """
    print(f"{Green}{banner_display}{Reset}")
    print("Choose Method \n1. Encrypt \n2. Decrypt\n")
    method = int(input("Enter Method(eg. 1):"))
    if method == 1:
        text = input("Enter the text: ")
        shift = int(input("Shift Number: "))
        encrypt(text, shift)
    elif method == 2:
        cipher_text = input("Enter the Cipher Text: ")
        shift = int(input("Shift Number: "))
        decrypt(cipher_text, shift)
    else:
        print("Something wrong")

main()