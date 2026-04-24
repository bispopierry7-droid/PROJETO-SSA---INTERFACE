def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i]  == item:
            return i #retorna o indice da lista:
    return -1 #retorna -1 se o item nao for encontrado:
        
#exemplo de uso
jogadores = ["lebron","guisantos","curry","jamorant"]
item_procurado = "guisantos"

resultado = busca_linear(jogadores, item_procurado)
if resultado != -1:
    print(f"Item '{item_procurado}' encontrado no indice {resultado} ")
else:
    print(f"Item '{item_procurado} nao encontrado na lista. ")
