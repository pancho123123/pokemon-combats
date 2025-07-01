import pygame
from random import randint
import random

ancho = 900
alto = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = ()


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Pokemon combat")
clock = pygame.time.Clock()

def draw_text1(surface, text, size, x, y):
   font = pygame.font.SysFont("serif", size)
   text_surface = font.render(text, True, WHITE)
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surface.blit(text_surface, text_rect)

def draw_text2(surface, text, size, x, y):
   font = pygame.font.SysFont("serif", size)
   text_surface = font.render(text, True, BLACK)
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surface.blit(text_surface, text_rect)

def draw_hp_bar(surface, x, y, percentage):
   BAR_LENGHT = 200
   BAR_HEIGHT = 10
   fill = (percentage / 100) * BAR_LENGHT
   border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
   fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
   pygame.draw.rect(surface, GREEN, fill)
   pygame.draw.rect(surface, WHITE, border, 2)

def draw_exp_bar(surface, x, y, percentage):
   BAR_LENGHT = 100
   BAR_HEIGHT = 10
   fill = (percentage / 100) * BAR_LENGHT
   border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
   fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
   pygame.draw.rect(surface, BLUE, fill)
   pygame.draw.rect(surface, WHITE, border, 2)



class Pokemon(pygame.sprite.Sprite):
   def __init__(self,img_int,team_int,pc=500):
      super().__init__()
      self.img_int = img_int
      if 0 <= img_int < len(pokemon_images):
         self.image = pokemon_images[img_int]
      else:
         raise ValueError("img_int fuera de rango")
      #self.image.set_colorkey(WHITE)
      self.rect = self.image.get_rect()
      self.team_int = team_int
      if self.team_int == 0:
         self.rect.bottomleft = 200,450
      else:
         self.rect.bottomleft = 600,250
      
      if 0 <= img_int < len(pokemon_type_list1):
         self.type1 = pokemon_type_list1[img_int]
      else:
         raise ValueError("img_int fuera de rango")
      if 0 <= img_int < len(pokemon_type_list1):
         self.type2 = pokemon_type_list1[img_int]
      elif self.type_int2 == None:
         self.type2 = None
      else:
         raise ValueError("img_int fuera de rango")
      self.pc = pc
      self.hp = pokemon_hp[img_int]
      self.ultimo_ataque = 0
      self.tiempo_entre_ataques = 1100#milisegs
      self.defense = 0
      self.attack = 0
      self.speed = 0

   def update(self):
      if self.team_int == 1:
         for pok in all_sprites:
            if pok.team_int == 0:
               if pygame.time.get_ticks() - self.ultimo_ataque > self.tiempo_entre_ataques:
                  pok.hp -= damage(self,pok)
                  self.ultimo_ataque = pygame.time.get_ticks()
               
            

      if self.hp <= 0:
         if self.team_int ==0:
            player_pokemon_list.remove(self)
         else:
            op_pokemon_list.remove(self)
            
         self.kill()



pokemon_images = []
pokemon_list = ["img/pok/abra.png","img/pok/absol.png","img/pok/aerodactyl.png","img/pok/aipom.png",
                "img/pok/alakazam.png","img/pok/arbok.png","img/pok/arcanine.png",
                "img/pok/ariados.png","img/pok/articuno.png","img/pok/beedrill.png",
                "img/pok/bellossom.png","img/pok/bellsprout.png","img/pok/blastoise.png",#10bellos
                "img/pok/blissey.png","img/pok/bulbasaur.png", "img/pok/butterfree.png",#13 blissey 
                "img/pok/caterpi.png","img/pok/celebi.png","img/pok/chansey.png", #16_caterpi
                "img/pok/charizard.png", "img/pok/charmander.png","img/pok/charmeleon.png",#20_charmander
                "img/pok/chinchou.png","img/pok/clefable.png","img/pok/clefairy.png",
                "img/pok/cleffa.png","img/pok/cloyster.png", "img/pok/corsola.png",
                "img/pok/crobat.png","img/pok/croconaw.png","img/pok/cubone.png",#30cubone
                "img/pok/cyndaquil.png", "img/pok/delibird.png", "img/pok/dewong.png",
                "img/pok/diglett.png","img/pok/ditto.png", "img/pok/dodrio.png",
                "img/pok/doduo.png","img/pok/donphan.png","img/pok/dragonair.png",
                "img/pok/dragonite.png", # 40 dragonite
   "img/pok/dratini.png","img/pok/drowzee.png","img/pok/dugtrio.png", 
   "img/pok/dunsparce.png", "img/pok/eevee.png","img/pok/ekans.png",
   "img/pok/electabuzz.png","img/pok/electrode.png","img/pok/elekid.png","img/pok/entei.png",#50entei
   "img/pok/espeon.png","img/pok/exeggcute.png","img/pok/exeggutor.png",
   "img/pok/farfetch.png","img/pok/fearow.png","img/pok/feraligatr.png",
   "img/pok/flaaffy.png","img/pok/flareon.png","img/pok/forretress.png",
   "img/pok/furret.png","img/pok/gastly.png","img/pok/gengar.png",#60furret
   "img/pok/geodude.png","img/pok/girafarig.png","img/pok/gligar.png",#63geodude,
   "img/pok/gloom.png","img/pok/golbat.png","img/pok/goldeen.png",#66gloom
   "img/pok/golduck.png","img/pok/golem.png", "img/pok/granbull.png",#70golem
   "img/pok/graveler.png","img/pok/grimer.png","img/pok/growlithe.png", 
   "img/pok/gyarados.png","img/pok/haunter.png","img/pok/heracross.png",
   "img/pok/hitmonchan.png","img/pok/hitmonlee.png","img/pok/hitmontop.png",#80hitmontop
   "img/pok/hoothoot.png","img/pok/hoppip.png","img/pok/horsea.png",
   "img/pok/houndoom.png","img/pok/houndour.png","img/pok/ho-oh.png","img/pok/hypno.png",
   "img/pok/igglybuff.png",
   "img/pok/ivysaur.png","img/pok/jigglypuff.png","img/pok/jolteon.png",#90jigglypuff
   "img/pok/jumpluff.png","img/pok/jynx.png","img/pok/kabuto.png",
   "img/pok/kabutops.png",
   "img/pok/kadabra.png","img/pok/kakuna.png","img/pok/kangaskhan.png",
   "img/pok/kingdra.png","img/pok/kingler.png","img/pok/koffing.png",#100kingler
   "img/pok/krabby.png","img/pok/lanturn.png","img/pok/lapras.png",
   "img/pok/larvitar.png",#
   "img/pok/ledyba.png","img/pok/lickitung.png","img/pok/lugia.png",
   "img/pok/machamp.png", 
   "img/pok/machoke.png","img/pok/machop.png","img/pok/magby.png",#110machoke
   "img/pok/magcargo.png","img/pok/magikarp.png","img/pok/magmar.png",
   "img/pok/magnemite.png","img/pok/magneton.png","img/pok/mankey.png",
   "img/pok/mantine.png","img/pok/mareep.png","img/pok/marill.png",#120mareep
   "img/pok/marowak.png",
   "img/pok/meganium.png",
   "img/pok/meowth.png","img/pok/metapod.png","img/pok/mew.png",
   "img/pok/mewtwo.png","img/pok/miltank.png",
   "img/pok/misdreavus.png","img/pok/moltres.png","img/pok/mr.mime.png",#130moltres
   "img/pok/muk.png",#1
   "img/pok/murkrow.png","img/pok/natu.png","img/pok/nidoking.png",#131murk
   "img/pok/nidoqueen.png","img/pok/nidoran1.png","img/pok/nidoran2.png",
   "img/pok/nidorina.png","img/pok/nidorino.png","img/pok/ninetales.png",#140nidorino
   "img/pok/noctowl.png","img/pok/octillery.png","img/pok/oddish.png",
   "img/pok/omanyte.png","img/pok/omastar.png",
   "img/pok/onix.png","img/pok/paras.png","img/pok/parasect.png",
   "img/pok/persian.png","img/pok/phanpy.png","img/pok/pichu.png","img/pok/pidgeot.png",#150persian
   "img/pok/pidgeotto.png","img/pok/pidgey.png","img/pok/pikachu.png",
   "img/pok/piloswine.png","img/pok/pineco.png","img/pok/politoed.png",
   "img/pok/poliwag.png","img/pok/poliwhirl.png","img/pok/poliwrath.png",#160poliwag
   "img/pok/ponyta.png","img/pok/porygon.png","img/pok/porygon2.png","img/pok/primeape.png",
   "img/pok/psyduck.png","img/pok/pupitar.png","img/pok/quagsire.png",
   "img/pok/quilava.png","img/pok/qwilfish.png","img/pok/raichu.png",#170quilava
   "img/pok/raikou.png","img/pok/rapidash.png","img/pok/raticate.png",
   "img/pok/rattata.png","img/pok/remoraid.png","img/pok/rhydon.png",
   "img/pok/rhyhorn.png","img/pok/sandshrew.png","img/pok/sandslash.png",#180sandshrew
   "img/pok/scizor.png","img/pok/scyther.png","img/pok/seadra.png","img/pok/seaking.png",
   "img/pok/seel.png","img/pok/sentret.png","img/pok/shellder.png",
   "img/pok/shukle.png","img/pok/skarmory.png","img/pok/skiploom.png",#190skarmory
   "img/pok/slowbro.png","img/pok/slowking.png","img/pok/slowpoke.png",
   "img/pok/slugma.png","img/pok/smeargle.png","img/pok/smoochum.png",
   "img/pok/sneasel.png","img/pok/snorlax.png","img/pok/snubbull.png",#200snubbull
   "img/pok/spearow.png","img/pok/spinarak.png","img/pok/squirtle.png",
   "img/pok/stantler.png","img/pok/starmie.png","img/pok/staryu.png",
   "img/pok/steelix.png","img/pok/sudowoodo.png","img/pok/suicune.png",
   "img/pok/sunflora.png","img/pok/sunkern.png",#210sunflora
   "img/pok/swinub.png","img/pok/tangela.png","img/pok/tauros.png",
   "img/pok/teddiursa.png","img/pok/tentacool.png","img/pok/tentacruel.png",
   "img/pok/togepi.png","img/pok/togetic.png",
   "img/pok/totodile.png","img/pok/typhlosion.png","img/pok/tyranitar.png",#220_totodile
   "img/pok/tyrogue.png","img/pok/umbreon.png","img/pok/unown.png",
   "img/pok/ursaring.png",
   "img/pok/vaporeon.png",
   "img/pok/venomoth.png","img/pok/venonat.png","img/pok/venusaur.png",#230 venus
   "img/pok/victreebel.png","img/pok/vileplume.png","img/pok/voltorb.png",
   "img/pok/vulpix.png","img/pok/wartortle.png","img/pok/weedle.png",
   "img/pok/weepinbell.png","img/pok/weezing.png","img/pok/wigglytuff.png",
   "img/pok/wobbuffet.png",#240wobbuffet
   "img/pok/wooper.png","img/pok/wurmple.png","img/pok/wynaut.png","img/pok/xatu.png","img/pok/yanma.png",
   "img/pok/zangoose.png",
   "img/pok/zapdos.png","img/pok/zigzagoon.png","img/pok/zubat.png"]#249zub
for img in pokemon_list:
	pokemon_images.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())


pokemon_type_list1 = [12,13,5,0,12,3,8,6,16,6,10, 10,9,0,10,6,6,12,0,8,8, 8,9,14,14,14,9,9,3,9,4,#30v
                      8, 16,9,4,0,0,0,4,17,17, 17,12,4,0,0,3,11,11,11,8, 12,10,10,0,0,9,11,8,6,0,#60v
                      7,7,5,0,4,10,3,9,9,5, 14,5,3,8,9,7,6,1,1,1, 0,10,9,13,13,8,12,0,10,0,#90v 
                      11,10,16,5,5,12,6,0,9,9, 3,9,9,9,5,6,0,12,1,1, 1,8,8,9,8,11,11,1,9,11,#120v 
                      9,4,10,0,6,12,12,0,7,8, 12,3,13,12,3,3,3,3,3,3, 8,0,9,10,5,5,5,6,6,0,#150v
                      4,11,0,0,0,11,16,6,9,9, 9,9,8,0,0,1,9,5,9,8, 9,11,11,8,0,0,9,4,4,4,#180v
                      4,6,6,9,9,9,0,9,6,15, 10,9,9,9,8,0,16,13,0,14, 0,6,9,0,9,9, 15,5,9,10,#210v
                      10,16,10,0,0,9,9,14,14,9, 8,5,1,13,12,0,9,6,6,10, 10,10,11,8,9,6,10,3,0,12, #240v
                      9,6,12,12,6,0,11,0,3]#249v
#0..normal    1..lucha    2..volador   3..veneno   4..tierra   5..roca   6..bicho
#7..fantasma   8..fuego   9..agua   10..planta   11..electrico   12..psiquico
#13..siniestro   14..hada   15..acero   16..hielo   17..dragon
pokemon_type_list2 = [None,None,2,None,None,None,None,3,2,3,None, 3,None,None,3,2,None,10,None,2,None,#20v
                      None,11,None,None,None,16,5,2,None,None, None,2,16,None,None,2,2,None,None,2,#40v
                      None,None,None,None,None,None,None,None,None,None, None,12,12,2,2,None,None,None,15,None,#60v
                      3,3,4,12,2,3,2,None,None,4, None,4,None,None,2,3,1,None,None,None,#80v
                      2,2,None,8,8,2,None,14,3,14, None,2,12,9,9,None,3,None,17,None,#100v
                      None,None,11,16,4,2,None,2,None,None, None,None,5,None,None,15,15,None,2,None,#120v
                      14,None,None,None,None,None,None,None,None,2, 14,None,2,2,4,4,None,None,None,None,#140v
                      None,2,None,3,9,9,4,10,10,None, None,None,2,2,2,None,4,None,None,None,#160
                      None,1,None,None,None,None,None,4,4,None, 3,None,None,None,None,None,None,5,5,None,#180v
                      None,15,2,None,None,None,None,None,5,2, 2,12,12,12,None,None,12,16,None,None,#200v
                      2,3,None,None,12,None,4,None,None,None, None,4,None,None,None,3,3,None,2,None,#220v
                      None,13,None,None,None,None,None,3,3,3, 3,3,None,None,None,3,3,None,14,None,#240v
                      4,None,None,2,2,None,2,None,2]#249v

class Arrow(pygame.sprite.Sprite):
   def __init__(self):
         super().__init__()
         self.image = pygame.image.load("img/flechas/flecha_negra.png")
         self.rect = self.image.get_rect()
         self.rect.topleft = 320,439

   def update(self):
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
               self.rect.top = 439
            if event.key == pygame.K_s:
               self.rect.top = 486
            if event.key == pygame.K_a:
               self.rect.left = 320
            if event.key == pygame.K_d:
               self.rect.left = 465

"""
"""
pokemon_hp = [50,70,80,70,80,70,70,50,120,82,90,85,85,270,74,70,60,130,259,67,73,70,103,103,97,90,100,87,80,90,
              #17chansey,fin28              
              84,75,71,120,56,85,70,62,70,72,70,75,70,50,100,89,72,60,65,70,80,80,90,105,77,90,90,
              #44eevee,fin54
              108,90,120,90,58,90,68,100,90,75,100,80,110,110,85,90,90,75,90,80,90,80,
              #60gastly,62geodude,fin77hitmonchan
              80,80,70,60,89,80,72,140,79,150,90,177,70,90,80,70,70,70,90,100,90,70,70,60,100,100,83,89,100,
              #89jigg,106finlicki
              130,70,65,90,70,65,110,80,52,80,70,90,93,150,70,100,87,120,90,100,90,68,120,70,90,73,70,110,110,
              #107lugia130,108machamp70,115magnemit52,120marill150,123meowth87,fin135_110nidoqueen
              89,98,90,90,75,100,90,71,55,90,68,68,70,85,110,70,95,93,92,74,100,80,100,82,90,100,
              #136nidoran1_89,140ninetales75,147paras68,150phanp110,157pineco80,159poliwag82,161poliwhrat100
              70,90,90,80,80,90,95,90,75 ,80,110,80,90,74,74,100,90,74,100,95,75,100,100,110,80,65,
              #162ponyta70,169quilava90,173raticate90,179sandsdrew75,180sands100,finshellder187
              100,100,100,90,90,110,80,120,70,65,120, 85,82,85,80,90,80,70,95,75,100,80,70,99,80,90,80,77,100,
              #188shukle100,191slowbro90,193slowpoke110,198snorlax120,199snubbull85,200spearow82,203stantler90,210sunkern70,fin216tentacruel
              80,83,80,95,120,80,100,75,120,130,78,90,95,100,100,75,80,110,60,90,100,150,220,
              #217togepi,223umbreon100,229venusaur95,234wartortle,fin240wobb
              112,100,150,66,80,74,120,100,92]
              #241woop,242wurmple,243wynaut,244xatu,245yanma,246zangoose,247zapdos,248zigzagoon,249zubat

tipo_ataque_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def show_game_over_screenp1():
   screen.fill(BLACK)
   draw_text1(screen, "YOU WIN", 20, ancho // 2, alto // 2)
   draw_text1(screen, "Press Q", 20, ancho // 2, alto * 3/4)

   pygame.display.flip()
   waiting = True
   while waiting:
      clock.tick(60)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
               waiting = False

def show_game_over_screenp2():
   screen.fill(BLACK)
   draw_text1(screen, "CPU WINS", 20, ancho // 2, alto // 2)
   draw_text1(screen, "Press Q", 20, ancho // 2, alto * 3/4)

   pygame.display.flip()
   waiting = True
   while waiting:
      clock.tick(60)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
               waiting = False

matriz_efectividad = [
   #1N, 2L, 3V, 4V, 5T, 6R, 7B, 8F, 9F, 10A, 11P, 12E, 13P, 14S, 15H, 16A, 18D
   [0.5,  1,  1,  1,  1,  0.5,  1, 0.5,  1,  1,  1,  1,  1,  1,  1,  0.5,  1,  1],#1Normal

   [2, 0.5,  1, 0.5,  1,  2, 0.5, 0.5,  1,  1,  1,  1, 0.5,  2, 0.5,  2,  1,  1],#2lucha
   
   [1,  2, 0.5,  1,  1,  0.5,  2,  1,  1,  1,  2, 0.5,  1,  1,  1,  0.5,  1,  1],#3volador
   
   [1,  1,  1, 0.5, 0.5,  0.5,  1,  1,  1,  1,  2,  1,  1,  1,  2,  0.5,  1,  1],#4veneno
   
   [1,  1,  1,  2, 0.5, 2, 0.5,  1,  2,  1,  0.5,  2,  1,  1,  1,  2,  1,             1],#5tierra
   
   [1, 0.5,  2,  1, 0.5, 0.5,  2,  1,  2,  1,  1,  1,  1,  1,  1,  0.5,  1,            1],#6roca
   
   [1, 0.5,  1, 0.5,  1,  1, 0.5,  1, 0.5,  1,  2,  1,  2,  2, 0.5,  0.5,  1,          1],#7bicho
   
   [0.5,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  2, 0.5,  1,  1,  1,           1],#8fantasma
   
   [1,  1,  1,  1,  1,  0.5,  2,  1, 0.5, 0.5,  2,  1,  1,  1,  1,  2,  1,         0.5],#9fuego
   
   [1,  1,  1,  2,  2,  2,  1,  1,  2, 0.5, 0.5,  1,  1,  1,  1,  2,  1,           0.5],#10agua
   
   [1,  1,  1, 0.5,  2,  2, 0.5,  1, 0.5, 2, 0.5,  1,  1,  1,  1,  1,  1,           0.5],#11planta
   
   [1,  1,  1, 0.5,  0.5,  1,  1,  1,  1,  2, 0.5, 0.5,  1,  1,  1,  1,  1,           0.5],#12electrico
   
   [1,  2,  1,  2,  1,  1,  1,  1,  1,  1,  1,  1, 0.5, 0.5,  1,  0.5,  1,             1],#13psiquico
   
   [1, 0.5,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2, 0.5, 0.5,  1,  1,            1],#14siniestro
   
   [1,  2,  1, 0.5,  1,  1,  1,  1, 0.5,  1,  1,  1,  1,  2,  1, 0.5,  1,  2],#15hada
   
   [1,  1,  1,  1,  1,  2,  1,  1, 0.5, 0.5,  1, 0.5,  1,  1,  2,  0.5,  1,  1],#16acero
   
   [1,  1,  1,  2,  2,  1,  1,  1, 0.5, 0.5,  2,  1,  1,  1,  1,  0.5,  0.5,  2],#17hielo
   
   [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.5,  0.5,  1,  2],#18dragon
]

def damage(atacante,defensor):
#   poder_de_ataque = atacante.poder_de_ataque
   tipo_atacante = pokemon_type_list1[atacante.img_int]
   tipo_defensor1 = pokemon_type_list1[defensor.img_int]
   tipo_defensor2 = pokemon_type_list2[defensor.img_int]


   efectividad_total = 1
   if tipo_defensor2 is not None:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor2]
   else:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]

   daño = 6*efectividad_total
   return daño


player_pokemon_list = []
op_pokemon_list = []

fighting = True
battle = False

carga1 = True
carga2 = True
counter_battle = True
game_over1 = False
game_over2 = False
player_pokemon_hp = 0
op_pokemon_hp = 0

all_sprites = pygame.sprite.Group()

start_time = 0

# pokemon = Pokemon(210,1)
# all_sprites.add(pokemon)
while fighting:
   clock.tick(60)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      for pok in all_sprites:
         if pok.team_int == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
               if pygame.time.get_ticks() - pok.ultimo_ataque > pok.tiempo_entre_ataques:
                  for poke in all_sprites:
                     if poke.team_int == 1:
                        poke.hp -= damage(pok,poke)
                        pok.ultimo_ataque = pygame.time.get_ticks()

   if game_over1:
      game_over1 = False
      show_game_over_screenp1()
      carga1 = True


   if game_over2:
      game_over2 = False
      show_game_over_screenp2()
      carga1 = True




   if carga1:
      carga1 = False
      all_sprites.empty()
      player_pokemon_list = []
      op_pokemon_list = []
      pokemon1 = Pokemon(randint(0,200),0)
      player_pokemon_list.append(pokemon1)
      all_sprites.add(pokemon1)
      player_pokemon_hp = pokemon1.hp
      #energia_max_pok1 = player_pokemon_list[0]
      pokemon2 = Pokemon(randint(0,200),0)
      player_pokemon_list.append(pokemon2)
      pokemon3 = Pokemon(randint(0,200),0)
      player_pokemon_list.append(pokemon3)
      pokemon4 = Pokemon(randint(0,200),1)
      op_pokemon_list.append(pokemon4)
      all_sprites.add(pokemon4)
      op_pokemon_hp = pokemon4.hp
      #energia_max_pok2 = op_pokemon_list[0]
      pokemon5 = Pokemon(randint(0,200),1)
      op_pokemon_list.append(pokemon5)
      pokemon6 = Pokemon(randint(0,200),1)
      op_pokemon_list.append(pokemon6)

   if len(player_pokemon_list) != 0 and len(op_pokemon_list) != 0:
      if len(all_sprites) < 2:
         for pok in all_sprites:
            if pok.team_int == 0:
               all_sprites.add(random.choice(op_pokemon_list))
               for poke in all_sprites:
                  if poke.team_int == 1:
                     op_pokemon_hp = poke.hp
            else:
               all_sprites.add(random.choice(player_pokemon_list))
               for pokem in all_sprites:
                  if pokem.team_int == 0:
                     player_pokemon_hp = pokem.hp
   #print(len(player_pokemon_list))
   if len(player_pokemon_list) == 0 or len(op_pokemon_list) == 0:
      if len(player_pokemon_list) == 0:
         game_over2 = True
      else:
         game_over1 = True



   screen.fill(BLACK)
   all_sprites.update()
   all_sprites.draw(screen)
   for pok in all_sprites:
      if pok.team_int == 0:
         draw_hp_bar(screen,pok.rect.x,pok.rect.y,(pok.hp/(player_pokemon_hp))*100)
         draw_text2(screen,f"{int(pok.hp)}/{player_pokemon_hp}",10,pok.rect.centerx,pok.rect.y)
      else:
         draw_hp_bar(screen,pok.rect.x,pok.rect.y,(pok.hp/op_pokemon_hp)*100)
         draw_text2(screen,f"{int(pok.hp)}/{op_pokemon_hp}",10,pok.rect.centerx,pok.rect.y)
   pygame.display.update()


"""
pokemon_name_list = ["abomasnow",
                     "abra","absol","accelgor","aerodactyl","aggron","aipom","alakazam","alomomola",
                     "altaria","amaura","ambipom","amoongus","ampharos","anorith","applin","araquanid",
                     "arbok","arboliva","arcanine","archen","archeops","ariados","armaldo","aron",
                     "articuno","audino","aurorus","avalugg","axew","azumarill","bagon","baltoy",
                     "banette","barbaracle","barboach","basculin","bastiodon","baxcalibur","bayleef",
                     "beartic","beautifly","beedrill","beheeyem","beldum","bellibolt","bellossom",
                     "bellsprout","bergmite","bewear","bibarel","bidoof","binacle","bisharp",
                     "blastoise","blaziken","blissey","blitzle","boldore","bombirdier","bonsly",
                     "bounsweet","braviary","breloom","bronzong","bronzor","bruxish","budew",
                     "buizel","bulbasaur","buneary","bunnelby","burmy","butterfree","cacnea",
                     "cacturne","camerupt","carbink","carracosta","carvanha","castform","caterpi",
                     "cetitan","chandelure","chansey","charcadet","charizard","charhabug","charmander",
                     "charmeleon","chatot","cherrim","cherubi","chesnaught","chikorita","chimchar",
                     "chimecho","chinchou","chingling","cinccino","cinderace","clamperi","clauncher",
                     "clawitzer","claydol","clefable","clefairy","cleffa","clodsire","cloyster",
                     "cobalion","cofagrigus","combee","combusken","conkeldurr","corphish","corsola",
                     "corviknight","cottonee","crabrawler","cradily","cranidos","crawdaunt",
                     "cresselia","croagunk","crobat","croconaw","crustle","cryogonal","cubchoo",
                     "cubone","cutiefly","cyndaquil","darkrai","darmanitan","dartrix","darumaka",
                     "decidueye","dedenne","deerling","deino","delcatty","delibird","delphox","dewong",
                     "dewpider","dialga","diancie","diglett","ditto","dodrio","doduo","donphan",
                     "dragalge","dragonair","dragonite","drampa","drapion","dratini","dreepy",
                     "drifblim","drifloon","drilbur","drizzile","drowzee","druddigon","dubwool",
                     "ducklett","dugtrio","dunsparce","durant","dusclops","dusknoir","duskull",
                     "dustox","dwebble","elektross","eevee","ekans","electabuzz","electrike",
                     "electrode","elekid","elgyem","entei","emboar","emolga","empoleon","escavalier",
                     "espeon","espurr","excadrill","exeggcute","exeggutor","exploud","falinks",
                     "farfetch'd","fearow","fennekin","feraligatr","ferroseed","ferrothorn",
                     "fidough","finneon","flaaffy","flabebe","flareon","fletchling","floatzel",
                     "floette","floragato","flygon","fomantis","foongus","forretress","frigibax",
                     "frillish","froakie","fuecoco","furfrou","furret","gabite","galvantula",
                     "garbodor","garchomp","gardevoir","gastly","genesect","gengar","geodude",
                     "gible","gigalith","girafarig","giratina","glaceon","glalie","glameow","gligar",
                     "gliscor","gloom","golbat","goldeen","golduck","golem","golett","golisopod",
                     "golurk","goodra","goomy","gossifleur","gothita","gourgeist","grandbull",
                     "graveler","greavard","greedent","greninja","grimer","grookey","groudon",
                     "grovyle","growlithe","grubbin","grumpig","gulpin","gumshoos","gurdurr",
                     "guzzlord","gyarados","happiny","hariyama","hatenna","haunter","haxorus",
                     "heatmor","heatran","heliolisk","helioptile","heracross","hitmonchan","hitmonlee","hitmontop","hoothoot",
   "hoppip","horsea","houndoom","houndour","hypno","ivysaur","jigglypuff","jolteon","jumpluff",
   "jynx","kabutops","kadabra","kakuna","kangaskhan","kingdra","kingler","koffing","krabby","lapras",
   "larvitar","img/pok/ledian.png","ledyba","lickitung","machamp","machoke","machop","magby","magcargo","magikarp","magmar",
   "magnemite","magneton","mantine","marill","marowak","meowth","metapod","miltank","misdreavus",
   "monkey","mr.mime","muk","murkrow","natu","nidoking","nidoqueen","nidoran1","nidoran2","nidorina",
   "nidorino","ninetales","noctowl","oddish","omastar","onix","paras","parasect","persian","phanpy",
   "pidgeot","pidgeotto","pidgey","pikachu","piloswine","pineco","politoed","poliwag","poliwhirl",
   "poliwrath","ponyta","porygon","primeape","psyduck","pupitar","quagsire","quilava","qwilfish",
   "raichu","rapidash","raticate","rattata","raikou","remoraid","rhydon","rhyhorn",
   "sandshrew.png","sandslash","scyther","seadra","seaking","seel","sentret","shellder","skarmory",
   "skiploom","slowbro","slowking","slowpoke","slugma","sneasel","snorlax","snubbull","spearow",
   "spinarak","squirtle","stantler","/starmie","staryu","steelix","sudowoodo","sunkern","swinub",
   "tauros","teddiursa","tentacool","tentacruel","togepi","totodile","typhlosion","tyranitar",
   "umbreon","ursaring","vaporeon","venomoth","venonat","venusaur","victreebel","vileplume",
   "voltorb","vulpix","wartortle","weedle","weepinbell","weezing.","wigglytuff",
   "wooper.png","xatu","yanma","zubat.png"
      ]

      #82jigg177,83jolt70,84jumpluff90,85jynx80,86kabut70,87kada70,88kakuna70,89kang90,90kingdra100,
#91kingler90,92koffing70,93krabb70,94lapras100, 60,95larvitar80,96
#82
#77porygon, +101caterpc344, 76spearow470, 63shelder, 100seel,79hypno, 89eevee, 92pidgey, 82sandygast, 
# 90rhyhorn489,1*, 90venonat, 95noibat, 89luv(pezrosa),lunatone87,sableye70,0*, absol57,0*,phantum75,
#stufful89,2*,seviper74, omanyte58,snubbull85,
"""