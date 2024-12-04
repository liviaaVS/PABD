[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/f63fFlqO)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17332254)

# Bem vindo dockeria da livia 🍬

## Cardápio:

    ### tortas:

    torta de morango 🍓
    torta de limão 🍋
    torta de chocolate 🍫

    <hr>

    ### bolos:

    bolo de cenoura 🥕
    bolo de chocolate 🍫
    bolo de laranja 🍊

## Explicando modelos do negócio:

### Cliente

O modelo `Cliente` representa um cliente da doceria. Ele possui os seguintes campos:

- `nome`: Um campo de texto com no máximo 100 caracteres que armazena o nome do cliente.
- `email`: Um campo de email que armazena o endereço de email do cliente.
- `telefone`: Um campo de texto com no máximo 15 caracteres que armazena o número de telefone do cliente.

### Doce

O modelo `Doce` representa um doce disponível na doceria. Ele possui os seguintes campos:

- `nome`: Um campo de texto com no máximo 100 caracteres que armazena o nome do doce.
- `preco`: Um campo decimal que armazena o preço do doce, com até 5 dígitos no total e 2 casas decimais.
- `descricao`: Um campo de texto que armazena a descrição do doce.

### Pedido

O modelo `Pedido` representa um pedido realizado por um cliente. Ele possui os seguintes campos:

- `numero`: Um campo inteiro que armazena o número do pedido.
- `data`: Um campo de data que armazena a data do pedido.
- `valor`: Um campo decimal que armazena o valor total do pedido, com até 5 dígitos no total e 2 casas decimais.
- `cliente`: Um campo de chave estrangeira que referencia o cliente que realizou o pedido. Se o cliente for deletado, o pedido também será.

### DocesPedido

O modelo `DocesPedido` representa a relação entre um pedido e os doces incluídos nele. Ele possui os seguintes campos:

- `quantidade`: Um campo inteiro que armazena a quantidade de um determinado doce no pedido.
- `produto`: Um campo de chave estrangeira que referencia o doce incluído no pedido. Se o doce for deletado, a relação também será.
- `pedido`: Um campo de chave estrangeira que referencia o pedido. Se o pedido for deletado, a relação também será.
