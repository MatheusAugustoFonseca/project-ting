import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    file = txt_importer(path_file)
    dict_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    file_already_exist = any(
        file_run["nome_do_arquivo"] == path_file for file_run in instance._data
    )

    if not file_already_exist:
        instance.enqueue(dict_info)
    print(dict_info)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        searched = instance.search(position)
        return sys.stdout.write(str(searched))
    except IndexError:
        sys.stderr.write("Posição inválida")
