#fall in python v.0.4.2
import pygame, sys, random, time
from pygame.locals import *
import math

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Fall in Python')
screen = pygame.display.set_mode((1920, 1080))
Icon=pygame.image.load('images/icon.png').convert()
pygame.display.set_icon(Icon)

bgm=pygame.mixer.Sound("sounds/tunnel.ogg") #메인 BGM
gameStart=pygame.mixer.Sound("sounds/Start_Sounds_001.wav")
gameEnd=pygame.mixer.Sound("sounds/lose sound 2 - 1_0.wav")
moveSound=pygame.mixer.Sound("sounds/Cloud Click.wav")


playerTexture=pygame.image.load('images/character_1.png').convert()#플레이어 스프라이트
playerTexture.set_colorkey((255, 255, 255))
playerTexture_1=pygame.image.load('images/character_1.png').convert()
playerTexture_2=pygame.image.load('images/character_2.png').convert()
playerTexture_3=pygame.image.load('images/character_3.png').convert()
playerTexture_4=pygame.image.load('images/character_4.png').convert()
playerTexture_5=pygame.image.load('images/character_5.png').convert()
playerTexture_6=pygame.image.load('images/character_6.png').convert()
playerTexture_1.set_colorkey((255, 255, 255))
playerTexture_2.set_colorkey((255, 255, 255))
playerTexture_3.set_colorkey((255, 255, 255))
playerTexture_4.set_colorkey((255, 255, 255))
playerTexture_5.set_colorkey((255, 255, 255))
playerTexture_6.set_colorkey((255, 255, 255))

normalBlockTexture=pygame.image.load('images/wall_normal.png').convert() #블럭 텍스처
normalBlockTexture.set_colorkey((255, 255, 255))
zeroBlockTexture=pygame.image.load('images/zero_block.png').convert()
zeroBlockTexture.set_colorkey((255, 255, 255))
newUpdateBlockTexture=pygame.image.load('images/new_update_block.png').convert()
newUpdateBlockTexture.set_colorkey((255, 255, 255))
endingBlockTexture=pygame.image.load('images/endingBlock.png').convert()
endingBlockTexture.set_colorkey((255, 255, 255))

backGround=pygame.image.load('images/background.png').convert()
devil=pygame.image.load('images/devil.png').convert()
devil.set_colorkey((255, 255, 255))
devilTurn=pygame.image.load('images/devilTurn.png').convert()
devilTurn.set_colorkey((255, 255, 255))
textBox=pygame.image.load('images/textbox.png').convert()
textBox.set_colorkey((255, 255, 255))
title=pygame.image.load('images/title.png').convert()
page1=pygame.image.load('images/1.png').convert() #시작 시 이미지
page2=pygame.image.load('images/2.png').convert()
page3=pygame.image.load('images/3.png').convert()
page4=pygame.image.load('images/4.png').convert()
textBox1=pygame.image.load('images/textBox1.png').convert()
textBox2=pygame.image.load('images/textBox2.png').convert()
textBox3=pygame.image.load('images/textBox3.png').convert()
textBox4=pygame.image.load('images/textBox4.png').convert()
textBox1.set_alpha(180)
textBox2.set_alpha(180)
textBox3.set_alpha(180)
textBox4.set_alpha(180)

howPlay=pygame.image.load('images/howPlay.png').convert()

startMark=pygame.image.load('images/startMark.png').convert()
#startMark.set_colorkey((0, 0, 0))
startMark.set_alpha(220)

fade=pygame.image.load('images/fade.png').convert()
fade.set_alpha(0)

font=pygame.font.Font("images/DungGeunMo.ttf", 35)
font2=pygame.font.Font("images/DungGeunMo.ttf", 30)
font3=pygame.font.Font("images/DungGeunMo.ttf", 45)

initPlayerDx=4 #플레이어 변화율 초기화값
genBlock_0=90 #블럭 생성 인자
genBlock_1=15
genBlock_2=10
totalGenBlock=0 #총 생성 블럭 수

class player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.dx=initPlayerDx
        self.dy=0.05
        self.zeroCount=3
    def draw(self):
        screen.blit(playerTexture, (self.x, self.y))
    def move(self):
        self.x+=self.dx
        self.dx*=1.04 #플레이어 이동 변화율 곱 인자 
    def rMove(self):
        self.x-=8

class normalBlock:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def draw(self):
        screen.blit(normalBlockTexture, (self.x, self.y))
    def move(self):
        self.x-=8
    def skill(self):
        return

class zeroPlusBlock(normalBlock): #0늘리는 특수 블록
    def draw(self):
        screen.blit(zeroBlockTexture, (self.x, self.y))
    def skill(self):
        player.zeroCount+=1
        
class genNewBlockBlock(normalBlock): #블록 업데이트
    def draw(self):
        screen.blit(newUpdateBlockTexture, (self.x, self.y))
    def skill(self):
        global totalGenBlock
        genBlock.gen(blocks[len(blocks)-1].x+theX)
        del blocks[0]

class endingBlock(normalBlock): #게임 클리어 조건 블럭
    def draw(self):
        screen.blit(endingBlockTexture, (self.x, self.y))
    def skill(self):
        global gameClear
        gameClear=True

class genBlock: #무작위 블럭 생성
    def __init__(self):
        self.blockType=0
        
    def gen(self, blockOrder): #0일반, 1제로 카운트 추가, 2블럭무작위생성
        global totalGenBlock

        if totalGenBlock == endingDeadLine: #노란 블럭 생성되는 수
            blocks.append(endingBlock(blockOrder, block_Y))
            totalGenBlock+=1
            return
        if totalGenBlock < endingDeadLine: #노란 블럭 생성된 후 확률 조정
            blockType=random.choices([0,1,2], [genBlock_0,genBlock_1,genBlock_2]).pop()
        else:
            blockType=random.choices([0,1,2,3], [genBlock_0,genBlock_1,genBlock_2,10]).pop() #노란 블럭 확률 생성
            
        if blockType==0:
            blocks.append(normalBlock(blockOrder, block_Y))
            totalGenBlock+=1
        elif blockType==1:
            blocks.append(zeroPlusBlock(blockOrder, block_Y))
            totalGenBlock+=1
        elif blockType==2:
            blocks.append(genNewBlockBlock(blockOrder, block_Y))
            totalGenBlock+=1
        elif blockType==3:
            blocks.append(endingBlock(blockOrder, block_Y))
            totalGenBlock+=1
            

firstReset=True
blocks=[]
canKeyGet=False
goBackBlock=False
goBackBlockCount=0
goPlayerCount=0
genBlock=genBlock()
#zeroCount=3
turnCountStack=0
turnCount=0
playerMove=False
playerMoveCount=0
player=player(600,795)
gameOver=False
playerTurn=True #플레이어, 컴 중 플레이 가능 여부
computerMove=False
computerRandom=0

devil_X=600#악마 좌표
devil_Y_sinMeta=0
devil_Y=200
devilEyeLight=False

block_Y=800#블록&플레이어 Y좌표
theX=128 #판정&블록 가로 기준값

endingSwitch=True

skipPage=False
PageCount=0
spriteTime=time.time()

skillSwitch=False

startSwitch=True
startMark_Y=400
startMark_Dy=1
startMark_alpha=220

fade_alpha=0

gameClear=False #게임 클리어 판별
endingDeadLine=150 #노란블럭 확정 출현 칸 수

endingBgmSwitch=True

startNow=False

while True: #메인화면
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                PageCount+=1
                if PageCount==1:
                    skipPage=True
            if event.key==pygame.K_BACKSPACE:
                startNow=True
                skipPage=True

    screen.blit(title, (0,0))       

    if (time.time()-spriteTime)>1:
        screen.blit(font.render("다음으로 <SPACE>", True, (255, 255, 255)), (760, 800))
        screen.blit(font.render("게임 바로 시작 <BACKSPACE>", True, (255, 255, 255)), (700, 850))
    if (time.time()-spriteTime)>2:
        spriteTime=time.time()

    if skipPage==True:
        skipPage=False
        gameStart.play(0)
        while fade_alpha<255:
            screen.blit(fade, (0,0))
            fade.set_alpha(fade_alpha)
            fade_alpha+=0.5
            pygame.display.update()
        break

    pygame.display.update()

PageCount=1
skipPage==False
fade_alpha=0
fade.set_alpha(0)

while True and startNow==False: #스토리 컷씬
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                PageCount+=1
                if PageCount==5:
                    skipPage=True
            if event.key==pygame.K_BACKSPACE:
                skipPage=True
        
    if PageCount==1:
        screen.blit(page1, (0,0))
        screen.blit(textBox1, (0,870))
    elif PageCount==2:
        screen.blit(page2, (0,0))
        screen.blit(textBox2, (0,870))
    elif PageCount==3:
        screen.blit(page3, (0,0))
        screen.blit(textBox3, (0,870))
    elif PageCount==4:
        screen.blit(page4, (0,0))
        screen.blit(textBox4, (0,870))
        
    if skipPage==True:
        skipPage=False
        gameStart.play(0)
        while fade_alpha<255:
            screen.blit(fade, (0,0))
            fade.set_alpha(fade_alpha)
            fade_alpha+=0.5
            pygame.display.update()
        break
    
    screen.blit(font3.render("다음 <SPACE>", True, (255, 255, 255)), (1590, 980))
    
    pygame.display.update()

PageCount=0
skipPage==False
fade_alpha=0
fade.set_alpha(0)

while True and startNow==False: #규칙 설명
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                PageCount+=1
                if PageCount==11:
                    skipPage=True
            if event.key==pygame.K_BACKSPACE:
                skipPage=True

    if PageCount==0:
        screen.blit(font3.render("시작하기 전에...", True, (255, 255, 255)), (100, 100))
    elif PageCount==1:
        screen.blit(font.render("당신과 악마의 턴이 번갈아가면서 진행됩니다", True, (255, 255, 255)), (100, 250))
    elif PageCount==2:
        screen.blit(font.render("당신은 당신의 턴에 1~3칸을 움직일 수 있습니다", True, (255, 255, 255)), (100, 320))
    elif PageCount==3:
        screen.blit(font.render("움직이지 않을 수도 있습니다", True, (255, 255, 255)), (100, 390))
    elif PageCount==4:
        screen.blit(font.render("당신의 턴이 끝나면 악마의 턴으로, 당신은 악마에 의해 1~3칸 앞으로 옮겨집니다", True, (255, 255, 255)), (100, 460))
    elif PageCount==5:
        screen.blit(font.render("턴이 끝날 때 마다 앞으로 한 칸이 생기고, 뒤로 한 칸이 없어집니다", True, (255, 255, 255)), (100, 530))
    elif PageCount==6:
        screen.blit(font.render("특별한 블록 위에 서서 블록의 힘을 취할 수 있습니다", True, (255, 255, 255)), (100, 600))
    elif PageCount==7:
        screen.blit(font.render("하얀 블록은 당신이 한 번 더 움직이지 않을 기회를 줍니다", True, (255, 255, 255)), (100, 670))
    elif PageCount==8:
        screen.blit(font.render("파란 블록은 맨 앞 블록을 주는 대신, 맨 뒤 블록을 가져갑니다", True, (255, 255, 255)), (100,740))
    elif PageCount==9:
        screen.blit(font.render("5턴마다 3개의 블록이 앞에서 생기고 뒤에서 사라지는 변화가 발생합니다", True, (255, 255, 255)), (100, 810))
    elif PageCount==10:
        screen.blit(font.render("노란 블록은 이 게임의 도착지입니다", True, (255, 255, 255)), (100, 880))

    screen.blit(font3.render("다음 <SPACE>", True, (255, 255, 255)), (1590, 980))
    
    if skipPage==True:
        skipPage=False
        gameStart.play(0)
        while fade_alpha<255:
            screen.blit(fade, (0,0))
            fade.set_alpha(fade_alpha)
            fade_alpha+=0.5
            pygame.display.update()
        break

    pygame.display.update()

PageCount=0
skipPage==False
fade_alpha=0
fade.set_alpha(0)

while True: #조작법
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                PageCount+=1
                if PageCount==1:
                    skipPage=True
            if event.key==pygame.K_BACKSPACE:
                skipPage=True
                
    screen.blit(howPlay, (0,0))
    screen.blit(font3.render("게임 시작 <SPACE>", True, (255, 255, 255)), (1480, 980))
    
    if skipPage==True:
        skipPage=False
        gameStart.play(0)
        while fade_alpha<255:
            screen.blit(fade, (0,0))
            fade.set_alpha(fade_alpha)
            fade_alpha+=0.5
            pygame.display.update()
        break

    pygame.display.update()
    
bgm.play(-1) #브금 켜기

while True: #메인 루프
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if playerTurn==True and canKeyGet==True and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_1:
                playerMove=True
                canKeyGet=False
                goPlayerCount=theX
                moveSound.play(0)
            elif event.key==pygame.K_2:
                playerMove=True
                canKeyGet=False
                goPlayerCount=theX*2
                moveSound.play(0)
            elif event.key==pygame.K_3:
                playerMove=True
                canKeyGet=False
                goPlayerCount=theX*3
                moveSound.play(0)
            elif event.key==pygame.K_0:
                if player.zeroCount>0:
                    player.zeroCount-=1
                    playerMove=True
                    canKeyGet=False
                    goPlayerCount=0
                else:
                    continue
                #if zeroCount>0:
                #    zeroCount-=1
                #    turnCountStack+=1
                #    turnCount+=1
                #    genBlock.gen(blocks[len(blocks)-1].x+80)
                #    del blocks[0]
                #    if player.x<blocks[0].x: #게임오버
                #        gameOver=True
                #break
            else:
                continue

            beforPlayerX=player.x #움직이기 전 플레이어 x좌표 저장(재대로 갔는지 확인용)
            player.dx=initPlayerDx #플레이어 움직임 변화율 초기화
            
            genBlock.gen(blocks[len(blocks)-1].x+theX) #블럭추가
            turnCountStack+=1
            turnCount+=1
    
    screen.blit(backGround, (0,0)) #배경
    screen.blit(textBox, (100,215))
    screen.blit(font.render("움직이지 않기: "+str(player.zeroCount), True, (0, 0, 0)), (120, 240))
    screen.blit(font.render("진행 턴 수: "+str(turnCount), True, (0, 0, 0)), (120, 290))

    if totalGenBlock>150: #특정 블럭 수 이후 출현 빈도 조절
        genBlock_0=90 #기본/ 블럭 생성 인자
        genBlock_1=10 #zero
        genBlock_2=30 #블럭 추가
    elif totalGenBlock>100:
        genBlock_0=90 #블럭 생성 인자
        genBlock_1=15
        genBlock_2=20
    elif totalGenBlock>30:
        genBlock_0=90 #블럭 생성 인자
        genBlock_1=20
        genBlock_2=20
        
    devil_Y=200+math.sin(devil_Y_sinMeta)*35
    devil_Y_sinMeta+=0.03
    if devil_Y_sinMeta >=3.14*2:
        devil_Y_sinMeta=0
    #screen.blit(devil, (devil_X,devil_Y)) #앙마 소환
    if devilEyeLight==True:
        screen.blit(devilTurn, (devil_X,devil_Y))
    else:
        screen.blit(devil, (devil_X,devil_Y))
    
    if firstReset==True: #블럭 초기 생성
        for i in range(600, 600+theX*5, theX):
            blocks.append(normalBlock(i, block_Y))
            totalGenBlock+=1
        firstReset=False

    if playerTurn==False and computerMove==True: #컴이 선택
        screen.blit(devilTurn, (devil_X,devil_Y))
        for i in range(len(blocks)):
            blocks[i].draw()
        player.draw()
        if turnCountStack>=4:
            screen.blit(font2.render("(다음 턴에 변화가 일어납니다...)", True, (200, 0, 50)), (740, 720))
        pygame.display.update()
        devilEyeLight=True
        pygame.time.wait(1000)
        
        computerRandom=random.choices([1,2,3], [35, 45, 20]).pop()
        player.dx=initPlayerDx #플레이어 움직임 변화율 초기화
        if computerRandom==1:
            playerMove=True
            goPlayerCount=theX
            moveSound.play(0)
        elif computerRandom==2:
            playerMove=True
            goPlayerCount=theX*2
            moveSound.play(0)
        elif computerRandom==3:
            playerMove=True
            goPlayerCount=theX*3
            moveSound.play(0)

        genBlock.gen(blocks[len(blocks)-1].x+theX) #블럭추가
        turnCountStack+=1
        turnCount+=1
        computerMove=False

    for i in range(len(blocks)): #블럭 그리기
        blocks[i].draw()

    if playerMove==True: #플레이어 옮기기
        if 0<goPlayerCount:
            player.move()
            playerMoveCount+=player.dx
            if (time.time()-spriteTime)>1:
                playerTexture=playerTexture_1
                spriteTime=time.time()
            if (time.time()-spriteTime)>0.1:
                playerTexture=playerTexture_2
            if (time.time()-spriteTime)>0.2:
                playerTexture=playerTexture_3
            if (time.time()-spriteTime)>0.4:
                playerTexture=playerTexture_4
            if (time.time()-spriteTime)>0.6:
                playerTexture=playerTexture_5
            if (time.time()-spriteTime)>7:
                playerTexture=playerTexture_6
        
        if playerMoveCount>=goPlayerCount:
            player.x=beforPlayerX+goPlayerCount
            playerTexture=playerTexture_1
            playerMove=False
            playerMoveCount=0
            goBackBlock=True
            
            
    
    if goBackBlock==True: #블럭 옮기기
        if 0<goPlayerCount:
            for i in range(len(blocks)):
                blocks[i].move()
            player.rMove()
            goBackBlockCount+=8
        
        if goBackBlockCount>=goPlayerCount:
            goBackBlock=False
            goBackBlockCount=0
            devilEyeLight=False

            for i in range(len(blocks)): #해당 블록 스킬 발동
                if player.x==blocks[i].x:
                    #skillSwitch=True
                    blocks[i].skill()
                    break
                
            if player.x>=blocks[len(blocks)-1].x+theX: #앞으로 넘어가면 게임오버
                gameOver=True
                
            if turnCountStack==5 and gameOver!=True: #5턴마다 3블럭 추가, 제거
                for i in range(3):
                    genBlock.gen(blocks[len(blocks)-1].x+theX)
                    del blocks[0]
                del blocks[len(blocks)-1]
                if player.x<blocks[0].x: #뒤로 넘어가면 게임오버
                    gameOver=True
                turnCountStack=0
            else:
                del blocks[0] #블럭제거

            if player.x<blocks[0].x: #뒤로 넘어가면 게임오버
                    gameOver=True
            
            if computerMove==False and playerTurn==True:
                computerMove=True
                playerTurn=False #플레이어 조작 불가
            #canKeyGet=True #입력제한 해제 코드
            if computerMove==False and playerTurn==False:
                playerTurn=True
                canKeyGet=True



    #if skillSwitch==True:
     #   blocks
      #  skillSwitch=False
        
    player.draw() #플레이어 그리기
    
    if turnCountStack>=4:
        screen.blit(font2.render("(다음 턴에 변화가 일어납니다...)", True, (200, 0, 50)), (740, 720))

    if gameClear==True: #게임 클리어 엔딩
        bgm.stop()
        pygame.time.wait(1000)
        gameEnd.play(0)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            pygame.quit()
                            sys.exit()
                        
            while fade_alpha<255:
                screen.blit(fade, (0,0))
                fade.set_alpha(fade_alpha)
                fade_alpha+=0.2
                pygame.display.update()

            if endingBgmSwitch==True:
                bgm.play(0)
                endingBgmSwitch=False
            
            screen.blit(fade, (0,0))
            screen.blit(font3.render("도착하였습니다!", True, (255, 255, 255)), (770, 300))
            screen.blit(font.render("총 진행된 턴 수: "+str(turnCount)+"턴", True, (255, 255, 255)), (770, 400))
            screen.blit(font.render("총 생성된 블록 수: "+str(totalGenBlock)+"칸", True, (255, 255, 255)), (770, 450))
            screen.blit(font.render("당신은 이제 오류를 보지 않을 겁니다!", True, (255, 255, 255)), (645, 700))
            
            if (time.time()-spriteTime)>1:
                screen.blit(font.render("<게임에서 나가기 위해 <SPACE>를 누르세요>", True, (255, 255, 255)), (600, 850))
            if (time.time()-spriteTime)>2:
                spriteTime=time.time()
                
            pygame.display.update()
        
    if gameOver==True: #게임 오버 엔딩
        bgm.stop()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            pygame.quit()
                            sys.exit()
            #특정키 눌러 재시작 구현 필요(그냥 끝냄으로 수정)
            #player.y+=1
            if endingSwitch==True:
                gameEnd.play(0)
                for i in range(player.y, player.y+500):
                    screen.blit(backGround, (0,0))
                    screen.blit(textBox, (100,215))
                    screen.blit(font.render("움직이지 않기: "+str(player.zeroCount), True, (0, 0, 0)), (120, 240))
                    screen.blit(font.render("진행 턴 수: "+str(turnCount), True, (0, 0, 0)), (120, 290))
                    screen.blit(devilTurn, (devil_X,devil_Y))
                    for i in range(len(blocks)): #블럭 그리기
                        blocks[i].draw()
                    player.y+=player.dy
                    player.dy*=1.01
                    playerTexture=playerTexture_2
                    player.draw()
                    pygame.display.update()
                    
                endingSwitch=False

            while fade_alpha<255:
                screen.blit(fade, (0,0))
                fade.set_alpha(fade_alpha)
                fade_alpha+=0.5
                pygame.display.update()
                
            screen.blit(fade, (0,0))
            screen.blit(font3.render("게임이 종료되었습니다", True, (255, 255, 255)), (740, 300))
            screen.blit(font.render("총 진행된 턴 수: "+str(turnCount)+"턴", True, (255, 255, 255)), (740, 400))
            screen.blit(font.render("총 생성된 블록 수: "+str(totalGenBlock)+"칸", True, (255, 255, 255)), (740, 450))
            if totalGenBlock<endingDeadLine:
                screen.blit(font.render("노란 블록 확정 생성까지: "+str(endingDeadLine-totalGenBlock)+"칸", True, (255, 255, 255)), (740, 500))

            if (time.time()-spriteTime)>1:
                screen.blit(font.render("종료하기 위해 <SPACE>...", True, (255, 255, 255)), (760, 850))
            if (time.time()-spriteTime)>2:
                spriteTime=time.time()
                
            pygame.display.update()
    
    if startSwitch==True:
        while fade_alpha>0:
            screen.blit(backGround, (0,0))
            screen.blit(textBox, (100,215))
            screen.blit(font.render("움직이지 않기: "+str(player.zeroCount), True, (0, 0, 0)), (120, 240))
            screen.blit(font.render("진행 턴 수: "+str(turnCount), True, (0, 0, 0)), (120, 290))
            screen.blit(devilTurn, (devil_X,devil_Y))
            for i in range(len(blocks)): #블럭 그리기
                blocks[i].draw()
            player.draw()
            screen.blit(startMark, (0,startMark_Y))
            
            screen.blit(fade, (0,0))
            fade.set_alpha(fade_alpha)
            fade_alpha-=2
            pygame.display.update()
            
        #screen.blit(startMark, (0,startMark_Y))
        pygame.display.update()
        pygame.time.wait(1000)
        
        while startMark_Y<1500:
            screen.blit(backGround, (0,0))
            screen.blit(textBox, (100,215))
            screen.blit(font.render("움직이지 않기: "+str(player.zeroCount), True, (0, 0, 0)), (120, 240))
            screen.blit(font.render("진행 턴 수: "+str(turnCount), True, (0, 0, 0)), (120, 290))
            screen.blit(devilTurn, (devil_X,devil_Y))
            for i in range(len(blocks)): #블럭 그리기
                blocks[i].draw()
            player.draw()
            
            screen.blit(startMark, (0,startMark_Y))
            startMark_Y+=startMark_Dy
            startMark_Dy*=1.015
            startMark_alpha-=1.8
            startMark.set_alpha(startMark_alpha)
            
            pygame.display.update()
        pygame.time.wait(500)
        canKeyGet=True
        startSwitch=False

    pygame.display.update()
