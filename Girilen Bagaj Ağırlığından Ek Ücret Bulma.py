kg=int(input("bagaj ağırlığını girin"))

b=kg-20
c=b*10
if kg<=20:
      print("Ek ücret gerekmemekte")
else:
      print("Kotanızı Aşan Ağırlık",b,"Bunun için",c,"TL Ödemeniz Gerekmekte")
