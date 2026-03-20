# Tamanho (quantidade de elementos) 
print("tamanho da lista 'frutas':", len(frutas))

# Fatiamento (slicing)
print("Fatiamento [0:2]:", frutas[0:2])

# Verificar se um item está na lista
print("Tem 'maçã'?", "maçã" in frutas)


frutas = ["maçã", "banana", "uva"]
numeros = [1,2,3,4]

#Acessando elementos
print("Primeira fruta:", frutas[0])      #"maçã"
print("Última fruta:", frutas[-1])       #"uva"

#Alterando elementos
frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

# Adicionando elementos
frutas.append("morango")         # adiciona no final
frutas.insert(1, "pera")         # adiciona na posição 1
print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("uva")           # remove pelo valor
ultima = frutas.pop()          # remove e retorna o último
print("Após remover'uva' e pop():", frutas, "| Última removida:", ultima)
