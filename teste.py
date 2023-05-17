def criar_database_mysql():
    # Obtém as informações de conexão do usuário
    host = input("Digite o nome do host: ")
    user = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    database_name = input("Digite o nome da database: ")
    
    # Cria a conexão com o servidor MySQL
    import mysql.connector
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    
    # Cria a database
    cursor.execute(f"CREATE DATABASE {database_name}")
    cursor.execute(f"USE {database_name}")
    
    # Obtém as informações das tabelas do usuário
    num_tables = int(input("Digite o número de tabelas que deseja criar: "))
    
    table_scripts = []
    for i in range(num_tables):
        table_name = input(f"Digite o nome da tabela {i+1}: ")
        num_columns = int(input(f"Digite o número de colunas para a tabela {table_name}: "))
        
        column_defs = []
        for j in range(num_columns):
            column_name = input(f"Digite o nome da coluna {j+1}: ")
            column_type = input(f"Digite o tipo da coluna {column_name} (por exemplo, VARCHAR(255)): ")
            column_def = f"{column_name} {column_type}"
            column_defs.append(column_def)
        
        table_script = f"CREATE TABLE {table_name} ({', '.join(column_defs)})"
        table_scripts.append(table_script)
    
    # Exibe o script completo da database
    print("\nScript da Database:")
    print(f"CREATE DATABASE {database_name};")
    print(f"USE {database_name};")
    for table_script in table_scripts:
        print(table_script + ";")
    
    # Fecha a conexão com o servidor MySQL
    cursor.close()
    conn.close()

# Chama a função para criar a database
criar_database_mysql()
