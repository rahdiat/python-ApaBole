def ApaBole(x, y):
  i = x
  while i <= y:
    if (i % 3) == 0 and (i % 5) == 0:
      print("ApaBole")
    elif (i % 5) == 0:
      print("Bole")
    elif (i % 3) == 0:
      print("Apa")
    else:
      print(i)
    i += 1

ApaBole(1, 100)