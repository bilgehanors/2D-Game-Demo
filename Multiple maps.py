import pygame
win = pygame.display.set_mode()
WIDTH , HEIGHT = win.get_width() , win.get_height()
back1 = pygame.image.load(".Assets/bgONUR.png")
back1 = pygame.transform.scale(back1 , (WIDTH , HEIGHT))
back2 = pygame.image.load(".Assets/Bahçe.png")
back2 = pygame.transform.scale(back2 , (WIDTH , HEIGHT))
class game():
    def __init__(self,back,px,py):
        self.px = px
        self.py = py
        win = pygame.display.set_mode()
        pygame.display.set_caption("Samurai Oguz")
        fps = 60
        player_height = 180
        player_width = 140
        
        self.back = "back"
        
        
        class Player():
            
            def __init__(self, x , y):
                self.image = pygame.image.load(".Assets/1w.png")
                self.rect = self.image.get_rect()
                self.direction = 0
                self.speed = 5
                self.attack = False
                self.attack_cd = 400
                self.attack_time = None
                self.direction = pygame.math.Vector2()
                self.animation_assets()
                self.frame_index = 0
                self.animation_speed = 0.12
                self.rect.x = x
                self.rect.y = y
                self.statu = 'wait'
                
                
            def animation_assets(self):
                path = ".Assets/Animations"
                self.door_assets = []
                for num in range(1,3):
                    self.door_assets.append(pygame.transform.scale(pygame.image.load('.Assets/Door'f'/{num}.png'), (180, 210)))
                
                self.animations = {'up':[],'down':[],'left':[],
                                   'right':[],'wait':[], 'down_attack':[]
                                   , 'right_attack': [], 'left_attack':[],
                                   'up_attack':[]}
                for animation in self.animations.keys() :
                    full_path = path +'/' + animation
                    for num in range(1,3):
                        self.animations[animation].append(pygame.transform.scale(pygame.image.load(f'{full_path}/{num}.png'), (180, 210)))
                    for num in range(4,7):
                        self.animations['down_attack'].append(pygame.transform.scale(pygame.image.load(f'{path}/down_attack/'+f'{num}.png'),(180, 210)))
                        self.animations['right_attack'].append(pygame.transform.scale(pygame.image.load(f'{path}/right_attack/'+f'{num}.png'),(180, 210)))
                        self.animations['left_attack'].append(pygame.transform.scale(pygame.image.load(f'{path}/left_attack/'+f'{num}.png'),(180, 210)))
            def get_ani(self):
                if self.direction.x == 0 and self.direction.y == 0:
                    if not '_attack' in self.statu :
                        self.statu = 'wait'
                if self.attack:
                    self.direction.x = 0
                    self.direction.y = 0
                    if not '_attack' in self.statu:
                        if 'wait' in self.statu:
                            self.statu = 'down_attack'
                        else :
                            self.statu = self.statu + '_attack'
                else :
                    if'attack' in self.statu:
                        self.statu  = self.statu.replace('_attack','')
                            
                    
                        
                
            def control(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.direction.y = -1
                    self.statu = 'up'
                    
                elif keys[pygame.K_s]:
                    self.direction.y = 1
                    self.statu = 'down'
                else :
                    self.direction.y = 0
        
                if keys[pygame.K_a]:
                    self.direction.x = -1
                    self.statu = 'left'
        
                elif keys[pygame.K_d]:
                    self.direction.x = 1
                    self.statu = 'right'
                else : 
                    self.direction.x = 0
        
                if keys[pygame.K_SPACE] and not self.attack :
                    self.attack = True
                    self.attack_time = pygame.time.get_ticks()
            def move(self, speed):
                if self.direction.magnitude() != 0 :
                    self.direction = self.direction.normalize()
                self.rect.center += self.direction * speed
                
            def cooldown(self):
                current_time = pygame.time.get_ticks()
                if self.attack :
                    if current_time - self.attack_time >= self.attack_cd:
                        self.attack = False 
                    
        
            def draw_animation(self):
                animation = self.animations[self.statu]
                self.frame_index += self.animation_speed
                if self.frame_index >= len(animation):
                    self.frame_index = 0
                self.image = animation[int(self.frame_index)]
                
         
                        
            def uptade(self):
                self.cooldown()
                self.control()
                self.get_ani()
                self.draw_animation()
                self.move(self.speed)
                if self.rect.y > 900:
                    game(back2,650,300)
                elif self.rect.x >=600 and self.rect.x <= 700 and self.rect.y <= 299 :
                    game(back1, 600, 890)
                win.blit(self.image, self.rect)
                
                
        class Monster():
            def __init__(self,x,y):
                self.image = pygame.transform.scale(pygame.image.load('.Assets/1.png'),(100,100))
                self.rect = self.image.get_rect()
                self.frame_index = 0
                self.animation_speed = 0.12
                self.monster_assets()
                self.rect.x = x
                self.rect.y = y
            def monster_assets(self):
                self.monster_animations = []
                self.monster_animations.append(pygame.transform.scale(pygame.image.load('.Assets/1.png'),(100,100)))
                self.monster_animations.append(pygame.transform.scale(pygame.image.load('.Assets/2.png'),(100,100)))
                self.monster_animations.append(pygame.transform.scale(pygame.image.load('.Assets/3.png'),(100,100)))
                
                
                
            def uptade(self):
                self.monster_assets()
                self.frame_index += self.animation_speed
                if self.frame_index >= len(self.monster_animations):
                    self.frame_index = 0
                self.image = self.monster_animations[int(self.frame_index)]
                if self.rect.x >= 200:
                    self.rect.x -= 2
                if self.rect.x == 150:
                    self.rect.x += 0
                win.blit(self.image,self.rect)
                       
        
        
        player = Player(self.px,self.py)
        #monster = Monster(1100,400)
                
        
        def draw_window():
            win.blit(back, (0,0))
            player.uptade()
            #monster.uptade()
            
            pygame.display.update()
            
        def main():
            clock = pygame.time.Clock()
            run = True
            while run :
                clock.tick(fps)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                
                
                draw_window()
            pygame.quit()
                
                
                
                
                
                
        if __name__ == "__main__":
            main()
game(back1,100,400)