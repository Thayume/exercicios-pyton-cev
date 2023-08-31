import math


print('olá, mundo')

nome = input('qual é o seu nome?')

print('é um prazer te conhecer', nome, 'seja bem vindo(a)')

# num1 = input('digite seu primeiro número')
# num2 = input('digite seu segundo número')
# print('o resultado é:', num1+num2)

num1 = int(input('digite seu primeiro número'))
num2 = int(input('digite seu segundo número'))
s = num1+num2
# print('a soma entre', num1, 'e', num2, 'é:', s)   (ao invés de ficar usando aspas
# toda hora usa-se colchetes)
print('a soma entre {} e {} vale {}'. format(num1, num2, s))


# ex05

n = int(input('digite um número'))
a = n-1
s = n+1
print('o número antecessoer de {} é: {} e o sucessor de {} é: {}'. format(n, a, n, s))
# ou podemos fazer: n = int(input('digite um número:'))
# print('o valor de {}, seu antecessor é {} e sucessor {}'. format(n, (n-1), (n+1)))

# ex06

n = int(input('digite um número'))
d = n*2
t = n*3
rq = n**2
# r = n**(1/2)
print('o dobro de {} é: {} o triplo  de {} é: {} e a raiz quadrada de {} é: {} '.format(n, d, n, t, n, rq))

# a raiz quadrada de {} é igual a {} {:.2f}.  ou  pow(n, (1/2)

# ex07

n1 = float(input('digite a nota de matemática:'))
n2 = float(input('digite a nota de português:'))
m = (n1+n2)/2
print('a média de português e matemática é', m)
# print('a média entre {:.1f} e {:.1f} é igual a {:.1f}'. format(n1, n2, média))

# ex08

nm = float(input('digite um número'))
c = (nm*10)*10
mm = (((nm*10)*10)*10)
# cm = nm * 100
# mm = nm * 1000
print('o número {} em centímetro é:{}cm e em milímetro é: {}mm'. format(nm, c, mm))
# se não quiser casa decimal usar: em centímetro é {:.0f}

# ex09

n = int(input('digite um número'))
u = n*1
d = n*2
t = n*3
q = n*4
c = n*5
s = n*6
st = n*7
o = n*8
nv = n*9
dz = n*10
print('a tabuáda do número {} é: {}x1={} \n {}x2={} \n {}x3={} {}x4={} {}x5={} {}x6={} {}x7={} {}x8={} {}x9={} \n{}x10={} '.
      format(n, n, u, n, d, n, t, n, q, n, c, n, s, n, st, n, o, n, nv, n, dz))


# ex10


d = float(input('digite quantos reais você tem'))
do = d / 3.27
print('a conversão de {} Reais em dólares fica: {} dólares'. format(d, do))


# ex11

larg = float(input('largura da parece'))
alt = float(input('altura da parede'))
area = larg * alt
print('sua parede tem {}x{} e sua área é de {}mq'. format(larg, alt, area))
tinta = area / 2
print('para pintar esta parede, você precisa de {}l de tinta'. format(tinta))

# ex12

pr = float(input('Digite o valor do produto:'))
desc = pr - (pr * 5 / 100)
print('o preço que antes era {}, agora com 5% de desconto é: {}'. format(pr, desc))

num1 = int(input('digite seu primeiro número'))
num2 = int(input('digite seu segundo número'))
s = num1+num2
print('a soma entre {} e {} vale {}'. format(num1, num2, s))

# ex0012
pr = float(input('Digite o valor do produto:'))
desc = pr - (pr * 5 / 100)
print('o preço que antes era {}, agora com 5% de desconto é: {:.2f}'. format(pr, desc))

# ex0013

sl = float(input('digite aqui o seu salário'))
aum = sl + (sl * 15 / 100)
print('o novo salário com 15% de desconto agora é: {}'. format(aum))

# ex0014

c = float(input('informe a temperatura em °C '))
f =((9 * c) / 5) + 32
print('a temperatura de {} °C corresponde a {} °F'.format(c, f))

# para usar o ° utilizar alt + 0176

# ex0015

d = int(input('quantos dias foram alugados? '))
km = float(input('quantos km foram rodados?'))
c = (60 * d) + (0.15 * km)
print('o total a pagar é: {:.2f} '. format(c))

# ex0016

from math import trunc
num = float(input('digite um número real'))
i = math.trunc(num)
print('o número {} tem a parte inteira de {}'.format(num, i))
# também podemos fazer sem importar nenhum módulo: .format(num, int(num))

# para comentar utilizar ''' '''
''' olá '''

"""  """



