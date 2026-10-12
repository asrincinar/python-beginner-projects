sifre = "1987"
tahmin = ""
deneme = 0
while tahmin != sifre and deneme < 3:
  tahmin = input("sifreyi dene:     ")
  if tahmin != sifre:
    deneme = deneme + 1
    if deneme == 1:
      print("yanlıs 1900 lerden dene")
    elif deneme == 2:
      print("80 lerde sonu")
    else:
      print("baska ip ucu hakkın kalmadı")
if tahmin == sifre:
  print ("KAPI ACILDI")
else:
  print("3 hakkinda bitti")
