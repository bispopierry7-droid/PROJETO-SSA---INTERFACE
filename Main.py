from SSA import triagem_bubblesort, busca_paciente
from Persistencia import salvar_fila_em_arquivo , carregar_fila_de_arquivo


def exibir_menu():
    print("\n" + "="*30)
    print(" Sistema SSA - SAUDE")
    print("1. Cadastrar Paciente")
    print("2. Ver fila(ordenar)")
    print("3. Buscar paciente")
    print("4. SAIR")
    return input("Escolha uma opção: ")


def iniciar_sistema():
    #CARREGAR DADOS DE UMA UNICA VEZ AO ABRIR
    fila = carregar_fila_de_arquivo()


    while True:
     opcao = exibir_menu()

     if opcao == "1":
        nome =input("nome do paciente: ")
        prioridade =int(input("prioridade (1 = urgente, 5 = leve): "))
        sintoma =input("Sintoma")
        idade = int(input("idade do paciente: "))

        paciente={
            "id": len(fila) + 1,
            "nome":nome,
            "prioridade":prioridade,
            "sintoma":sintoma, 
            "Idade":idade           
        }

        fila.append(paciente)
        salvar_fila_em_arquivo(fila)
        print("Paciente Cadastrado com sucesso")

    
     elif opcao == "2":
        if not fila:
            print("Fila vazia.")    
        else:
            #chama a logica de ordenacao
            fila_ordenada=triagem_bubblesort(fila)
            print("\n--- Fila de atendimento ---")
            for p in fila_ordenada:
                print(f"P{p['prioridade']} | {p['nome']} | {p['sintoma']} | {p['Idade']}")
        
    
     elif opcao == "3":
        nome_busca=input("Digite o nome para buscar: ")
        #CHAMA LOGICA DE BUSCA LINEAR
        p = busca_paciente(fila, nome_busca)
        if p:
            print(f"Paciente encontrado: ID {p['id']} - Nome {p['nome']} - Prioridade {p['prioridade']} - Sintoma {p['sintoma']}")
        else:
            print("Paciente nao encontrado  :C")

     elif opcao == "4":  
            print("encerrando o sistema SSA")
            break
       
     else:
      print("opcao invalida.")

if __name__ == "__main__":
    iniciar_sistema()





    

