a=int(input("1. Ürünün Fiyatını Girin:"))
b=int(input("2. Ürünün Fiyatını Girin:"))

toplam=a+b

if(toplam<200):
      print("Ödenecek Miktar:",toplam)
else:
      indirim=toplam-(toplam*0.25)
      toplam=toplam-indirim
      print("Ödenecek Miktar:",indirim,"(%25 indirim ile)")
      print("İndirim İle Tasaaruf Ettiğiniz Miktar:",toplam)
