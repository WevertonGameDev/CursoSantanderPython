frutas = {"Maçã", "Banana", "Laranja"}

frutas.add("Pêra")
print(f"Adicionado Pêra: {frutas}")

frutas.remove("Banana")
print(f"Removido Banana: {frutas}")

frutas.discard("Uva")
print(f"Discarta a Uva: {frutas} (Como não tem, não faz nada)")

frutas.clear()
print(f"Limpa o Conjunto: {frutas}")
