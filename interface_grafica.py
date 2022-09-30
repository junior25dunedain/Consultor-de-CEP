import PySimpleGUI as pg

def Tela_inicial():
    pg.theme('DarkBlue3')

    cep = [[pg.Text('Informe um CEP (só numeros):',font='arial 12',pad=(0,0))],[pg.Input(size=(20,0),font='arial 12',pad=(0,0),key='cep')]]

    coluna1 = [
        [pg.Text('LOGRADOURO:',font='arial 12')],
        [pg.Text('BAIRRO:',font='arial 12')],
        [pg.Text('LOCALIDADE:', font='arial 12')],
        [pg.Text('UF:', font='arial 12')],
        [pg.Text('IBGE:', font='arial 12')],
        [pg.Text('DDD:', font='arial 12')]
    ]

    coluna2 = [
        [pg.Input(font='arial 12 bold',key='logradouro',size=(35,1))],
        [pg.Input(font='arial 12 bold', key='bairro', size=(30, 1))],
        [pg.Input(font='arial 12 bold', key='localidade', size=(30, 1))],
        [pg.Input(font='arial 12 bold', key='uf', size=(4, 1))],
        [pg.Input(font='arial 12 bold', key='ibge', size=(15, 1))],
        [pg.Input(font='arial 12 bold', key='ddd', size=(4, 1))]
    ]

    botoes = [
        [pg.Button('Consultar',font='arial 12',size=(10,1),pad=((0,15),0)),
        pg.CButton('Sair', font='arial 12', size=(8, 1))]

    ]

    layaout = [
        [pg.Text('Consulta_CEP',font='arial 18 bold')],
        [pg.Column(cep, justification='center',element_justification='center')],
        [pg.Column(coluna1,pad=((0,20),0)), pg.Column(coluna2)],
        [pg.Column(botoes, justification='center')]
    ]

    telaprint =pg.Window('Consulta_CEP', element_padding=(0,10),layout=layaout, size=(600,500), finalize=True)
