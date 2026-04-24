#BANCO DE DADOS TEMPORARIO(LISTA ORDENADA)

fila_hospitalar=[
    {"id" : 1,"nome": "cleber","prioridade" : 2, "idade": 30, "sintomas": "febre"},
    {"id" : 2,"nome": "thiago","prioridade" : 1, "idade": 25, "sintomas": "dor_cabeca"},
    {"id" : 3,"nome": "pierry","prioridade" : 3, "idade": 18, "sintomas": "tosse"},
    {"id" : 4,"nome": "maria","prioridade" : 2, "idade": 40, "sintomas": "dor"}
]
#CBSBJ
def triagem_bubblesort(fila):
    n=len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j]['prioridade'] == fila[j+1]['prioridade']:
                if fila[j]['idade'] < fila[j+1]['idade']:
                    #swap de troca, se prioridade for igual a idade entra como critério
                    fila[j], fila[j+1] = fila[j+1], fila[j]
                                       
            elif fila[j]['prioridade'] > fila[j+1]['prioridade']:
                #swap de troca por prioridade
                fila[j], fila[j+1] = fila[j+1], fila[j]
             

def busca_paciente(fila, nome):
    for paciente in fila:
        if paciente['nome'].lower() == nome.lower():
            return paciente
    return None


print(f"--sistema SSA: estado inicial--")
for p in fila_hospitalar:
    status = "URGENTE" if p['prioridade' ] <=2 else "ESTAVEL"
    print(f"ID:{p['id']}, nome: {p['nome']}, prioridade{p['prioridade']}, idade{p['idade']}, sintomas{p['sintomas']}")

print("\n -- Sistema SSA apos triagem--")
triagem_bubblesort(fila_hospitalar)
for p in fila_hospitalar:
    status = "URGENTE" if p['prioridade' ] <=2 else "ESTAVEL"
    print(f"ID:{p['id']}, nome: {p['nome']}, prioridade{p['prioridade']}, idade{p['idade']}, sintomas{p['sintomas']}") 


print("\n--Busca de paciente por nome--")
nome_busca = "thiago"
paciente_encontrado = busca_paciente(fila_hospitalar, nome_busca)


if paciente_encontrado:
    print(f"Paciente encontrado: {paciente_encontrado['nome']}")
else:
    print(f"Paciente nao encontrado! ")







