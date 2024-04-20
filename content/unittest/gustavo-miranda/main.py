from calculadora import soma

print(soma(2, 2))
print(soma(5, 15))
print(soma(2, 22))
print(soma(33, -1))

try:
    print(soma("33", -1))
except AssertionError as e:
    print(f'Erro foi: {e}')
    