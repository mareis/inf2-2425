farger = ["Rød", "Oransj", "Gul", "Grønn", "Blå", "Indigoblå", "Lilla"]

for nr, farge in enumerate(farger):
    print(f'[{nr + 1}] {farge}')

while True:
    try:
        tall = int(input("Velg farge 1-7: "))
        if 1 <= tall <= 7:
            print("Du valgte fargen,",farger[tall-1])
            break
        else:
            print("Tallet må være i intervallet [1,7]")


    except ValueError:
        print("Du skrev ikke inn et heltall")

