from db import conectar

def inserir_usuarios(nome,email,idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome,email,idade) VALUES(%s, %s, %s)",
        (nome,email,idade)
    )

    conn.commit()
    conn.close()


def atualizar_usuario(id_usuario, novo_nome, novo_email, nova_idade):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """ 
        UPDATE usuarios
        SET nome = %s , email = %s, idade = %s
        WHERE id = %s
        """,

        (novo_nome, novo_email, nova_idade, id_usuario)
    )

    conn.commit()
    conn.close()

def deletar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = %s",
        (id_usuario)
    )

    conn.commit()
    conn.close()

def consultar_banco():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios"
    )

    print(cursor.fetchall())
    
    conn.close()    


