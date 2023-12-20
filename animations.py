import pygame

#this is the file where each frame of every animation is stored in a list
#each frame will be selected one by one and displayed on to the screen when needed and the methods in the player and enemy class will
#iterate throgh theses lists when they are needed
#each file is loaded by using pygame and the file path is specified 

#this list stores each frame in the enemy running animation
enemy_run = [pygame.image.load("images/enemy/run_right/run_right0.xcf"),pygame.image.load("images/enemy/run_right/run_right1.xcf"),
             pygame.image.load("images/enemy/run_right/run_right2.xcf"),pygame.image.load("images/enemy/run_right/run_right3.xcf"),
             pygame.image.load("images/enemy/run_right/run_right4.xcf"),pygame.image.load("images/enemy/run_right/run_right5.xcf")]

#this list stores each frame in the enemy special attack animation
enemy_special_attack = [pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack0.xcf"),pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),pygame.image.load("images/enemy/special_attack/special_attack1.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack2.xcf"),pygame.image.load("images/enemy/special_attack/special_attack2.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack2.xcf"),pygame.image.load("images/enemy/special_attack/special_attack3.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack3.xcf"),pygame.image.load("images/enemy/special_attack/special_attack4.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack5.xcf"),pygame.image.load("images/enemy/special_attack/special_attack6.xcf"),
                        pygame.image.load("images/enemy/special_attack/special_attack7.xcf")]

#this list stores each frame in the enemy attack animation                  
enemy_attack = [pygame.image.load("images/enemy/attack/attack0.xcf"),pygame.image.load("images/enemy/attack/attack1.xcf"),
                pygame.image.load("images/enemy/attack/attack2.xcf"),pygame.image.load("images/enemy/attack/attack3.xcf"),
                pygame.image.load("images/enemy/attack/attack4.xcf")]

#this list stores each frame in the enemy idle animation
enemy_idle = [pygame.image.load("images/enemy/idle/idle0.xcf"),pygame.image.load("images/enemy/idle/idle1.xcf"),pygame.image.load("images/enemy/idle/idle2.xcf"),
              pygame.image.load("images/enemy/idle/idle3.xcf"),pygame.image.load("images/enemy/idle/idle4.xcf"),pygame.image.load("images/enemy/idle/idle5.xcf"),
              pygame.image.load("images/enemy/idle/idle6.xcf"),pygame.image.load("images/enemy/idle/idle7.xcf"),pygame.image.load("images/enemy/idle/idle8.xcf"),
              pygame.image.load("images/enemy/idle/idle9.xcf"),pygame.image.load("images/enemy/idle/idle10.xcf"),pygame.image.load("images/enemy/idle/idle11.xcf")]

#this list stores each frame in the enemy dead animation
enemy_dead = [pygame.image.load("images/enemy/dead/dead0.xcf"),pygame.image.load("images/enemy/dead/dead1.xcf")]

#this list stores each frame in the player idle animation
idle = [pygame.image.load("images/player/idle/idle0.xcf"),pygame.image.load("images/player/idle/idle1.xcf"),
        pygame.image.load("images/player/idle/idle2.xcf"),pygame.image.load("images/player/idle/idle3.xcf")]

#this list stores each frame in the player dead animation
dead = [pygame.image.load("images/player/player_dead/dead0.xcf"),pygame.image.load("images/player/player_dead/dead1.xcf")]

#this list stores each frame in the player ultimate attack animation
special_attack = [pygame.image.load("images/player/special_attack/special_attack0.xcf"),pygame.image.load("images/player/special_attack/special_attack1.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack2.xcf"),pygame.image.load("images/player/special_attack/special_attack3.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack4.xcf"),pygame.image.load("images/player/special_attack/special_attack5.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack6.xcf"),pygame.image.load("images/player/special_attack/special_attack7.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack8.xcf"),pygame.image.load("images/player/special_attack/special_attack9.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack10.xcf"),pygame.image.load("images/player/special_attack/special_attack11.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack12.xcf"),pygame.image.load("images/player/special_attack/special_attack13.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack14.xcf"),pygame.image.load("images/player/special_attack/special_attack15.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack16.xcf"),pygame.image.load("images/player/special_attack/special_attack17.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack18.xcf"),pygame.image.load("images/player/special_attack/special_attack19.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack20.xcf"),pygame.image.load("images/player/special_attack/special_attack21.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack22.xcf"),pygame.image.load("images/player/special_attack/special_attack23.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack24.xcf"),pygame.image.load("images/player/special_attack/special_attack25.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack32.xcf"),pygame.image.load("images/player/special_attack/special_attack33.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack34.xcf"),pygame.image.load("images/player/special_attack/special_attack35.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack36.xcf"),pygame.image.load("images/player/special_attack/special_attack37.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack38.xcf"),pygame.image.load("images/player/special_attack/special_attack39.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack40.xcf"),pygame.image.load("images/player/special_attack/special_attack41.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack42.xcf"),pygame.image.load("images/player/special_attack/special_attack26.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack27.xcf"),pygame.image.load("images/player/special_attack/special_attack28.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack29.xcf"),pygame.image.load("images/player/special_attack/special_attack30.xcf"),
                  pygame.image.load("images/player/special_attack/special_attack31.xcf")]

#this list stores each frame in the player normal attack and player special attack animation
attack = [pygame.image.load("images/player/attack/attack0.xcf"),pygame.image.load("images/player/attack/attack1.xcf"),
          pygame.image.load("images/player/attack/attack2.xcf"),pygame.image.load("images/player/attack/attack3.xcf"),
          pygame.image.load("images/player/attack/attack4.xcf"),pygame.image.load("images/player/attack/attack5.xcf"),
          pygame.image.load("images/player/attack/attack6.xcf"),pygame.image.load("images/player/attack/attack7.xcf"),
          pygame.image.load("images/player/attack/attack8.xcf"),pygame.image.load("images/player/attack/attack9.xcf"),
          pygame.image.load("images/player/attack/attack10.xcf"),pygame.image.load("images/player/attack/attack11.xcf"),
          pygame.image.load("images/player/attack/attack12.xcf"),pygame.image.load("images/player/attack/attack13.xcf"),
          pygame.image.load("images/player/attack/attack14.xcf"),pygame.image.load("images/player/attack/attack15.xcf"),
          pygame.image.load("images/player/attack/attack16.xcf"),pygame.image.load("images/player/attack/attack17.xcf"),
          pygame.image.load("images/player/attack/attack18.xcf"),pygame.image.load("images/player/attack/attack19.xcf"),
          pygame.image.load("images/player/attack/attack20.xcf"),pygame.image.load("images/player/attack/attack21.xcf"),
          pygame.image.load("images/player/attack/attack22.xcf"),pygame.image.load("images/player/attack/attack23.xcf"),
          pygame.image.load("images/player/attack/attack24.xcf"),pygame.image.load("images/player/attack/attack25.xcf")]


