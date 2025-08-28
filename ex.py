item = float(input("digite um valor:"))
quant = int(input("digite a quantidade:"))
total = item * quant
desconto = total * 0.10

totalDesc= total - desconto

print("a compra do senhor foi de",quant,"garrafas com o valor de ", item,"o total fica",total,"total com desconto:",totalDesc)