gizlisayi = 27
tahmin = ""
deneme = 0
while gizlisayi != tahmin and deneme < 3:
  tahmin = int(input("Tahmininizi girin:   "))
  if tahmin != gizlisayi:
    deneme = deneme + 1
    if deneme == 1 and tahmin < gizlisayi:
      print("2 deneme hakkınız kaldı girdiginiz sayıyı buyutunuz.")
    elif deneme == 1 and tahmin > gizlisayi:
      print ("2 deneme hakkınız kaldı girdiginiz sayıyı kucultunuz.")
    elif deneme == 2 and tahmin < gizlisayi:
      print("1 deneme hakkınız kaldı girdiginiz sayıyı buyutunuz")
    elif deneme == 2 and tahmin > gizlisayi:
      print ("1 deneme hakkınız kaldı girdiginiz sayıyı kucultunuz.")
    elif deneme == 3 and tahmin < gizlisayi:
      print ("deneme hakkınız bitti sayı tahmininizden daha büyük")
    elif deneme == 3 and tahmin > gizlisayi:
      print("deneme hakkınız bitti sayı tahmininizden daha kucuk")
if tahmin == gizlisayi:
  print("DOGRU KAZANDIN")
else: 
  print("Kaybettin sayı", gizlisayi, "'idi'")
