import json
import os
FILENAME = "fila_hospitalar.json"
def salvar_fila_em_arquivo(lista):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(lista,f,indent=4,ensure_ascii=False)


def carregar_fila_de_arquivo():
    if os.path.exists(FILENAME):
        with open(FILENAME,"r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []