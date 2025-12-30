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
YELLOW = (255,255,0)


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

def draw_hp_bar2(surface, x, y, percentage):
   BAR_LENGHT = 200
   BAR_HEIGHT = 10
   fill = (percentage / 100) * BAR_LENGHT
   border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
   fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
   pygame.draw.rect(surface, YELLOW, fill)
   pygame.draw.rect(surface, WHITE, border, 2)

def draw_hp_bar3(surface, x, y, percentage):
   BAR_LENGHT = 200
   BAR_HEIGHT = 10
   fill = (percentage / 100) * BAR_LENGHT
   border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
   fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
   pygame.draw.rect(surface, RED, fill)
   pygame.draw.rect(surface, WHITE, border, 2)



class Pokemon(pygame.sprite.Sprite):
   def __init__(self,reg_int,team_int,img_int = None,pc=500):
      super().__init__()
      self.reg_int = reg_int
      self.img_int = img_int
      if reg_int == 0:
         self.img_int = randint(0,150)
         self.image = pokemon_images_kanto[self.img_int]
         self.type1 = pokemon_type_kanto1[self.img_int]
         self.type2 = pokemon_type_kanto2[self.img_int]
         self.hp = pokemon_hp_kanto[self.img_int]
         self.defense = pokemon_defense_kanto[self.img_int]
         self.attack = pokemon_attack_kanto[self.img_int]
      elif reg_int == 1:
         self.img_int = randint(0,99)
         self.image = pokemon_images_johto[self.img_int]
         self.type1 = pokemon_type_johto1[self.img_int]
         self.type2 = pokemon_type_johto2[self.img_int]
         self.hp = pokemon_hp_johto[self.img_int]
         self.defense = pokemon_defense_johto[self.img_int]
         self.attack = pokemon_attack_johto[self.img_int]
      elif reg_int == 2:
         self.img_int = randint(0,134)
         self.image = pokemon_images_hoenn[self.img_int]
         self.type1 = pokemon_type_hoenn1[self.img_int]
         self.type2 = pokemon_type_hoenn2[self.img_int]
         self.hp = pokemon_hp_hoenn[self.img_int]
         self.defense = pokemon_defense_hoenn[self.img_int]
         self.attack = pokemon_attack_hoenn[self.img_int]
      elif reg_int == 3:
         self.img_int = randint(0,106)
         self.image = pokemon_images_sinnoh[self.img_int]
         self.type1 = pokemon_type_sinnoh1[self.img_int]
         self.type2 = pokemon_type_sinnoh2[self.img_int]
         self.hp = pokemon_hp_sinnoh[self.img_int]
         self.defense = pokemon_defense_sinnoh[self.img_int]
         self.attack = pokemon_attack_sinnoh[self.img_int]
      elif reg_int == 4:
         self.img_int = randint(0,155)
         self.image = pokemon_images_teselia[self.img_int]
         self.type1 = pokemon_type_teselia1[self.img_int]
         self.type2 = pokemon_type_teselia2[self.img_int]
         self.hp = pokemon_hp_teselia[self.img_int]
         self.defense = pokemon_defense_teselia[self.img_int]
         self.attack = pokemon_attack_teselia[self.img_int]
      elif reg_int == 5:
         self.img_int = randint(0,71)
         self.image = pokemon_images_kalos[self.img_int]
         self.type1 = pokemon_type_kalos1[self.img_int]
         self.type2 = pokemon_type_kalos2[self.img_int]
         self.hp = pokemon_hp_kalos[self.img_int]
         self.defense = pokemon_defense_kalos[self.img_int]
         self.attack = pokemon_attack_kalos[self.img_int]
      elif reg_int == 6:
         self.img_int = randint(0,105)
         self.image = pokemon_images_alola[self.img_int]
         self.type1 = pokemon_type_alola1[self.img_int]
         self.type2 = pokemon_type_alola2[self.img_int]
         self.hp = pokemon_hp_alola[self.img_int]
         self.defense = pokemon_defense_alola[self.img_int]
         self.attack = pokemon_attack_alola[self.img_int]
      else:
         raise ValueError("img_int fuera de rango")
      #self.image.set_colorkey(WHITE)
      self.rect = self.image.get_rect()
      self.team_int = team_int
      if self.team_int == 0:
         self.rect.bottomleft = 200,450
      else:
         self.rect.bottomleft = 600,250

      self.pc = pc
      self.ultimo_ataque = 0
      self.tiempo_entre_ataques = 1100#milisegs
      self.speed = 0

   def update(self):
      if self.team_int == 1:
         for pok in all_sprites:
            if pok.team_int == 0:
               if pygame.time.get_ticks() - self.ultimo_ataque > self.tiempo_entre_ataques:
                  pok.hp -= damage(op_pokemon_type_attack,self.attack,pok)
                  self.ultimo_ataque = pygame.time.get_ticks()
      else:
         for poke in all_sprites:
            if poke.team_int == 1:
               if pygame.time.get_ticks() - self.ultimo_ataque > self.tiempo_entre_ataques:
                  poke.hp -= damage(player_pokemon_type_attack,self.attack,poke)
                  self.ultimo_ataque = pygame.time.get_ticks()
               
            

      if self.hp <= 0:
         if self.team_int ==0:
            player_pokemon_list.remove(self)
            pokeball1.int -= 1
         else:
            op_pokemon_list.remove(self)
            pokeball2.int -= 1
            
         self.kill()

class Type(pygame.sprite.Sprite):
   def __init__(self,img_int,x,y,team_int,scx,scy):
      super().__init__()
      self.img_int = img_int
      if 0 <= img_int < len(type_images):
         self.image = pygame.transform.scale(type_images[img_int],(scx,scy))
         #self.image.set_colorkey(WHITE)
      else:
         raise ValueError("img_int fuera de rango")

      self.rect = self.image.get_rect()
      self.team_int = team_int
      self.rect.x = x
      self.rect.y = y

class Pokeball(pygame.sprite.Sprite):
   def __init__(self,team_int,img_int):
      super().__init__()
      self.int = img_int
      self.image1 = pygame.image.load("img/text/1.png")
      self.image2 = pygame.image.load("img/text/2.png")
      self.image3 = pygame.image.load("img/text/3.png")
      self.image = pygame.image.load("img/text/3.png")
      
      self.image.set_colorkey(WHITE)
      self.rect = self.image.get_rect()
      self.team_int = team_int
      if self.team_int == 0:
         self.rect.topright = 355,220
      else:
         self.rect.topright = 755,20

   def update(self):
      if self.int == 2:
         self.image = self.image2
      if self.int == 1:
         self.image = self.image1
      self.image.set_colorkey(WHITE)



pokemon_images_kanto = []
pokemon_list_kanto = [
   "img/pok/kanto/bulbasaur.png","img/pok/kanto/ivysaur.png","img/pok/kanto/venusaur.png",
   "img/pok/kanto/charmander.png","img/pok/kanto/charmeleon.png","img/pok/kanto/charizard.png",
   "img/pok/kanto/squirtle.png","img/pok/kanto/wartortle.png","img/pok/kanto/blastoise.png",
   "img/pok/kanto/caterpie.png","img/pok/kanto/metapod.png","img/pok/kanto/butterfree.png", #10 metap
   "img/pok/kanto/weedle.png","img/pok/kanto/kakuna.png","img/pok/kanto/beedrill.png",
   "img/pok/kanto/pidgey.png","img/pok/kanto/pidgeotto.png","img/pok/kanto/pidgeot.png",
   "img/pok/kanto/rattata.png","img/pok/kanto/raticate.png","img/pok/kanto/spearow.png", #20 spearow
   "img/pok/kanto/fearow.png","img/pok/kanto/ekans.png","img/pok/kanto/arbok.png",
   "img/pok/kanto/pikachu.png","img/pok/kanto/raichu.png","img/pok/kanto/sandshrew.png",
   "img/pok/kanto/sandslash.png","img/pok/kanto/nidoran1.png","img/pok/kanto/nidorino.png",
   "img/pok/kanto/nidoking.png","img/pok/kanto/nidoran2.png","img/pok/kanto/nidorina.png", #30 nidoking
   "img/pok/kanto/nidoqueen.png","img/pok/kanto/clefairy.png","img/pok/kanto/clefable.png",
   "img/pok/kanto/vulpix.png","img/pok/kanto/ninetales.png","img/pok/kanto/jigglypuff.png",
   "img/pok/kanto/wigglytuff.png","img/pok/kanto/zubat.png","img/pok/kanto/golbat.png", #40 zubat
   "img/pok/kanto/oddish.png","img/pok/kanto/gloom.png","img/pok/kanto/vileplume.png",
   "img/pok/kanto/paras.png","img/pok/kanto/parasect.png","img/pok/kanto/venonat.png",
   "img/pok/kanto/venomoth.png","img/pok/kanto/diglett.png","img/pok/kanto/dugtrio.png", #50 dugtrio
   "img/pok/kanto/meowth.png","img/pok/kanto/persian.png","img/pok/kanto/psyduck.png",
   "img/pok/kanto/golduck.png","img/pok/kanto/mankey.png","img/pok/kanto/primeape.png",
   "img/pok/kanto/growlithe.png","img/pok/kanto/arcanine.png","img/pok/kanto/poliwag.png", 
   "img/pok/kanto/poliwhirl.png","img/pok/kanto/poliwrath.png","img/pok/kanto/abra.png", #60 poliwhi
   "img/pok/kanto/kadabra.png","img/pok/kanto/alakazam.png","img/pok/kanto/machop.png",
   "img/pok/kanto/machoke.png","img/pok/kanto/machamp.png","img/pok/kanto/bellsprout.png",
   "img/pok/kanto/weepinbell.png","img/pok/kanto/victreebel.png","img/pok/kanto/tentacool.png", #70 victr
   "img/pok/kanto/tentacruel.png","img/pok/kanto/geodude.png","img/pok/kanto/graveler.png",
   "img/pok/kanto/golem.png","img/pok/kanto/ponyta.png","img/pok/kanto/rapidash.png",
   "img/pok/kanto/slowpoke.png","img/pok/kanto/slowbro.png","img/pok/kanto/magnemite.png", # 80 magnemite
   "img/pok/kanto/magneton.png","img/pok/kanto/farfetchd.png","img/pok/kanto/doduo.png",
   "img/pok/kanto/dodrio.png","img/pok/kanto/seel.png","img/pok/kanto/dewgong.png",
   "img/pok/kanto/grimer.png","img/pok/kanto/muk.png","img/pok/kanto/shellder.png",
   "img/pok/kanto/cloyster.png","img/pok/kanto/gastly.png","img/pok/kanto/haunter.png",  # 90 cloyster
   "img/pok/kanto/gengar.png","img/pok/kanto/onix.png","img/pok/kanto/drowzee.png",
   "img/pok/kanto/hypno.png","img/pok/kanto/krabby.png","img/pok/kanto/kingler.png",
   "img/pok/kanto/voltorb.png","img/pok/kanto/electrode.png","img/pok/kanto/exeggcute.png", # 100 electrode
   "img/pok/kanto/exeggutor.png","img/pok/kanto/cubone.png","img/pok/kanto/marowak.png",
   "img/pok/kanto/hitmonlee.png","img/pok/kanto/hitmonchan.png","img/pok/kanto/lickitung.png",
   "img/pok/kanto/koffing.png","img/pok/kanto/weezing.png","img/pok/kanto/rhyhorn.png", # 110 rhyhorn
   "img/pok/kanto/rhydon.png","img/pok/kanto/chansey.png","img/pok/kanto/tangela.png",
   "img/pok/kanto/kangaskhan.png","img/pok/kanto/horsea.png","img/pok/kanto/seadra.png",
   "img/pok/kanto/goldeen.png","img/pok/kanto/seaking.png","img/pok/kanto/staryu.png",
   "img/pok/kanto/starmie.png","img/pok/kanto/mrmime.png","img/pok/kanto/scyther.png", # 120 starmie
   "img/pok/kanto/jynx.png","img/pok/kanto/electabuzz.png","img/pok/kanto/magmar.png",
   "img/pok/kanto/pinsir.png","img/pok/kanto/tauros.png","img/pok/kanto/magikarp.png",
   "img/pok/kanto/gyarados.png","img/pok/kanto/lapras.png","img/pok/kanto/ditto.png", # 130 lapras
   "img/pok/kanto/eevee.png","img/pok/kanto/vaporeon.png","img/pok/kanto/jolteon.png",
   "img/pok/kanto/flareon.png","img/pok/kanto/porygon.png","img/pok/kanto/omanyte.png",
   "img/pok/kanto/omastar.png","img/pok/kanto/kabuto.png","img/pok/kanto/kabutops.png", # 140 kabutops
   "img/pok/kanto/aerodactyl.png","img/pok/kanto/snorlax.png","img/pok/kanto/articuno.png",
   "img/pok/kanto/zapdos.png","img/pok/kanto/moltres.png","img/pok/kanto/dratini.png",
   "img/pok/kanto/dragonair.png","img/pok/kanto/dragonite.png","img/pok/kanto/mewtwo.png",
   "img/pok/kanto/mew.png"           # 150 mew
                ]
for img in pokemon_list_kanto:
	pokemon_images_kanto.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_johto = []
pokemon_list_johto = [
   "img/pok/johto/chikorita.png","img/pok/johto/bayleef.png","img/pok/johto/meganium.png",
   "img/pok/johto/cyndaquil.png","img/pok/johto/quilava.png","img/pok/johto/typhlosion.png",
   "img/pok/johto/totodile.png","img/pok/johto/croconaw.png","img/pok/johto/feraligatr.png",
   "img/pok/johto/sentret.png","img/pok/johto/furret.png","img/pok/johto/hoothoot.png", # 10 furret
   "img/pok/johto/noctowl.png","img/pok/johto/ledyba.png","img/pok/johto/ledian.png",
   "img/pok/johto/spinarak.png","img/pok/johto/ariados.png","img/pok/johto/crobat.png",
   "img/pok/johto/chinchou.png","img/pok/johto/lanturn.png","img/pok/johto/pichu.png", # 20 pichu
   "img/pok/johto/cleffa.png","img/pok/johto/igglybuff.png","img/pok/johto/togepi.png",
   "img/pok/johto/togetic.png","img/pok/johto/natu.png","img/pok/johto/xatu.png",
   "img/pok/johto/mareep.png","img/pok/johto/flaaffy.png","img/pok/johto/ampharos.png",
   "img/pok/johto/bellossom.png","img/pok/johto/marill.png","img/pok/johto/azumarill.png", # 30 bellosom
   "img/pok/johto/sudowoodo.png","img/pok/johto/politoed.png","img/pok/johto/hoppip.png",
   "img/pok/johto/skiploom.png","img/pok/johto/jumpluff.png","img/pok/johto/aipom.png",
   "img/pok/johto/sunkern.png","img/pok/johto/sunflora.png","img/pok/johto/yanma.png", # 40 sunflora
   "img/pok/johto/wooper.png","img/pok/johto/quagsire.png","img/pok/johto/espeon.png",
   "img/pok/johto/umbreon.png","img/pok/johto/murkrow.png","img/pok/johto/slowking.png",
   "img/pok/johto/misdreavus.png","img/pok/johto/unown.png","img/pok/johto/wobbuffet.png", # 50 wobbuffet
   "img/pok/johto/girafarig.png","img/pok/johto/pineco.png","img/pok/johto/forretress.png",
   "img/pok/johto/dunsparce.png","img/pok/johto/gligar.png","img/pok/johto/steelix.png",
   "img/pok/johto/snubbull.png","img/pok/johto/granbull.png","img/pok/johto/qwilfish.png",
   "img/pok/johto/scizor.png","img/pok/johto/shukle.png","img/pok/johto/heracross.png", #60 scizor
   "img/pok/johto/sneasel.png","img/pok/johto/teddiursa.png","img/pok/johto/ursaring.png",
   "img/pok/johto/slugma.png","img/pok/johto/magcargo.png","img/pok/johto/swinub.png",
   "img/pok/johto/piloswine.png","img/pok/johto/corsola.png","img/pok/johto/remoraid.png", # 70 corsola
   "img/pok/johto/octillery.png","img/pok/johto/delibird.png","img/pok/johto/mantine.png",
   "img/pok/johto/skarmory.png","img/pok/johto/houndour.png","img/pok/johto/houndoom.png",
   "img/pok/johto/kingdra.png","img/pok/johto/phanpy.png","img/pok/johto/donphan.png", # 80 donphan
   "img/pok/johto/porygon2.png","img/pok/johto/stantler.png","img/pok/johto/smeargle.png",
   "img/pok/johto/tyrogue.png","img/pok/johto/hitmontop.png","img/pok/johto/smoochum.png",
   "img/pok/johto/elekid.png","img/pok/johto/magby.png","img/pok/johto/miltank.png",
   "img/pok/johto/blissey.png","img/pok/johto/raikou.png","img/pok/johto/entei.png", # 90 blissey
   "img/pok/johto/suicune.png","img/pok/johto/larvitar.png","img/pok/johto/pupitar.png",
   "img/pok/johto/tyranitar.png","img/pok/johto/lugia.png","img/pok/johto/ho-oh.png",
   "img/pok/johto/celebi.png",
         ]
for img in pokemon_list_johto:
	pokemon_images_johto.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_hoenn = []
pokemon_list_hoenn = [
   "img/pok/hoenn/treecko.png","img/pok/hoenn/grovyle.png","img/pok/hoenn/sceptille.png",
   "img/pok/hoenn/torchik.png","img/pok/hoenn/combusken.png","img/pok/hoenn/blaziken.png",
   "img/pok/hoenn/mudkip.png","img/pok/hoenn/marshtomp.png","img/pok/hoenn/swampert.png",
   "img/pok/hoenn/poochyena.png","img/pok/hoenn/mightyena.png","img/pok/hoenn/zigzagoon.png",# 10 mightyena
   "img/pok/hoenn/linoone.png","img/pok/hoenn/wurmple.png","img/pok/hoenn/silcoon.png",
   "img/pok/hoenn/beautifly.png","img/pok/hoenn/cascoon.png","img/pok/hoenn/dustox.png",
   "img/pok/hoenn/lotad.png","img/pok/hoenn/lombre.png","img/pok/hoenn/ludicolo.png",     # 20 ludicolo
   "img/pok/hoenn/seedot.png","img/pok/hoenn/nuzleaf.png","img/pok/hoenn/shiftry.png",
   "img/pok/hoenn/taillow.png","img/pok/hoenn/swellow.png","img/pok/hoenn/wingull.png",
   "img/pok/hoenn/pelipper.png","img/pok/hoenn/ralts.png","img/pok/hoenn/kirlia.png",
   "img/pok/hoenn/gardevoir.png","img/pok/hoenn/surskit.png","img/pok/hoenn/masquerain.png",#  30 gardevoir
   "img/pok/hoenn/shroomish.png","img/pok/hoenn/breloom.png","img/pok/hoenn/slakoth.png",
   "img/pok/hoenn/vigoroth.png","img/pok/hoenn/slaking.png","img/pok/hoenn/nincada.png",
   "img/pok/hoenn/ninjask.png","img/pok/hoenn/shedinja.png","img/pok/hoenn/whismur.png",# 40 shedinja
   "img/pok/hoenn/loudred.png","img/pok/hoenn/exploud.png","img/pok/hoenn/makuhita.png",
   "img/pok/hoenn/hariyama.png","img/pok/hoenn/azurill.png","img/pok/hoenn/nosepass.png",
   "img/pok/hoenn/skitty.png","img/pok/hoenn/delcatty.png","img/pok/hoenn/sableye.png",# 50 sableye
   "img/pok/hoenn/mawile.png","img/pok/hoenn/aron.png","img/pok/hoenn/lairon.png",
   "img/pok/hoenn/aggron.png","img/pok/hoenn/meditite.png","img/pok/hoenn/medicham.png",
   "img/pok/hoenn/electrike.png","img/pok/hoenn/manectric.png","img/pok/hoenn/plusle.png",
   "img/pok/hoenn/minum.png","img/pok/hoenn/volbeat.png","img/pok/hoenn/illumise.png",# 60 minum
   "img/pok/hoenn/roselia.png","img/pok/hoenn/gulpin.png","img/pok/hoenn/swalot.png",
   "img/pok/hoenn/carvanha.png","img/pok/hoenn/sharpedo.png","img/pok/hoenn/wailmer.png",
   "img/pok/hoenn/wailord.png","img/pok/hoenn/numel.png","img/pok/hoenn/camerupt.png",# 70 numel
   "img/pok/hoenn/torkoal.png","img/pok/hoenn/spoink.png","img/pok/hoenn/grumpig.png",
   "img/pok/hoenn/spinda.png","img/pok/hoenn/trapinch.png","img/pok/hoenn/vibrava.png",
   "img/pok/hoenn/flygon.png","img/pok/hoenn/cacnea.png","img/pok/hoenn/cacturne.png",# 80 cacturne
   "img/pok/hoenn/swablu.png","img/pok/hoenn/altaria.png","img/pok/hoenn/zangoose.png",
   "img/pok/hoenn/seviper.png","img/pok/hoenn/lunatone.png","img/pok/hoenn/solrock.png",
   "img/pok/hoenn/barboach.png","img/pok/hoenn/whiscash.png","img/pok/hoenn/corpish.png",
   "img/pok/hoenn/crawdaunt.png","img/pok/hoenn/baltoy.png","img/pok/hoenn/claydol.png",# 90 crawdaunt
   "img/pok/hoenn/lileep.png","img/pok/hoenn/cradily.png","img/pok/hoenn/anorith.png",
   "img/pok/hoenn/armaldo.png","img/pok/hoenn/feebas.png","img/pok/hoenn/milotic.png",
   "img/pok/hoenn/castform.png","img/pok/hoenn/kecleon.png","img/pok/hoenn/shuppet.png",# 100 kecleon
   "img/pok/hoenn/banette.png","img/pok/hoenn/duskull.png","img/pok/hoenn/dusclops.png",
   "img/pok/hoenn/tropius.png","img/pok/hoenn/chimecho.png","img/pok/hoenn/absol.png",
   "img/pok/hoenn/wynaut.png","img/pok/hoenn/snorunt.png","img/pok/hoenn/glalie.png",# 110 glalie
   "img/pok/hoenn/spheal.png","img/pok/hoenn/sealeo.png","img/pok/hoenn/walrein.png",
   "img/pok/hoenn/clamperl.png","img/pok/hoenn/huntail.png","img/pok/hoenn/gorebyss.png",
   "img/pok/hoenn/relicanth.png","img/pok/hoenn/luvdisc.png","img/pok/hoenn/bagon.png",
   "img/pok/hoenn/shelgon.png","img/pok/hoenn/salamence.png","img/pok/hoenn/beldum.png",# 120 shelgon
   "img/pok/hoenn/metang.png","img/pok/hoenn/metagross.png","img/pok/hoenn/regirock.png",
   "img/pok/hoenn/regice.png","img/pok/hoenn/registeel.png","img/pok/hoenn/latias.png",
   "img/pok/hoenn/latios.png","img/pok/hoenn/kyogre.png","img/pok/hoenn/groudon.png",# 130 kyogre
   "img/pok/hoenn/rayquaza.png","img/pok/hoenn/jirachi.png","img/pok/hoenn/deoxys.png"
                ]
for img in pokemon_list_hoenn:
	pokemon_images_hoenn.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_sinnoh = []
pokemon_list_sinnoh = [
   "img/pok/sinnoh/turtwig.png","img/pok/sinnoh/grotle.png","img/pok/sinnoh/torterra.png",
   "img/pok/sinnoh/chimchar.png","img/pok/sinnoh/monferno.png","img/pok/sinnoh/infernape.png",
   "img/pok/sinnoh/piplup.png","img/pok/sinnoh/prinplup.png","img/pok/sinnoh/empoleon.png",
   "img/pok/sinnoh/starly.png","img/pok/sinnoh/staravia.png","img/pok/sinnoh/staraptor.png",# 10 staravia
   "img/pok/sinnoh/bidoof.png","img/pok/sinnoh/bibarel.png","img/pok/sinnoh/kricketot.png",
   "img/pok/sinnoh/kricketune.png","img/pok/sinnoh/shinx.png","img/pok/sinnoh/luxio.png",
   "img/pok/sinnoh/luxray.png","img/pok/sinnoh/budew.png","img/pok/sinnoh/roserade.png",# 20 roserade
   "img/pok/sinnoh/cranidos.png","img/pok/sinnoh/rampardos.png","img/pok/sinnoh/shieldon.png",
   "img/pok/sinnoh/bastiodon.png","img/pok/sinnoh/burmy.png","img/pok/sinnoh/wormadam.png",
   "img/pok/sinnoh/mothim.png","img/pok/sinnoh/combee.png","img/pok/sinnoh/vespiquen.png",
   "img/pok/sinnoh/pachirisu.png","img/pok/sinnoh/buizel.png","img/pok/sinnoh/floatzel.png", # 30 parichisu
   "img/pok/sinnoh/cherubi.png","img/pok/sinnoh/cherrim.png","img/pok/sinnoh/shellos.png",
   "img/pok/sinnoh/gastrodon.png","img/pok/sinnoh/ambipom.png","img/pok/sinnoh/drifloon.png",
   "img/pok/sinnoh/drifblim.png","img/pok/sinnoh/buneary.png","img/pok/sinnoh/lopunny.png",# 40 buneary
   "img/pok/sinnoh/mismagius.png","img/pok/sinnoh/honchkrow.png","img/pok/sinnoh/glameow.png",
   "img/pok/sinnoh/purugly.png","img/pok/sinnoh/chingling.png","img/pok/sinnoh/stunky.png",
   "img/pok/sinnoh/skuntank.png","img/pok/sinnoh/bronzor.png","img/pok/sinnoh/bronzong.png", # 50 bronzong
   "img/pok/sinnoh/bonsly.png","img/pok/sinnoh/mimejr.png","img/pok/sinnoh/happiny.png",
   "img/pok/sinnoh/chatot.png","img/pok/sinnoh/spiritomb.png","img/pok/sinnoh/gible.png",
   "img/pok/sinnoh/gabite.png","img/pok/sinnoh/garchomp.png","img/pok/sinnoh/munchlax.png",
   "img/pok/sinnoh/riolu.png","img/pok/sinnoh/lucario.png","img/pok/sinnoh/hippopotas.png",# 60 riolu
   "img/pok/sinnoh/hippowdon.png","img/pok/sinnoh/skorupi.png","img/pok/sinnoh/drapion.png",
   "img/pok/sinnoh/croagunk.png","img/pok/sinnoh/toxicroak.png","img/pok/sinnoh/carnivine.png",
   "img/pok/sinnoh/finneon.png","img/pok/sinnoh/lumineon.png","img/pok/sinnoh/mantyke.png",# 70 lumineon
   "img/pok/sinnoh/snover.png","img/pok/sinnoh/abomasnow.png","img/pok/sinnoh/weavile.png",
   "img/pok/sinnoh/magnezone.png","img/pok/sinnoh/lickilicky.png","img/pok/sinnoh/rhyperior.png",
   "img/pok/sinnoh/tangrowth.png","img/pok/sinnoh/electivire.png","img/pok/sinnoh/magmortar.png",
   "img/pok/sinnoh/togekiss.png","img/pok/sinnoh/yanmega.png","img/pok/sinnoh/leafeon.png",
   "img/pok/sinnoh/glaceon.png","img/pok/sinnoh/gliscor.png","img/pok/sinnoh/mamoswine.png",
   "img/pok/sinnoh/porygon-z.png","img/pok/sinnoh/gallade.png","img/pok/sinnoh/probopass.png",
   "img/pok/sinnoh/dusknoir.png","img/pok/sinnoh/froslass.png","img/pok/sinnoh/rotom.png",
   "img/pok/sinnoh/uxie.png","img/pok/sinnoh/mesprit.png","img/pok/sinnoh/azelf.png",
   "img/pok/sinnoh/dialga.png","img/pok/sinnoh/palkia.png",
   "img/pok/sinnoh/heatran.png","img/pok/sinnoh/regigigas.png","img/pok/sinnoh/giratina.png",
   "img/pok/sinnoh/cresselia.png","img/pok/sinnoh/phione.png","img/pok/sinnoh/manaphy.png",
   "img/pok/sinnoh/darkrai.png","img/pok/sinnoh/shaymin.png","img/pok/sinnoh/arceus.png"
   ]
for img in pokemon_list_sinnoh:
	pokemon_images_sinnoh.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_teselia = []
pokemon_list_teselia = [
   "img/pok/teselia/victini.png","img/pok/teselia/snivy.png","img/pok/teselia/servine.png",
   "img/pok/teselia/serperior.png","img/pok/teselia/tepig.png","img/pok/teselia/pignite.png",
   "img/pok/teselia/emboar.png","img/pok/teselia/oshawott.png","img/pok/teselia/dewott.png",
   "img/pok/teselia/samurott.png","img/pok/teselia/patrat.png","img/pok/teselia/watchog.png",#10patrat
   "img/pok/teselia/lillipup.png","img/pok/teselia/herdier.png","img/pok/teselia/stoutland.png",
   "img/pok/teselia/purrloin.png","img/pok/teselia/liepard.png","img/pok/teselia/pansage.png",
   "img/pok/teselia/simisage.png","img/pok/teselia/pansear.png","img/pok/teselia/simisear.png",#20simisear
   "img/pok/teselia/panpour.png","img/pok/teselia/simipour.png","img/pok/teselia/munna.png",
   "img/pok/teselia/musharna.png","img/pok/teselia/pidove.png","img/pok/teselia/tranquill.png",
   "img/pok/teselia/unfezant.png","img/pok/teselia/blitzle.png","img/pok/teselia/zebstrika.png",
   "img/pok/teselia/roggenrola.png","img/pok/teselia/boldore.png","img/pok/teselia/gigalith.png",#30 roggenrola
   "img/pok/teselia/woobat.png","img/pok/teselia/swoobat.png","img/pok/teselia/drilbur.png",
   "img/pok/teselia/excadrill.png","img/pok/teselia/audino.png","img/pok/teselia/timburr.png",
   "img/pok/teselia/gurdurr.png","img/pok/teselia/conkeldurr.png","img/pok/teselia/tympole.png",#40 conkeldurr
   "img/pok/teselia/palpitoad.png","img/pok/teselia/seismitoad.png","img/pok/teselia/throh.png",
   "img/pok/teselia/sawk.png","img/pok/teselia/sewaddle.png","img/pok/teselia/swadloon.png",
   "img/pok/teselia/leavanny.png","img/pok/teselia/venipede.png","img/pok/teselia/whirlipede.png",#50 whirlipede
   "img/pok/teselia/scolipede.png","img/pok/teselia/coottonee.png","img/pok/teselia/whimsicott.png",
   "img/pok/teselia/petilil.png","img/pok/teselia/lilligant.png","img/pok/teselia/basculin.png",
   "img/pok/teselia/sandile.png","img/pok/teselia/krokorok.png","img/pok/teselia/krookodile.png",#60 darumka
   "img/pok/teselia/darumka.png","img/pok/teselia/darmanitan.png","img/pok/teselia/maractus.png",
   "img/pok/teselia/dwebble.png","img/pok/teselia/crustle.png","img/pok/teselia/scraggy.png",
   "img/pok/teselia/scrafty.png","img/pok/teselia/sigilyph.png","img/pok/teselia/yamask.png",
   "img/pok/teselia/cofagrigus.png","img/pok/teselia/tirtouga.png","img/pok/teselia/carracosta.png",#70 tirtoga
   "img/pok/teselia/archen.png","img/pok/teselia/archeops.png","img/pok/teselia/trubbish.png",
   "img/pok/teselia/garbodor.png","img/pok/teselia/zorua.png","img/pok/teselia/zoroark.png",
   "img/pok/teselia/minccino.png","img/pok/teselia/cinccino.png","img/pok/teselia/gothita.png",#80 gothita
   "img/pok/teselia/gothorita.png","img/pok/teselia/gothitelle.png","img/pok/teselia/solosis.png",
   "img/pok/teselia/duosion.png","img/pok/teselia/reuniclus.png","img/pok/teselia/ducklett.png",
   "img/pok/teselia/swanna.png","img/pok/teselia/vanillite.png","img/pok/teselia/vanillish.png",#90 vanilluxe
   "img/pok/teselia/vanilluxe.png","img/pok/teselia/deerling.png","img/pok/teselia/sawsbuck.png",
   "img/pok/teselia/emolga.png","img/pok/teselia/karrablast.png","img/pok/teselia/escavalier.png",
   "img/pok/teselia/foongus.png","img/pok/teselia/amoonguss.png","img/pok/teselia/frillish.png",
   "img/pok/teselia/jellicent.png","img/pok/teselia/alomomola.png","img/pok/teselia/joltik.png",#100 alomomola
   "img/pok/teselia/galvantula.png","img/pok/teselia/ferroseed.png","img/pok/teselia/ferrothorn.png",
   "img/pok/teselia/klink.png","img/pok/teselia/klang.png","img/pok/teselia/klinklang.png",
   "img/pok/teselia/tynamo.png","img/pok/teselia/eelektrik.png","img/pok/teselia/eelektross.png",
   "img/pok/teselia/elgyem.png","img/pok/teselia/beheeyem.png","img/pok/teselia/litwick.png",
   "img/pok/teselia/lampent.png","img/pok/teselia/chandelure.png","img/pok/teselia/axew.png",
   "img/pok/teselia/fraxure.png","img/pok/teselia/haxorus.png","img/pok/teselia/cubchoo.png",
   "img/pok/teselia/beartic.png","img/pok/teselia/cryogonal.png","img/pok/teselia/shelmet.png",
   "img/pok/teselia/accelgor.png","img/pok/teselia/stunfisk.png","img/pok/teselia/mienfoo.png",
   "img/pok/teselia/mienshao.png","img/pok/teselia/druddigon.png","img/pok/teselia/golett.png",
   "img/pok/teselia/golurk.png","img/pok/teselia/pawniard.png","img/pok/teselia/bisharp.png",
   "img/pok/teselia/bouffalant.png","img/pok/teselia/rufflet.png","img/pok/teselia/braviary.png",
   "img/pok/teselia/vullaby.png","img/pok/teselia/mandibuzz.png","img/pok/teselia/heatmor.png",
   "img/pok/teselia/durant.png","img/pok/teselia/deino.png","img/pok/teselia/zweilous.png",
   "img/pok/teselia/hydreigon.png","img/pok/teselia/larvesta.png","img/pok/teselia/volcarona.png",
   "img/pok/teselia/cobalion.png","img/pok/teselia/terrakion.png","img/pok/teselia/virizion.png",
   "img/pok/teselia/tornadus.png","img/pok/teselia/thundurus.png","img/pok/teselia/reshiram.png",
   "img/pok/teselia/zekrom.png","img/pok/teselia/landorus.png","img/pok/teselia/kyurem.png",
   "img/pok/teselia/keldeo.png","img/pok/teselia/meloetta.png","img/pok/teselia/genesect.png"
]
for img in pokemon_list_teselia:
	pokemon_images_teselia.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_kalos = []
pokemon_list_kalos = [
   "img/pok/kalos/chespin.png","img/pok/kalos/quilladin.png","img/pok/kalos/chesnaught.png",
   "img/pok/kalos/fennekin.png","img/pok/kalos/braixen.png","img/pok/kalos/delphox.png",
   "img/pok/kalos/froakie.png","img/pok/kalos/frogadier.png","img/pok/kalos/greninja.png",
   "img/pok/kalos/bunnelby.png","img/pok/kalos/diggersby.png","img/pok/kalos/fletchling.png",
   "img/pok/kalos/fletchinder.png","img/pok/kalos/talonflame.png","img/pok/kalos/scatterbug.png",
   "img/pok/kalos/spewpa.png","img/pok/kalos/vivillon.png","img/pok/kalos/litleo.png",
   "img/pok/kalos/pyroar.png","img/pok/kalos/flabebe.png","img/pok/kalos/floette.png",
   "img/pok/kalos/florges.png","img/pok/kalos/skiddo.png","img/pok/kalos/gogoat.png",
   "img/pok/kalos/pancham.png","img/pok/kalos/pangoro.png","img/pok/kalos/furfrou.png",
   "img/pok/kalos/espurr.png","img/pok/kalos/meowstic.png","img/pok/kalos/honedge.png",
   "img/pok/kalos/doublade.png","img/pok/kalos/aegislash.png","img/pok/kalos/spritzee.png",
   "img/pok/kalos/aromatisse.png","img/pok/kalos/swirlix.png","img/pok/kalos/slurpuff.png",
   "img/pok/kalos/inkay.png","img/pok/kalos/malamar.png","img/pok/kalos/binacle.png",
   "img/pok/kalos/barbaracle.png","img/pok/kalos/skrelp.png","img/pok/kalos/dragalge.png",
   "img/pok/kalos/clauncher.png","img/pok/kalos/clawitzer.png","img/pok/kalos/helioptile.png",
   "img/pok/kalos/heliolisk.png","img/pok/kalos/tyrunt.png","img/pok/kalos/tyrantrum.png",
   "img/pok/kalos/amaura.png","img/pok/kalos/aurorus.png","img/pok/kalos/sylveon.png",
   "img/pok/kalos/hawlucha.png","img/pok/kalos/dedenne.png","img/pok/kalos/carbink.png",
   "img/pok/kalos/goomy.png","img/pok/kalos/sliggoo.png","img/pok/kalos/goodra.png",
   "img/pok/kalos/klefki.png","img/pok/kalos/phantump.png","img/pok/kalos/trevenant.png",
   "img/pok/kalos/pumpkaboo.png","img/pok/kalos/gourgeist.png","img/pok/kalos/bergmite.png",
   "img/pok/kalos/avalugg.png","img/pok/kalos/noibat.png","img/pok/kalos/noivern.png",
   "img/pok/kalos/xerneas.png","img/pok/kalos/yveltal.png","img/pok/kalos/zygarde.png",
   "img/pok/kalos/diancie.png","img/pok/kalos/hoopa.png","img/pok/kalos/volcanion.png",
]
for img in pokemon_list_kalos:
	pokemon_images_kalos.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_alola = []
pokemon_list_alola = [
   "img/pok/alola/rattata.png","img/pok/alola/raticate.png","img/pok/alola/raichu.png",
   "img/pok/alola/sandshrew.png","img/pok/alola/sandslash.png","img/pok/alola/vulpix.png",
   "img/pok/alola/ninetales.png","img/pok/alola/diglett.png","img/pok/alola/dugtrio.png",
   "img/pok/alola/meowth.png","img/pok/alola/persian.png","img/pok/alola/geodude.png",
   "img/pok/alola/graveler.png","img/pok/alola/golem.png","img/pok/alola/grimer.png",
   "img/pok/alola/muk.png","img/pok/alola/exeggutor.png","img/pok/alola/marowak.png",
   "img/pok/alola/rowlet.png","img/pok/alola/dartrix.png","img/pok/alola/decidueye.png",
   "img/pok/alola/litten.png","img/pok/alola/torracat.png","img/pok/alola/incineroar.png",
   "img/pok/alola/popplio.png","img/pok/alola/brionne.png","img/pok/alola/primarina.png",
   "img/pok/alola/pikipek.png","img/pok/alola/trumbeak.png","img/pok/alola/toucannon.png",
   "img/pok/alola/yungoos.png","img/pok/alola/gumshoos.png","img/pok/alola/grubbin.png",
   "img/pok/alola/charjabug.png","img/pok/alola/vikavolt.png","img/pok/alola/crabrawler.png",
   "img/pok/alola/crabominable.png","img/pok/alola/oricorio.png","img/pok/alola/cutiefly.png",
   "img/pok/alola/ribombee.png","img/pok/alola/rockruff.png","img/pok/alola/lycanroc.png",
   "img/pok/alola/wishiwashi.png","img/pok/alola/mareanie.png","img/pok/alola/toxapex.png",
   "img/pok/alola/mudbray.png","img/pok/alola/mudsdale.png","img/pok/alola/dewpider.png",
   "img/pok/alola/araquanid.png","img/pok/alola/fomantis.png","img/pok/alola/lurantis.png",
   "img/pok/alola/morelull.png","img/pok/alola/shiinotic.png","img/pok/alola/salandit.png",
   "img/pok/alola/salazzle.png","img/pok/alola/stufful.png","img/pok/alola/bewear.png",
   "img/pok/alola/bounsweet.png","img/pok/alola/steenee.png","img/pok/alola/tsareena.png",
   "img/pok/alola/comfey.png","img/pok/alola/oranguru.png","img/pok/alola/passimian.png",
   "img/pok/alola/wimpod.png","img/pok/alola/golisopod.png","img/pok/alola/sandygast.png",
   "img/pok/alola/palossand.png","img/pok/alola/pyukumuku.png","img/pok/alola/typeNull.png",
   "img/pok/alola/silvally.png","img/pok/alola/minior.png","img/pok/alola/komala.png",
   "img/pok/alola/turtonator.png","img/pok/alola/togedemaru.png","img/pok/alola/mimikyu.png",
   "img/pok/alola/bruxish.png","img/pok/alola/drampa.png","img/pok/alola/dhelmise.png",
   "img/pok/alola/jangmo-o.png","img/pok/alola/hakamo-o.png","img/pok/alola/kommo-o.png",
   "img/pok/alola/tapukoko.png","img/pok/alola/tapulele.png","img/pok/alola/tapubulu.png",
   "img/pok/alola/tapufini.png","img/pok/alola/cosmog.png","img/pok/alola/cosmoem.png",
   "img/pok/alola/solgaleo.png","img/pok/alola/lunala.png","img/pok/alola/nihilego.png",
   "img/pok/alola/buzzwole.png","img/pok/alola/pheromosa.png","img/pok/alola/xurkitree.png",
   "img/pok/alola/celesteela.png","img/pok/alola/kartana.png","img/pok/alola/guzzlord.png",
   "img/pok/alola/necrozma.png","img/pok/alola/magearna.png","img/pok/alola/marshadow.png",
   "img/pok/alola/poipole.png","img/pok/alola/naganadel.png","img/pok/alola/stakataka.png",
   "img/pok/alola/blacephalon.png","img/pok/alola/zeraora.png","img/pok/alola/meltan.png",
   "img/pok/alola/melmetal.png"
]
for img in pokemon_list_alola:
	pokemon_images_alola.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_galar = []
pokemon_list_galar = [
 #  "img/pok/.png"
]
for img in pokemon_list_galar:
	pokemon_images_galar.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_hisui = []
pokemon_list_hisui = [
 #  "img/pok/.png"
]
for img in pokemon_list_hisui:
	pokemon_images_hisui.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_paldea = []
pokemon_list_paldea = [
  # "img/pok/.png"
]
for img in pokemon_list_paldea:
	pokemon_images_paldea.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())


pokemon_name_list = ["abomasnow","abra","absol","aerodactyl","aggron","aipom","alakazam",
                     "altaria","ambipom","ampharos","anorith","arbok","arcanine","archeops",
                     "ariados","armaldo","aron","articuno","audino","azelf","azurill","bagon",
                     "baltoy","banette","barboach","bastiodon","bayleef","beautifly","beedrill",
                     "beldum","bellossom","bellsprout","bibarel","bidoof","blastoise","blaziken",
                     "blissey","blitzle","boldore","bonsly","breloom","bronzong","bronzor","budew",
                     "buizel","bulbasaur","buneary","burmy","butterfree","cacnea","cacturne",
                     "camerupt","carnivine","carvanha","cascoon","castform","caterpie","celebi",
                     "chansey","charizard","charmander","charmeleon","chatot","cherrim","cherubi",
                     "chikorita","chimchar","chimecho","chinchou","chingling","clamperl","clauncher",
                     "claydol","clefable","clefairy","cleffa","cloyster","combee","combusken",
                     "conkeldurr","corphish","corsola","cradily","cranidos","crawdaunt",
                     "cresselia","croagunk","crobat","croconaw","cubone","cyndaquil",
                     "delcatty","delibird","delphox","dewgong","diglett","ditto","dodrio","doduo",
                     "donphan","dragonair","dragonite","dratini","drifblim","drifloon","drowzee",
                     "dugtrio","dunsparce","dusclops","duskull","dustox","eevee","ekans","electabuzz","electrike",
                     "electrode","elekid","empoleon","entei","espeon","exeggcute","exeggutor","exploud",
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
                     "heatmor","heatran","heliolisk","helioptile","heracross","hitmonchan","hitmonlee",
                     "hitmontop","hoothoot","hoppip","horsea","houndoom","houndour","hypno","ivysaur",
                     "jigglypuff","jolteon","jumpluff","jynx","kabutops","kadabra","kakuna","kangaskhan",
                     "kingdra","kingler","koffing","krabby","lapras","larvitar","ledian",
                     "ledyba","lickitung","machamp","machoke","machop","magby","magcargo","magikarp","magmar",
                     "magnemite","magneton","mantine","marill","marowak","meowth","metapod","miltank","misdreavus",
                     "monkey","mr.mime","muk","murkrow","natu","nidoking","nidoqueen","nidoran1","nidoran2",
                     "nidorina","nidorino","ninetales","noctowl","oddish","omastar","onix","paras","parasect",
                     "persian","phanpy","pidgeot","pidgeotto","pidgey","pikachu","piloswine","pineco",
                     "politoed","poliwag","poliwhirl","poliwrath","ponyta","porygon","primeape","psyduck",
                     "pupitar","quagsire","quilava","qwilfish","raichu","rapidash","raticate","rattata",
                     "raikou","remoraid","rhydon","rhyhorn","sandshrew","sandslash","scyther","seadra",
                     "seaking","seel","sentret","shellder","skarmory","skiploom","slowbro","slowking",
                     "slowpoke","slugma","sneasel","snorlax","snubbull","spearow","spinarak","squirtle",
                     "stantler","/starmie","staryu","steelix","sudowoodo","sunkern","swinub",
                     "tauros","teddiursa","tentacool","tentacruel","togepi","totodile","typhlosion",
                     "tyranitar","tyrogue","umbreon","unnown","ursaring","vaporeon","venomoth","venonat","venusaur",
                     "vespiquen","vibrava",
                     "victreebel","vigoroth","vileplume","volbeat","voltorb","vulpix","wailmer","wailord",
                     "walrein","wartortle","weedle","weepinbell",
                     "weezing","whiscash","whismur","wigglytuff","wingull","wobbuffet",
                     "wooper","wormadam","wurmple","wynaut","xatu","yanma","zangoose","zapdos",
                     "zigzagoon","zubat.png"
      ]


#0..normal    1..lucha    2..volador   3..veneno   4..tierra   5..roca   6..bicho      78cacn
#7..fantasma   8..fuego   9..agua   10..planta   11..electrico   12..psiquico
#13..siniestro   14..hada   15..acero   16..hielo   17..dragon           ( )


pokemon_type_kanto1 = [
   10,10,10,8,8,8,9,9,9,6,6, 6,6,6,6,0,0,0,0,0,0, 0,3,3,11,11,4,4,3,3,3, #30
   3,3,3,14,14,8,8,0,0,3, 3,10,10,10,6,6,6,6,4,4, 0,0,9,9,1,1,8,8,9,9,   #60
   9,12,12,12,1,1,1,10,10,10, 9,9,5,5,5,8,8,9,9,11, 11,0,0,0,9,9,3,3,9,9,#90
   7,7,7,5,12,12,9,9,11,11, 10,10,4,4,1,1,0,3,3,4, 4,0,10,0,9,9,9,9,9,9, #120
   12,6,16,11,8,6,0,9,9,9, 0,0,9,11,8,0,5,5,5,5, 5,0,16,11,8,17,17,17,12,12#150
]

pokemon_type_kanto2 = [
   3,3,3,18,18,2,18,18,18,18,18, 2,3,3,3,2,2,2,18,18,2, 2,18,18,18,18,18,18,18,18,4,     #30
   18,18,4,18,18,18,18,14,14,2, 2,3,3,3,10,10,3,3,18,18, 18,18,18,18,18,18,18,18,18,18,  #60
   1,18,18,18,18,18,18,3,3,3, 3,3,4,4,4,18,18,12,12,15, 15,2,2,2,18,16,18,18,18,16,      #90
   3,3,3,4,18,18,18,18,18,18, 12,12,18,18,18,18,18,18,18,5, 5,18,18,18,18,18,18,18,18,12,#120
   14,2,12,18,18,18,18,18,2,16, 18,18,18,18,18,18,9,9,9,9, 2,18,2,2,2,18,18,2,18,18      #150
]

pokemon_type_johto1 = [
   10,10,10,8,8,8,9,9,9,0,0, 0,0,6,6,6,6,3,9,9,11, 14,0,14,14,12,12,11,11,11,10,#30
   9,9,5,9,10,10,10,0,10,10, 6,9,9,12,13,13,9,7,12,12, 0,6,6,0,4,15,14,14,9,6,#60
   6,6,13,0,0,8,8,16,16,9, 9,9,16,9,15,13,13,9,4,4, 0,0,0,1,1,16,11,8,0,0,#90
   11,8,9,5,5,5,12,8,12
]

pokemon_type_johto2 = [
   18,18,18,18,18,18,18,18,18,18,18, 2,2,2,2,3,3,2,11,11,18, 18,14,18,2,18,2,18,18,18,18,#30
   14,14,18,18,2,2,2,18,18,18, 2,4,4,18,18,2,12,18,18,18, 12,18,15,18,2,4,18,18,3,15,#60
   5,1,16,18,18,18,18,4,4,5, 18,18,2,2,2,8,8,17,18,18, 18,18,18,18,18,12,18,18,18,18,#90
   18,18,18,4,4,13,2,2,10
]

pokemon_type_hoenn1 = [
   10,10,10,8,8,8,9,9,9,13,13, 0,0,6,6,6,6,6,9,9,9, 10,10,10,0,0,9,9,12,12,12,#30
   10,6,10,10,0,0,0,6,6,6, 0,0,0,1,1,0,5,0,0,13, 15,15,15,15,1,1,11,11,11,11,#60
   6,6,10,10,3,9,9,9,9,8, 8,8,12,12,0,4,4,4,10,10, 0,17,0,3,5,5,9,9,9,9,#90
   4,4,5,5,5,5,9,9,0,0, 7,7,7,7,10,12,13,12,16,16, 16,16,16,9,9,9,9,9,17,17,#120
   17,15,15,15,5,16,15,17,17,9, 4,17,15,12,
]

pokemon_type_hoenn2 = [
   18,18,18,18,1,1,18,4,4,18,18, 18,18,18,18,2,18,3,10,10,10, 18,13,13,2,2,2,2,14,14,14,#30
   9,2,18,1,18,18,18,4,2,7, 18,18,18,18,18,14,18,18,18,7, 14,5,5,5,12,12,18,18,18,18,#60
   18,18,3,18,18,13,13,18,18,4, 4,18,18,18,18,18,17,17,18,13, 2,2,18,18,12,12,4,4,18,13,#90
   12,12,10,10,6,6,18,18,18,18, 18,18,18,18,2,18,18,18,18,18, 9,9,9,18,18,18,5,18,18,18,#120
   2,12,12,12,18,18,18,12,12,18, 18,2,12,18,
]

pokemon_type_sinnoh1 = [
   10,10,10,8,8,8,9,9,9,0,0, 0,0,0,6,6,11,11,11,10,10, 5,5,5,5,6,6,6,6,6,11,#30
   9,9,10,10,9,9,0,7,7,0, 0,7,13,0,0,12,3,3,15,15, 5,12,0,0,7,17,17,17,0,1,#60
   1,4,4,3,3,3,3,10,9,9, 9,10,10,13,11,0,4,10,11,8, 14,6,10,16,4,16,0,12,5,7,#90
   16,11,12,12,12,15,9,8,0,7, 12,9,9,13,10,0
   ]

pokemon_type_sinnoh2 = [
   18,18,4,18,1,1,18,18,15,2,2, 2,18,9,18,18,18,18,18,3,3, 18,18,15,15,18,10,2,2,2,18,#30
   18,18,18,18,18,4,18,2,2,18, 18,18,2,18,18,18,13,13,12,12, 18,14,18,2,13,4,4,4,18,18,#60
   15,18,18,6,13,1,1,18,18,18, 2,16,16,16,15,18,5,18,18,18, 2,2,18,18,2,4,18,1,15,18,#90
   7,7,18,18,18,17,17,15,18,17, 18,18,18,18,18,18
   ]

pokemon_type_teselia1 = [
   12,10,10,10,8,8,8,9,9,9,0, 0,0,0,0,13,13,10,10,8,8,#20
   9,9,12,12,0,0,0,11,11,5, 5,5,12,12,4,4,0,1,1,1,#40
   9,9,9,1,1,6,6,6,6,6, 6,10,10,10,10,9,4,4,4,8,#60
   8,10,6,6,13,13,12,7,7,9, 9,5,5,3,3,13,13,0,0,12,#80
   12,12,12,12,12,9,9,16,16,16, 0,0,11,6,6,10,10,9,9,9,#100
   6,6,10,10,15,15,15,11,11,11, 12,12,7,7,7,17,17,17,16,16,#120
   16,6,6,4,1,1,17,4,4,13, 13,0,0,0,13,13,8,6,13,13,#140
   13,6,6,15,5,10,2,11,17,17, 4,17,9,0,6
   ]

pokemon_type_teselia2 = [
   8,18,18,18,18,1,1,18,18,18,18, 18,18,18,18,18,18,18,18,18,18,#20
   18,18,18,18,2,2,2,18,18,18, 18,18,2,2,18,15,18,18,18,18,#40
   18,4,4,18,18,10,10,10,3,3, 3,14,14,18,18,18,13,13,13,18,#60
   18,18,5,5,1,1,2,18,18,5, 5,2,2,18,18,18,18,18,18,18,#80
   18,18,18,18,18,2,2,18,18,18, 10,10,2,18,15,3,3,7,7,18,#100
   11,11,15,15,18,18,18,18,18,18, 18,18,8,8,8,18,18,18,18,18,#120
   18,18,18,11,18,18,18,7,7,15, 15,18,2,2,2,2,18,15,17,17,#140
   17,8,8,1,1,1,18,2,8,11, 2,16,1,12,15
   ]

pokemon_type_kalos1 = [
   10,10,10,8,8,8,9,9,9,0,0, 0,8,8,6,6,6,8,8,14,14, 14,10,10,1,1,0,12,12,15,15,#30
   15,14,14,14,14,13,13,5,5,3, 3,9,9,11,11,5,5,5,5,14, 1,11,5,17,17,17,15,7,7,7,#60
   7,16,16,2,2,14,13,17,5,12, 8
   ]

pokemon_type_kalos2 = [
   18,18,1,18,18,12,18,18,13,18,4, 2,2,2,18,18,2,0,0,18,18, 18,18,18,18,13,18,18,18,7,7,#30
   7,18,18,18,18,12,12,9,9,9, 17,18,18,0,0,17,17,16,16,18, 2,14,14,18,18,18,14,10,10,10,#60
   10,18,18,17,17,18,2,4,14,7, 9
]

pokemon_type_alola1 = [
   13,13,11,16,16,16,16,4,4,13,13, 5,5,5,3,3,10,8,10,10,10, 8,8,8,9,9,9,0,0,0,0,#30
   0,6,6,6,1,1,8,6,6,5, 5,9,3,3,4,4,9,9,10,10, 10,10,3,3,0,0,10,10,10,14,#60
   0,1,6,6,7,7,9,0,0,5, 0,8,11,7,9,0,7,17,17,17, 11,12,10,9,12,12,12,12,5,6,#90
   6,11,15,10,13,12,15,1,3,3, 5,8,11,15,15
   ]

pokemon_type_alola2 = [
   0,0,12,15,15,18,14,15,15,18,18, 11,11,11,13,13,17,7,2,2,7, 18,18,13,18,18,14,2,2,2,18,#30
   18,18,11,11,18,16,2,14,14,18, 18,18,9,9,18,18,6,6,18,18, 14,14,8,8,1,1,18,18,18,18,#60
   12,18,9,9,4,4,18,18,18,2, 18,17,15,14,12,17,10,18,1,1, 14,14,14,14,18,18,15,7,3,1,#90
   1,18,2,15,17,18,14,7,18,17, 15,7,18,18,18
   ]

pokemon_hp_kanto = [
   75,72,95,75,71,66,81,76,72,120,126, 69,113,120,73,91,90,81,77,68,84,#20
   71,73,68,72,63,75,71,98,91,78, 86,80,71,97,83,77,72,174,123,91,#40
   78,71,73,68,70,69,95,72,55,57, 86,77,81,73,71,65,80,71,82,84,#60
   77,53,53,51,92,80,71,83,78,74, 74,74,66,66,66,64,64,111,80,52,#80
   54,77,64,61,100,88,96,83,62,53, 58,57,56,67,92,82,52,54,75,65,#100
   87,74,83,69,53,55,104,68,66,89, 77,250,66,86,63,62,73,78,60,59,#120
   50,62,62,64,64,57,68,100,70,101, 90,87,93,58,57,76,57,62,55,58,#140
   68,107,71,66,67,74,72,65,62,74
]

pokemon_hp_johto = [
   82,78,74,75,73,66,78,77,71,89,89, 113,95,89,77,83,79,74,103,109,81,#20
   103,169,87,69,72,66,89,84,74,73, 153,106,72,80,90,91,84,77,98,75,#40
   82,112,92,57,89,76,80,69,77,221, 74,81,73,103,73,71,84,77,69,60,#60
   84,65,63,82,72,79,65,98,86,77, 73,73,76,68,68,72,68,68,112,71,#80
   72,73,135,100,58,70,72,70,83,171, 67,79,78,83,79,69,72,66,74,
   ]

pokemon_hp_hoenn = [
   73,67,62,76,73,68,79,79,78,86,75, 102,87,105,113,71,113,86,97,86,75,#20
   97,95,81,85,69,86,65,86,74,59, 85,70,105,59,95,81,80,76,68,13,#40
   120,104,89,118,106,130,66,99,86,70, 67,74,65,60,78,80,77,67,71,72,#60
   75,75,62,111,95,78,70,135,134,92, 70,72,82,74,86,71,76,71,77,70,#80
   87,78,69,74,81,81,93,99,69,62, 84,67,89,80,64,65,90,74,82,66,#100
   78,66,66,59,95,73,62,176,90,79, 106,96,86,62,59,57,83,84,75,71,#120
   67,76,71,59,65,65,73,60,59,60, 60,66,73,47
]

pokemon_hp_sinnoh = [
   81,80,76,80,80,69,83,76,71,88,79, 71,109,85,108,88,85,78,68,82,55,#20
   76,71,69,77,107,71,77,93,74,86, 87,77,82,74,104,94,71,112,118,80,#40
   69,59,81,87,75,79,92,88,116,68, 74,53,201,82,58,88,75,71,122,75,#60
   63,88,81,75,67,85,76,75,85,78, 71,87,80,60,58,91,77,77,62,62,#80
   65,70,57,57,68,78,65,59,65,51, 72,58,68,64,60,60,58,65,64,91,#100
   92,79,73,54,74,72,
]

pokemon_hp_teselia = [
   73,86,78,72,95,88,82,88,82,77,89, 69,83,78,71,86,72,87,71,86,71, 86,71,104,89,91,81,68,85,71,81,#30
   73,66,98,77,80,80,106,94,81,75, 91,92,86,96,65,81,77,68,77,71, 60,90,66,77,65,72,82,80,74,86,#60
   79,73,77,65,71,66,66,74,62,72, 67,66,59,84,74,69,59,96,73,82, 75,67,68,71,84,103,75,70,68,63,#90
   89,74,71,77,61,104,102,80,87,134, 83,70,81,71,76,69,59,78,77,71, 76,65,84,73,52,69,67,58,87,74,#120
   68,91,74,96,67,60,67,86,73,66, 59,77,84,77,91,99,77,57,84,80, 68,74,62,71,65,71,62,62,61,61,#150
   64,75,65,67,57
   ]

pokemon_hp_kalos = [
   87,74,71,74,70,62,76,70,66,97,98, 89,80,75,104,115,84,81,72,77,72,#20
   62,89,93,84,77,75,86,75,12,12, 12,102,88,89,78,90,77,79,65,82,#40
   64,82,63,81,60,71,66,95,93,74, 72,74,70,81,71,67,65,73,74,75,#60
   60,81,72,91,71,75,75,57,50,57, 60
   ]

pokemon_hp_alola = [
   77,83,63,74,71,77,70,55,51,83,75, 66,66,66,96,83,74,69,99,87,67,#20
   77,77,74,79,69,65,73,74,71,89, 84,83,70,63,70,78,71,79,63,82,#40
   67,44,87,65,76,77,86,77,87,67, 74,69,78,66,90,88,112,102,62,59,#60
   80,77,85,62,80,77,77,78,75,77, 62,63,66,60,66,67,62,81,69,59,#80
   58,55,57,62,117,88,76,76,70,70, 63,59,75,44,152,67,59,64,80,61,#100
   52,48,67,78,81
   ]

pokemon_defense_kanto = [
   67,68,68,61,61,61,78,78,80,58,79, 62,53,75,59,59,61,64,55,65,46,#20
   59,65,68,63,63,67,68,64,66,66, 54,59,59,63,64,74,76,37,42,59,#40
   65,63,65,63,62,66,64,61,63,66, 60,65,57,63,50,56,53,58,59,65,#60
   69,46,51,58,47,55,55,41,47,54, 89,81,72,73,70,60,63,56,68,65,#80
   65,64,49,56,77,76,49,62,79,94, 40,48,54,131,82,80,61,65,69,72,#100
   72,52,87,82,68,76,71,79,79,61, 58,71,69,62,64,66,64,61,65,69,#120
   82,63,57,62,61,64,68,84,61,65, 64,70,56,64,62,63,75,72,73,68,#140
   58,57,80,60,58,59,63,61,53,70
   ]

pokemon_defense_johto = [
   78,78,78,61,61,62,65,66,67,62,59, 69,68,87,93,55,58,67,58,58,55,#20
   64,35,90,83,55,60,53,56,60,75, 88,73,74,70,78,77,87,61,58,57,#40
   50,56,62,60,97,45,68,67,53,66, 57,73,82,61,81,104,49,50,59,62,#60
   345,62,62,52,51,50,88,54,55,82, 48,56,56,93,93,48,54,71,57,64,#80
   65,55,82,63,84,52,59,55,75,61, 64,56,80,59,62,64,94,75,68
]

pokemon_defense_hoenn = [
   59,58,61,54,57,52,56,62,61,51,58, 73,61,54,68,47,68,90,66,68,69,#20
   66,47,49,48,56,48,72,56,60,67, 63,61,77,55,59,63,48,90,50,73,#40
   39,47,55,42,43,72,130,60,65,69, 69,76,82,87,81,78,53,51,60,69,#60
   76,76,60,68,69,29,36,38,38,50, 56,84,65,73,66,46,56,63,44,47,#80
   91,86,50,51,61,61,59,60,57,54, 87,97,80,78,52,63,84,75,68,80,#100
   44,52,115,110,71,69,47,77,65,68, 59,63,64,74,70,68,76,86,56,67,#120
   53,83,82,70,104,104,108,75,65,66, 66,53,68,41
]

pokemon_defense_sinnoh = [
   63,64,67,57,54,57,62,66,66,47,53, 51,57,55,74,50,47,50,57,74,64,#20
   35,37,125,136,78,82,47,77,81,95, 44,46,60,65,63,57,57,48,42,59,#40
   81,70,39,55,59,60,55,53,120,85, 72,82,77,44,82,52,57,58,54,51,#60
   55,64,66,91,78,51,52,58,75,78, 96,62,62,59,70,71,59,63,57,60,#80
   71,54,75,70,82,49,50,67,112,97, 63,67,100,72,53,61,63,66,61,73,#100
   91,68,68,61,68,71
]

pokemon_defense_teselia = [
   68,73,78,82,53,48,45,55,55,57,55, 65,58,63,66,55,49,62,53,62,53,#20
   62,53,56,61,57,56,54,46,54,63, 63,68,55,58,48,45,77,50,56,52,#40
   56,59,57,61,56,77,85,62,75,98, 68,84,75,58,59,55,46,49,55,46,#60
   41,54,72,75,70,88,63,87,94,74, 74,42,47,75,64,48,49,56,54,72,#80
   74,79,46,47,53,67,56,66,67,66, 60,58,62,52,65,60,59,73,70,54,#100
   62,53,97,88,78,77,79,57,62,56, 55,59,63,56,60,55,51,55,48,53,#120
   78,93,48,69,53,48,62,54,56,59, 64,66,50,53,75,85,52,70,58,61,#140
   58,55,59,78,60,78,54,54,61,61, 57,53,60,69,65
   ]

pokemon_defense_kalos = [
   64,74,70,63,61,65,74,57,58,64,78, 58,57,63,62,82,48,58,55,72,75,#20
   79,58,54,56,54,70,64,70,12,12, 12,65,59,69,66,64,65,77,75,67,#40
   80,70,62,53,63,61,66,59,59,70, 60,61,138,70,76,78,77,62,59,70,#60
   87,68,80,59,63,58,58,68,100,61, 67
]

pokemon_defense_alola = [
   56,73,62,70,75,73,76,64,63,57,63, 72,72,69,49,62,53,82,61,65,65,#20
   51,50,61,62,64,65,43,53,55,42, 48,55,76,55,57,51,58,56,60,53,#40
   52,80,70,124,55,60,87,96,51,66, 73,75,50,51,52,50,68,69,68,89,#60
   75,56,70,75,66,69,112,67,69,54, 62,86,60,80,57,58,63,69,76,78,#80
   61,66,70,90,60,159,56,56,63,64, 33,44,68,57,37,60,70,59,65,55,#100
   95,49,58,61,60,
   
]

pokemon_attack_kanto = [
   70,71,72,74,74,77,62,65,67,58,50, 74,64,51,75,68,68,70,77,74,79,#20
   78,71,72,73,78,70,71,62,64,69, 73,71,76,63,69,65,69,62,68,66,#40
   70,74,72,75,74,74,64,75,84,80, 69,71,73,74,84,83,75,77,71,68,#60
   68,101,95,91,74,75,79,84,82,80, 61,64,72,72,73,79,79,62,67,86,#80
   84,69,88,84,56,61,71,68,70,70, 100,95,92,53,57,61,87,84,69,72,#100
   63,79,57,65,83,75,58,68,69,67, 74,37,74,68,78,78,71,72,78,78,#120
   77,79,83,77,80,82,73,36,77,62, 64,64,70,80,83,72,76,74,78,80,#140
   79,63,66,80,80,74,75,80,86,69
]

pokemon_attack_johto = [
   61,63,66,73,74,77,69,69,73,66,68, 55,62,56,58,74,74,72,63,62,74,#20
   61,63,56,66,79,77,72,72,75,69, 42,56,70,68,58,60,58,72,58,77,#40
   78,62,66,86,53,84,67,72,76,41, 76,65,66,63,64,59,77,79,77,80,#60
   26,79,79,77,82,78,65,67,71,64, 82,77,76,63,63,83,83,72,62,73,#80
   71,78,46,63,72,82,76,81,62,48, 78,76,62,71,71,77,60,73,68
]

pokemon_attack_hoenn = [
   75,80,79,77,77,85,74,72,72,74,74, 57,67,66,56,86,56,57,61,64,68,#20
   61,75,78,76,80,77,73,71,74,80, 67,76,55,89,66,69,80,60,85,141,#40
   72,73,70,70,75,42,54,64,68,72, 74,66,69,68,62,64,78,83,75,69,#60
   66,66,82,56,61,105,97,69,69,72, 78,64,67,67,66,87,74,76,85,88,#80
   55,61,85,81,71,71,66,64,78,86, 57,61,58,62,86,79,36,66,68,70,#100
   84,87,56,61,60,71,91,42,64,68, 62,65,66,73,76,81,61,58,78,74,#120
   84,62,66,78,61,61,56,73,81,77, 77,85,69,115
]

pokemon_attack_sinnoh = [
   68,70,71,72,76,81,67,71,75,76,78, 83,62,72,50,77,77,80,81,64,82,#20
   95,94,53,49,53,65,84,58,65,55, 79,85,70,73,62,67,67,70,72,66,#40
   78,87,71,74,72,71,72,42,66,68, 74,33,83,71,73,75,78,62,80,85,#60
   66,69,60,70,74,81,78,62,66,59, 67,69,82,80,62,74,71,84,84,73,#80
   79,75,80,68,80,85,80,58,70,72, 77,60,72,88,80,81,77,80,61,56,#100
   68,69,87,68,72
]

pokemon_attack_teselia = [
   68,62,63,65,69,75,80,71,73,76,70, 74,71,70,73,71,83,67,80,67,80,#20
   67,80,65,66,68,73,80,79,81,69, 74,74,67,75,79,84,55,72,74,78,#40
   68,67,70,65,82,62,61,76,64,60, 78,57,70,73,79,79,80,80,78,77,#60
   88,80,66,70,69,65,76,61,65,67, 71,93,93,62,71,86,92,67,79,64,#80
   67,69,88,88,75,59,76,73,73,78, 68,77,74,78,78,63,64,64,64,58,#100
   68,81,55,63,64,67,74,74,73,77, 76,79,68,78,88,81,85,88,77,79,#120
   68,53,85,60,82,93,77,73,79,79, 82,70,75,79,59,55,79,81,70,71,#140
   78,77,80,66,79,66,86,86,80,80, 80,75,79,74,81
]

pokemon_attack_kalos = [
   66,69,69,72,78,78,76,79,82,62,58, 68,74,71,62,50,78,71,79,66,68,#20
   70,68,70,73,79,69,67,70,12,12, 12,62,68,63,68,65,69,63,72,67,#40
   69,65,79,74,81,75,76,66,67,69, 76,73,49,65,67,70,69,73,75,69,#60
   69,67,66,67,73,76,76,79,68,84, 78
]

pokemon_attack_alola = [
   77,64,81,68,69,65,69,82,88,71,73, 72,72,73,70,68,78,65,63,67,75,#20
   77,81,73,71,75,77,87,80,81,81, 78,72,69,86,79,80,76,73,79,75,#40
   84,82,64,55,77,73,57,59,74,75, 67,69,79,88,72,77,57,60,76,69,#60
   66,76,64,73,67,69,52,69,69,87, 80,67,76,72,80,80,80,66,69,72,#80
   81,80,80,68,57,43,74,73,74,76, 111,97,71,98,68,77,75,81,69,89,#100
   69,100,81,72,69
]

pokemon_sta = []

type_images = []

type_list = ["img/type/normal.png","img/type/lucha.png","img/type/volador.png","img/type/veneno.png",
             "img/type/tierra.png","img/type/roca.png","img/type/bicho.png","img/type/fantasma.png",
             "img/type/fuego.png","img/type/agua.png","img/type/planta.png","img/type/electrico.png",
             "img/type/psiquico.png","img/type/siniestro.png","img/type/hada.png","img/type/acero.png",
             "img/type/hielo.png","img/type/dragon.png","img/type/none.png"]
for img in type_list:
   type_images.append(pygame.transform.scale(pygame.image.load(img),(50,50)).convert())

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


def show_game_over_screenp3():
   screen.fill(BLACK)
   draw_text1(screen, "DRAW", 30, ancho // 2, alto // 2)
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
   [1,  1,  1,  1,  1,  0.625,  1, 0.391,  1,  1,  1,  1,  1,  1,  1,  0.625,  1,  1],#1Normal

   [1.6, 1, 0.625, 0.625,  1,  1.6, 0.625, 0.391,  1,  1,  1,  1, 0.625,  1.6, 0.625,  1.6,  1.6,  1],#2lucha
   
   [1,  1.6, 1,  1,  1,  0.625,  1.6,  1,  1,  1,  1.6, 0.625,  1,  1,  1,  0.625,  1,  1],#3volador
   
   [1,  1,  1, 0.625, 0.625,  0.625,  1,  0.625,  1,  1,  1.6,  1,  1,  1,  1.6,  0.391,  1,  1],#4veneno
   
   [1,  1,  0.391,  1.6, 1, 1.6, 0.625,  1,  1.6,  1,  0.625,  1.6,  1,  1,  1,  1.6,  1,      1],#5tierra
   
   [1, 0.625,  1.6,  1, 0.625, 1,  1.6,  1,  1.6,  1,  1,  1,  1,  1,  1,  0.625,  1.6,        1],#6roca
   
   [1, 0.625,  0.625, 0.625,  1,  1, 1,  0.625, 0.625,  1,  1.6,  1,  1.6,  1.6, 0.625,  0.625,  1,  1],#7bicho
   
   [0.391,  1,  1,  1,  1,  1,  1,  1.6,  1,  1,  1,  1,  1.6, 0.625,  1,  1,  1,       1],#8fantasma
   
   [1,  1,  1,  1,  1,  0.625,  1.6,  1, 0.625, 0.625,  1.6,  1,  1,  1,  1,  1.6,  1.6,     0.625],#9fuego
   
   [1,  1,  1,  1,  1.6,  1.6,  1,  1,  1.6, 0.625, 0.625,  1,  1,  1,  1,  1,  1,       0.625],#10agua
   
   [1,  1,  0.625, 0.625,  1.6,  1.6, 0.625,  1, 0.625, 1.6, 0.625,  1,  1,  1,  1,  0.625,  1, 0.625],#11planta
   
   [1,  1,  1.6, 1,  0.391,  1,  1,  1,  1,  1.6, 0.625, 0.625,  1,  1,  1,  1,  1,        0.625],#12electrico
   
   [1,  1.6,  1,  1.6,  1,  1,  1,  1,  1,  1,  1,  0.625, 0.391, 1,  1,  0.625,  1,    1],#13psiquico
   
   [1, 0.625,  1,  1,  1,  1,  1,  1.6,  1,  1,  1,  1,  1.6, 0.625, 0.625,  1,  1,        1],#14siniestro
   
   [1,  1.6,  1, 0.625,  1,  1,  1,  1, 0.625,  1,  1,  1,  1,  1.6,  1, 0.625,  1,  1.6],#15hada
   
   [1,  1,  1,  1,  1,  1.6,  1,  1, 0.625, 0.625,  1, 0.625,  1,  1,  1.6,  0.625,  1.6,  1],#16acero
   
   [1,  1,  1.6,  1,  1.6,  1,  1,  1, 0.625, 0.625,  1.6,  1,  1,  1,  1,  0.625,  0.625,  1.6],#17hielo
   
   [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.391,  0.625,  1,  1.6],#18dragon
]

def damage(tip_atacante,attack_atacante,defensor):
#   poder_de_ataque = atacante.poder_de_ataque
   tipo_atacante = tip_atacante
   tipo_defensor1 = defensor.type1
   tipo_defensor2 = defensor.type2


   efectividad_total = 1
   if tipo_defensor2 is not 18:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor2]
   else:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]

   daño = 6*(attack_atacante/(defensor.defense))*efectividad_total #6 es un valor de ataque, medio.
   return daño


player_pokemon_list = []
op_pokemon_list = []

player_pokemon_type_attack = 0
op_pokemon_type_attack = 0

fighting = True

numero_de_regiones = 6

carga1 = True
game_over1 = False
game_over2 = False
game_over3 = False
player_pokemon_hp = 0
op_pokemon_hp = 0

all_sprites = pygame.sprite.Group()
pokeballs = pygame.sprite.Group()
type_pokemon = pygame.sprite.Group()
type2_pokemon = pygame.sprite.Group()


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
                        poke.hp -= damage(player_pokemon_type_attack,pok.attack,poke)
                        pok.ultimo_ataque = pygame.time.get_ticks()

   if game_over1:
      game_over1 = False
      show_game_over_screenp1()
      carga1 = True


   if game_over2:
      game_over2 = False
      show_game_over_screenp2()
      carga1 = True

   if game_over3:
      game_over3 = False
      show_game_over_screenp3()
      carga1 = True



   if carga1:
      carga1 = False
      all_sprites.empty()
      player_pokemon_list = []
      op_pokemon_list = []
      pokemon1 = Pokemon(randint(0,numero_de_regiones),0)
      player_pokemon_list.append(pokemon1)
      all_sprites.add(pokemon1)
      player_pokemon_hp = pokemon1.hp
      if pokemon1.type2 != 18:
      
         player_pokemon_type_attack = random.choice([pokemon1.type1,pokemon1.type2])
      else:
         player_pokemon_type_attack = pokemon1.type1
      type1 = Type(player_pokemon_type_attack,270,460,0,50,50)
      type_pokemon.add(type1)
      type1a = Type(pokemon1.type1,pokemon1.rect.x,pokemon1.rect.top - 30,0,25,25)
      type1b = Type(pokemon1.type2,pokemon1.rect.x + 30,pokemon1.rect.top - 30,0,25,25)
      type2_pokemon.add(type1a,type1b)
      pokemon2 = Pokemon(randint(0,numero_de_regiones),0)
      player_pokemon_list.append(pokemon2)
      pokemon3 = Pokemon(randint(0,numero_de_regiones),0)
      player_pokemon_list.append(pokemon3)
      pokemon4 = Pokemon(randint(0,numero_de_regiones),1)
      op_pokemon_list.append(pokemon4)
      all_sprites.add(pokemon4)
      op_pokemon_hp = pokemon4.hp
      if pokemon4.type2 != 18:
         op_pokemon_type_attack = random.choice([pokemon4.type1,pokemon4.type2])
      else:
         op_pokemon_type_attack = pokemon4.type1
      type2 = Type(op_pokemon_type_attack,670,260,1,50,50)
      type_pokemon.add(type2)
      type2a = Type(pokemon4.type1,pokemon4.rect.x,pokemon4.rect.top - 30,1,25,25)
      type2b = Type(pokemon4.type2,pokemon4.rect.x + 30,pokemon4.rect.top - 30,1,25,25)
      type2_pokemon.add(type2a,type2b)
      pokemon5 = Pokemon(randint(0,numero_de_regiones),1)
      op_pokemon_list.append(pokemon5)
      pokemon6 = Pokemon(randint(0,numero_de_regiones),1)
      op_pokemon_list.append(pokemon6)
      pokeball1 = Pokeball(0,3)
      pokeball2 = Pokeball(1,3)
      pokeballs.add(pokeball1,pokeball2)

   if len(player_pokemon_list) != 0 and len(op_pokemon_list) != 0:
      while len(all_sprites) < 2:
         if len(all_sprites) == 1:
            for pok in all_sprites:
               if pok.team_int == 0:
                  all_sprites.add(random.choice(op_pokemon_list))
                  for poke in all_sprites:
                     if poke.team_int == 1:
                        op_pokemon_hp = poke.hp
                        if poke.type2 != 18:
                           op_pokemon_type_attack = random.choice([poke.type1,poke.type2])
                        else:
                           op_pokemon_type_attack = poke.type1
                        for ty in type_pokemon:
                           if ty.team_int == 1:
                              ty.kill()
                              type2 = Type(op_pokemon_type_attack,670,260,1,50,50)
                              type_pokemon.add(type2)
                        for ty in type2_pokemon:
                           if ty.team_int == 1:
                              ty.kill()
                        type2a = Type(poke.type1,poke.rect.x,poke.rect.top - 30,1,25,25)
                        type2b = Type(poke.type2,poke.rect.x + 30,poke.rect.top - 30,1,25,25)
                        type2_pokemon.add(type2a,type2b)
               else:
                  all_sprites.add(random.choice(player_pokemon_list))
                  for pokem in all_sprites:
                     if pokem.team_int == 0:
                        player_pokemon_hp = pokem.hp
                        if pokem.type2 != 18:
                           player_pokemon_type_attack = random.choice([pokem.type1,pokem.type2])
                        else:
                           player_pokemon_type_attack = pokem.type1
                        for typ in type_pokemon:
                           if typ.team_int == 0:
                              typ.kill()
                              type1 = Type(player_pokemon_type_attack,270,460,0,50,50)
                              type_pokemon.add(type1)
                        for typ in type2_pokemon:
                           if typ.team_int == 0:
                              typ.kill()
                        type1a = Type(pokem.type1,pokem.rect.x,pokem.rect.top - 30,0,25,25)
                        type1b = Type(pokem.type2,pokem.rect.x + 30,pokem.rect.top - 30,0,25,25)
                        type2_pokemon.add(type1a,type1b)
         elif len(all_sprites) == 0:
            all_sprites.add(random.choice(op_pokemon_list))
            for poke in all_sprites:
               if poke.team_int == 1:
                  op_pokemon_hp = poke.hp
                  if poke.type2 != 18:
                     op_pokemon_type_attack = random.choice([poke.type1,poke.type2])
                  else:
                     op_pokemon_type_attack = poke.type1
                  for ty in type_pokemon:
                     if ty.team_int == 1:
                        ty.kill()
                        type2 = Type(op_pokemon_type_attack,670,260,1,50,50)
                        type_pokemon.add(type2)
                  for ty in type2_pokemon:
                     if ty.team_int == 1:
                        ty.kill()
                  type2a = Type(poke.type1,poke.rect.x,poke.rect.top - 30,1,25,25)
                  type2b = Type(poke.type2,poke.rect.x + 30,poke.rect.top - 30,1,25,25)
                  type2_pokemon.add(type2a,type2b)
            all_sprites.add(random.choice(player_pokemon_list))
            for pokem in all_sprites:
               if pokem.team_int == 0:
                  player_pokemon_hp = pokem.hp
                  if pokem.type2 != 18:
                     player_pokemon_type_attack = random.choice([pokem.type1,pokem.type2])
                  else:
                     player_pokemon_type_attack = pokem.type1
                  for typ in type_pokemon:
                     if typ.team_int == 0:
                        typ.kill()
                        type1 = Type(player_pokemon_type_attack,270,460,0,50,50)
                        type_pokemon.add(type1)
                  for typ in type2_pokemon:
                     if typ.team_int == 0:
                        typ.kill()
                  type1a = Type(pokem.type1,pokem.rect.x,pokem.rect.top - 30,0,25,25)
                  type1b = Type(pokem.type2,pokem.rect.x + 30,pokem.rect.top - 30,0,25,25)
                  type2_pokemon.add(type1a,type1b)
   #print(len(player_pokemon_list))
   if len(player_pokemon_list) == 0 or len(op_pokemon_list) == 0:
      if len(player_pokemon_list) == 0 and len(op_pokemon_list) == 0:
         game_over3 = True
      elif len(player_pokemon_list) == 0:
         game_over2 = True
      else:
         game_over1 = True

   

   screen.fill(BLACK)
   all_sprites.update()
   # pokeball1.int = len(player_pokemon_list)
   # pokeball2.int = len(op_pokemon_list)
   pokeballs.update()
   all_sprites.draw(screen)
   type_pokemon.draw(screen)
   type2_pokemon.draw(screen)
   
   pokeballs.draw(screen)
   for pok in all_sprites:
      if pok.team_int == 0:
         if pok.hp/player_pokemon_hp > 0.5:
            draw_hp_bar(screen,pok.rect.x,pok.rect.y,(pok.hp/(player_pokemon_hp))*100)
         elif pok.hp/player_pokemon_hp > 0.20:
            draw_hp_bar2(screen,pok.rect.x,pok.rect.y,(pok.hp/(player_pokemon_hp))*100)
         else:
            draw_hp_bar3(screen,pok.rect.x,pok.rect.y,(pok.hp/(player_pokemon_hp))*100)
         draw_text2(screen,f"{int(pok.hp)}/{player_pokemon_hp}",10,pok.rect.centerx,pok.rect.y)
         draw_text1(screen,"ATTACK:",10,pok.rect.x,480)
         draw_text1(screen,f"Pokemones: {len(player_pokemon_list)}",15,pok.rect.x,495)
      else:
         if pok.hp/op_pokemon_hp > 0.5:
            draw_hp_bar(screen,pok.rect.x,pok.rect.y,(pok.hp/op_pokemon_hp)*100)
         elif pok.hp/op_pokemon_hp > 0.20:
            draw_hp_bar2(screen,pok.rect.x,pok.rect.y,(pok.hp/op_pokemon_hp)*100)
         else:
            draw_hp_bar3(screen,pok.rect.x,pok.rect.y,(pok.hp/op_pokemon_hp)*100)
         draw_text2(screen,f"{int(pok.hp)}/{op_pokemon_hp}",10,pok.rect.centerx,pok.rect.y)
         draw_text1(screen,"ATTACK:",10,pok.rect.x,280)
         draw_text1(screen,f"Pokemones: {len(op_pokemon_list)}",15,pok.rect.x,295)
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
"""