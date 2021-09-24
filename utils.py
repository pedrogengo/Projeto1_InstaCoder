import csv

def open_csv(filename):
    with open(filename, newline='') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        rows = list(f)
    return rows

def merge_sort(lista, inicio=0, fim=None, is_tuple = False):
    if fim is None:
        fim = len(lista)
    
    if (fim - inicio) > 1:
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio, is_tuple)
        merge_sort(lista, meio, fim, is_tuple)
        merge(lista, inicio, meio, fim, is_tuple)
        return lista

def merge(lista, inicio, meio, fim, is_tuple = False):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    
    i = 0
    j = 0
    
    for list_index in range(inicio, fim):
        if i >= len(esquerda):
            lista[list_index] = direita[j]
            j += 1
        elif j >= len(direita):
            lista[list_index] = esquerda[i]
            i += 1
        else:
            if is_tuple:
                if esquerda[i][1] <= direita[j][1]:
                    lista[list_index] = esquerda[i]
                    i += 1
                else:
                    lista[list_index] = direita[j]
                    j += 1
            else:
                if esquerda[i] <= direita[j]:
                    lista[list_index] = esquerda[i]
                    i += 1
                else:
                    lista[list_index] = direita[j]
                    j += 1