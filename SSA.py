
def triagem_bubblesort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j]['prioridade'] == fila[j+1]['prioridade']:
                idade_j = fila[j].get('idade') or fila[j].get('Idade', 0)
                idade_j1 = fila[j+1].get('idade') or fila[j+1].get('Idade', 0)
                if idade_j < idade_j1:
                    fila[j], fila[j+1] = fila[j+1], fila[j]
                                       
            elif fila[j]['prioridade'] > fila[j+1]['prioridade']:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    
    return fila  


def busca_paciente(fila, nome):
    for paciente in fila:
        if paciente['nome'].lower() == nome.lower():
            return paciente
    return None


