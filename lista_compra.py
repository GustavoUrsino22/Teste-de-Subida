# Pedir os itens do carrinho
carrinho = set(input("Digite os itens do carrinho, separados por vírgula: ").split(","))

# Pedir os itens que você tem na mão
itens_na_mao = set(input("Digite os itens que você tem na mão, separados por vírgula: ").split(","))

# Deixe na sua mão somente aquilo que não está no carrinho
itens_a_adicionar = itens_na_mao.difference(carrinho)

# Remover itens duplicados
itens_a_adicionar = itens_a_adicionar.difference(itens_na_mao.intersection(carrinho))

# Adicionar os itens restantes ao carrinho
carrinho.update(itens_a_adicionar)

print("Itens no carrinho após adicionar o que você tem na mão:", carrinho)
