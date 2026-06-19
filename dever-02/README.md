        # Resultados obtidos:  
-----------------------------------------------------------------------------  
Tempo para n=10  : 0.000004 segundos  
Tempo para n=100 : 0.000019 segundos  
Tempo para n=500 : 0.000145 segundos  
Tempo para n=1000: 0.000582 segundos  

A complexidade de tempo do código anexado é Linear, representada assintoticamente por O(n).  

## Breve Explicação:

Quantidade de Chamadas: Para calcular o fatorial de um número n, a função calcular_fatorial(n) entra em recursão e chama a si mesma n vezes até atingir o caso base.

Custo por Chamada: Dentro de cada uma dessas execuções, ocorrem apenas operações primitivas de custo constante O(1) (a condição do if e uma operação de multiplicação).

Resultado: Multiplicando n chamadas pelo custo O(1) de cada uma, o tempo de execução cresce de forma diretamente proporcional ao tamanho da entrada, confirmando a complexidade O(n).