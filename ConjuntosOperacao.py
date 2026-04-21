# Para criar um conjunto, utilize chaves ou a função set():
conjunto1 = set([1, 2, 3])
conjunto2 = set([3, 4, 5])

uniao = conjunto1 | conjunto2
print(f"União: {uniao}")

intersecao = conjunto1 & conjunto2
print(f"Interseção: {intersecao}")

diferenca = conjunto1 - conjunto2
print(f"Diferença: {diferenca}")

diferencaSimetrica = conjunto1 ^ conjunto2
print(f"Diferença Simétrica: {diferencaSimetrica}")
