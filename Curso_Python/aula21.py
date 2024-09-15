# Operadores lógicos - AND
# and (e) or (ou) not (não)
# AND - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# Tipos de valor falsy: "0", "0.0", "", "False"

entrada = input("[E]ntrada [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"
if entrada == "E" and senha_digitada == senha_permitida: # Exemplo de AND, uma condição e a outra precisam
                                                         # ser verdadeiras para executar o IF.
    print("Entrar ")
else:
    print("Sair ")