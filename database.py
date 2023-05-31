from controle.Conexao import Conexao
import env

con = Conexao(dbname = env.databaseName ,host = env.hostName, port = env.port, user = env.userName, password = env.password )

def criarTabelas():
    sqls = ['''
    create table "Usuarios"(
    "id_user" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "nome" varchar(255) not null,
    "nascimento" varchar(10) not null,
    "login" varchar(255) not null,
    "senha" varchar(255) not null,
    "email" varchar(255) not null unique,
    "sex" varchar(255)
    )
    ''',

    '''create table "Gestão"(
    "id_gestão" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "tipo" varchar(255) not null default 1,
    "valor" float(2) not null,
    "data" varchar(10) not null,
    "vencimento" varchar(10) default 1,
    "total" float(2) default 0,
    "status" varchar(255) default 0,
    "mês" varchar(255) not null,
    "reserva" float(2) default 0,
    "id_user" int not null default 1,

        CONSTRAINT fk_user
        FOREIGN KEY("id_user")
        REFERENCES "Usuarios"("id_user")
    )
    '''
    ]

    for sql in sqls:
        if con.manipularBanco(sql):
            print("Tabela criada.")

# ver tabelas ----------------------------------------------------------------------------

def verdespesas(conexao):
    verDespesas = conexao.consultarBanco('''
    select * from "Gestão
    where "vencimento" != 1
    ''')
    
    return verDespesas


def verGanhos(conexao):
    verGanhos = conexao.consultarBanco('''
    select * from "Gestão"
    where "vencimento" = 1
    ''')

    return verGanhos


# adicionar -----------------------------------------------------------------------------------


def adicionarUsuario(conexao,nome,nascimento,login,senha,email,sex):

    inserirUser = conexao.manipularBanco(f'''
    insert into "Usuarios"
    values (default,'{nome}','{nascimento}', '{login}','{senha}','{email}','{sex}')
    ''')


def adicionarDespesas(conexao,tipo,valor,data,vencimento,total,status,mês,IdUser):

    inserirDespesa = conexao.manipularBanco(f'''
    insert into "Gestão"
    values (default, '{tipo}', '{valor}', '{data}', '{vencimento}', '{totalGastos()}', '{status}', '{mês}', '{IdUser}')
    ''')


def adicionarGanhos(conexao,tipo,valor,data,status,mês,IdUser):
    
        
    inserirGanhos = conexao.manipularBanco(f'''
    insert into "Gestão"
    values (default, '{tipo}', '{valor}', '{data}', default, '{totalGanhos()}', '{status}', '{mês}', '{IdUser}')
    ''')


def adicionarReservas(conexao,tipo,data,mês,idUser):
    
    inserirReserva = conexao.manipularBanco(f'''
    insert into "Gestão"
    values (default,'{tipo}',default,'{data}',default,'{totalReserva()}',default,'{mês}','{idUser}')
    ''')


# delete -----------------------------------------------------------------------------------------------------------


def deletarDespesas(conexao,id):

    deletarDespesa = conexao.manipularBanco(f'''
    delete from "Gestão"
    where "id_gestão" = '{id}' and "vencimento" != '1'
    ''')


def deletarGanhos(conexao,id):

    deletarGanho = conexao.manipularBanco(f'''
    delete from "Gestão"
    where "id_gestão" = '{id}' and "vencimento" = '1'
    ''')


def deletarReservaContinua(conexao):
    pass



# update -----------------------------------------------------------------------------------------------------------

def atualizarDespesa(conexao,coluna,variavel,id):

    updateDespesa = conexao.manipularBanco(f'''
    update "Gestão"
    set '{coluna}' = '{variavel}' 
    where "id_gestão" = '{id}'
    ''')


def atualizarGanhos(conexao,coluna,variavel,id):

    updateGanho = conexao.manipularBanco(f'''
    update "Gestão"
    set '{coluna}' = '{variavel}'
    where "id_gestão" = '{id}'
    ''')
    

# Pedir que o usuario diga o valor que foi subtraido do total da reserva ---------------------------------------------------
def atualizarReserva(conexao,variavell):

    total = totalReserva()
    total2 = total - variavell

    updateReserva = conexao.manipularBanco(f'''
    update "Gestão"
    set "reserva" = '{total2}'
    ''')


def updateLogin(conexao,senhaAntiga,senhaNova):

    verSenhas = conexao.consultarBanco('''
    select "senha" from "Usuarios"
    order by "id_user" ASC
''')
    controle = False

    for senha in verSenhas:
        if senha[2] == senhaAntiga:
            controle = True
    
    if controle == True:
        updateLogin = conexao.manipularBanco(f'''
        update "Usuarios"
        set "senha" = '{senhaNova}'
        ''')

    if controle == False:
        return "Error!"
    






# Funções auxiliares --------------------------------------------------------------------------------------------------

def totalGanhos(conexao):

    totalganhos = conexao.consultarBanco('''
        select sum(valor) from "Gestão"
        where vencimento = '1'
        ''')
    
    return totalganhos[0][0]


def totalGastos(conexao):

    totalgastos = conexao.consultarBanco('''
        select sum(valor) from "Gestão"
        where vencimento != '1'
        ''')
    
    return totalgastos[0][0]


def totalReserva(conexao):

    totalReserva = conexao.consultarBanco('''
        select sum(reserva) from "Gestão"
        where reserva = 'reserva'
        ''')
    
    return totalReserva[0][0]


def updateStatus(conexao,variavel,id):

    status = conexao.manipularBanco(f'''
    update "Gestão"
    set "status" = '{variavel}'
    where "id_gestão" = '{id}'
    ''')

# media de despesas de um mês especifico -------------------------------------------------------------------------------------------------
def despesasMes(conexao,variavel):

    media = conexao.consultarBanco(f'''
    select (sum(valor)/count(*)) as media
    where vencimento != '1' and "mês" = '{variavel}'
    ''')

    return media[0][0]

# media de ganhos de um mês especifico -------------------------------------------------------------------------------------------------
def ganhosMes(conexao,variavel):

    media = conexao.consultarBanco(f'''
    select (sum(valor)/count(*)) as media
    where vencimento = '1' and "mês" = '{variavel}'
    ''')

    return media[0][0]




# criarTabelas()

# adicionarDespesas(con,"despesa",50.00,"20/08/1998","20/09/1998","150","não paga","02","1")
# adicionarUsuario(con,"Victor","03/08/2005","admin","admin","teste@gmail.com","masculino")
# adicionarGanhos(con,"ganho",150.00,"20/08/1998","não recebido","02","1")


