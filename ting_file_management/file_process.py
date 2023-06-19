import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(data)
    print(data)
    return data


def remove(instance):
    if not instance or len(instance) == 0:
        return print("Não há elementos")

    file = instance.dequeue()["nome_do_arquivo"]
    print(str(f"Arquivo {file} removido com sucesso"))


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
