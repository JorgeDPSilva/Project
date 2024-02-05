import json

# Abre o arquivo contendo os acórdãos
with open('datasets/atco1_acordaos.json','r',encoding='utf-8') as json_file:
        #load do ficheiro
        dataset = json.load(json_file)

id_count = 0


for i, acordao in enumerate(dataset["acordaos"]):
    acordao["id"] = "a" + str(i + 1)

with open('datasets/atco1_acordaosIds.json', 'w') as f:
    json.dump(dataset, f,ensure_ascii=False, indent=4)