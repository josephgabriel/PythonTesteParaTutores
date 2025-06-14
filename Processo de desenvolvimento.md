para esse projeto irei desenvolver um código de um jogo que apresente

-> Simplicidade com qualidade
-> Respeito às regras
-> Demonstração de didática, organização e domínio

1. **ESCOLHA DO GENÊRO E PROCESSO CRIATIVO**

Escolhi fazer um roguelike com visão de cima, onde o herói se move suavemente entre as células e evita inimigos, igual no exemplo da imagem abaixo.

![EXEMPLO](https://imgs.search.brave.com/dodFVU7i6Yy_qSTMi2CbRXofu7YA9DwCmmksoq32cJg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9oYXBw/eW1hZy50di93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMC8xMC9p/bWFnZS0xMS5qcGVn)

Escolhi fazer um jogo que se baseia em um cavaleiro que busca trocar de espada até chegar na maior de todas e a medida que ele vai avançando de fase ele aumenta a espada.

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

   criei os designs utilizando a ferramente Piskel, foram ao todo 20 sprites, 16 para o heroi e 4 para os inimigos

   criei tambem os 4 cenarios

![image](https://github.com/user-attachments/assets/8d28eb3f-7a8c-4243-b191-c40aaa489541)
criei os herois e inimigos e fiz com que quando o heroi colidisse com o inimigo este retornasse a posição original

criei a função load level que me permitiu mudar de fase toda vez que o player colidisse com o bau da espada

criei os obstaculos para cada fase

criei os herois e inimigos

atualizei o heroi e os inimigos para que não passasem por cima dos objetos e nem saissem da tela

estava tendo problemas com os inimigos nascendo encima dos obstaculos então ao inves de fazer eles nascerem em posiçoes aleatorias fiz com que eu definisse em cada fase onde eles iriam nascer

para os inimigos eu criei um AI simples para eles fazerem patrulha

adicionei o metodo tipico update() do pgzero representando basicamento o motor do jogo que roda a cada frame atualizando os movimentos do player e as ações do inimigos 
a cada instante.

5. **ARQUIVOS DE SOM**

   eu decidir adiconar 4 tipos de som
   
   Som do Menu, 🎵 Som de fundo, 💥 Som de colisão, 🏆 Som de vitória

   
