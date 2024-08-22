alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    encrypted_text=""
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26
        encrypted_text += alphabet[new_position]
    print(f"The text after encryption is: {encrypted_text}")
def decryption(encypted_text,shift_key):
    plain_text=""
    for char in encypted_text:
        position=alphabet.index(char)
        new_position=(position-shift_key)%26
        plain_text += alphabet[new_position]
    print(f"The text after decryption is: {plain_text}")    
endCode=False   
while not endCode: 
    userName=input("Type 'encrypt' for encryption and 'decrypt' for decryption:")
    text=input("Type the message:\n")        
    shift=int(input("Enter the shift key:\n"))
    if userName=="encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif userName=="decrypt":
        decryption(encypted_text=text,shift_key=shift)
    goingAgain=input("Type 'yes' if want to run the code again, 'no' if not:")
    if goingAgain =='no':
        endCode=True
    print("Thank You!")        


               