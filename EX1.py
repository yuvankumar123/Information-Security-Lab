def encrypt():
    text = input("\t\tInput String: ")
    encrypted_text = "".join(chr(ord(char) + 3) for char in text)
    print("\n\t\tEncrypted String:", encrypted_text)

def decrypt():
    text = input("\t\tInput String: ")
    decrypted_text = "".join(chr(ord(char) - 3) for char in text)
    print("\n\t\tDecrypted String:", decrypted_text)

def main():
    print("\t\tConfidentiality\n")
    while True:
        print("\t\tChoose operation\n\t\t1. Encryption\n\t\t2. Decryption\n\t\t3. Exit\n")
        choice = input("\t\t")
        
        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '3':
            break
        else:
            print("\t\tInvalid choice!")
        
        cont = input("\n\t\tDo you want to continue (Y/N): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
