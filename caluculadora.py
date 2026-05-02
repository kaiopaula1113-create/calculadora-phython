value = float(input('digite um número:'))
value2 = float(input('digite outro:'))
sinal = input('escolha um sinal:')
if sinal == '+':
  print(value + value2)
if sinal == '-':
    print(value - value2)
if sinal == '*':
    print(value * value2)
if sinal == '/':
    print(value / value2)
if sinal == '%':
    print(value % value2)
if sinal == '**':
    print(value ** value2)
if sinal == '//':
    print(value // value2)
if sinal == '**(1/2)':
    print('as raizes são {} e {}'.format(value**(1/    2), value2**(1/2)))
