mult = 1
PI = 3.14

for ciclo1 in range(2):
  nro = input("ingresar nro:")
  nro = int(nro)
  if (nro > 0):
    mult = mult * nro * PI
  else:
    print("error")

print()
print(mult)