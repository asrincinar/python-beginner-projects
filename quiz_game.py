cevap1 = "print"
cevap2 = "15"
cevap3 = "!="
cevap4 = "while"
cevap5 = "int"
puan = 0
print ("Python bilgi yarısması:")
print ("1. soru Python'da ekrana yazı yazdıran komut nedir?")
cevap = input("cevabiniz:  ").lower()
if cevap == cevap1:
  puan = puan + 1
  print("Puanınız:",puan,)
  print("Doğru +1 puan kazandınız")
else:
  print("Puanınız:",puan,)
  print("soruyu yanlıs bildiniz puan kazanamadınız")
print("2. soru 5 * 3 kaç eder?")
cevap = input("cevabınız:  ").lower()
if cevap == cevap2:
  puan = puan + 1
  print("Puanınız:",puan,)
  print("Doğru +1 puan kazandınız")
else:
  print("Puanınız:",puan,)
  print("soruyu yanlıs bildiniz puan kazanamadınız")
print("3. soru Python'da eşit değil anlamına gelen operatör nedir?")
cevap = input("cevabınız:  ").lower()
if cevap == cevap3:
  puan = puan + 1
  print("Puanınız:",puan,)
  print("Doğru +1 puan kazandınız")
else:
  print("Puanınız:",puan,)
  print("soruyu yanlıs bildiniz puan kazanamadınız")
print("4. soru Koşul doğru kaldığı sürece tekrarlanan döngü hangisidir?")
cevap = input("cevabınız:  ").lower()
if cevap == cevap4:
  puan = puan + 1
  print("Puanınız:",puan,)
  print("Doğru +1 puan kazandınız")
else:
  print("Puanınız:",puan,)
  print("soruyu yanlıs bildiniz puan kazanamadınız")
print("5. soru Kullanıcı girdisini tam sayıya çevirmek için ne kullanılır?")
cevap = input("cevabınız:  ").lower()
if cevap == cevap5:
  puan = puan + 1
  print("Puanınız:",puan,)
  print("Doğru +1 puan kazandınız")
else:
  print("Puanınız:",puan,)
  print("Soruyu yanlıs bildiniz puan kazanamadınız")

print("Yarisma bitti!")
print("Puanınız:",puan,"/5")
