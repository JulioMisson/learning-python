valor1= int(input("digite o valor:"))
valor2= int(input("digite o degundo valor:"))
contas = [
    f"{valor1} + {valor2} = {  valor1 + valor2}",
    f"{valor1} - {valor2} = {valor1 -    valor2}",
    f"{valor1} * {valor2} = {valor1 *   valor2}",
    f"{valor1} / {valor2} = {valor1 /  valor2 }",
    f"{valor1} //{valor2} = {valor1 // valor2}",
    f"{valor1} % {valor2} = {valor1 %   valor2}",
    f"{valor1} ** {valor2} = {valor1 **   valor2}"
]
 
for contas in contas:
    print(contas)