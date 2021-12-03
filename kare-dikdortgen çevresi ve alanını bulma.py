kenar1=int(input("1.kenarı girin: "))
kenar2=int(input("2.kenarı girin: "))
cevre=(kenar1+kenar2)*2
alan=(kenar1*kenar2)
print("                     ")
if kenar1==kenar2:
      print("karenin çevresi= ",cevre)
      print("karenin alanı= ",alan)
else:
          print("dikdörtgenin çevresi=",cevre)
          print("dikdörtgenin alanı=",alan)
