from interface_grafica import *
from consultas import *

Tela_inicial()
while True:
    window, event, valor = pg.read_all_windows()

    if event == pg.WIN_CLOSED:
        break

    if event == 'Consultar':
        try:
            logradouro = Consulta(valor['cep'])['logradouro']
            bairro = Consulta(valor['cep'])['bairro']
            localidade = Consulta(valor['cep'])['localidade']
            uf = Consulta(valor['cep'])['uf']
            ibge = Consulta(valor['cep'])['ibge']
            ddd = Consulta(valor['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)
            Salvar(valor['cep'],logradouro,bairro,localidade,uf,ibge,ddd)
        except:
            pg.Popup('Verifique se o campo "CEP" foi preenchido corretamente\n'
                     '                         ou se ta conectado a internet', font='arial 12',title='ERRO!')

