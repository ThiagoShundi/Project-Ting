def exists_word(word, instance):
    modified_word = word.lower()
    result = []

    for file_data in instance._data:
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]
        counter = []

        for index, line in enumerate(lines, start=1):
            if modified_word in line.lower():
                counter.append({"linha": index})

        if counter:
            result.append({
                "palavra": modified_word,
                "arquivo": file_name,
                "ocorrencias": counter,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
