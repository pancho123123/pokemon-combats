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
   "larvitar","ledyba","lickitung","machamp","machoke","machop","magby","magcargo","magikarp","magmar",
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

pokemon_images = []
pokemon_list = ["img/pok/abra.png","img/pok/aerodactyl.png","img/pok/aipom.png",
                "img/pok/alakazam.png","img/pok/arbok.png","img/pok/arcanine.png",
                "img/pok/ariados.png","img/pok/beedrill.png","img/pok/bellossom.png",
                "img/pok/bellsprout.png","img/pok/blastoise.png",
   "img/pok/bulbasaur.png", "img/pok/butterfree.png", "img/pok/caterpi.png", #12
   "img/pok/chansey.png", "img/pok/charizard.png", "img/pok/charmander.png", 
   "img/pok/charmeleon.png", "img/pok/chinchou.png","img/pok/clefairy.png",
   "img/pok/cleffa.png","img/pok/cloyster.png", "img/pok/corsola.png",
   "img/pok/crobat.png","img/pok/croconaw.png","img/pok/cubone.png",
   "img/pok/cyndaquil.png", "img/pok/delibird.png", "img/pok/dewong.png",
   "img/pok/diglett.png","img/pok/ditto.png", "img/pok/dodrio.png","img/pok/doduo.png",#30
   "img/pok/donphan.png","img/pok/dragonair.png", "img/pok/dragonite.png",
   "img/pok/dratini.png","img/pok/drowzee.png","img/pok/dugtrio.png", 
   "img/pok/dunsparce.png", "img/pok/eevee.png","img/pok/ekans.png",#39
   "img/pok/electabuzz.png","img/pok/electrode.png","img/pok/entei.png",
   "img/pok/espeon.png","img/pok/exeggcute.png","img/pok/exeggutor.png",
   "img/pok/farfetch.png","img/pok/fearow.png","img/pok/feraligatr.png",#fin50
   "img/pok/flaaffy.png","img/pok/flareon.png","img/pok/forretress.png",#51flafy,52flareon
   "img/pok/furret.png","img/pok/gastly.png","img/pok/gengar.png",
   "img/pok/geodude.png","img/pok/girafarig.png","img/pok/gligar.png",#57geodude,
   "img/pok/gloom.png","img/pok/golbat.png","img/pok/goldeen.png",#60gloom
   "img/pok/golduck.png","img/pok/golem.png", "img/pok/granbull.png",
   "img/pok/graveler.png","img/pok/grimer.png","img/pok/growlithe.png", #66graveler, 68growlithe
   "img/pok/gyarados.png","img/pok/haunter.png","img/pok/heracross.png",
   "img/pok/hitmonchan.png","img/pok/hitmonlee.png","img/pok/hitmontop.png",#72
   "img/pok/hoothoot.png","img/pok/hoppip.png","img/pok/horsea.png",#74,75
   "img/pok/houndoom.png","img/pok/houndour.png","img/pok/hypno.png",
   "img/pok/ivysaur.png","img/pok/jigglypuff.png","img/pok/jolteon.png",#82
   "img/pok/jumpluff.png","img/pok/jynx.png","img/pok/kabutops.png",
   "img/pok/kadabra.png","img/pok/kakuna.png","img/pok/kangaskhan.png",
   "img/pok/kingdra.png","img/pok/kingler.png","img/pok/koffing.png",
   "img/pok/krabby.png","img/pok/lapras.png","img/pok/larvitar.png",#94lapras
   "img/pok/ledyba.png","img/pok/lickitung.png","img/pok/machamp.png", 
   "img/pok/machoke.png","img/pok/machop.png","img/pok/magby.png",
   "img/pok/magcargo.png","img/pok/magikarp.png","img/pok/magmar.png",
   "img/pok/magnemite.png","img/pok/magneton.png","img/pok/mankey.png",
   "img/pok/mantine.png","img/pok/marill.png","img/pok/marowak.png",
   "img/pok/meowth.png","img/pok/metapod.png","img/pok/miltank.png",
   "img/pok/misdreavus.png","img/pok/mr.mime.png","img/pok/muk.png",#115
   "img/pok/murkrow.png","img/pok/natu.png","img/pok/nidoking.png",
   "img/pok/nidoqueen.png","img/pok/nidoran1.png","img/pok/nidoran2.png",
   "img/pok/nidorina.png","img/pok/nidorino.png","img/pok/ninetales.png",
   "img/pok/noctowl.png","img/pok/oddish.png","img/pok/omastar.png",
   "img/pok/onix.png","img/pok/paras.png","img/pok/parasect.png",#130
   "img/pok/persian.png","img/pok/phanpy.png","img/pok/pidgeot.png",
   "img/pok/pidgeotto.png","img/pok/pidgey.png","img/pok/pikachu.png",#135
   "img/pok/piloswine.png","img/pok/pineco.png","img/pok/politoed.png",
   "img/pok/poliwag.png","img/pok/poliwhirl.png","img/pok/poliwrath.png",
   "img/pok/ponyta.png","img/pok/porygon.png","img/pok/primeape.png",
   "img/pok/psyduck.png","img/pok/pupitar.png","img/pok/quagsire.png",
   "img/pok/quilava.png","img/pok/qwilfish.png","img/pok/raichu.png",#151
   "img/pok/rapidash.png","img/pok/raticate.png","img/pok/rattata.png",#154
   "img/pok/raikou.png","img/pok/remoraid.png","img/pok/rhydon.png",#157
   "img/pok/rhyhorn.png","img/pok/sandshrew.png","img/pok/sandslash.png",#159
   "img/pok/scyther.png","img/pok/seadra.png","img/pok/seaking.png",
   "img/pok/seel.png","img/pok/sentret.png","img/pok/shellder.png",#165
   "img/pok/skarmory.png","img/pok/skiploom.png","img/pok/slowbro.png",
   "img/pok/slowking.png","img/pok/slowpoke.png","img/pok/slugma.png",
   "img/pok/sneasel.png","img/pok/snorlax.png","img/pok/snubbull.png",#174
   "img/pok/spearow.png","img/pok/spinarak.png","img/pok/squirtle.png",#176
   "img/pok/stantler.png","img/pok/starmie.png","img/pok/staryu.png",
   "img/pok/steelix.png","img/pok/sudowoodo.png","img/pok/sunkern.png",
   "img/pok/swinub.png","img/pok/tauros.png","img/pok/teddiursa.png",
   "img/pok/tentacool.png","img/pok/tentacruel.png","img/pok/togepi.png",
   "img/pok/totodile.png","img/pok/typhlosion.png","img/pok/tyranitar.png",
   "img/pok/umbreon.png","img/pok/ursaring.png","img/pok/vaporeon.png",
   "img/pok/venomoth.png","img/pok/venonat.png","img/pok/venusaur.png",
   "img/pok/victreebel.png","img/pok/vileplume.png","img/pok/voltorb.png",#"202"
   "img/pok/vulpix.png","img/pok/wartortle.png","img/pok/weedle.png",#205
   "img/pok/weepinbell.png","img/pok/weezing.png","img/pok/wigglytuff.png",
   "img/pok/wooper.png","img/pok/xatu.png","img/pok/yanma.png",
   "img/pok/zubat.png"]
for img in pokemon_list:
	pokemon_images.append(pygame.transform.scale(pygame.image.load(img),(200,200)).convert())

""" 
   
"""
pokemon_type_list1 = [12,5,0,12,3,8,6,6,10,10,9,10,6,6,0,8,8,8,9,14,14,9,9,3,9,#24
                      4,8,16,9,4,0,0,0,4,17,17,17,12,4,0,0,3,11,11,8,12,10,10,0,#48
                      0,9,11,8,6,0,7,7,5,0,4,10,3,9,9,5,14,5,3,8,9,7,6,1,1,1,0,#75
                      10,9,13,13,12,10,0,11,10,16,5,12,6,0,9,9,3,9,9,5,6,0,1,1,1,#100
                      8,8,9,8,11,11,1,9,9,4,0,6,0,7,12,3,13,12,3,3,3,3,3,3,8,0,10,#127
                      5,5,6,6,0,4,0,0,0,11,16,6,9,9,9,9,8,0,1,9,5,9,8,9,11,8,0,#154
                      0,11,9,4,4,4,4,6,9,9,9,0,9,15,10,9,9,8,13,0,14,0,6,9,0,9,#180
                      9,15,5,10,16,0,0,9,9,14,9,8,5,13,0,9,6,6,10,10,10,11,8,9,#204
                      6,10,3,0,9,12,6,3]#212
#0..normal    1..lucha    2..volador   3..veneno   4..tierra   5..roca   6..bicho
#7..fantasma   8..fuego   9..agua   10..planta   11..electrico   12..psiquico
#13..siniestro   14..hada   15..acero   16..hielo   17..dragon
pokemon_type_list2 = [None,2,None,None,None,None,3,3,None,3,None,3,2,None,None,2,None,None,11,None,#19
                     None,16,5,2,None,None,None,2,16,None,None,2,2,None,None,2,None,None,None,None,#39
                     None,None,None,None,None,None,12,12,2,2,None,None,None,15,None,3,3,4,12,2,3,2,#61
                     None,None,4,None,4,None,None,2,3,1,None,None,None,2,2,None,8,8,None,3,14,None,#83
                     2,12,9,None,3,None,17,None,None,None,16,4,2,None,None,None,None,None,5,None,#103
                     None,15,15,None,2,14,None,None,None,None,None,14,None,2,2,4,4,None,None,None,#123
                     None,None,2,3,9,4,10,10,None,None,2,2,2,None,4,None,None,None,None,1,None,None,#145
                     None,None,4,4,None,3,None,None,None,None,None,None,5,5,None,None,2,None,None,#164
                     None,None,None,2,2,12,12,None,16,None,None,2,3,None,None,12,None,4,None,None,#184
                     4,None,None,3,3,None,None,None,13,None,None,None,3,3,3,3,3,None,None,None,#204
                     3,3,None,14,4,2,2,2]#212

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

pokemon_hp = [50,80,70,80,70,70,50,82,42,85,52,74,40,60,259,67,73,70,103,97,90,100,87,41,50,
              #14chansey,fin24              
              84,75,71,120,56,85,70,62,40,72,70,75,70,50,100,89,72,60,65,80,80,90,105,77,90,
              #40eevee,fin49
              90,108,90,120,90,58,90,68,100,90,75,100,80,110,110,85,90,90,75,90,80,90,80,
              #55gastly,57geodude,fin72hitmonchan
              80,80,70,60,89,80,72,79,90,177,70,90,80,70,70,70,90,100,90,70,70,100,83,89,100,
              #82jigg,97finlicki
              70,65,90,70,65,110,80,52,80,70,90,150,70,87,120,90,68,70,100,73,70,110,110,
              #98machamp70,105magnemit52,109marill150,111meowth89,fin120_110nidoqueen
              89,98,90,90,75,100,90,71,90,68,70,85,110,95,93,92,74,100,80,100,82,90,100,
              #121nidoran1_89,125ninetales75,130paras68,133phanp110,139pineco80,141poliwag82,
              70,90,80,80,90,95,90,75,80,80,90,80,110,74,120,95,75,100,80,100,110,100,80,65,
              #144ponyta70,150quilava90,155rat80,160sandsdrew75,165seel100,finshellder167
              100,100,80,80,110,80,65,120,85,82,85,80,90,80,70,95,75,70,99,90,80,77,100,
              #168skarmory100,170slowbro80,172slowpoke110,175snorlax120,176snubbull85,177spearow82,180stantler90,185sunkern70,fin190tentacruel
              80,83,95,120,100,120,130,78,90,95,100,100,110,75,80,110,60,90,100,120,112,
              #191togepi,195umbreon100,200venusaur100,205wartortle,210wooper,yamna,zubat
              66,80,92]
              #211xatu,212yanma,213zubat

#82jigg177,83jolt70,84jumpluff90,85jynx80,86kabut70,87kada70,88kakuna70,89kang90,90kingdra100,
#91kingler90,92koffing70,93krabb70,94lapras100, 60,95larvitar80,96
#82
#77porygon, +101caterpc344, 76spearow470, 63shelder, 100seel,79hypno, 89eevee, 92pidgey, 82sandygast, 
# 90rhyhorn489,1*, 90venonat, 95noibat, 89luv(pezrosa),lunatone87,sableye70,0*, absol57,0*,phantum75,
#stufful89,2*,seviper74, omanyte58,snubbull85,


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
   [1,  1,  1,  1,  1,  1,  1, 0.5,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],#1Normal

   [2, 0.5,  1, 0.5,  1,  1, 0.5, 0.5,  1,  1,  1,  1, 0.5,  2, 0.5,  1,  1,  1],#2lucha
   
   [1,  2, 0.5,  1,  1,  1,  2,  1,  1,  1,  1, 0.5,  1,  1,  1,  1,  1,  1],#3volador
   
   [1,  1,  1, 0.5, 0.5,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1],#4veneno
   
   [1,  1,  1,  2, 0.5, 1, 0.5,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1,             1],#5tierra
   
   [1, 0.5,  2,  1, 0.5, 0.5,  2,  1,  2,  1,  1,  1,  1,  1,  1,  1,  1,            1],#6roca
   
   [1, 0.5,  1, 0.5,  1,  1, 0.5,  1, 0.5,  1,  1,  1,  2,  1, 0.5,  1,  1,          1],#7bicho
   
   [0.5,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  2, 0.5,  1,  1,  1,           1],#8fantasma
   
   [1,  1,  1,  1,  1,  1,  2,  1, 0.5, 0.5,  2,  1,  1,  1,  1,  2,  1,           1],#9fuego
   
   [1,  1,  1,  2,  1,  1,  1,  1,  2, 0.5, 0.5,  1,  1,  1,  1,  1,  1,            1],#10agua
   
   [1,  1,  1, 0.5,  2,  1, 0.5,  1, 0.5, 2, 0.5,  1,  1,  1,  1,  1,  1,             1],#11planta
   
   [1,  1,  1, 0.5,  1,  1,  1,  1,  1,  2, 0.5, 0.5,  1,  1,  1,  1,  1,           1],#12electrico
   
   [1,  2,  1,  2,  1,  1,  1,  1,  1,  1,  1,  1, 0.5, 0.5,  1,  1,  1,             1],#13psiquico
   
   [1, 0.5,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2, 0.5, 0.5,  1,  1,            1],#14siniestro
   
   [1,  2,  1, 0.5,  1,  1,  1,  1, 0.5,  1,  1,  1,  1,  2,  1, 0.5,  1,  2],#15hada
   
   [1,  1,  1,  1,  1,  1,  1,  1, 0.5, 0.5,  1, 0.5,  1,  1,  2,  1,  1,  1],#16acero
   
   [1,  1,  1,  2,  1,  1,  1,  1, 0.5, 0.5,  1,  1,  1,  1,  1,  1,  1,  2],#17hielo
   
   [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.5,  1,  1,  2],#18dragon
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
      #energia_max_pok1 = player_pokemon_list[0]
      pokemon2 = Pokemon(randint(0,200),0)
      player_pokemon_list.append(pokemon2)
      pokemon3 = Pokemon(randint(0,200),0)
      player_pokemon_list.append(pokemon3)
      pokemon4 = Pokemon(randint(0,200),1)
      op_pokemon_list.append(pokemon4)
      all_sprites.add(pokemon4)
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
            else:
               all_sprites.add(random.choice(player_pokemon_list))
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
      draw_hp_bar(screen,pok.rect.x,pok.rect.y,pok.hp)
   pygame.display.update()


"""
   # current_time = pygame.time.get_ticks()
   # elapsed_time = current_time - start_time

   # if battle:
   #    if elapsed_time > probably_battle_number:
   #       probably_battle_number = randint(0,7000)
   #       area1 = False
   #       fighting = True
"""