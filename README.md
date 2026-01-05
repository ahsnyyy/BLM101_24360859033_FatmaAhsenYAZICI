# BLM101_24360859033_FatmaAhsenYAZICI
Bilgisayar Mühendisliği Giriş Dönem Projesi- Makine Dili ve Brookshear Mimarisi
Öğrenci Ad/Soyad: Fatma Ahsen YAZICI
Öğrenci No: 24360859033
Proje Konusu: Makine Dili ve Brookshear Mimarisi
YouTube Video Linki: https://youtu.be/5LgmGStcGFg

---

# Brookshear Machine Language Decoder

## Proje Açıklaması
Bu proje, Brookshear mimarisine ait 4 haneli hexadecimal (HEX) makine dili
komutlarını analiz eden bir Python programıdır. Program, girilen komutu
opcode, register ve address olarak ayırarak komutun ne işe yaradığını
kullanıcıya açıklamalı şekilde göstermektedir.

## Programın Çalışma Şekli
Program çalıştırıldığında kullanıcıdan 4 haneli bir HEX kod girişi istenir.
Girilen kodun öncelikle uzunluğu kontrol edilir ve yalnızca hexadecimal
karakterler içerip içermediği doğrulanır. Geçerli bir kod girildiğinde,
komut üç farklı parçaya ayrılır:

- İlk hane opcode bilgisini temsil eder.
- İkinci hane register bilgisini temsil eder.
- Üçüncü ve dördüncü haneler address bilgisini temsil eder.

Bu parçalama işleminin ardından opcode değerine göre Appendix C tablosuna
uygun şekilde komutun yaptığı işlem ekrana yazdırılır.

## Programın Genel Yapısı
Bu projede Python programlama dili kullanılmıştır. Programda herhangi bir
harici kütüphane kullanılmamış olup yalnızca Python’un temel yapıları
kullanılmıştır.

## Algoritma Mantığı
1. Kullanıcıdan 4 haneli HEX kod alınır.
2. Kodun uzunluğu ve HEX karakter uygunluğu kontrol edilir.
3. Kod opcode, register ve address alanlarına ayrılır.
4. Opcode değerine göre ilgili komutun açıklaması belirlenir.
5. Sonuç kullanıcıya ekranda gösterilir.
6. Geçersiz opcode girilmesi durumunda kullanıcı bilgilendirilir.


