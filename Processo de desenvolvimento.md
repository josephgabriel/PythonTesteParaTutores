para esse projeto irei desenvolver um código de um jogo que apresente

-> Simplicidade com qualidade
-> Respeito às regras
-> Demonstração de didática, organização e domínio

1. **ESCOLHA DO GENÊRO E PROCESSO CRIATIVO**

Escolhi fazer um roguelike com visão de cima, onde o herói se move suavemente entre as células e evita inimigos, igual no exemplo da imagem abaixo.

![EXEMPLO](https://imgs.search.brave.com/dodFVU7i6Yy_qSTMi2CbRXofu7YA9DwCmmksoq32cJg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9oYXBw/eW1hZy50di93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMC8xMC9p/bWFnZS0xMS5qcGVn)

o que eu penso em fazer inicialmente é um jogo em que há o heroi e ele precisa salvar a princesa que esta em uma carruagem de um ataque de goblins! os inimigos vão surgindo e ele precisa ir derrotando eles até acabar com todos.

chamarei o jogo de "Goblin slayer".

2. **CRIAÇÃO DA ESTRUTUTA INICIAL**
   para esse projeto utilizei o VScode como ferramenta de programação
   criei um diretorio chamado "RogueLikeGame", nele adicionei um arquivo main.py, images/ e sounds/, contendo respectivamente o código principal, os sprites(.png .jpeg) e arquivos .ogg.

   instalei a biblioteca Pyzero pelo terminal utilizando o comando 'pip install pgzero'.
   as outras bibliotecas utilizadas(Math e Random) não foi necessario fazer isso porque ja veem instaladas no Python.

3. **CRIAÇÃO DE UM MENU**
   A criação do Menu deve seguir as especificações:
   '✅ Menu Principal com botões: Começar jogo, Musica e sons ON/OFF, Saida.'

   com isso começei a programação

   segundo a documentação do PyZero

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
  (hero_idle, hero_walk, enemy_idle, enemy_walk)

   criei os herois e inimigos

    hero = Character(100, 100, hero_idle, hero_walk)

   para os inimigos eu criei um AI simples para eles fazerem a patrulha da princesa

   adicionei o metodo tipico update() do pgzero representando basicamento o motor do jogo que roda a cada frame atualizando os movimentos do player e as ações do inimigos 
   a cada instante.
   
   
   
