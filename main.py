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
                  pok.hp -= damage(op_pokemon_attack,pok)
                  self.ultimo_ataque = pygame.time.get_ticks()
      else:
         for poke in all_sprites:
            if poke.team_int == 1:
               if pygame.time.get_ticks() - self.ultimo_ataque > self.tiempo_entre_ataques:
                  poke.hp -= damage(player_pokemon_attack,poke)
                  self.ultimo_ataque = pygame.time.get_ticks()
               
            

      if self.hp <= 0:
         if self.team_int ==0:
            player_pokemon_list.remove(self)
         else:
            op_pokemon_list.remove(self)
            
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
         self.image = pygame.image.load("img/text/2.png")
      elif self.int == 1:
         self.image = pygame.image.load("img/text/1.png")
      self.image.set_colorkey(WHITE)



pokemon_images = []
pokemon_list = ["img/pok/abomasnow.png","img/pok/abra.png","img/pok/absol.png",
                "img/pok/aerodactyl.png","img/pok/aggron.png","img/pok/aipom.png",
                "img/pok/alakazam.png","img/pok/altaria.png","img/pok/ambipom.png",
                "img/pok/ampharos.png","img/pok/anorith.png","img/pok/arbok.png", #10 anorith
                "img/pok/arcanine.png","img/pok/arceus.png","img/pok/ariados.png",
                "img/pok/armaldo.png","img/pok/aron.png","img/pok/articuno.png",
                "img/pok/audino.png","img/pok/azelf.png","img/pok/azurill.png", #20 azurill
                "img/pok/bagon.png","img/pok/baltoy.png","img/pok/banette.png",
                "img/pok/barboach.png","img/pok/bastiodon.png","img/pok/bayleef.png",
                "img/pok/beautifly.png","img/pok/beedrill.png","img/pok/beldum.png",
                "img/pok/bellossom.png","img/pok/bellsprout.png","img/pok/bibarel.png", #30 bellosom
                "img/pok/bidoof.png","img/pok/blastoise.png","img/pok/blaziken.png",
                "img/pok/blissey.png","img/pok/blitzle.png","img/pok/boldore.png",
                "img/pok/bonsly.png","img/pok/breloom.png","img/pok/bronzong.png", #40 breloom
                "img/pok/bronzor.png","img/pok/budew.png","img/pok/buizel.png",
                "img/pok/bulbasaur.png","img/pok/buneary.png","img/pok/burmy.png", 
                "img/pok/butterfree.png","img/pok/cacnea.png","img/pok/cacturne.png", #50 cacturne
                "img/pok/camerupt.png","img/pok/carnivine.png","img/pok/carvanha.png",
                "img/pok/cascoon.png","img/pok/castform.png","img/pok/caterpi.png",
                "img/pok/celebi.png","img/pok/chansey.png","img/pok/charizard.png",
                "img/pok/charmander.png","img/pok/charmeleon.png","img/pok/chatot.png", #60 charmander
                "img/pok/cherrim.png","img/pok/cherubi.png","img/pok/chikorita.png",
                "img/pok/chimchar.png","img/pok/chimecho.png","img/pok/chinchou.png",
                "img/pok/chingling.png","img/pok/clamperl.png","img/pok/claydol.png", #70 clamperl
                "img/pok/clefable.png","img/pok/clefairy.png","img/pok/cleffa.png",
                "img/pok/cloyster.png","img/pok/combee.png","img/pok/combusken.png",
                "img/pok/conkeldurr.png","img/pok/corpish.png","img/pok/corsola.png", #80 corsola
                "img/pok/cradily.png","img/pok/cranidos.png","img/pok/crawdaunt.png",
                "img/pok/cresselia.png","img/pok/croagunk.png","img/pok/crobat.png",
                "img/pok/croconaw.png","img/pok/cubone.png","img/pok/cyndaquil.png",
                "img/pok/delcatty.png","img/pok/delibird.png","img/pok/deoxys.png", #90 delcatty
                "img/pok/dewgong.png","img/pok/diglett.png","img/pok/ditto.png",
                "img/pok/dodrio.png","img/pok/doduo.png","img/pok/donphan.png",
                "img/pok/dragonair.png","img/pok/dragonite.png","img/pok/dratini.png", #100 dragonite
                "img/pok/drifblim.png","img/pok/drifloon.png","img/pok/drowzee.png",
                "img/pok/dugtrio.png","img/pok/dunsparce.png","img/pok/dusclops.png",
                "img/pok/duskull.png","img/pok/dustox.png","img/pok/eevee.png", #110 eevee
                "img/pok/ekans.png","img/pok/electabuzz.png","img/pok/electrike.png",
                "img/pok/electrode.png","img/pok/elekid.png","img/pok/empoleon.png",
                "img/pok/entei.png","img/pok/espeon.png","img/pok/exeggcute.png",
                "img/pok/exeggutor.png","img/pok/exploud.png","img/pok/farfetch.png", #120 exeggutor
                "img/pok/fearow.png","img/pok/feebas.png","img/pok/feraligatr.png",
                "img/pok/flaaffy.png","img/pok/flareon.png","img/pok/floatzel.png",
                "img/pok/flygon.png","img/pok/forretress.png","img/pok/furret.png", #130 forretress
                "img/pok/gabite.png","img/pok/garchomp.png","img/pok/gardevoir.png",
                "img/pok/gastly.png","img/pok/gastrodon.png","img/pok/gengar.png",
                "img/pok/geodude.png","img/pok/gible.png","img/pok/girafarig.png", #140 girfarig
                "img/pok/glalie.png","img/pok/glameow.png","img/pok/gligar.png",
                "img/pok/gloom.png","img/pok/golbat.png","img/pok/goldeen.png",
                "img/pok/golduck.png","img/pok/golem.png","img/pok/gorebyss.png",
                "img/pok/granbull.png","img/pok/graveler.png","img/pok/grimer.png", #150 granbull
                "img/pok/grotle.png","img/pok/groudon.png","img/pok/grovyle.png",
                "img/pok/growlithe.png","img/pok/grumpig.png","img/pok/gulpin.png",
                "img/pok/gyarados.png","img/pok/happiny.png","img/pok/hariyama.png", #160 happiny
                "img/pok/haunter.png","img/pok/heracross.png","img/pok/hippopotas.png",
                "img/pok/hippowdon.png","img/pok/hitmonchan.png","img/pok/hitmonlee.png",
                "img/pok/hitmontop.png","img/pok/honchkrow.png","img/pok/ho-oh.png", #170 ho-oh
                "img/pok/hoothoot.png","img/pok/hoppip.png","img/pok/horsea.png",
                "img/pok/houndoom.png","img/pok/houndour.png","img/pok/huntail.png",
                "img/pok/hypno.png","img/pok/igglybuff.png","img/pok/infernape.png",
                "img/pok/illumise.png","img/pok/ivysaur.png","img/pok/jigglypuff.png", #180 illumise
                "img/pok/jirachi.png","img/pok/jolteon.png","img/pok/jumpluff.png",
                "img/pok/jynx.png","img/pok/kabuto.png","img/pok/kabutops.png",
                "img/pok/kadabra.png","img/pok/kakuna.png","img/pok/kangaskhan.png", #190 kakuna
                "img/pok/kecleon.png","img/pok/kingdra.png","img/pok/kingler.png",
                "img/pok/kirlia.png","img/pok/koffing.png","img/pok/krabby.png",
                "img/pok/kricketot.png","img/pok/kricketune.png","img/pok/kyogre.png", #200 kyogre
                "img/pok/lairon.png","img/pok/lanturn.png","img/pok/lapras.png",
                "img/pok/larvitar.png","img/pok/latias.png","img/pok/latios.png",
                "img/pok/ledian.png","img/pok/ledyba.png","img/pok/lickitung.png",
                "img/pok/lileep.png","img/pok/linoone.png","img/pok/lombre.png", #210 lileep
                "img/pok/lopunny.png","img/pok/lotad.png","img/pok/loudred.png",
                "img/pok/lucario.png","img/pok/ludicolo.png","img/pok/lugia.png",
                "img/pok/lunatone.png","img/pok/luvdisc.png","img/pok/luxio.png", #220 luvdisc
                "img/pok/luxray.png","img/pok/machamp.png","img/pok/machoke.png",
                "img/pok/machop.png","img/pok/magby.png","img/pok/magcargo.png",
                "img/pok/magikarp.png","img/pok/magmar.png","img/pok/magnemite.png", #230 magnemite
                "img/pok/magneton.png","img/pok/makuhita.png","img/pok/manectric.png",
                "img/pok/mankey.png","img/pok/mantine.png","img/pok/mareep.png",
                "img/pok/marill.png","img/pok/marowak.png","img/pok/marshtomp.png",
                "img/pok/masquerain.png","img/pok/mawile.png","img/pok/medicham.png", #240 masquerain
                "img/pok/meditite.png","img/pok/meganium.png","img/pok/meowth.png",
                "img/pok/metagross.png","img/pok/metang.png","img/pok/metapod.png",
                "img/pok/mew.png","img/pok/mewtwo.png","img/pok/mightyena.png", #250 mewtwo
                "img/pok/milotic.png","img/pok/miltank.png","img/pok/mimejr.png",
                "img/pok/minum.png","img/pok/misdreavus.png","img/pok/mismagius.png",
                "img/pok/moltres.png","img/pok/monferno.png","img/pok/mothim.png", #260 mothim
                "img/pok/mr.mime.png","img/pok/mudkip.png","img/pok/muk.png",
                "img/pok/munchlax.png","img/pok/murkrow.png","img/pok/natu.png",
                "img/pok/nidoking.png","img/pok/nidoqueen.png","img/pok/nidoran1.png", 
                "img/pok/nidoran2.png","img/pok/nidorina.png","img/pok/nidorino.png", #270 nidoran2
                "img/pok/nincada.png","img/pok/ninetales.png","img/pok/ninjask.png",
                "img/pok/noctowl.png","img/pok/nosepass.png","img/pok/numel.png",
                "img/pok/nuzleaf.png","img/pok/octillery.png","img/pok/oddish.png", #280 octillery
                "img/pok/omanyte.png","img/pok/omastar.png","img/pok/onix.png",
                "img/pok/pachirisu.png","img/pok/paras.png","img/pok/parasect.png",
                "img/pok/pelipper.png","img/pok/persian.png","img/pok/phanpy.png", #290 phanpy
                "img/pok/pichu.png","img/pok/pidgeot.png","img/pok/pidgeotto.png",
                "img/pok/pidgey.png","img/pok/pikachu.png","img/pok/piloswine.png",
                "img/pok/pineco.png","img/pok/pinsir.png","img/pok/piplup.png",
                "img/pok/plusle.png","img/pok/politoed.png","img/pok/poliwag.png", #300 plusle
                "img/pok/poliwhirl.png","img/pok/poliwrath.png","img/pok/ponyta.png",
                "img/pok/poochyena.png","img/pok/porygon.png","img/pok/porygon2.png",
                "img/pok/primeape.png","img/pok/prinplup.png","img/pok/psyduck.png", #310 prinplup
                "img/pok/pupitar.png","img/pok/purugly.png",
                "img/pok/quagsire.png","img/pok/quilava.png","img/pok/qwilfish.png",
                "img/pok/raichu.png","img/pok/raikou.png","img/pok/ralts.png",
                "img/pok/rampardos.png","img/pok/rapidash.png","img/pok/raticate.png", # 320 rapardos
                "img/pok/rattata.png","img/pok/rayquaza.png","img/pok/regice.png",
                "img/pok/regirock.png","img/pok/registeel.png","img/pok/relicanth.png",
                "img/pok/remoraid.png","img/pok/rhydon.png","img/pok/rhyhorn.png", #330 rhydon
                "img/pok/riolu.png","img/pok/roselia.png","img/pok/roserade.png",
                "img/pok/sableye.png","img/pok/salamence.png","img/pok/sandshrew.png",
                "img/pok/sandslash.png","img/pok/sceptille.png","img/pok/scizor.png", #340 scizor
                "img/pok/scyther.png","img/pok/seadra.png","img/pok/seaking.png",
                "img/pok/sealeo.png","img/pok/seedot.png","img/pok/seel.png", 
                "img/pok/sentret.png","img/pok/seviper.png","img/pok/sharpedo.png",
                "img/pok/shedinja.png","img/pok/shelgon.png","img/pok/shellder.png",#350 shedinja
                "img/pok/shellos.png","img/pok/shieldon.png","img/pok/shiftry.png",
                "img/pok/shinx.png","img/pok/shroomish.png","img/pok/shukle.png",
                "img/pok/shuppet.png","img/pok/silcoon.png","img/pok/skarmory.png",#360 silcoon
                "img/pok/skiploom.png","img/pok/skitty.png","img/pok/skuntank.png","img/pok/slaking.png",
                "img/pok/slakoth.png","img/pok/slowbro.png","img/pok/slowking.png",
                "img/pok/slowpoke.png","img/pok/slugma.png","img/pok/smeargle.png",#370 slugma
                "img/pok/smoochum.png","img/pok/sneasel.png","img/pok/snorlax.png",
                "img/pok/snorunt.png","img/pok/snubbull.png","img/pok/solrock.png",
                "img/pok/spearow.png","img/pok/spheal.png","img/pok/spinarak.png", #380 spinarak
                "img/pok/spinda.png","img/pok/spiritomb.png","img/pok/spoink.png",
                "img/pok/squirtle.png","img/pok/stantler.png","img/pok/staraptor.png",
                "img/pok/staravaria.png","img/pok/starly.png","img/pok/starmie.png",
                "img/pok/staryu.png","img/pok/steelix.png","img/pok/stunky.png",#390 staryu
                "img/pok/sudowoodo.png","img/pok/suicune.png","img/pok/sunflora.png",
                "img/pok/sunkern.png","img/pok/surskit.png","img/pok/swablu.png",
                "img/pok/swalot.png","img/pok/swampert.png","img/pok/swellow.png", #400 swampert
                "img/pok/swinub.png","img/pok/taillow.png","img/pok/tangela.png",
                "img/pok/tauros.png","img/pok/teddiursa.png","img/pok/tentacool.png",
                "img/pok/tentacruel.png","img/pok/togepi.png","img/pok/togetic.png", #410 togetic
                "img/pok/torchik.png","img/pok/torkoal.png","img/pok/torterra.png",
                "img/pok/totodile.png","img/pok/trapinch.png","img/pok/treecko.png",
                "img/pok/tropius.png","img/pok/turtwig.png","img/pok/typhlosion.png",
                "img/pok/tyranitar.png","img/pok/tyrogue.png","img/pok/umbreon.png", #420 tyranitar
                "img/pok/unown.png","img/pok/ursaring.png","img/pok/vaporeon.png",
                "img/pok/venomoth.png","img/pok/venonat.png","img/pok/venusaur.png",
                "img/pok/vespiquen.png","img/pok/vibrava.png","img/pok/victreebel.png", #430 vibrava
                "img/pok/vigoroth.png","img/pok/vileplume.png","img/pok/volbeat.png",
                "img/pok/voltorb.png","img/pok/vulpix.png","img/pok/wailmer.png",
                "img/pok/wailord.png","img/pok/walrein.png","img/pok/wartortle.png", #440 wartortle
                "img/pok/weedle.png","img/pok/weepinbell.png","img/pok/weezing.png",
                "img/pok/whiscash.png","img/pok/whismur.png","img/pok/wigglytuff.png",
                "img/pok/wingull.png","img/pok/wobbuffet.png","img/pok/wooper.png",
                "img/pok/wormadam.png","img/pok/wurmple.png","img/pok/wynaut.png",#450 wormadam
                "img/pok/xatu.png","img/pok/yanma.png","img/pok/zangoose.png",
                "img/pok/zapdos.png","img/pok/zigzagoon.png","img/pok/zubat.png"]#458 zubat
for img in pokemon_list:
	pokemon_images.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

"""

"""
pokemon_type_list1 = [16,12,13,5,15,0,12,17,0,11,5, 3,8,0,6,5,15,16,0,12,0, 17,4,7,9,5,10,6,6,15,10, #30v
                      10,0,0,9,8,0,11,5,5,10, 15,15,10,9,10,0,6,6,10,10, 8,10,9,6,0,6,12,0,8,8, #60v
                      8,0,10,10,10,8,12,9,12,9, 4,14,14,14,9,6,8,1,9,9, 5,5,9,12,3,3,9,4,8,0, #90v
                      16,12,9,4,0,0,0,4,17,17, 17,7,7,12,4,0,7,7,6,0, 3,11,11,11,11,9,8,12,10,10, #120v
                      0,0,0,9,9,11,8,9,4,6, 0,17,17,12,7,9,7,5,17,0, 16,0,4,10,3,9,9,5,9,14, #150v
                      5,3,10,4,10,8,12,3,9,0, 1,7,6,4,4,1,1,1,13,8, 0,10,9,13,13,9,12,0,8,6, #180v
                      10,0,15,11,10,16,5,5,12,6, 0,0,9,9,12,3,9,6,6,9, 15,9,9,5,17,17,6,6,0,5, #210v
                      0,9,0,9,0,1,9,12,5,9, 11,11,1,1,1,8,8,9,8,11, 11,1,11,1,9,11,9,4,9,6, #240v
                      15,1,1,10,0,15,15,6,12,12, 13,9,0,12,11,7,7,8,8,6, 12,9,3,0,13,12,3,3,3,3, #270v
                      3,3,6,8,6,0,5,8,10,9, 10,5,5,5,11,6,6,9,0,4, 11,0,0,0,11,16,6,6,9,11, #300v
                      9,9,9,9,8,13,0,0,1,9, 9,5,0,9,8,9,11,11,12,5, 8,0,0,17,16,5,15,9,9,4, #330
                      4,1,10,10,13,17,4,4,10,6, 6,9,9,16,10,9,0,3,9,6, 17,9,9,5,10,11,10,6,7,6, #360
                      15,10,0,3,0,0,9,9,9,8, 0,16,13,0,16,14,5,0,16,6, 0,7,12,9,0,0,0,0,9,9, #390
                      15,3,5,9,10,10,10,2,3,9, 0,16,0,10,0,0,9,9,14,14, 8,8,10,9,4,10,10,10,8,5, #420
                      1,13,12,0,9,6,6,10,6,4, 10,0,10,6,11,8,9,9,16,9, 6,10,3,9,0,9,0,12,9,6, #450
                      6,12,12,6,0,11,0,3]#458v
#0..normal    1..lucha    2..volador   3..veneno   4..tierra   5..roca   6..bicho      78cacn
#7..fantasma   8..fuego   9..agua   10..planta   11..electrico   12..psiquico
#13..siniestro   14..hada   15..acero   16..hielo   17..dragon           ( )

pokemon_type_list2 = [18,18,18,2,5,18,18,2,18,18,6, 18,18,18,3,6,5,2,18,18,14, #20v
                      18,12,18,4,15,18,2,3,12,18, 3,9,18,18,1,18,18,18,18,1, #40v
                      12,12,3,18,3,18,18,2,18,13, 4,18,13,18,18,18,10,18,2,18, #60v
                      18,2,18,18,18,18,18,11,18,18, 12,18,18,18,16,2,1,18,18,5, #80v
                      10,18,13,18,1,2,18,18,18,18, 2,18,16,18,18,2,2,18,18,2, #100v
                      18,2,2,18,18,18,18,18,3,18, 18,18,18,18,18,15,18,18,12,12, #120v
                      18,2,2,18,18,18,18,18,17,15, 18,4,4,14,3,4,3,4,4,12, #140v
                      18,18,2,3,2,18,18,4,18,18, 4,18,18,18,18,18,18,18,2,18, #160
                      18,3,1,18,18,18,18,18,2,2, 2,2,18,8,8,18,18,14,1,18, #180v
                      3,14,12,18,2,12,9,9,18,3, 18,18,17,18,14,18,18,18,18,18, #200v
                      5,11,16,4,12,12,2,2,18,10, 18,10,18,10,18,18,10,2,12,18, #220v
                      18,18,18,18,18,18,5,18,18,15, 15,18,18,18,2,18,14,18,4,2, #240v
                      14,12,12,18,18,12,12,18,18,18, 18,18,18,14,18,18,18,2,1,2, #260v
                      14,18,18,18,2,2,4,4,18,18, 18,18,4,18,2,2,18,4,13,18, #280v
                      3,9,9,4,18,10,10,2,18,18, 18,2,2,2,18,4,18,18,18,18, #300v
                      18,18,18,1,18,18,18,18,18,18, 18,4,18,4,18,3,18,18,14,18, #320v
                      18,18,18,2,18,18,18,5,18,5, 5,18,3,3,7,18,18,18,18,15, #340v
                      2,18,18,9,18,18,18,18,13,7, 18,18,18,15,13,18,18,5,18,18, #360
                      2,2,18,13,18,18,12,12,12,18, 18,12,16,18,18,18,12,2,9,3, #380
                      18,13,18,18,18,2,2,2,12,18, 4,13,18,18,18,18,9,0,18,4, #400
                      2,4,2,18,18,18,3,3,18,2, 18,18,4,18,18,18,2,18,18,13, #420v
                      18,18,18,18,18,3,3,3,2,17, 3,18,3,18,18,18,18,18,9,18, #440
                      3,3,18,2,18,4,14,18,4,10, 18,18,2,2,18,2,18,2]#458v

"""
"""
pokemon_hp = [85,50,70,80,120,80,80,67,80,90,80, 70,85,85,70,80,75,80,85,75,90, #20v
              
              73,75,70,90,80,90,85,90,80,90, 85,90,116,85,85,270,95,85,70,70, #40v
              
              80,70,70,70,74,70,80,70,78,80, 80,85,77,90,85,100,130,259,67,73, #60
              
              70,70,70,70,70,70,80,103,70,64, 80,103,97,90,100,85,80,85,70,87, #80
              
              90,70,75,105,85,80,90,84,75,90, 75,80,120,56,85,70,62,70,72,70, #100
              
              75,100,80,70,50,100,72,68,85,89, 72,60,65,70,75,90,80,80,90,105, #120
              
              100,77,90,35,90,100,80,80,90,90, 58,80,90,90,68,120,88,68,80,100, #140
              
              90,90,70,75,85,85,110,110,40,85, 90,90,80,70,70,75,70,110,90,201, #160
              
              90,80,90,88,98,80,80,80,70,80, 70,60,89,80,72,70,79,95,74,90, #180
              
              90,177,65,70,90,80,70,70,70,90, 100,80,90,70,70,70,60,108,115,70, #200
              
              80,100,100,83,70,70,80,89,100,85, 70,60,80,70,70,70,70,80,70,70, #220
              
              80,90,70,65,90,70,65,110,80,52, 80,80,70,70,90,93,150,70,80,70, #240
              
              70,75,70,100,87,65,60,120,90,100, 80,60,90,70,70,68,80,80,80,70, #260
              
              70,70,90,100,73,70,110,110,89,98, 90,90,70,75,60,100,70,70,60,90, #280
              
              71,55,90,68,70,68,70,60,85,110, 70,95,93,92,74,100,80,70,70,60, #300
              
              100,82,90,100,70,70,90,90,80,80, 80,90,100,95,90,75,80,80,70,80, #320
              
              80,85,74,60,70,70,65,90,74,100, 90,70,70,80,70,90,74,100,70,95, #340
              
              75,100,100,70,70,110,80,70,65,70, 80,65,110,80,70,70,70,100,65,80, #360
              
              100,100,70,90,90,70,90,90,110,80, 120,70,65,120,70,85,80,82,70,85, #380
              
              70,65,70,80,90,97,80,70,80,70, 95,70,80,80,80,70,70,70,120,90, #400
              
              80,99,70,80,90,80,77,100,80,83, 70,70,100,80,90,70,70,70,95,120, #420
              
              80,100,75,120,130,78,90,95,75,85, 100,80,100,75,75,80,100,120,90,110, #440
              
              60,90,100,87,80,100,150,220,112,75, 100,150,66,80,74,80,100,92]#458

tipo_ataque_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

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

matriz_efectividad = [
   #1N, 2L, 3V, 4V, 5T, 6R, 7B, 8F, 9F, 10A, 11P, 12E, 13P, 14S, 15H, 16A, 18D
   [1,  1,  1,  1,  1,  0.625,  1, 0.625,  1,  1,  1,  1,  1,  1,  1,  0.625,  1,  1],#1Normal

   [1.6, 0.625,  1, 0.625,  1,  1.6, 0.625, 0.625,  1,  1,  1,  1, 0.625,  1.6, 0.625,  1.6,  1,  1],#2lucha
   
   [1,  1.6, 0.625,  1,  1,  0.625,  1.6,  1,  1,  1,  1.6, 0.625,  1,  1,  1,  0.625,  1,  1],#3volador
   
   [1,  1,  1, 0.625, 0.625,  0.625,  1,  1,  1,  1,  1.6,  1,  1,  1,  1.6,  0.625,  1,  1],#4veneno
   
   [1,  1,  1,  1.6, 0.625, 1.6, 0.625,  1,  1.6,  1,  0.625,  1.6,  1,  1,  1,  1.6,  1,         1],#5tierra
   
   [1, 0.625,  1.6,  1, 0.625, 0.625,  1.6,  1,  1.6,  1,  1,  1,  1,  1,  1,  0.625,  1,        1],#6roca
   
   [1, 0.625,  1, 0.625,  1,  1, 0.625,  1, 0.625,  1,  1.6,  1,  1.6,  1.6, 0.625,  0.625,  1,      1],#7bicho
   
   [0.625,  1,  1,  1,  1,  1,  1,  1.6,  1,  1,  1,  1,  1.6, 0.625,  1,  1,  1,       1],#8fantasma
   
   [1,  1,  1,  1,  1,  0.625,  1.6,  1, 0.625, 0.625,  1.6,  1,  1,  1,  1,  1.6,  1.6,     0.625],#9fuego
   
   [1,  1,  1,  1,  1.6,  1.6,  1,  1,  1.6, 0.625, 0.625,  1,  1,  1,  1,  1,  1,       0.625],#10agua
   
   [1,  1,  1, 0.625,  1.6,  1.6, 0.625,  1, 0.625, 1.6, 0.625,  1,  1,  1,  1,  0.625,  1,       0.625],#11planta
   
   [1,  1,  1.6, 1,  0.625,  1,  1,  1,  1,  1.6, 0.625, 0.625,  1,  1,  1,  1,  1,        0.625],#12electrico
   
   [1,  1.6,  1,  1.6,  1,  1,  1,  1,  1,  1,  1,  1, 0.625, 0.625,  1,  0.625,  1,        1],#13psiquico
   
   [1, 0.625,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1.6, 0.625, 0.625,  1,  1,        1],#14siniestro
   
   [1,  1.6,  1, 0.625,  1,  1,  1,  1, 0.625,  1,  1,  1,  1,  1.6,  1, 0.625,  1,  1.6],#15hada
   
   [1,  1,  1,  1,  1,  1.6,  1,  1, 0.625, 0.625,  1, 0.625,  1,  1,  1.6,  0.625,  1,  1],#16acero
   
   [1,  1,  1,  1.6,  1.6,  1,  1,  1, 0.625, 0.625,  1.6,  1,  1,  1,  1,  0.625,  0.625,  1.6],#17hielo
   
   [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.625,  0.625,  1,  1.6],#18dragon
]

def damage(tip_atacante,defensor):
#   poder_de_ataque = atacante.poder_de_ataque
   tipo_atacante = tip_atacante
   tipo_defensor1 = pokemon_type_list1[defensor.img_int]
   tipo_defensor2 = pokemon_type_list2[defensor.img_int]


   efectividad_total = 1
   if tipo_defensor2 is not 18:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor2]
   else:
      efectividad_total *= matriz_efectividad[tipo_atacante][tipo_defensor1]

   daño = 6*efectividad_total
   return daño


player_pokemon_list = []
op_pokemon_list = []

player_pokemon_attack = 0
op_pokemon_attack = 0

fighting = True

numero_max_pokemon = 458

carga1 = True
game_over1 = False
game_over2 = False
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
      pokemon1 = Pokemon(randint(0,numero_max_pokemon),0)
      player_pokemon_list.append(pokemon1)
      all_sprites.add(pokemon1)
      player_pokemon_hp = pokemon1.hp
      if pokemon_type_list2[pokemon1.img_int] != 18:
         player_pokemon_attack = random.choice([pokemon_type_list1[pokemon1.img_int],pokemon_type_list2[pokemon1.img_int]])
      else:
         player_pokemon_attack = pokemon_type_list1[pokemon1.img_int]
      type1 = Type(player_pokemon_attack,270,460,0,50,50)
      type_pokemon.add(type1)
      type1a = Type(pokemon_type_list1[pokemon1.img_int],pokemon1.rect.x,pokemon1.rect.top - 30,0,25,25)
      type1b = Type(pokemon_type_list2[pokemon1.img_int],pokemon1.rect.x + 30,pokemon1.rect.top - 30,0,25,25)
      type2_pokemon.add(type1a,type1b)
      pokemon2 = Pokemon(randint(0,numero_max_pokemon),0)
      player_pokemon_list.append(pokemon2)
      pokemon3 = Pokemon(randint(0,numero_max_pokemon),0)
      player_pokemon_list.append(pokemon3)
      pokemon4 = Pokemon(randint(0,numero_max_pokemon),1)
      op_pokemon_list.append(pokemon4)
      all_sprites.add(pokemon4)
      op_pokemon_hp = pokemon4.hp
      if pokemon_type_list2[pokemon4.img_int] != 18:
         op_pokemon_attack = random.choice([pokemon_type_list1[pokemon4.img_int],pokemon_type_list2[pokemon4.img_int]])
      else:
         op_pokemon_attack = pokemon_type_list1[pokemon4.img_int]
      type2 = Type(op_pokemon_attack,670,260,1,50,50)
      type_pokemon.add(type2)
      type2a = Type(pokemon_type_list1[pokemon4.img_int],pokemon4.rect.x,pokemon4.rect.top - 30,1,25,25)
      type2b = Type(pokemon_type_list2[pokemon4.img_int],pokemon4.rect.x + 30,pokemon4.rect.top - 30,1,25,25)
      type2_pokemon.add(type2a,type2b)
      pokemon5 = Pokemon(randint(0,numero_max_pokemon),1)
      op_pokemon_list.append(pokemon5)
      pokemon6 = Pokemon(randint(0,numero_max_pokemon),1)
      op_pokemon_list.append(pokemon6)
      pokeball1 = Pokeball(0,0)
      pokeball2 = Pokeball(1,0)
      pokeballs.add(pokeball1,pokeball2)

   if len(player_pokemon_list) != 0 and len(op_pokemon_list) != 0:
      if len(all_sprites) < 2:
         for pok in all_sprites:
            if pok.team_int == 0:
               all_sprites.add(random.choice(op_pokemon_list))
               for poke in all_sprites:
                  if poke.team_int == 1:
                     op_pokemon_hp = poke.hp
                     if pokemon_type_list2[poke.img_int] != 18:
                        op_pokemon_attack = random.choice([pokemon_type_list1[poke.img_int],pokemon_type_list2[poke.img_int]])
                     else:
                        op_pokemon_attack = pokemon_type_list1[poke.img_int]
                     for ty in type_pokemon:
                        if ty.team_int == 1:
                           ty.kill()
                           type2 = Type(op_pokemon_attack,670,260,1,50,50)
                           type_pokemon.add(type2)
                     for ty in type2_pokemon:
                        if ty.team_int == 1:
                           ty.kill()
                     type2a = Type(pokemon_type_list1[poke.img_int],poke.rect.x,poke.rect.top - 30,1,25,25)
                     type2b = Type(pokemon_type_list2[poke.img_int],poke.rect.x + 30,poke.rect.top - 30,1,25,25)
                     type2_pokemon.add(type2a,type2b)
            else:
               all_sprites.add(random.choice(player_pokemon_list))
               for pokem in all_sprites:
                  if pokem.team_int == 0:
                     player_pokemon_hp = pokem.hp
                     if pokemon_type_list2[pokem.img_int] != 18:
                        player_pokemon_attack = random.choice([pokemon_type_list1[pokem.img_int],pokemon_type_list2[pokem.img_int]])
                     else:
                        player_pokemon_attack = pokemon_type_list1[pokem.img_int]
                     for typ in type_pokemon:
                        if typ.team_int == 0:
                           typ.kill()
                           type1 = Type(player_pokemon_attack,270,460,0,50,50)
                           type_pokemon.add(type1)
                     for typ in type2_pokemon:
                        if typ.team_int == 0:
                           typ.kill()
                     type1a = Type(pokemon_type_list1[pokem.img_int],pokem.rect.x,pokem.rect.top - 30,0,25,25)
                     type1b = Type(pokemon_type_list2[pokem.img_int],pokem.rect.x + 30,pokem.rect.top - 30,0,25,25)
                     type2_pokemon.add(type1a,type1b)
   #print(len(player_pokemon_list))
   if len(player_pokemon_list) == 0 or len(op_pokemon_list) == 0:
      if len(player_pokemon_list) == 0:
         game_over2 = True
      else:
         game_over1 = True

   

   screen.fill(BLACK)
   all_sprites.update()
   pokeball1.int = len(player_pokemon_list)
   pokeball2.int = len(op_pokemon_list)
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

      #82jigg177,83jolt70,84jumpluff90,85jynx80,86kabut70,87kada70,88kakuna70,89kang90,90kingdra100,
#91kingler90,92koffing70,93krabb70,94lapras100, 60,95larvitar80,96
#82
#77porygon, +101caterpc344, 76spearow470, 63shelder, 100seel,79hypno, 92pidgey, 82sandygast, 
# 90rhyhorn489,1*, 90venonat, 95noibat, 89luv(pezrosa),lunatone87,sableye70,0*, absol57,0*,phantum75,
#stufful89,2*,seviper74, omanyte58,snubbull85,
"""