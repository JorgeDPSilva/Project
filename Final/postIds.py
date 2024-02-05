import requests
import json
import time

response = requests.get('http://localhost:3000/acordaos')

if response.status_code == 200:
    acordaos = response.json()
    max_id = max([int(a['id'][1:]) for a in acordaos if 'id' in a])
    print(f'Maior ID: a{max_id}')
else:
    print(f'Erro {response.status_code}: {response.reason}')



with open('datasets/jtcampct_acordaos.json','r',encoding='utf-8') as json_file:
        dataset = json.load(json_file)

id_count = max_id
print (max_id)

for id_count, acordao in enumerate(dataset["acordaos"],id_count):
    
    acordao["id"] = "a" + str(id_count + 1)
    
'''
with open('jdgpj_acordaos.json', 'w',encoding='utf-8' ) as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)
'''
#data={'Processo': '83348', 'Tribunal 1ª instância': 'Supremo Tribunal de Justiça', 'Data da Decisão': '05/06/93', 'Texto das Cláusulas Abusivas': 'Os termos de uma cláusula de um contrato tipo em que se estabelece que o fornecimento de gás poderá ser feito directamente pela empresa fornecedora ou por pessoa ou entidade a designar por esta, permitem perfeitamente que a sua interpretação se faça no sentido de autorizar a possibilidade de cessão contratual, ou de subcontratação, proibida em absoluto pela alínea d) o artigo 18.º do referido decreto-lei. A cláusula do contrato que estabelece que a fornecedora de gás pode alterar os preços de aluguer do contador em qualquer momento é proibida pela alínea d) do artigo 22.º do referido diploma. É proibida, nos termos do artigo 18.º, alíneas a) a d) do citado Decreto-Lei, a cláusula desse contrato em que a fornecedora de gás se propõe eximir--se da reponsabilidade que, pela lei geral, lhe é atribuída em consequência de fornecimento do gás, por si ou concomitantemente com as respectivas instalações, sem olhar à culpa ou à ausência de culpa do lesado ou de terceiro. É uma cláusula absolutamente proibida a exclusão da responsabilidade da empresa. Não é admissível uma cláusula de alteração aleatória de preços.', 'Recursos': 'N', 'Texto Integral': '', 'url': '/jdgpj.nsf/f1d984c391da274c80257b820038a5b4/d501dd4774a0342980257a400056cdc2?OpenDocument', 'tribunal': 'jdgpj', 'id': 'a6268'}
num = 0  
ini = time.time()
for acordao in dataset["acordaos"]:  
    num += 1
    response = requests.get('http://localhost:3000/acordaos')
    if response not in dataset["acordaos"]:
        data=acordao
        post = requests.post('http://localhost:3000/acordaos', json=data,timeout=1000)
    
        if post.status_code <= 300:
            print(f'{post.status_code}: {acordao["id"]}  {post.reason}' )
        else:
            print(f'Erro {post.status_code}: {post.reason}')

fim = time.time()

def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return " %d horas,%02d minutos,%02d segundos" % (hour, min, sec) 

tempo = convert(int(fim -ini))

print(f'Carreguei {num} acordãos no tempo'+ str(tempo))            
