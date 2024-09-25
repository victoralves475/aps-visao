import os
import subprocess

# Caminho para a pasta raiz
root_dir = os.getcwd()  # Altere para o caminho desejado
plantuml_jar = 'plantuml-1.2022.12.jar'  # Certifique-se de que o JAR está no mesmo diretório ou forneça o caminho correto

# Função para converter arquivos .puml em .svg
def convert_puml_to_svg(file_path):
    output_file = file_path.replace('.puml', '.svg')
    command = ['java', '-jar', plantuml_jar, '-tsvg', '-pipe']
    
    with open(file_path, 'rb') as puml_file:
        result = subprocess.run(command, stdin=puml_file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        with open(output_file, 'wb') as svg_file:
            svg_file.write(result.stdout)
        print(f'Convertido: {file_path} -> {output_file}')
    else:
        print(f'Erro ao converter {file_path}: {result.stderr.decode()}')

# Percorre a pasta raiz em busca de arquivos .puml
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.puml'):
            file_path = os.path.join(dirpath, filename)
            convert_puml_to_svg(file_path)
