"""
Python'da Veri Tiplerini araştırınız, her bir veri tipi için 
kendi cümlelerinizle açıklamalar yazınız.
"""

#string => Metinsel ifade anlamına gelmektedir.
#int, integer => Tam sayıları ifade eder.
# float => Ondalıklı sayıları ifade eder.
# bool ve boolean => True veya False ifadeleri için kullanılır.
# matematiksel operatörler
# % => mod operatörler => tam bölünüyorsa 0, bölünmüyorsa 1.
# mantıksal oparatörler => Eşit, büyük ve küçüktür işaretleri
# or and, and => ve or => veya
# karar yapıları
#if elif - if else => indent kullanılır.

"""
Kodlama.io sitesinde değişken olarak kullanıldığını 
düşündüğünüz verileri, veri tipleriyle örneklendiriniz
"""
#string: Eğitmenlerimiz, kurs programı, ders programı
#int: öğrenci yorum sayısı, dersin tamamlanma yüzdesi
#boolean: Bitir ve devam et butonları


"""
Kodlama.io sitesinde şart blokları kullanıldığını 
düşündüğünüz kısımları örneklendiriniz ve Python dilinde
bu örnekleri koda dökünüz.
"""

email="aaaa@gmail.com"
password="aabb"
input1=input("mail giriniz: ")
input2=input("parola giriniz: ")
if(input1==email and input2==password):
    print("Succesful, your email or password is in correct")
else:
    print("Your Email or Password is incorrect, please try again!")
