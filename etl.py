# EXTRACT
usuarios = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Julia", "idade": 27}
]

# TRANSFORM
for usuario in usuarios:
    usuario["mensagem"] = (
        f"Olá {usuario['nome']}, "
        f"seja bem-vindo(a) ao projeto ETL com Python!"
    )

# LOAD
for usuario in usuarios:
    print(usuario)
