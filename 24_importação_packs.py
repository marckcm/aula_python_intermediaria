import calc_precos as vd

preco = 49.90
preco_aum = vd.aumento(preco, 15, formata=True)
print(preco_aum)

preco_red = vd.reducao(preco, 15, formata=True)
print(preco_red)

print(vd.real(preco))
