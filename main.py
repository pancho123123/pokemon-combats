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
      elif reg_int == 1:
         self.img_int = randint(0,99)
         self.image = pokemon_images_johto[self.img_int]
         self.type1 = pokemon_type_johto1[self.img_int]
         self.type2 = pokemon_type_johto2[self.img_int]
         self.hp = pokemon_hp_johto[self.img_int]
      elif reg_int == 2:
         self.img_int = randint(0,134)
         self.image = pokemon_images_hoenn[self.img_int]
         self.type1 = pokemon_type_hoenn1[self.img_int]
         self.type2 = pokemon_type_hoenn2[self.img_int]
         self.hp = pokemon_hp_hoenn[self.img_int]
      elif reg_int == 3:
         self.img_int = randint(0,106)
         self.image = pokemon_images_sinnoh[self.img_int]
         self.type1 = pokemon_type_sinnoh1[self.img_int]
         self.type2 = pokemon_type_sinnoh2[self.img_int]
         self.hp = pokemon_hp_sinnoh[self.img_int]
      elif reg_int == 4:
         self.img_int = randint(0,155)
         self.image = pokemon_images_teselia[self.img_int]
         self.type1 = pokemon_type_teselia1[self.img_int]
         self.type2 = pokemon_type_teselia2[self.img_int]
         self.hp = pokemon_hp_teselia[self.img_int]
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
      # else:
      #    for poke in all_sprites:
      #       if poke.team_int == 1:
      #          if pygame.time.get_ticks() - self.ultimo_ataque > self.tiempo_entre_ataques:
      #             poke.hp -= damage(player_pokemon_attack,poke)
      #             self.ultimo_ataque = pygame.time.get_ticks()
               
            

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



pokemon_images_kanto = []
pokemon_list_kanto = [
   "img/pok/bulbasaur.png","img/pok/ivysaur.png","img/pok/venusaur.png",
   "img/pok/charmander.png","img/pok/charmeleon.png","img/pok/charizard.png",
   "img/pok/squirtle.png","img/pok/wartortle.png","img/pok/blastoise.png",
   "img/pok/caterpie.png","img/pok/metapod.png","img/pok/butterfree.png", #10 metap
   "img/pok/weedle.png","img/pok/kakuna.png","img/pok/beedrill.png",
   "img/pok/pidgey.png","img/pok/pidgeotto.png","img/pok/pidgeot.png",
   "img/pok/rattata.png","img/pok/raticate.png","img/pok/spearow.png", #20 spearow
   "img/pok/fearow.png","img/pok/ekans.png","img/pok/arbok.png",
   "img/pok/pikachu.png","img/pok/raichu.png","img/pok/sandshrew.png",
   "img/pok/sandslash.png","img/pok/nidoran1.png","img/pok/nidorino.png",
   "img/pok/nidoking.png","img/pok/nidoran2.png","img/pok/nidorina.png", #30 nidoking
   "img/pok/nidoqueen.png","img/pok/clefairy.png","img/pok/clefable.png",
   "img/pok/vulpix.png","img/pok/ninetales.png","img/pok/jigglypuff.png",
   "img/pok/wigglytuff.png","img/pok/zubat.png","img/pok/golbat.png", #40 zubat
   "img/pok/oddish.png","img/pok/gloom.png","img/pok/vileplume.png",
   "img/pok/paras.png","img/pok/parasect.png","img/pok/venonat.png",
   "img/pok/venomoth.png","img/pok/diglett.png","img/pok/dugtrio.png", #50 dugtrio
   "img/pok/meowth.png","img/pok/persian.png","img/pok/psyduck.png",
   "img/pok/golduck.png","img/pok/mankey.png","img/pok/primeape.png",
   "img/pok/growlithe.png","img/pok/arcanine.png","img/pok/poliwag.png", 
   "img/pok/poliwhirl.png","img/pok/poliwrath.png","img/pok/abra.png", #60 poliwhi
   "img/pok/kadabra.png","img/pok/alakazam.png","img/pok/machop.png",
   "img/pok/machoke.png","img/pok/machamp.png","img/pok/bellsprout.png",
   "img/pok/weepinbell.png","img/pok/victreebel.png","img/pok/tentacool.png", #70 victr
   "img/pok/tentacruel.png","img/pok/geodude.png","img/pok/graveler.png",
   "img/pok/golem.png","img/pok/ponyta.png","img/pok/rapidash.png",
   "img/pok/slowpoke.png","img/pok/slowbro.png","img/pok/magnemite.png", # 80 magnemite
   "img/pok/magneton.png","img/pok/farfetchd.png","img/pok/doduo.png",
   "img/pok/dodrio.png","img/pok/seel.png","img/pok/dewgong.png",
   "img/pok/grimer.png","img/pok/muk.png","img/pok/shellder.png",
   "img/pok/cloyster.png","img/pok/gastly.png","img/pok/haunter.png",  # 90 cloyster
   "img/pok/gengar.png","img/pok/onix.png","img/pok/drowzee.png",
   "img/pok/hypno.png","img/pok/krabby.png","img/pok/kingler.png",
   "img/pok/voltorb.png","img/pok/electrode.png","img/pok/exeggcute.png", # 100 electrode
   "img/pok/exeggutor.png","img/pok/cubone.png","img/pok/marowak.png",
   "img/pok/hitmonlee.png","img/pok/hitmonchan.png","img/pok/lickitung.png",
   "img/pok/koffing.png","img/pok/weezing.png","img/pok/rhyhorn.png", # 110 rhyhorn
   "img/pok/rhydon.png","img/pok/chansey.png","img/pok/tangela.png",
   "img/pok/kangaskhan.png","img/pok/horsea.png","img/pok/seadra.png",
   "img/pok/goldeen.png","img/pok/seaking.png","img/pok/staryu.png",
   "img/pok/starmie.png","img/pok/mrmime.png","img/pok/scyther.png", # 120 starmie
   "img/pok/jynx.png","img/pok/electabuzz.png","img/pok/magmar.png",
   "img/pok/pinsir.png","img/pok/tauros.png","img/pok/magikarp.png",
   "img/pok/gyarados.png","img/pok/lapras.png","img/pok/ditto.png", # 130 lapras
   "img/pok/eevee.png","img/pok/vaporeon.png","img/pok/jolteon.png",
   "img/pok/flareon.png","img/pok/porygon.png","img/pok/omanyte.png",
   "img/pok/omastar.png","img/pok/kabuto.png","img/pok/kabutops.png", # 140 kabutops
   "img/pok/aerodactyl.png","img/pok/snorlax.png","img/pok/articuno.png",
   "img/pok/zapdos.png","img/pok/moltres.png","img/pok/dratini.png",
   "img/pok/dragonair.png","img/pok/dragonite.png","img/pok/mewtwo.png",
   "img/pok/mew.png"           # 150 mew
                ]
for img in pokemon_list_kanto:
	pokemon_images_kanto.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_johto = []
pokemon_list_johto = [
   "img/pok/chikorita.png","img/pok/bayleef.png","img/pok/meganium.png",
   "img/pok/cyndaquil.png","img/pok/quilava.png","img/pok/typhlosion.png",
   "img/pok/totodile.png","img/pok/croconaw.png","img/pok/feraligatr.png",
   "img/pok/sentret.png","img/pok/furret.png","img/pok/hoothoot.png", # 10 furret
   "img/pok/noctowl.png","img/pok/ledyba.png","img/pok/ledian.png",
   "img/pok/spinarak.png","img/pok/ariados.png","img/pok/crobat.png",
   "img/pok/chinchou.png","img/pok/lanturn.png","img/pok/pichu.png", # 20 pichu
   "img/pok/cleffa.png","img/pok/igglybuff.png","img/pok/togepi.png",
   "img/pok/togetic.png","img/pok/natu.png","img/pok/xatu.png",
   "img/pok/mareep.png","img/pok/flaaffy.png","img/pok/ampharos.png",
   "img/pok/bellossom.png","img/pok/marill.png","img/pok/azumarill.png", # 30 bellosom
   "img/pok/sudowoodo.png","img/pok/politoed.png","img/pok/hoppip.png",
   "img/pok/skiploom.png","img/pok/jumpluff.png","img/pok/aipom.png",
   "img/pok/sunkern.png","img/pok/sunflora.png","img/pok/yanma.png", # 40 sunflora
   "img/pok/wooper.png","img/pok/quagsire.png","img/pok/espeon.png",
   "img/pok/umbreon.png","img/pok/murkrow.png","img/pok/slowking.png",
   "img/pok/misdreavus.png","img/pok/unown.png","img/pok/wobbuffet.png", # 50 wobbuffet
   "img/pok/girafarig.png","img/pok/pineco.png","img/pok/forretress.png",
   "img/pok/dunsparce.png","img/pok/gligar.png","img/pok/steelix.png",
   "img/pok/snubbull.png","img/pok/granbull.png","img/pok/qwilfish.png",
   "img/pok/scizor.png","img/pok/shukle.png","img/pok/heracross.png", #60 scizor
   "img/pok/sneasel.png","img/pok/teddiursa.png","img/pok/ursaring.png",
   "img/pok/slugma.png","img/pok/magcargo.png","img/pok/swinub.png",
   "img/pok/piloswine.png","img/pok/corsola.png","img/pok/remoraid.png", # 70 corsola
   "img/pok/octillery.png","img/pok/delibird.png","img/pok/mantine.png",
   "img/pok/skarmory.png","img/pok/houndour.png","img/pok/houndoom.png",
   "img/pok/kingdra.png","img/pok/phanpy.png","img/pok/donphan.png", # 80 donphan
   "img/pok/porygon2.png","img/pok/stantler.png","img/pok/smeargle.png",
   "img/pok/tyrogue.png","img/pok/hitmontop.png","img/pok/smoochum.png",
   "img/pok/elekid.png","img/pok/magby.png","img/pok/miltank.png",
   "img/pok/blissey.png","img/pok/raikou.png","img/pok/entei.png", # 90 blissey
   "img/pok/suicune.png","img/pok/larvitar.png","img/pok/pupitar.png",
   "img/pok/tyranitar.png","img/pok/lugia.png","img/pok/ho-oh.png",
   "img/pok/celebi.png",
         ]
for img in pokemon_list_johto:
	pokemon_images_johto.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_hoenn = []
pokemon_list_hoenn = [
   "img/pok/treecko.png","img/pok/grovyle.png","img/pok/sceptille.png",
   "img/pok/torchik.png","img/pok/combusken.png","img/pok/blaziken.png",
   "img/pok/mudkip.png","img/pok/marshtomp.png","img/pok/swampert.png",
   "img/pok/poochyena.png","img/pok/mightyena.png","img/pok/zigzagoon.png",# 10 mightyena
   "img/pok/linoone.png","img/pok/wurmple.png","img/pok/silcoon.png",
   "img/pok/beautifly.png","img/pok/cascoon.png","img/pok/dustox.png",
   "img/pok/lotad.png","img/pok/lombre.png","img/pok/ludicolo.png",     # 20 ludicolo
   "img/pok/seedot.png","img/pok/nuzleaf.png","img/pok/shiftry.png",
   "img/pok/taillow.png","img/pok/swellow.png","img/pok/wingull.png",
   "img/pok/pelipper.png","img/pok/ralts.png","img/pok/kirlia.png",
   "img/pok/gardevoir.png","img/pok/surskit.png","img/pok/masquerain.png",#  30 gardevoir
   "img/pok/shroomish.png","img/pok/breloom.png","img/pok/slakoth.png",
   "img/pok/vigoroth.png","img/pok/slaking.png","img/pok/nincada.png",
   "img/pok/ninjask.png","img/pok/shedinja.png","img/pok/whismur.png",# 40 shedinja
   "img/pok/loudred.png","img/pok/exploud.png","img/pok/makuhita.png",
   "img/pok/hariyama.png","img/pok/azurill.png","img/pok/nosepass.png",
   "img/pok/skitty.png","img/pok/delcatty.png","img/pok/sableye.png",# 50 sableye
   "img/pok/mawile.png","img/pok/aron.png","img/pok/lairon.png",
   "img/pok/aggron.png","img/pok/meditite.png","img/pok/medicham.png",
   "img/pok/electrike.png","img/pok/manectric.png","img/pok/plusle.png",
   "img/pok/minum.png","img/pok/volbeat.png","img/pok/illumise.png",# 60 minum
   "img/pok/roselia.png","img/pok/gulpin.png","img/pok/swalot.png",
   "img/pok/carvanha.png","img/pok/sharpedo.png","img/pok/wailmer.png",
   "img/pok/wailord.png","img/pok/numel.png","img/pok/camerupt.png",# 70 numel
   "img/pok/torkoal.png","img/pok/spoink.png","img/pok/grumpig.png",
   "img/pok/spinda.png","img/pok/trapinch.png","img/pok/vibrava.png",
   "img/pok/flygon.png","img/pok/cacnea.png","img/pok/cacturne.png",# 80 cacturne
   "img/pok/swablu.png","img/pok/altaria.png","img/pok/zangoose.png",
   "img/pok/seviper.png","img/pok/lunatone.png","img/pok/solrock.png",
   "img/pok/barboach.png","img/pok/whiscash.png","img/pok/corpish.png",
   "img/pok/crawdaunt.png","img/pok/baltoy.png","img/pok/claydol.png",# 90 crawdaunt
   "img/pok/lileep.png","img/pok/cradily.png","img/pok/anorith.png",
   "img/pok/armaldo.png","img/pok/feebas.png","img/pok/milotic.png",
   "img/pok/castform.png","img/pok/kecleon.png","img/pok/shuppet.png",# 100 kecleon
   "img/pok/banette.png","img/pok/duskull.png","img/pok/dusclops.png",
   "img/pok/tropius.png","img/pok/chimecho.png","img/pok/absol.png",
   "img/pok/wynaut.png","img/pok/snorunt.png","img/pok/glalie.png",# 110 glalie
   "img/pok/spheal.png","img/pok/sealeo.png","img/pok/walrein.png",
   "img/pok/clamperl.png","img/pok/huntail.png","img/pok/gorebyss.png",
   "img/pok/relicanth.png","img/pok/luvdisc.png","img/pok/bagon.png",
   "img/pok/shelgon.png","img/pok/salamence.png","img/pok/beldum.png",# 120 shelgon
   "img/pok/metang.png","img/pok/metagross.png","img/pok/regirock.png",
   "img/pok/regice.png","img/pok/registeel.png","img/pok/latias.png",
   "img/pok/latios.png","img/pok/kyogre.png","img/pok/groudon.png",# 130 kyogre
   "img/pok/rayquaza.png","img/pok/jirachi.png","img/pok/deoxys.png"
                ]
for img in pokemon_list_hoenn:
	pokemon_images_hoenn.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_sinnoh = []
pokemon_list_sinnoh = [
   "img/pok/turtwig.png","img/pok/grotle.png","img/pok/torterra.png",
   "img/pok/chimchar.png","img/pok/monferno.png","img/pok/infernape.png",
   "img/pok/piplup.png","img/pok/prinplup.png","img/pok/empoleon.png",
   "img/pok/starly.png","img/pok/staravia.png","img/pok/staraptor.png",# 10 staravia
   "img/pok/bidoof.png","img/pok/bibarel.png","img/pok/kricketot.png",
   "img/pok/kricketune.png","img/pok/shinx.png","img/pok/luxio.png",
   "img/pok/luxray.png","img/pok/budew.png","img/pok/roserade.png",# 20 roserade
   "img/pok/cranidos.png","img/pok/rampardos.png","img/pok/shieldon.png",
   "img/pok/bastiodon.png","img/pok/burmy.png","img/pok/wormadam.png",
   "img/pok/mothim.png","img/pok/combee.png","img/pok/vespiquen.png",
   "img/pok/pachirisu.png","img/pok/buizel.png","img/pok/floatzel.png", # 30 parichisu
   "img/pok/cherubi.png","img/pok/cherrim.png","img/pok/shellos.png",
   "img/pok/gastrodon.png","img/pok/ambipom.png","img/pok/drifloon.png",
   "img/pok/drifblim.png","img/pok/buneary.png","img/pok/lopunny.png",# 40 buneary
   "img/pok/mismagius.png","img/pok/honchkrow.png","img/pok/glameow.png",
   "img/pok/purugly.png","img/pok/chingling.png","img/pok/stunky.png",
   "img/pok/skuntank.png","img/pok/bronzor.png","img/pok/bronzong.png", # 50 bronzong
   "img/pok/bonsly.png","img/pok/mimejr.png","img/pok/happiny.png",
   "img/pok/chatot.png","img/pok/spiritomb.png","img/pok/gible.png",
   "img/pok/gabite.png","img/pok/garchomp.png","img/pok/munchlax.png",
   "img/pok/riolu.png","img/pok/lucario.png","img/pok/hippopotas.png",# 60 riolu
   "img/pok/hippowdon.png","img/pok/skorupi.png","img/pok/drapion.png",
   "img/pok/croagunk.png","img/pok/toxicroak.png","img/pok/carnivine.png",
   "img/pok/finneon.png","img/pok/lumineon.png","img/pok/mantyke.png",# 70 lumineon
   "img/pok/snover.png","img/pok/abomasnow.png","img/pok/weavile.png",
   "img/pok/magnezone.png","img/pok/lickilicky.png","img/pok/rhyperior.png",
   "img/pok/tangrowth.png","img/pok/electivire.png","img/pok/magmortar.png",
   "img/pok/togekiss.png","img/pok/yanmega.png","img/pok/leafeon.png",
   "img/pok/glaceon.png","img/pok/gliscor.png","img/pok/mamoswine.png",
   "img/pok/porygon-z.png","img/pok/gallade.png","img/pok/probopass.png",
   "img/pok/dusknoir.png","img/pok/froslass.png","img/pok/rotom.png",
   "img/pok/uxie.png","img/pok/mesprit.png","img/pok/azelf.png",
   "img/pok/dialga.png","img/pok/palkia.png",
   "img/pok/heatran.png","img/pok/regigigas.png","img/pok/giratina.png",
   "img/pok/cresselia.png","img/pok/phione.png","img/pok/manaphy.png",
   "img/pok/darkrai.png","img/pok/shaymin.png","img/pok/arceus.png"
   ]
for img in pokemon_list_sinnoh:
	pokemon_images_sinnoh.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_teselia = []
pokemon_list_teselia = [
   "img/pok/victini.png","img/pok/snivy.png","img/pok/servine.png",
   "img/pok/serperior.png","img/pok/tepig.png","img/pok/pignite.png",
   "img/pok/emboar.png","img/pok/oshawott.png","img/pok/dewott.png",
   "img/pok/samurott.png","img/pok/patrat.png","img/pok/watchog.png",#10patrat
   "img/pok/lillipup.png","img/pok/herdier.png","img/pok/stoutland.png",
   "img/pok/purrloin.png","img/pok/liepard.png","img/pok/pansage.png",
   "img/pok/simisage.png","img/pok/pansear.png","img/pok/simisear.png",#20simisear
   "img/pok/panpour.png","img/pok/simipour.png","img/pok/munna.png",
   "img/pok/musharna.png","img/pok/pidove.png","img/pok/tranquill.png",
   "img/pok/unfezant.png","img/pok/blitzle.png","img/pok/zebstrika.png",
   "img/pok/roggenrola.png","img/pok/boldore.png","img/pok/gigalith.png",#30 roggenrola
   "img/pok/woobat.png","img/pok/swoobat.png","img/pok/drilbur.png",
   "img/pok/excadrill.png","img/pok/audino.png","img/pok/timburr.png",
   "img/pok/gurdurr.png","img/pok/conkeldurr.png","img/pok/tympole.png",#40 conkeldurr
   "img/pok/palpitoad.png","img/pok/seismitoad.png","img/pok/throh.png",
   "img/pok/sawk.png","img/pok/sewaddle.png","img/pok/swadloon.png",
   "img/pok/leavanny.png","img/pok/venipede.png","img/pok/whirlipede.png",#50 whirlipede
   "img/pok/scolipede.png","img/pok/coottonee.png","img/pok/whimsicott.png",
   "img/pok/petilil.png","img/pok/lilligant.png","img/pok/basculin.png",
   "img/pok/sandile.png","img/pok/krokorok.png","img/pok/krookodile.png",#60 darumka
   "img/pok/darumka.png","img/pok/darmanitan.png","img/pok/maractus.png",
   "img/pok/dwebble.png","img/pok/crustle.png","img/pok/scraggy.png",
   "img/pok/scrafty.png","img/pok/sigilyph.png","img/pok/yamask.png",
   "img/pok/cofagrigus.png","img/pok/tirtouga.png","img/pok/carracosta.png",#70 tirtoga
   "img/pok/archen.png","img/pok/archeops.png","img/pok/trubbish.png",
   "img/pok/garbodor.png","img/pok/zorua.png","img/pok/zoroark.png",
   "img/pok/minccino.png","img/pok/cinccino.png","img/pok/gothita.png",#80 gothita
   "img/pok/gothorita.png","img/pok/gothitelle.png","img/pok/solosis.png",
   "img/pok/duosion.png","img/pok/reuniclus.png","img/pok/ducklett.png",
   "img/pok/swanna.png","img/pok/vanillite.png","img/pok/vanillish.png",#90 vanilluxe
   "img/pok/vanilluxe.png","img/pok/deerling.png","img/pok/sawsbuck.png",
   "img/pok/emolga.png","img/pok/karrablast.png","img/pok/escavalier.png",
   "img/pok/foongus.png","img/pok/amoonguss.png","img/pok/frillish.png",
   "img/pok/jellicent.png","img/pok/alomomola.png","img/pok/joltik.png",#100 alomomola
   "img/pok/galvantula.png","img/pok/ferroseed.png","img/pok/ferrothorn.png",
   "img/pok/klink.png","img/pok/klang.png","img/pok/klinklang.png",
   "img/pok/tynamo.png","img/pok/eelektrik.png","img/pok/eelektross.png",
   "img/pok/elgyem.png","img/pok/beheeyem.png","img/pok/litwick.png",
   "img/pok/lampent.png","img/pok/chandelure.png","img/pok/axew.png",
   "img/pok/fraxure.png","img/pok/haxorus.png","img/pok/cubchoo.png",
   "img/pok/beartic.png","img/pok/cryogonal.png","img/pok/shelmet.png",
   "img/pok/accelgor.png","img/pok/stunfisk.png","img/pok/mienfoo.png",
   "img/pok/mienshao.png","img/pok/druddigon.png","img/pok/golett.png",
   "img/pok/golurk.png","img/pok/pawniard.png","img/pok/bisharp.png",
   "img/pok/bouffalant.png","img/pok/rufflet.png","img/pok/braviary.png",
   "img/pok/vullaby.png","img/pok/mandibuzz.png","img/pok/heatmor.png",
   "img/pok/durant.png","img/pok/deino.png","img/pok/zweilous.png",
   "img/pok/hydreigon.png","img/pok/larvesta.png","img/pok/volcarona.png",
   "img/pok/cobalion.png","img/pok/terrakion.png","img/pok/virizion.png",
   "img/pok/tornadus.png","img/pok/thundurus.png","img/pok/reshiram.png",
   "img/pok/zekrom.png","img/pok/landorus.png","img/pok/kyurem.png",
   "img/pok/keldeo.png","img/pok/meloetta.png","img/pok/genesect.png"
]
for img in pokemon_list_teselia:
	pokemon_images_teselia.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_kalos = []
pokemon_list_kalos = [
 #  "img/pok/.png"
]
for img in pokemon_list_kalos:
	pokemon_images_kalos.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

pokemon_images_alola = []
pokemon_list_alola = [
#   "img/pok/.png"
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
   7,7,7,5,12,12,9,9,12,12, 10,10,4,4,1,1,0,3,3,4, 4,0,10,0,9,9,9,9,9,9, #120
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
pokemon_attack = []

pokemon_def = []

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
   
   [1,  1.6,  1,  1.6,  1,  1,  0.625,  1,  1,  1,  1,  1, 0.625, 0.625,  1,  0.625,  1,        1],#13psiquico
   
   [1, 0.625,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1.6, 0.625, 0.625,  1,  1,        1],#14siniestro
   
   [1,  1.6,  1, 0.625,  1,  1,  1,  1, 0.625,  1,  1,  1,  1,  1.6,  1, 0.625,  1,  1.6],#15hada
   
   [1,  1,  1,  1,  1,  1.6,  1,  1, 0.625, 0.625,  1, 0.625,  1,  1,  1.6,  0.625,  1,  1],#16acero
   
   [1,  1,  1.6,  1,  1.6,  1,  1,  1, 0.625, 0.625,  1.6,  1,  1,  1,  1,  0.625,  0.625,  1.6],#17hielo
   
   [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.625,  0.625,  1,  1.6],#18dragon
]

def damage(tip_atacante,defensor):
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

   daño = 6*efectividad_total
   return daño


player_pokemon_list = []
op_pokemon_list = []

player_pokemon_attack = 0
op_pokemon_attack = 0

fighting = True

numero_max_pokemon = 458
numero_de_regiones = 4

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
      pokemon1 = Pokemon(randint(0,numero_de_regiones),0)
      player_pokemon_list.append(pokemon1)
      all_sprites.add(pokemon1)
      player_pokemon_hp = pokemon1.hp
      if pokemon1.type2 != 18:
      
         player_pokemon_attack = random.choice([pokemon1.type1,pokemon1.type2])
      else:
         player_pokemon_attack = pokemon1.type1
      type1 = Type(player_pokemon_attack,270,460,0,50,50)
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
         op_pokemon_attack = random.choice([pokemon4.type1,pokemon4.type2])
      else:
         op_pokemon_attack = pokemon4.type1
      type2 = Type(op_pokemon_attack,670,260,1,50,50)
      type_pokemon.add(type2)
      type2a = Type(pokemon4.type1,pokemon4.rect.x,pokemon4.rect.top - 30,1,25,25)
      type2b = Type(pokemon4.type2,pokemon4.rect.x + 30,pokemon4.rect.top - 30,1,25,25)
      type2_pokemon.add(type2a,type2b)
      pokemon5 = Pokemon(randint(0,numero_de_regiones),1)
      op_pokemon_list.append(pokemon5)
      pokemon6 = Pokemon(randint(0,numero_de_regiones),1)
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
                     if poke.type2 != 18:
                        op_pokemon_attack = random.choice([poke.type1,poke.type2])
                     else:
                        op_pokemon_attack = poke.type1
                     for ty in type_pokemon:
                        if ty.team_int == 1:
                           ty.kill()
                           type2 = Type(op_pokemon_attack,670,260,1,50,50)
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
                        player_pokemon_attack = random.choice([pokem.type1,pokem.type2])
                     else:
                        player_pokemon_attack = pokem.type1
                     for typ in type_pokemon:
                        if typ.team_int == 0:
                           typ.kill()
                           type1 = Type(player_pokemon_attack,270,460,0,50,50)
                           type_pokemon.add(type1)
                     for typ in type2_pokemon:
                        if typ.team_int == 0:
                           typ.kill()
                     type1a = Type(pokem.type1,pokem.rect.x,pokem.rect.top - 30,0,25,25)
                     type1b = Type(pokem.type2,pokem.rect.x + 30,pokem.rect.top - 30,0,25,25)
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
"""
