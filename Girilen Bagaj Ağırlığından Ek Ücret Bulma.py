#Her KG İçin 10 TL Ücret Alınmakta.
kg=int(input("Bagaj ağırlığını girin"))

b=kg-20
c=b*10
if kg<=20:
      print("Ek ücret gerekmemekte")
else:
      print("Kotanızı Aşan Ağırlık",b,"Bunun için",c,"TL Ödemeniz Gerekmekte")
