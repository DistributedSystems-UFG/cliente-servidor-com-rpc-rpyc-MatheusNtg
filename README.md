# ClientServerBasics
## Matheus da Silva Rodrigues

Este documento descreve uma aplicação calculadora implementada no estilo de cliente e servidor

### Cliente

O nosso cliente envia obtem as operações que o nosso usuário deseja realizar, enviando uma requisição para o servidor, que irá de fato realizar a operação.
Ao executar o cliente, o programa irá obter algumas informações essenciais para que a operação desejada seja realizada. O programa cliente irá perguntar qual é a operação que o usuário deseja realizar, bem como quais são os operadores para tal operação. Uma vez informado todos os dados necessários o cliente empacota a mensagem usando o pacote `pickle` e envia a mensagem para o servidor. Assim que a mensagem é enviada o cliente espera pela resposta do servidor, ao receber uma resposta o cliente desempacota a mensagem recebida e imprime o resultado da operação.

### Servidor

O servidor espera em um loop infinito por uma requisição de qualquer cliente, uma vez que a requisição é recebida ele desempacota a mensagem, filtra a operação necessária, executa a operação, recupera o resultado da operação e enpacota tal resultado em uma mensagem para ser enviada para o servidor.

### Link com apresentação:

[Vídeo](https://drive.google.com/file/d/1dHsoWTdgfDnaXO8cRblaHrrMmVVM8YL_/view?usp=sharing)
