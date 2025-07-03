import pygame

pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("Seu Lugar _ com letra _ Moana.mp3")  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)         


tamanhoTela = (800, 500)
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption('runner')


fundo = pygame.image.load("ceu.png")
fundo = pygame.transform.scale(fundo, tamanhoTela)

jogadorCor = (255, 255, 0)
chaoCor = (0, 0, 0)
obstaculoCor = (255, 0, 0)

fonte = pygame.font.Font(None, 36)
fonte_titulo = pygame.font.Font(None, 72)
fonte_msg = pygame.font.Font(None, 36)


clock = pygame.time.Clock()


posicaoX = 50
posicaoY = 430
larguraJogador = 50
alturaJogador = 50
jogador = pygame.Rect(posicaoX, posicaoY, larguraJogador, alturaJogador)


posicaoXchao = 0
posicaoYchao = 430
larguraChao = 800
alturaChao = 200
chao = pygame.Rect(posicaoXchao, posicaoYchao, larguraChao, alturaChao)

posicaoXobstaculo = 800
posicaoYobstaculo = 380
larguraObstaculo = 50
alturaObstaculo = 50
obstaculo = pygame.Rect(posicaoXobstaculo, posicaoYobstaculo, larguraObstaculo, alturaObstaculo)
obstaculoVelocidade = 5


gravidadeJogador = 3
impulsoJogador = 150

ESTADO_INICIO = 'inicio'
ESTADO_JOGANDO = 'jogando'
ESTADO_GAMEOVER = 'gameover'
estado_jogo = ESTADO_INICIO


DistanciaPercorrida = 0.0
gameRun = True

def resetar():
    global DistanciaPercorrida, jogador, obstaculo
    DistanciaPercorrida = 0
    jogador.x = posicaoX
    jogador.y = 380  
    obstaculo.x = posicaoXobstaculo


jogador.y = 380

while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        elif event.type == pygame.KEYDOWN:
            if estado_jogo == ESTADO_INICIO and event.key == pygame.K_SPACE:
                estado_jogo = ESTADO_JOGANDO
            elif estado_jogo == ESTADO_GAMEOVER:
                if event.key == pygame.K_r:
                    resetar()
                    estado_jogo = ESTADO_JOGANDO
                elif event.key == pygame.K_ESCAPE:
                    gameRun = False

    if estado_jogo == ESTADO_INICIO:
        tela.blit(fundo, (0, 0))
        titulo = fonte_titulo.render('Runner', True, (255, 255, 255))
        instrucao = fonte_msg.render('Pressione ESPAÇO para jogar', True, (255, 255, 255))
        tela.blit(titulo, titulo.get_rect(center=(400, 200)))
        tela.blit(instrucao, instrucao.get_rect(center=(400, 260)))
        pygame.display.update()
        clock.tick(60)
        continue

    if estado_jogo == ESTADO_JOGANDO:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and jogador.y == 380:
            jogador.y -= impulsoJogador

      
        jogador.y += gravidadeJogador
        if jogador.colliderect(chao):
            jogador.y = 380

 
        obstaculo.x -= obstaculoVelocidade
        if obstaculo.right < 0:
            obstaculo.x = tamanhoTela[0]

 
        if jogador.colliderect(obstaculo):
            estado_jogo = ESTADO_GAMEOVER
            continue

   
        DistanciaPercorrida += 0.03

     
        tela.blit(fundo, (0, 0))
        texto_distancia = fonte.render('Distância: ' + str(round(DistanciaPercorrida, 1)), True, (255, 255, 255))
        tela.blit(texto_distancia, (10, 10))
        pygame.draw.rect(tela, jogadorCor, jogador)
        pygame.draw.rect(tela, chaoCor, chao)
        pygame.draw.rect(tela, obstaculoCor, obstaculo)
        pygame.display.update()
        clock.tick(60)
        continue

    if estado_jogo == ESTADO_GAMEOVER:
        tela.blit(fundo, (0, 0))
        msg_gameover = fonte_titulo.render('Game Over', True, (255, 255, 255))
        distancia_final = fonte_msg.render(f'Distância: {round(DistanciaPercorrida, 1)}', True, (255, 255, 255))
        instrucao2 = fonte_msg.render('Pressione R para reiniciar ou ESC para sair', True, (255, 255, 255))
        tela.blit(msg_gameover, msg_gameover.get_rect(center=(400, 200)))
        tela.blit(distancia_final, distancia_final.get_rect(center=(400, 260)))
        tela.blit(instrucao2, instrucao2.get_rect(center=(400, 320)))
        pygame.display.update()
        clock.tick(60)

pygame.quit()
