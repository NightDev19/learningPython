age = 18
height = 170

if age >= 18:
    if height >= 170:
        print("Legal age and tall")
    elif height >= 150:
        print("Legal age but average")
    else:
        print("Legal age but short")
else:
    print("Underage")