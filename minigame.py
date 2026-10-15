secim = ""
secim2 = ""

print("""
================================
         GECE VARDİYASI
================================

Saat 03:00.

Gözlerini karanlık bir restoranda açıyorsun.
Buraya nasıl geldiğini hatırlamıyorsun.

Dışarıda şiddetli yağmur yağıyor.
Elektrikler birkaç saniyeliğine yanıp sönüyor.

Ayağa kalkıp çıkış kapısına koşuyorsun.
Kapı kilitli.

Tam o sırada duvardaki hoparlörden cızırtılı
bir ses geliyor:

"Buradaysan... sakın mutfağa gitme."

Ses kesiliyor.
Önünde iki kapı var.

1 - Mutfağa git
2 - Depoya git

Ne yapacaksın?""")  
secim = int(input("seciminiz:  "))
if secim == 1:
  print("""Mutfağa giriyorsun.

Her yerde eski tabaklar ve boş yemek kapları var.
Yerde sürüklenmiş gibi görünen koyu izler görüyorsun.

Birden arkandaki buzdolabının kapağı çarpıyor!

İçeriden bir fısıltı duyuyorsun:

"Geç kaldın..."

Ne olduğunu anlamaya çalışırken
kapının dışından ayak sesleri geliyor.""") 
elif secim == 2:
  print("""Depoya giriyorsun.

Raflar eski kutularla dolu.
Odanın köşesinde eski bir güvenlik monitörü var.

Monitör kapalı olmasına rağmen
ekranda bir anlığına bir görüntü beliriyor.

Görüntüde sen varsın.

Ama ekrandaki sen,
sen daha hareket etmeden başını çeviriyor.

Monitör kapanıyor.

Ardından rafların arkasından metalik bir ses geliyor.
Sanki yere bir anahtar düşmüş gibi...
İleriden sesler geliyor.
1 - Sesi takip et
2 - Depodan çık""")
  secim2 = int(input("seciminiz:  "))
  if secim2 == 1:
    print("""Çıkış kapısına geri dönüyorsun.
Anahtarı kilide sokup çeviriyorsun.

Kilit açılıyor!

Yağmurun altına çıkıp koşmaya başlıyorsun.
Arkandan restoranın kapısı yavaşça kapanıyor.

İYİ SON — RESTORANDAN KURTULDUN.""")
  elif secim2 == 2:
    print("""Çıkış kapısına ulaşıyorsun.
Kapıyı zorluyorsun ama açılmıyor.

Hoparlörden aynı ses duyuluyor:
"Sana mutfağa gitme demiştim..."

KÖTÜ SON — RESTORANDA MAHSUR KALDIN.""")
