real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dollar = real / 5.17
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dollar))