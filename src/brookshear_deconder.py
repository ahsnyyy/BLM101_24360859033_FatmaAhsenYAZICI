# Makine Dili ve Brookshear Mimarisi
# 4 haneli HEX kodu alınır.
# Kodu opcode, register ve address olarak ayırır.
# Appendix C tablosuna göre açıklamayı gösterir.

# Kullanıcıdan komut alıyoruz
komut = input("4 haneli HEX kod giriniz (orn: 14A3): ").upper()

# --- HATA KONTROLLERİ ---

# Uzunluk kontrolü
if len(komut) != 4:
    print("Hata: Kod 4 haneli olmalidir.")
    exit()

# HEX karakter kontrolü
hex_karakterler = "0123456789ABCDEF"
for karakter in komut:
    if karakter not in hex_karakterler:
        print("Hata: HEX olmayan karakter girdiniz.")
        exit()

# --- KODU PARÇALAMA ---
opcode = komut[0]        # 1. hane
register = komut[1]      # 2. hane
address = komut[2:]      # 3 ve 4. haneler

# Parçalanmış halini ekranda göster
print("\n--- Kodun Parcalanmis Hali ---")
print("Opcode   :", opcode)
print("Register :", register)
print("Address  :", address)

# --- OPCODE'A GÖRE YORUMLAMA ---
print("\n--- Komutun Aciklamasi ---")

if opcode == "1":
    print(address + " adresindeki bellek hucresinin icerigi " +
          register + " numarali yazmaca yuklenecek (LOAD from Memory).")

elif opcode == "2":
    print(register + " numarali yazmac, " +
          address + " degeri ile yuklenecek (LOAD Immediate).")

elif opcode == "3":
    print(register + " numarali yazmacin icerigi " +
          address + " adresindeki bellek hucresine kaydedilecek (STORE).")

elif opcode == "4":
    print(address[1] + " numarali yazmacin icerigi " +
          register + " numarali yazmaca tasinacak (MOVE).")

elif opcode == "5":
    print(address[0] + " ve " + address[1] +
          " numarali yazmaclar toplanacak, sonuc " +
          register + " numarali yazmaca yazilacak (ADD).")

elif opcode == "6":
    print(address[0] + " ve " + address[1] +
          " numarali yazmaclar kayan noktalı toplanacak, sonuc " +
          register + " yazmacina yazilacak.")

elif opcode == "7":
    print(address[0] + " ve " + address[1] +
          " numarali yazmaclara OR islemi uygulanacak, sonuc " +
          register + " yazmacina yazilacak.")

elif opcode == "8":
    print(address[0] + " ve " + address[1] +
          " numarali yazmaclara AND islemi uygulanacak, sonuc " +
          register + " yazmacina yazilacak.")

elif opcode == "9":
    print(address[0] + " ve " + address[1] +
          " numarali yazmaclara XOR islemi uygulanacak, sonuc " +
          register + " yazmacina yazilacak.")

elif opcode == "A":
    print(register + " numarali yazmac " +
          address + " kadar saga dondurulecek (ROTATE).")

elif opcode == "B":
    print("Eger " + register +
          " numarali yazmac 0 ise, program " +
          address + " adresine atlayacak (JUMP).")

elif opcode == "C":
    print("Program durdurulacak (HALT).")

else:
    print("Bilinmeyen Op-code.")
