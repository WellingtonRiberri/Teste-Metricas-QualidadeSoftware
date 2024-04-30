import datetime

def valida_cartao(numero, nome, validade, codigo_seguranca):
    # Verifica se o número do cartão tem 16 dígitos
    if len(numero) != 16 or not numero.isdigit():
        return ("Inválido", "Compra negada")
    
    # Verifica se a validade do cartão está no formato correto (MM/AAAA)
    try:
        validade = datetime.datetime.strptime(validade, '%m/%Y')
    except ValueError:
        return ("Inválido", "Compra negada")

    # Verifica se a validade do cartão é maior que a data atual
    if validade < datetime.datetime.now():
        return ("Inválido", "Compra negada")

    # Verifica se o código de segurança tem 3 dígitos
    if len(codigo_seguranca) != 3 or not codigo_seguranca.isdigit():
        return ("Inválido", "Compra negada")

    return ("Válido", "Compra autorizada")

# Test cases
test_cases = [
    ("1234567890123456", "Wellington", "07/2028", "333", ("Válido", "Compra autorizada")),
    ("1234567890123456", "Wellington", "07/2028", "312", ("Válido", "Compra autorizada")),
    ("1234567890123dd456", "Wellington", "07/2026", "333", ("Inválido", "Compra negada")),
]

# Run test cases
for numero, nome, validade, codigo_seguranca, expected_result in test_cases:
    resultado = valida_cartao(numero, nome, validade, codigo_seguranca)
    print(f"Entrada: {numero}, {nome}, {validade}, {codigo_seguranca} - Resultado esperado: {expected_result}, Resultado obtido: {resultado}")
