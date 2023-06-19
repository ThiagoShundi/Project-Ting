from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file in instance._data:
        return None

    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    print(str(data))
    instance.enqueue(path_file)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")

    file = instance.dequeue()
    print(str(f"Arquivo {file} removido com sucesso"))


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
