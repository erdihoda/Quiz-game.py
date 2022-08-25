print("A doni te luani? ")

playing = input("A doni te luani? ")

if playing.lower() != "PO":
    quit()

print("Mire! le te luajme :)")
print("\n")

score = 0

## Pyetja e Pare
answer = input("Kush e krijoi Python? ")

if answer.lower() == "Guido Van Rossum":
    print("E sakte!")
    score += 1
    print("Tani rezultati juaj eshte", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pyetja e Dyte
answer = input("Ronaldo apo Messi")

if answer.lower() == "Ronaldo":
    print("E sakte!")
    score += 1
    print("Tani rezultati juaj eshte ", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pyetja e Trete
answer = input("Pronari i Tesles? ")

if answer.lower() == "Elon Musk":
    print("E sakte!")
    score += 1
    print("Tani Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## pyrtja e katert
answer = input("Hard-Disku e eshte me e shpejte se SSD? ")

if answer.lower() == "Jo nuk eshte":
    print("E sakte!")
    score += 1
    print("Tani rezultati juaj eshte ", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

print("You got " + str(score) + " question(s) correct!")
print("Which is " + str((score / 4) * 100) + "%")