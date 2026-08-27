import sqlite3
# Importa o SQLite


def conectar():
    # Define a função responsável pela conexão
    conexao = sqlite3.connect("mini_wms.db")
    # Cria a conexão com o banco de dados
    return conexao
    # Retorna a conexão


def criar_tabelas():
    # Função responsável por criar a tabela
    conexao = conectar()
    # Obtém a conexão com o banco
    cursor = conexao.cursor()
    # Cria o cursor para executar comandos SQL

    # Testei o comando SQL para garantir que os dados da tabela
    # usuarios não seriam alterados e, em seguida, criei a tabela produtos

    comando_sql = """
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY,
            codigo_barras TEXT,
            sku TEXT,
            descricao TEXT,
            caixaria INTEGER,
            validade TEXT,
            lote TEXT,
            quantidade INTEGER,
            valor_unitario REAL 
         
        );
    
    """

    cursor.execute(comando_sql)
    # Executa o comando SQL criado acima
    comando_inserir = """
        INSERT INTO produtos (
            codigo_barras,
            sku,
            descricao,
            caixaria,
            validade,
            lote,
            quantidade,
            valor_unitario
        )

        VALUES (
          '789000000001',
        'SKU001',
        'Arroz Tipo 1 5kg',
        '6',
        '2031/08/01',
        'LOTE001',
        '86',
        '25.90'
    ),
    (
        '789000000002',
        'SKU002',
        'Feijão Carioca 1kg',
        '12',
        '2031/09/15',
        'LOTE002',
        '120',
        '8.49'
    ),
    (
        '789000000003',
        'SKU003',
        'Açúcar Refinado 1kg',
        '10',
        '2032/01/20',
        'LOTE003',
        '95',
        '4.79'
    ),
    (
        '789000000004',
        'SKU004',
        'Café Torrado 500g',
        '12',
        '2031/11/10',
        'LOTE004',
        '74',
        '16.90'
    ),
    (
        '789000000005',
        'SKU005',
        'Macarrão Espaguete 500g',
        '20',
        '2032/02/05',
        'LOTE005',
        '150',
        '5.49'
    ),
    (
        '789000000006',
        'SKU006',
        'Farinha de Trigo 1kg',
        '10',
        '2032/03/12',
        'LOTE006',
        '63',
        '5.99'
    ),
    (
        '789000000007',
        'SKU007',
        'Óleo de Soja 900ml',
        '12',
        '2031/12/18',
        'LOTE007',
        '110',
        '7.89'
    ),
    (
        '789000000008',
        'SKU008',
        'Leite Integral 1L',
        '12',
        '2027/06/30',
        'LOTE008',
        '180',
        '5.29'
    ),
    (
        '789000000009',
        'SKU009',
        'Biscoito Cream Cracker 350g',
        '20',
        '2032/04/22',
        'LOTE009',
        '92',
        '6.49'
    ),
    (
        '789000000010',
        'SKU010',
        'Molho de Tomate 340g',
        '24',
        '2032/05/10',
        'LOTE010',
        '140',
        '3.79'
    ),
    (
        '789000000011',
        'SKU011',
        'Sardinha em Lata 125g',
        '24',
        '2033/01/15',
        'LOTE011',
        '65',
        '6.99'
    ),
    (
        '789000000012',
        'SKU012',
        'Milho Verde 170g',
        '24',
        '2033/02/18',
        'LOTE012',
        '88',
        '4.59'
    ),
    (
        '789000000013',
        'SKU013',
        'Ervilha em Conserva 170g',
        '24',
        '2033/02/18',
        'LOTE013',
        '81',
        '4.39'
    ),
    (
        '789000000014',
        'SKU014',
        'Leite em Pó 400g',
        '12',
        '2032/07/25',
        'LOTE014',
        '70',
        '14.90'
    ),
    (
        '789000000015',
        'SKU015',
        'Achocolatado 400g',
        '12',
        '2032/08/14',
        'LOTE015',
        '54',
        '11.90'
    ),
    (
        '789000000016',
        'SKU016',
        'Sal Refinado 1kg',
        '20',
        '2034/01/10',
        'LOTE016',
        '100',
        '3.49'
    ),
    (
        '789000000017',
        'SKU017',
        'Vinagre de Álcool 750ml',
        '12',
        '2034/03/05',
        'LOTE017',
        '72',
        '4.29'
    ),
    (
        '789000000018',
        'SKU018',
        'Maionese 500g',
        '12',
        '2032/06/20',
        'LOTE018',
        '58',
        '9.90'
    ),
    (
        '789000000019',
        'SKU019',
        'Ketchup 400g',
        '12',
        '2032/07/18',
        'LOTE019',
        '62',
        '8.49'
    ),
    (
        '789000000020',
        'SKU020',
        'Mostarda 200g',
        '12',
        '2032/08/22',
        'LOTE020',
        '48',
        '6.79'
    ),
    (
        '789000000021',
        'SKU021',
        'Detergente Neutro 500ml',
        '24',
        '2034/02/10',
        'LOTE021',
        '130',
        '2.99'
    ),
    (
        '789000000022',
        'SKU022',
        'Sabão em Pó 1kg',
        '12',
        '2034/04/15',
        'LOTE022',
        '75',
        '12.49'
    ),
    (
        '789000000023',
        'SKU023',
        'Amaciante 2L',
        '6',
        '2034/05/20',
        'LOTE023',
        '48',
        '15.90'
    ),
    (
        '789000000024',
        'SKU024',
        'Água Sanitária 1L',
        '12',
        '2034/06/12',
        'LOTE024',
        '90',
        '5.49'
    ),
    (
        '789000000025',
        'SKU025',
        'Desinfetante Lavanda 500ml',
        '12',
        '2034/07/08',
        'LOTE025',
        '84',
        '6.29'
    ),
    (
        '789000000026',
        'SKU026',
        'Limpador Multiuso 500ml',
        '12',
        '2034/08/19',
        'LOTE026',
        '69',
        '7.49'
    ),
    (
        '789000000027',
        'SKU027',
        'Esponja de Limpeza 3un',
        '20',
        '2035/01/15',
        'LOTE027',
        '105',
        '4.99'
    ),
    (
        '789000000028',
        'SKU028',
        'Papel Higiênico 12un',
        '8',
        '2035/02/10',
        'LOTE028',
        '42',
        '18.90'
    ),
    (
        '789000000029',
        'SKU029',
        'Papel Toalha 2un',
        '12',
        '2035/03/18',
        'LOTE029',
        '55',
        '9.49'
    ),
    (
        '789000000030',
        'SKU030',
        'Sacos para Lixo 30L',
        '20',
        '2035/04/12',
        'LOTE030',
        '70',
        '12.90'
    ),
    (
        '789000000031',
        'SKU031',
        'Shampoo 350ml',
        '12',
        '2034/09/10',
        'LOTE031',
        '64',
        '13.90'
    ),
    (
        '789000000032',
        'SKU032',
        'Condicionador 350ml',
        '12',
        '2034/09/10',
        'LOTE032',
        '59',
        '14.90'
    ),
    (
        '789000000033',
        'SKU033',
        'Sabonete 90g',
        '48',
        '2035/01/20',
        'LOTE033',
        '210',
        '2.79'
    ),
    (
        '789000000034',
        'SKU034',
        'Creme Dental 90g',
        '48',
        '2035/02/15',
        'LOTE034',
        '135',
        '5.99'
    ),
    (
        '789000000035',
        'SKU035',
        'Escova Dental Média',
        '24',
        '2036/01/10',
        'LOTE035',
        '88',
        '8.49'
    ),
    (
        '789000000036',
        'SKU036',
        'Desodorante Aerosol 150ml',
        '12',
        '2035/05/18',
        'LOTE036',
        '73',
        '12.99'
    ),
    (
        '789000000037',
        'SKU037',
        'Papel Alumínio 30cm',
        '24',
        '2036/02/20',
        'LOTE037',
        '47',
        '7.90'
    ),
    (
        '789000000038',
        'SKU038',
        'Filme PVC 15m',
        '24',
        '2036/03/15',
        'LOTE038',
        '52',
        '6.49'
    ),
    (
        '789000000039',
        'SKU039',
        'Guardanapo 50un',
        '24',
        '2036/04/10',
        'LOTE039',
        '80',
        '4.79'
    ),
    (
        '789000000040',
        'SKU040',
        'Filtro de Café 103',
        '20',
        '2036/05/12',
        'LOTE040',
        '61',
        '6.90'
    ),
    (
        '789000000041',
        'SKU041',
        'Refrigerante Cola 2L',
        '6',
        '2027/10/10',
        'LOTE041',
        '96',
        '9.99'
    ),
    (
        '789000000042',
        'SKU042',
        'Refrigerante Laranja 2L',
        '6',
        '2027/11/15',
        'LOTE042',
        '82',
        '8.99'
    ),
    (
        '789000000043',
        'SKU043',
        'Suco de Uva 1L',
        '12',
        '2028/01/12',
        'LOTE043',
        '68',
        '7.99'
    ),
    (
        '789000000044',
        'SKU044',
        'Suco de Laranja 1L',
        '12',
        '2028/02/20',
        'LOTE044',
        '71',
        '7.49'
    ),
    (
        '789000000045',
        'SKU045',
        'Água Mineral 1,5L',
        '6',
        '2028/03/15',
        'LOTE045',
        '150',
        '3.49'
    ),
    (
        '789000000046',
        'SKU046',
        'Água Mineral 500ml',
        '12',
        '2028/03/15',
        'LOTE046',
        '220',
        '1.99'
    ),
    (
        '789000000047',
        'SKU047',
        'Energético 473ml',
        '12',
        '2028/05/10',
        'LOTE047',
        '56',
        '8.90'
    ),
    (
        '789000000048',
        'SKU048',
        'Chá Mate 1L',
        '12',
        '2028/06/18',
        'LOTE048',
        '65',
        '6.90'
    ),
    (
        '789000000049',
        'SKU049',
        'Achocolatado Líquido 200ml',
        '27',
        '2027/12/20',
        'LOTE049',
        '108',
        '3.49'
    ),
    (
        '789000000050',
        'SKU050',
        'Iogurte Natural 170g',
        '24',
        '2027/09/05',
        'LOTE050',
        '90',
        '3.29'
    ),
    (
        '789000000051',
        'SKU051',
        'Queijo Mussarela 500g',
        '10',
        '2027/08/20',
        'LOTE051',
        '45',
        '24.90'
    ),
    (
        '789000000052',
        'SKU052',
        'Presunto Cozido 500g',
        '10',
        '2027/08/18',
        'LOTE052',
        '39',
        '19.90'
    ),
    (
        '789000000053',
        'SKU053',
        'Manteiga 200g',
        '12',
        '2027/10/05',
        'LOTE053',
        '57',
        '11.90'
    ),
    (
        '789000000054',
        'SKU054',
        'Margarina 500g',
        '12',
        '2028/01/15',
        'LOTE054',
        '72',
        '8.49'
    ),
    (
        '789000000055',
        'SKU055',
        'Requeijão Cremoso 200g',
        '12',
        '2027/11/20',
        'LOTE055',
        '49',
        '9.90'
    ),
    (
        '789000000056',
        'SKU056',
        'Creme de Leite 200g',
        '24',
        '2033/05/15',
        'LOTE056',
        '100',
        '4.99'
    ),
    (
        '789000000057',
        'SKU057',
        'Leite Condensado 395g',
        '24',
        '2033/06/10',
        'LOTE057',
        '95',
        '6.49'
    ),
    (
        '789000000058',
        'SKU058',
        'Fermento em Pó 100g',
        '24',
        '2033/08/18',
        'LOTE058',
        '66',
        '4.79'
    ),
    (
        '789000000059',
        'SKU059',
        'Canela em Pó 30g',
        '24',
        '2034/01/20',
        'LOTE059',
        '44',
        '3.99'
    ),
    (
        '789000000060',
        'SKU060',
        'Orégano 10g',
        '24',
        '2034/02/12',
        'LOTE060',
        '53',
        '2.99'
    ),
    (
        '789000000061',
        'SKU061',
        'Sabão em Barra 5un',
        '12',
        '2035/06/15',
        'LOTE061',
        '62',
        '9.90'
    ),
    (
        '789000000062',
        'SKU062',
        'Desengordurante 500ml',
        '12',
        '2035/07/20',
        'LOTE062',
        '48',
        '8.49'
    ),
    (
        '789000000063',
        'SKU063',
        'Limpa Vidros 500ml',
        '12',
        '2035/08/10',
        'LOTE063',
        '51',
        '7.90'
    ),
    (
        '789000000064',
        'SKU064',
        'Álcool Líquido 1L',
        '12',
        '2035/09/15',
        'LOTE064',
        '80',
        '9.49'
    ),
    (
        '789000000065',
        'SKU065',
        'Luvas de Limpeza M',
        '12',
        '2036/01/15',
        'LOTE065',
        '45',
        '12.90'
    ),
    (
        '789000000066',
        'SKU066',
        'Luvas de Limpeza G',
        '12',
        '2036/01/15',
        'LOTE066',
        '49',
        '12.90'
    ),
    (
        '789000000067',
        'SKU067',
        'Vassoura Multiuso',
        '6',
        '2036/03/20',
        'LOTE067',
        '30',
        '19.90'
    ),
    (
        '789000000068',
        'SKU068',
        'Rodo 40cm',
        '6',
        '2036/04/18',
        'LOTE068',
        '35',
        '18.90'
    ),
    (
        '789000000069',
        'SKU069',
        'Pá para Lixo',
        '12',
        '2036/05/10',
        'LOTE069',
        '40',
        '11.90'
    ),
    (
        '789000000070',
        'SKU070',
        'Balde Plástico 10L',
        '6',
        '2036/06/12',
        'LOTE070',
        '27',
        '15.90'
    ),
    (
        '789000000071',
        'SKU071',
        'Caderno Universitário 100fl',
        '10',
        '2037/01/10',
        'LOTE071',
        '50',
        '16.90'
    ),
    (
        '789000000072',
        'SKU072',
        'Caneta Esferográfica Azul',
        '50',
        '2037/02/15',
        'LOTE072',
        '300',
        '1.99'
    ),
    (
        '789000000073',
        'SKU073',
        'Lápis Preto HB',
        '50',
        '2037/03/20',
        'LOTE073',
        '250',
        '1.49'
    ),
    (
        '789000000074',
        'SKU074',
        'Borracha Branca',
        '50',
        '2037/04/18',
        'LOTE074',
        '180',
        '1.29'
    ),
    (
        '789000000075',
        'SKU075',
        'Apontador Escolar',
        '50',
        '2037/05/10',
        'LOTE075',
        '120',
        '2.49'
    ),
    (
        '789000000076',
        'SKU076',
        'Papel Sulfite A4 500fl',
        '5',
        '2037/06/15',
        'LOTE076',
        '75',
        '28.90'
    ),
    (
        '789000000077',
        'SKU077',
        'Pasta Plástica A4',
        '20',
        '2037/07/20',
        'LOTE077',
        '90',
        '5.90'
    ),
    (
        '789000000078',
        'SKU078',
        'Marcador Permanente Preto',
        '24',
        '2037/08/10',
        'LOTE078',
        '65',
        '4.99'
    ),
    (
        '789000000079',
        'SKU079',
        'Fita Adesiva Transparente',
        '24',
        '2037/09/15',
        'LOTE079',
        '70',
        '3.49'
    ),
    (
        '789000000080',
        'SKU080',
        'Cola Branca 90g',
        '24',
        '2037/10/20',
        'LOTE080',
        '58',
        '4.90'
    ),
    (
        '789000000081',
        'SKU081',
        'Pilha Alcalina AA 4un',
        '24',
        '2038/01/10',
        'LOTE081',
        '45',
        '14.90'
    ),
    (
        '789000000082',
        'SKU082',
        'Pilha Alcalina AAA 4un',
        '24',
        '2038/02/15',
        'LOTE082',
        '48',
        '15.90'
    ),
    (
        '789000000083',
        'SKU083',
        'Lâmpada LED 9W',
        '12',
        '2038/03/20',
        'LOTE083',
        '65',
        '8.90'
    ),
    (
        '789000000084',
        'SKU084',
        'Lâmpada LED 12W',
        '12',
        '2038/04/18',
        'LOTE084',
        '59',
        '10.90'
    ),
    (
        '789000000085',
        'SKU085',
        'Extensão Elétrica 5m',
        '6',
        '2038/05/10',
        'LOTE085',
        '32',
        '29.90'
    ),
    (
        '789000000086',
        'SKU086',
        'Adaptador Tomada 10A',
        '24',
        '2038/06/15',
        'LOTE086',
        '75',
        '7.90'
    ),
    (
        '789000000087',
        'SKU087',
        'Carregador USB-C',
        '12',
        '2038/07/20',
        'LOTE087',
        '42',
        '34.90'
    ),
    (
        '789000000088',
        'SKU088',
        'Cabo USB-C 1m',
        '24',
        '2038/08/10',
        'LOTE088',
        '80',
        '19.90'
    ),
    (
        '789000000089',
        'SKU089',
        'Fone de Ouvido Bluetooth',
        '6',
        '2038/09/15',
        'LOTE089',
        '28',
        '59.90'
    ),
    (
        '789000000090',
        'SKU090',
        'Suporte para Celular',
        '12',
        '2038/10/20',
        'LOTE090',
        '37',
        '24.90'
    ),
    (
        '789000000091',
        'SKU091',
        'Organizador Plástico 5L',
        '6',
        '2039/01/10',
        'LOTE091',
        '40',
        '18.90'
    ),
    (
        '789000000092',
        'SKU092',
        'Caixa Organizadora 10L',
        '6',
        '2039/02/15',
        'LOTE092',
        '35',
        '29.90'
    ),
    (
        '789000000093',
        'SKU093',
        'Pote Plástico 1L',
        '12',
        '2039/03/20',
        'LOTE093',
        '72',
        '8.90'
    ),
    (
        '789000000094',
        'SKU094',
        'Garrafa Térmica 1L',
        '6',
        '2039/04/18',
        'LOTE094',
        '25',
        '49.90'
    ),
    (
        '789000000095',
        'SKU095',
        'Copo Plástico 300ml 10un',
        '20',
        '2039/05/10',
        'LOTE095',
        '100',
        '6.90'
    ),
    (
        '789000000096',
        'SKU096',
        'Prato Plástico 10un',
        '20',
        '2039/06/15',
        'LOTE096',
        '85',
        '9.90'
    ),
    (
        '789000000097',
        'SKU097',
        'Talheres Plásticos 20un',
        '20',
        '2039/07/20',
        'LOTE097',
        '90',
        '7.90'
    ),
    (
        '789000000098',
        'SKU098',
        'Guardanapo Decorado 20un',
        '24',
        '2039/08/10',
        'LOTE098',
        '65',
        '5.90'
    ),
    (
        '789000000099',
        'SKU099',
        'Papel Toalha Industrial',
        '6',
        '2039/09/15',
        'LOTE099',
        '38',
        '24.90'
    ),
    (
        '789000000100',
        'SKU100',
        'Filme Plástico Industrial',
        '6',
        '2039/10/20',
        'LOTE100',
        '30',
        '39.90'
    );
    """


    cursor.execute(comando_inserir)

    comanod_select = """
        SELECT  *  FROM produtos;

"""
    cursor.execute(comanod_select)
    dados_exibir = cursor.fetchall()
    print(dados_exibir)
    conexao.commit()
    # Confirma e registra a alteração realizada no banco
    
    print("100 itens inseridos com sucesso!")
    # Exibe uma mensagem de confirmação

    conexao.close()
    # Fecha a conexão para finalizar o acesso ao banco


criar_tabelas()
# Chama a função para executar o processo