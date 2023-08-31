import math
# ou utilizar "from math import sqrt"
num = int(input('digite um número'))
raiz = math.sqrt(num)
print("a raiz de um {} é igual a {:.2f} ".format(num, raiz))
# ou então .format(num, math.ceil(raiz) que vai arredondar para cima

# ex0017

import math
# from math import hypot

co = float(input('digite aqui o cateto oposto do triangulo'))
ca = float(input('digite aqui o cateto adjacente do triangulo'))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# raiz quadrada
hi = math.hypot(co, ca)
print('a hipotenusa é: {:.2f}'.format(hi))

# ex0018

from math import cos, tan, sen

a = float(input('digite o angulo que você deseja'))
r = math.cos(a), math.tan(a)
print('o seno de {}')

# ex0019

# ex0020

# ex0021



