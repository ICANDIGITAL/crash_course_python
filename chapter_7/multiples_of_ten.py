dez = input("Give me a number and I can instantly let you know if it's a multiple of ten. ")
dez = int(dez)

if dez % 10 == 0:
    print("The number " + str(dez) + " is divisible by ten.")

else:
    print("The number " + str(dez) + " is not divisible by ten.")