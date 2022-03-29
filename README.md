# ClientServerBasics
## Matheus da Silva Rodrigues

Este documento descreve uma aplicação calculadora implementada no estilo de cliente e servidor utilizando rpyc

## Dependências
 
 * python3
 * rpyc


### Cliente

Para esta aplicação, o nosso cliente utiliza somente os métodos expostos pelo servidos utilizando a bibliteca `rpyc`. Para isto basta nos conectarmos ao servidor utilizando as informações de conexão necessárias e chamarmos os métodos expostos assim como chamaríamos um método local. 

### Servidor

Para que um servidor possa expor seus métodos, ele necessita herdar uma classe do rpyc chamada `rpyc.Service`, uma vez que a nossa classe herda desta basta implementarmos nossos métodos exposos publicamente com a seguinte assinatura: `exposed_<nome_do_metodo>(self, <args>)`. Desta forma, todo e qualquer método que seguir esta assinatura será exposto para o cliente.

### Link com apresentação:

[Vídeo](https://drive.google.com/file/d/1dHsoWTdgfDnaXO8cRblaHrrMmVVM8YL_/view?usp=sharing)
