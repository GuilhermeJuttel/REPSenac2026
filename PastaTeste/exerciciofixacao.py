#Peça ao usuário seu nome e cumprimente utilizando a função print(), ex.: "Olá, Carol!"
nome = input("digite o seu nome: ")
print(f"olá, {nome}")

#Peça ao usuário sua idade e exiba na tela: "Você tem {idade} anos!"
idade = input("\nfale sua idade meu nobre: ")
print(f"caba, tua idade é {idade}")

#Leia o nome e a cidade da pessoa e imprima: "{nome} mora em {cidade}."
cidade = input("\nés da onde meu nobre? ")
pergunta = input(f"O {nome} moras em {cidade} mesmo? ")
if(pergunta == "sim"):
    print("és um baita")
else:print("ent és mentiroso, falasse antes uma coisa e agora é outra!")

#Leia um número e imprima o dobro dele.
numero = int(input("\nfale o valor de um produto que eu digo quanto vai ter de imposto :) "))
dobro = numero * 2
print(f"seu imposto é {dobro}")
rapaz = input(f"gostou? ")
if(rapaz == "sim"):
    print("que bom :)")
else:print("que pena, moras no Brasil!")