def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    for i in range(len(plaintext)):
        plaintext_char = ord(plaintext[i]) #mengonversi karakter plaintext ke nilai ASCII
        key_char = ord(key[i]) #mengonversi karakter kunci ke nilai ASCII
        encrypted_char = plaintext_char ^ key_char #Melakukan XOR antara nilai ASCII karakter plaintext dan kunci 
        encrypted_text += format(encrypted_char, '08b') #mengonversi hasil XOR ke biner dan menggabungkan dengan string terenkripsi

        # Menunjukkan proses enkripsi dalam output
        print(f"Iterasi {i + 1}:")
        print(f"  - Karakter Plaintext: {plaintext[i]} (ASCII: {plaintext_char})")
        print(f"  - Kunci: {key[i]} (ASCII: {key_char})")
        print(f"  - XOR: {encrypted_char}")
        print(f"  - Byte Terenkripsi: {format(encrypted_char, '08b')}")
        print(f"  - Teks Terenkripsi Sementara: {encrypted_text}\n")

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]

    for i in range(len(encrypted_text)//8):
        encrypted_byte = encrypted_text[i*8:(i+1)*8] #mengambil 8-bit dari string terenkripsi
        encrypted_char = int(encrypted_byte, 2) #mengonversi 8-bit menjadi nilai ASCII
        key_char = ord(key[i]) #mengonversi karakter kunci ke nilai ASCII
        decrypted_char = encrypted_char ^ key_char #melakukan XOR antara niai ASCII karakter terenkripsi dan kunci
        decrypted_text += chr(decrypted_char) #mengonversi hasil XOR menjadi karakter dan menggabungkan dengan string terenkripsi

        # Menunjukkan proses dekripsi dalam output
        print(f"Iterasi {i + 1}:")
        print(f"  - Byte Terenkripsi: {encrypted_byte}")
        print(f"  - Kunci: {key[i]} (ASCII: {key_char})")
        print(f"  - XOR: {decrypted_char}")
        print(f"  - Karakter Terdekripsi: {chr(decrypted_char)}")
        print(f"  - Teks Terdekripsi Sementara: {decrypted_text}\n")

    return decrypted_text

# Input dari pengguna
plaintext = input("Masukkan plaintext: ")
key = input("Masukkan kunci: ")

# Enkripsi
encrypted_text = vigenere_encrypt(plaintext, key)
print(f"\nPlaintext: {plaintext}")
print(f"Kunci: {key}")
print(f"Enkripsi: {encrypted_text}\n")

# Dekripsi
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Dekripsi: {decrypted_text}")

