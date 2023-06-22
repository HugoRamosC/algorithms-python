# Projeto Algorithms Python

[MEUS COMMITS](https://github.com/HugoRamosC/algorithms-python/commits)

## O que foi desenvolvido?

Neste projeto foi necessário resolver problemas e otimizar algoritmos desenvolvendo a capacidade de implementar soluções para os mais diversos problemas do dia a dia!

### Tecnologias utilizadas:

- Lógica em Python;
- interpretação de problemas;
- interpretação de um código legado;
- otimizar a resolução de problemas e;
- resolver problemas/Otimizar algoritmos sob pressão.

### Requisitos obrigatórios do Projeto

- [x] 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

    Busque qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. 
    
    O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.
    
    Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada `força bruta` em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável `target_time` e serão analisados os retornos da função.
    
    
    <details>
     <summary>
       <b>Clique aqui para ver um exemplo.</b>
     </summary>
    
    ```md
    # Nos arrays temos 6 estudantes
    
    # estudante             1       2       3       4       5       6
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    
    target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
    target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
    target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
    target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
    target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.
    
    Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
    ```
    
    </details>
    
    * Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
    
    * O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução.
    
    * O algoritmo deve utilizar a solução iterativa;
    
    * Caso o `target_time` passado seja nulo, o valor retornado pela função deve ser `None` (considere o horário 0 como um horário válido);
    
    * O código deve ser feito dentro do arquivo `challenges/challenge_study_schedule.py`.


- [x] 2 - Criptografia de inversões (Testes)

    Durante a dinâmica em grupos de um processo seletivo, a empresa contratante definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa deve criar uma função de criptografia, e a segunda pessoa deve implementar os testes da função implementada pela primeira pessoa.
    
    Você fará o papel da _**segunda pessoa**_ nessa dinâmica, ou seja: deve implementar os testes de uma função de criptografia.
    
    Esse teste deve se chamar `test_encrypt_message`, e ele deve garantir que a função de criptografia `encrypt_message` deve respeitar uma lógica específica.
    
    <details>
    <summary>
    <b>🧠 Entenda a lógica da função de criptografia</b>
    </summary>
    
    * Recebe uma string `message` e um inteiro `key` como parâmetros
    * Se `key` e `message` não possuírem os tipos corretos, uma exceção deve ser lançada
    * Se `key` não for um índice positivo válido de `message`, retorna a string `message` invertida
    * Se `key` for ímpar:
    * divide `message` no índice `key`, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas
    * Se `key` for par:
    * divide `message` no índice `key`, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com `"_"` entre elas
    
    
    </details>


- [x] 3 - Palíndromos (Recursividade)

    Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um _booleano_, `True` ou `False`.
    
    Mas o que é um palíndromo?
    
    > Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`.
    
    :warning: Neste projeto iremos focar somente em **palavras palíndromas** e não em frases ou números.
    
    <details>
     <summary>
       <b>Clique aqui para ver um exemplo.</b>
     </summary>
    
    ```md
    word = "ANA"
    # saída: True
    
    word = "SOCOS"
    # saída: True
    
    word = "REVIVER"
    # saída: True
    
    word = "COXINHA"
    # saída: False
    
    word = "AGUA"
    # saída: False
    ```
    
    </details>
    
    * O algoritmo deve ser feito utilizando a solução recursiva;
    
    * Não se preocupe com a análise da complexidade desse algoritmo;
    
    * Se for passado uma _string_ vazia, retorne `False`;
    
    * O código deve ser feito dentro do arquivo `challenges/challenge_palindromes_recursive.py`.


- [x] 4 - Anagramas (Algoritmo de ordenação)

  Faça um algoritmo que consiga comparar duas _strings_, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla `()` com a primeira string ordenada, a segunda string ordenada e um _booleano_, `True` ou `False` representando se são anagramas.
  
  O algoritmo deve considerar letras _maiúsculas_ e _minúsculas_ como iguais durante a comparação das entradas, ou seja, ser _case insensitive_.
  
  Mas o que é um anagrama?
  
  > "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."
  
  <details>
   <summary>
     <b>Clique aqui para ver um exemplo.</b>
   </summary>
  
  ```md
  first_string = "amor"
  second_string = "roma"
  # saída: ('amor', 'amor', True)
  # Explicação: Nesse caso a palavra 'amor' ordenada continua 'amor' e 'roma' ordenado vira 'amor, além disso a função é True, pois a palavra "roma" é um anagrama de "amor".
  
  
  first_string = "pedra"
  second_string = "perda"
  # saída: ('adepr', 'adepr', True)
  # Explicação: Nesse caso o retorno também é True. Na palavra "pedra", trocamos o "d" de lugar com o "r" e formamos "perda", sendo assim um anagrama e temos as duas strings ordenadas.
  
  
  first_string = "pato"
  second_string = "tapo"
  # saída: ('aopt', 'aopt', True)
  
  
  first_string = "Amor"
  second_string = "Roma"
  # saída: ('amor', 'amor', True)
  # Explicação: Nesse caso o retorno da função é True, pois a palavra "Roma" é um anagrama de "Amor" independente da letra "R" e "A" serem maiúsculas.
  
  
  # Agora vamos pra um exemplo em que não existe um anagrama
  first_string = "coxinha"
  second_string = "empada"
  # saída: ('achinox', 'aademp', False)
  ```
  
  </details>
  
  * Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
  * O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;
  
  * Utilize algoritmos de ordenação para realizar este requisito.
  * Utilize qualquer algoritmo que quiser (_Selection sort_, _Insertion sort_, _Bubble sort_, _Merge sort_, _Quick sort_ ou _TimSort_), desde que atinja a complexidade `O(n log n)`.
  * :warning: Você deverá implementar **sua própria função de ordenação**, ou seja, o uso de funções prontas **não** é permitido.
    * Exemplos de funções não permitidas: __sort_, _sorted_ e _Counter__;
  
  * :warning: **Não** será permitido realizar nenhuma **importação** neste arquivo!
  
  * A função retorna `True` caso uma _string_ **seja** um anagrama da outra independente se as letras são maiúsculas ou minúsculas;
  
  * A função retorna `False` caso uma _string_ **não seja** um anagrama da outra;
  
  * O código deve ser feito dentro do arquivo `challenges/challenge_anagrams.py`.



# Requisitos Bônus

- [x] 5 - Encontrando números repetidos (Algoritmo de busca)

    Dada um _array_ de números inteiros contendo `n + 1` inteiros, chamado de `nums`, em que cada inteiro está no intervalo `[1, n]`.
    
    Retorne apenas um número duplicado em `nums`.
    
    <details>
     <summary>
       <b>Clique aqui para ver um exemplo.</b>
     </summary>
    
    ```md
    nums = [1, 3, 4, 2, 2]
    # saída: 2
    
    nums = [3, 1, 3, 4, 2]
    # saída: 3
    
    nums = [1, 1]
    # saída: 1
    
    nums = [1, 1, 2]
    # saída: 1
    
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    # saída: 7
    ```
    
    </details>
    
    * Caso não passe nenhum valor ou uma string ou não houver números repetidos retorne `False`;
    
    * Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
      * O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;
    
    * O array montado deve:
    
      * Ter apenas números inteiros positivos maiores do que 1;
    
      * Ter apenas um único número repetindo duas ou mais vezes, todos os outros números devem aparecer apenas uma vez;
    
      * Ter, no mínimo, dois números.
    
    * O código deve ser feito dentro do arquivo `challenge_find_the_duplicate.py`.


- [x] 6 - Palíndromos (Iteratividade)

Resolva o mesmo problema apresentado no `requisito 2 - Palíndromos`, porém dessa vez utilizando a solução iterativa.

* Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
  * O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;

* O algoritmo deve utilizar a solução iterativa;

* O código deve ser feito dentro do arquivo `challenge_palindromes_iterative.py`.
