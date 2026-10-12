try:
  sayi1 = int(input("1. sayi   "))
  sayi2 = int(input("2. sayi   "))
  islem = input("lutfen yapmak istediginiz islemi seciniz: (+ - * /)   ")
  if islem == "+": 
    print(sayi1 + sayi2)
  elif islem == "-":
    print(sayi1 - sayi2)
  elif islem == "*":
    print(sayi1 * sayi2)
  elif islem == "/" and sayi2 != 0:
     print(sayi1 / sayi2)
  elif islem == "/" and sayi2 == 0:
    print("Malesef bunu yapamıyoruz")
  else:
    print("Hayır dostum sadece +,-,*,/ koy")
except ValueError:
  print("Dostum bu bir sayı değil.")
