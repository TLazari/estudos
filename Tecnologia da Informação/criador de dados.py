import csv
import random
import faker

# Inicializar o faker para geração de dados aleatórios
fake = faker.Faker('pt_BR')

# Listas de tipos sanguíneos e resposta para a posse de veículo
tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
possui_veiculo = ['Sim', 'Não']

# Criar e escrever no arquivo CSV
with open('dados_pessoas.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Index', 'Nome', 'Cidade', 'Estado', 'Tipo Sanguíneo', 'Possui Veículo']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1, 1001):
        writer.writerow({
            'Index': i,
            'Nome': fake.name(),
            'Cidade': fake.city(),
            'Estado': fake.estado_sigla(),
            'Tipo Sanguíneo': random.choice(tipos_sanguineos),
            'Possui Veículo': random.choice(possui_veiculo),
        })

print("Arquivo 'dados_pessoas.csv' gerado com sucesso!")