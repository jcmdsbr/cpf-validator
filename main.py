def cpf_validator(document: str):
    multiplier_1 = range(10, 1, -1)
    multiplier_2 = range(11, 1, -1)
    invalid_sequence = ['1' * 11, '2' * 11, '3' * 11, '4' * 11, '5' * 11, '6' * 11, '7' * 11, '8' * 11, '9' * 11]
    document = ''.join(elem for elem in document.strip() if elem.isalnum())

    if document in invalid_sequence:
        return False

    if len(document) != 11:
        return False

    temp_cpf = document[0:9]

    sum_elem = 0

    for i in range(9):
        sum_elem += int(temp_cpf[i]) * multiplier_1[i]

    result = sum_elem % 11

    result = 0 if result < 2 else 11 - result

    digit = str(result)

    temp_cpf = temp_cpf + digit

    sum_elem = 0

    for i in range(10):
        sum_elem += int(temp_cpf[i]) * multiplier_2[i]

    result = sum_elem % 11

    result = 0 if result < 2 else 11 - result

    digit = digit + str(result)

    return document.endswith(digit)


# generate cpf from https://www.4devs.com.br/gerador_de_cpf

cpf = '502.295.490-71'

print(cpf_validator(cpf))
