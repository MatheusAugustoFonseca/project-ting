def exists_word(word, instance):
    """Aqui irá sua implementação"""
    results = []

    for i in range(len(instance)):
        file = instance.search(i)
        occurence = []
        report = {}

        for index, content in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in content.lower():
                occurence.append({"linha": index + 1})
        report["palavra"] = word
        report["arquivo"] = file["nome_do_arquivo"]
        report["ocorrencias"] = occurence

        if occurence != []:
            results.append(report)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# iniciando o projeto
