def Consulta(cep):
    import requests
    url = 'https://viacep.com.br/ws/%s/json/' % cep
    rep = requests.get(url)
    rep_json = rep.json()
    return rep_json


def Salvar(cep,logad,bair,loca,uf,ibg,dd):
    with open('cep_armazenados.txt','a+') as arq:
        arq.write(f'''As informações do CEP -> {cep[:5]}-{cep[5:]} são:
  * Logradouro: {logad}
  * Bairro: {bair}
  * Localidade: {loca}
  * UF: {uf}
  * IBGE: {ibg}
  * DDD: {dd}\n''')



