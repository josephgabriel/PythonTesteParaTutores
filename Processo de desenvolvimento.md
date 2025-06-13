para esse projeto irei desenvolver um código de um jogo que apresente

-> Simplicidade com qualidade
-> Respeito às regras
-> Demonstração de didática, organização e domínio

1. **ESCOLHA DO GENÊRO E PROCESSO CRIATIVO**

Escolhi fazer um roguelike com visão de cima, onde o herói se move suavemente entre as células e evita inimigos, igual no exemplo da imagem abaixo.

![EXEMPLO](https://imgs.search.brave.com/dodFVU7i6Yy_qSTMi2CbRXofu7YA9DwCmmksoq32cJg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9oYXBw/eW1hZy50di93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMC8xMC9p/bWFnZS0xMS5qcGVn)

2. **CRIAÇÃO DA ESTRUTUTA INICIAL**
   para esse projeto utilizei o VScode como ferramenta de programação
   criei um diretorio chamado "RogueLikeGame", nele adicionei um arquivo main.py, images/ e sounds/, contendo respectivamente o código principal, os sprites(.png .jpeg) e arquivos .ogg.

   instalei a biblioteca Pyzero pelo terminal utilizando o comando 'pip install pgzero'.
   as outras bibliotecas utilizadas(Math e Random) não foi necessario fazer isso porque ja veem instaladas no Python.

3. **CRIAÇÃO DE UM MENU**
   A criação do Menu deve seguir as especificações:
   '✅ Menu Principal com botões: Começar jogo, Musica e sons ON/OFF, Saida.'

   com isso começei a programação

   segundo a documentação do PyZero:

   PyZero não tem um sistema de botões pronto como em outros frameworks, mas a gente pode:
   
   Desenhar "botões" com **screen.draw.filled_rect()** e **screen.draw.text()**, detectar cliques com **on_mouse_down()** e verificar colisão com **Rect.collidepoint()**
   Controlar estados do jogo com variáveis (ex: tela_atual = 'menu')

   ![image](https://github.com/user-attachments/assets/6c874d69-92cf-47d3-9684-9919a09967e5)

4. **ESTRUTURA BASE DO JOGO**
   com a criação de um menu simples irei partir já para a criação do jogo em si

   começei criando uma **class** chamada character(personagem) que será usada para o player e para os enemys.

   Definir uma variavel chamada HERO_SPEED para receber a velocidade do player

   a class character contem 4 metodos
   '__init__'(Configura posição, imagens e variáveis iniciais)
   'update'	(Atualiza animação e retângulo para colisão)
   'draw' (Desenha o personagem na tela com a imagem certa)
   'move' (Atualiza posição e estado de movimento)

   adicionei uma parte em que colocarei as imagens sprites do meu heroi e dos inimigos
  (hero_idle, hero_walk, enemy_idle, enemy_walk) utilizei a ferramenta web PISKEL para criar designs simples em pixel art.

![image](https://github.com/user-attachments/assets/8d28eb3f-7a8c-4243-b191-c40aaa489541)



   criei os herois e inimigos

    hero = Character(100, 100, hero_idle, hero_walk)

   para os inimigos eu criei um AI simples para eles fazerem a patrulha da princesa

   adicionei o metodo tipico update() do pgzero representando basicamento o motor do jogo que roda a cada frame atualizando os movimentos do player e as ações do inimigos 
   a cada instante.

   Encontrei algumas dificuldades porque meus inimigos ficavam tremendo e não se moviam de uma forma legal

   para melhorar meus inimigos eu comecei definindo atributos extras da class character utilizando a biblioteca random
   ![image](https://github.com/user-attachments/assets/9d69b8b1-102e-4ddb-9552-6b56e51ca8cd)

   tambem editei o metodo enemy_Ai para ficar algo mais visivelmente legal
   ![image](https://github.com/user-attachments/assets/677983f3-46ac-4fa4-84a0-c79b230b0f26)

   tambem fiz um metodo para impedir o heroi de sair da tela.

   outro problema que eu encontrei foi que meus inimigos extrapolavam a borda
   isso eu resolvi adicionando esses codigos no final do meu metodo enemy_Ai
   
   ![image](https://github.com/user-attachments/assets/8b376722-8c1d-445b-8c1b-f9e1390ca966)

   mas o que acontece se o heroi tocar no inimigo? eu fiz para que toda vez que o heroi tocar em um inimigo ele volte a posicção inicial, fiz isso definindo uma posição inicial ao heroi e na enemy_ai fiz com que toda vez que houvesse uma colisão do heroi com inimigo voltasse a posição original.

   mais a frente criei 3 tipos de backgrounds para 3 fases que eu quero implementar no jogo um verde(facil), marrom(medio) e vermelho(dificil)

   para a criação de obstaculos criei uma lista chamada 'obstacles' e o seguinte trecho do codigo em def update()

   ![image](https://github.com/user-attachments/assets/45f1a94c-f374-44f3-8b75-341dc60d3603)

   Primeiro tentamos mover só no eixo X.
   Se colidir, desfazemos o movimento no X.
   Depois tentamos mover no eixo Y.
   Se colidir, desfazemos o movimento no Y.

   minha próxima preocupação agora é fazer os inimigos não atravessarem os obstaculos, criar uma especie de 'linha de chegada' e configurar para que o player ao chegar 
   nela vá para a proxima fase fazendo isso até ir ao final exibindo uma tela de 'vitoria' e depois cuidar dos efeitos sonoros e terminar de personalizar o menu para deixar algo mais bonito.

   
