
# a_raw = raw_input ("vnesi stevilo A:")
# b_raw = raw_input("vnesi stevilo B:")
# operacija = raw_input("Operacija: ")

def get_izracun(vpisano_stevilo_a, stevilo_b, vpisana_operacija):
    if (vpisano_stevilo_a.find(".") == -1):
        a = int(vpisano_stevilo_a)
    else:
        a = float(vpisano_stevilo_a)

    if (stevilo_b.find(".") == -1):
        b = int(stevilo_b)
    else:
        b = float(stevilo_b)

    if (vpisana_operacija == "+"):
        rezultat = a + b
        return rezultat
    elif (vpisana_operacija == "-"):
        rezultat = a - b
        return rezultat
    elif (vpisana_operacija == "*"):
        rezultat = a * b
        return rezultat
    elif (vpisana_operacija == "/"):
        rezultat = a / b
        return rezultat
    else:
        return "Te operacije ne poznam"


