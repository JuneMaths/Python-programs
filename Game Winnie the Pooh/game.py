import pygame
import sys
import time
import random

# #########				POMOCNE FUNKCJE				##########
def Zaladuj_obrazek(name):
	'''Funkcja ładuje obrazek tak aby jego brzegi były przeźroczyste'''
	im = pygame.image.load(name)
	im = im.convert_alpha()
	return im


def text_to_button(napis, bx, by, bw, bh, color = (78,52,46)):
	'''Funkcja dodaje tekst do guzika'''
	smallfont = pygame.font.SysFont("georgia", 20)
	textSurface = smallfont.render(napis, True, color)
	textRect = textSurface.get_rect()
	textRect.center = ((bx + (bw / 2)), by + (bh / 2))
	window.blit(textSurface, textRect)


def button(napis, bx, by, bw, bh, kolor1, kolor2, action = None):
	'''Funkcja tworzy przycisk i wykonuje akcje kiedy zostanie przyciśnięty'''
	cur = pygame.mouse.get_pos() #pozycja kursora
	click = pygame.mouse.get_pressed()
	if bx+bw > cur[0] > bx and by+bh > cur[1] > by:
		pygame.draw.rect(window, kolor2, (bx, by, bw, bh)) #kolor aktywny
		if click[0] == 1 and action != None:
			if action == 'o autorze':
				pygame.draw.rect(window, (0, 0, 0), (50, 360, 200, 100))
				window.blit(autor_text_render,(30, 395))
			elif action == 'wyniki':
				pygame.draw.rect(window, (0, 0, 0), (50, 200, 300, 250))
				window.blit(wyniki_text_render, (20, 250))
				lista_w = naj_wyniki()
				w1_text_render = conf_text("1. " + lista_w[0])
				w2_text_render = conf_text("2. " + lista_w[1])
				w3_text_render = conf_text("3. " + lista_w[2])
				window.blit(w1_text_render, (50, 290))
				window.blit(w2_text_render, (50, 330))
				window.blit(w3_text_render, (50, 370))
			elif action == 'zasady gry':
				pygame.draw.rect(window, (0, 0, 0), (50, 200, 500, 300))
				window.blit(zasady_text0_render, (200, 240))
				window.blit(zasady_text1_render, (10, 290))
				window.blit(zasady_text2_render, (10, 320))
				window.blit(zasady_text3_render, (10, 350))
				window.blit(zasady_text4_render, (10, 380))
				window.blit(zasady_text5_render, (10, 410))
			elif action == 'wyjdz':
				sys.exit(0)
	else:
		pygame.draw.rect(window, kolor1, (bx, by, bw, bh)) #kolor nieaktywny
	text_to_button(napis, bx, by, bw, bh)


def zapisz_wynik_jezeli_na_podjum(wynik):
	'''Funkcja otwiera plik, w którym przechowywane są ostatnie najlepsze wyniki.
	Dodaje zdobyty wynik w danej rundzie i porównuje go z poprzednimi. 
	Jeżeli wynik jest jednym z pierwszych trzech najlepszych to akutalizuje plik.'''
	with open('najlepsze_wyniki.txt','r') as plik:
		dane = plik.read()
		lista = dane.split('%%nowe dane%%')
	lista = lista[0:3]
	plik.close()
	lista.append(str(wynik))
	lista1 = []
	for i in range(len(lista)):
		lista1.append(int(lista[i]))
	lista1.sort(reverse = True)
	lista2 = []
	for i in range(len(lista1)):
		lista2.append(str(lista1[i]))
	odstep = '%%nowe dane%%'
	plik = open('najlepsze_wyniki.txt', 'w')
	for i in range(len(lista2)):
		plik.write(lista2[i])
		plik.write(odstep)
	plik.close()


def naj_wyniki():
	'''Funkcja zwraca listę najlepszych wyników z pliku.'''
	with open('najlepsze_wyniki.txt','r') as plik:
		dane = plik.read()
		lista = dane.split('%%nowe dane%%')
	lista_w = lista[0:3]
	plik.close()
	return lista_w


def conf_text(text):
	'''Funkcja konfiguruje tekst na odpowiednią czcionkę, wielkość i kolor'''
	czcionka = pygame.font.SysFont("georgia", 20)
	t_text = text
	t_text_render = czcionka.render(t_text, 5, (255, 255, 255))
	return t_text_render


def sprawdz_rekord():
	'''Funkcja sprawdza rekord'''
	lista_w = naj_wyniki()
	rekord_text_render = conf_text("Rekord:  %s" % (str(lista_w[0])))
	return rekord_text_render



# ##########						OKNO						##########
pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("POOH THE WINE")


# ##########						TEKST 						##########
czcionka = pygame.font.SysFont("georgia", 20)
text = "ABY ROZPOCZĄĆ NACIŚNIJ SPACJĘ"
text_render = czcionka.render(text, 5, (0, 0, 0))
#TEXT
autor_text_render = conf_text("Autor: Julia Adamska")
zasady_text0_render = conf_text("ZASADY GRY")
zasady_text1_render = conf_text("Kubusiowi skończył się miodek i jest bardzo głodny.")
zasady_text2_render = conf_text("Pomóż Kubusiowi zaspokoić jego niekończący się apetyt")
zasady_text3_render = conf_text("zbierając jak najwięcej miodków.")
zasady_text4_render = conf_text("Uważaj jednak na pszczoły i nie pozwól im dopaść Kubusia!")
zasady_text5_render = conf_text("Powodzenia ;) ")
wyniki_text_render = conf_text("OSTATNIE NAJLEPSZE WYNIKI:")
punkty_text_render = conf_text("Zdobyte punkty:")
zycia_text_render = conf_text("Życia:")
licznik_miodu_text_render = conf_text("Ilość zebranych miodków:")


# #########						 MUSIC 						##########
pygame.mixer.music.load('piano_pooh.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


# #########						KLASY						##########
class Pooh(pygame.sprite.Sprite):
	def __init__(self):
		'''Funkcja inicjuje Kubusia Puchatka'''
		pygame.sprite.Sprite.__init__(self)
		self.image = Zaladuj_obrazek("baloon.png")
		self.rect = self.image.get_rect() #rozmiar rysunku
		self.rect.center = (850, 650) #gdzie wstawić
		self.x_velocity = 0
		self.y_velocity = 0
		
	def update(self):
		'''Funkcja aktualizuje pozycję kubusia i nie pozwala mu się przemieszczać poza granice.'''
		self.rect.move_ip((self.x_velocity, self.y_velocity)) #move in-place
		if self.rect.left < 480:
			self.rect.left = 480
		elif self.rect.right > 1205:
			self.rect.right = 1205
		if self.rect.top <= 0:
			self.rect.top = 0
		elif self.rect.bottom >= 720:
			self.rect.bottom = 720


class Bees(pygame.sprite.Sprite):
	def __init__(self):
		'''Funkcja inicjuje pszczoły i nadaje im losową prędkość'''
		pygame.sprite.Sprite.__init__(self)
		self.image = Zaladuj_obrazek("bee_anemy.png")
		self.rect=self.image.get_rect()
		self.rect.centerx = 500
		self.rect.centery = 120
		self.x_velocity = random.randint(-4, 4)
		self.y_velocity = random.randint(-4, 4)	
		
	def update(self):
		'''Funkcja aktualizuje pozycje pszczół i zmienia ich prędkość jak odbiją się od ścian.'''
		self.rect.move_ip((self.x_velocity,self.y_velocity))
		if self.rect.left <= 480 or self.rect.right >= 1205:
			self.x_velocity = -(self.x_velocity)
		if self.rect.top <= 0 or self.rect.bottom >= 720:
			self.y_velocity = -(self.y_velocity)


class Hunny(pygame.sprite.Sprite):
	def __init__(self):
		'''Funkcja inicjuje miodek, który pojawia się na losowej pozycji na planszy.'''
		pygame.sprite.Sprite.__init__(self)
		self.image = Zaladuj_obrazek("hunny.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randint(500, 1200)
		self.rect.centery = random.randint(20, 700)


class Miodki(pygame.sprite.Sprite):
	def __init__(self):
		'''Funkcja inicjuje licznik miodków'''
		pygame.sprite.Sprite.__init__(self)
		self.miodki = 0
		
	def update(self):
		'''Funkcja aktualizuje licznik miodków. Jeżeli wracamy do menu licznik się zeruje.'''
		if stan == 'start':
			self.miodki += 1
		elif stan == 'intro':
			self.miodki = 0
		self.image = conf_text(str(self.miodki))
		self.rect = self.image.get_rect()
		self.rect.center=(250, 400)


class Lives(pygame.sprite.Sprite):
	def __init__(self):
		'''Funkcja inicjuje licznik żyć.'''
		pygame.sprite.Sprite.__init__(self)
		self.live = 3

	def update(self):
		'''Funkcja aktualizuje licznik żyć.'''
		if stan == 'start':
			if self.live == 3:
				self.live = 2
			elif self.live == 2:
				self.live = 1
			elif self.live == 1:
				self.live = 0
		elif stan == 'intro':
			self.live = 3
		self.image = conf_text(str(self.live))
		self.rect = self.image.get_rect()
		self.rect.center = (250, 500)


class Wynik(pygame.sprite.Sprite):		
	def __init__(self):
		'''Funkcja inicjuje licznik punktów.'''
		pygame.sprite.Sprite.__init__(self)
		self.wynik = 0
		
	def update(self):
		'''Funkcja aktualizuje licznik punktów. Jeżeli wracamy do menu, licznik się zeruje.'''
		if stan == 'start':
			self.wynik = self.wynik + (miodki.miodki)*(live.live)*100
		elif stan == 'intro':
			self.wynik = 0
		self.image = conf_text(str(self.wynik))
		self.rect = self.image.get_rect()
		self.rect.center = (250, 300)


# ##########					INICJACJA					##########
# ##POOH
poohSprite = pygame.sprite.RenderClear() #kontener na kubusia
pooh = Pooh()                       #stwórz kubusia
poohSprite.add(pooh)                #dodaj go do grupy	

# ##BEES
beesSprite = pygame.sprite.RenderClear()

# ##HUNNY
hunnySprite = pygame.sprite.RenderClear()
hunny = Hunny()

# ##Miodki
miodkiSprite = pygame.sprite.RenderClear()
miodki = Miodki()
miodkiSprite.add(miodki)

# ##Lives
livesSprite = pygame.sprite.RenderClear()
live = Lives()
livesSprite.add(live)

# ##Wynik
wynikSprite = pygame.sprite.RenderClear()
wynik = Wynik()
wynikSprite.add(wynik)


# ##########						OBRAZKI						##########
f1 = Zaladuj_obrazek('pr1.jpg')
f2 = Zaladuj_obrazek('pr2.jpg')
f3 = Zaladuj_obrazek('pr3.jpg')
f4 = Zaladuj_obrazek('bgnlas.jpg')
f5 = Zaladuj_obrazek('lose.jpg')


# #########						RUNNING						##########
run = 0
start_tlo = 1
stan = 'intro'
clock = pygame.time.Clock()
beetime = 0
hunnytime = 0
rekord_pobity = 0
while True:
	run += 1
	clock.tick(40) #liczba klatek na sekundę
	for event in pygame.event.get(): #obsługa zdarzeń
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif event.type == pygame.KEYDOWN: #przyciśnięcie klawisza
			if event.key == pygame.K_SPACE:
				stan = 'start'
			elif event.key == pygame.K_ESCAPE:
				if stan == 'start':
					stan='intro'
				elif stan == 'intro':
					sys.exit(0)
			if event.key == pygame.K_LEFT:
				pooh.x_velocity = -4
			elif event.key == pygame.K_RIGHT:
				pooh.x_velocity = 4
			elif event.key == pygame.K_UP:
				pooh.y_velocity = -4
			elif event.key == pygame.K_DOWN:
				pooh.y_velocity= 4
				
		elif event.type == pygame.KEYUP: #puszczenie klawisza
			if event.key == pygame.K_LEFT:
				pooh.x_velocity = 0
			elif event.key == pygame.K_RIGHT:
				pooh.x_velocity = 0
			elif event.key == pygame.K_UP:
				pooh.y_velocity= 0
			elif event.key == pygame.K_DOWN:
				pooh.y_velocity = 0
					
	if run == 1: #wstęp
		window.blit(f1, (100, 0))
		pygame.display.flip()
		pygame.time.wait(2000)
		window.blit(f2, (0, 0))
		pygame.display.flip()	
		pygame.time.wait(2000)
		
	elif stan == 'intro': #menu
		window.fill((0, 0, 0))
		window.blit(f3 ,(60, 0))
		window.blit(text_render, (480, 160))
		#guziki
		button('O AUTORZE', 410, 550, 130, 60, (255, 179, 0), (255, 202, 40), 'o autorze')
		button('ZASADY GRY', 610, 550, 130, 60, (255, 179, 0), (255, 202, 40), 'zasady gry')
		button('WYNIKI', 810, 550, 130, 60, (255, 179, 0), (255, 202, 40), 'wyniki')
		button('WYJŚCIE', 70, 20, 130, 60, (255, 179, 0), (255, 202, 40), 'wyjdz')
		#wyzerowanie liczników
		miodkiSprite.update()
		livesSprite.update()
		wynikSprite.update()
		#usunięcie postaci
		beesSprite.empty()
		hunnySprite.empty()
		pygame.display.flip()
		start_tlo = 1
		
	elif stan == 'przegrana':
		#obraz
		window.blit(f5, (0, 0))
		pygame.display.flip()
		#muzyka
		pygame.mixer.music.load('beesatak.mp3')
		pygame.mixer.music.play()
		pygame.time.wait(5300)
		stan='intro'
		#wracamy do muzyki w tle
		pygame.mixer.music.load('piano_pooh.mp3')
		pygame.mixer.music.set_volume(0.5)
		pygame.mixer.music.play(-1)
		#zapisujemy wynik
		zapisz_wynik_jezeli_na_podjum(wynik.wynik)
		
	elif stan == 'start':
		if start_tlo == 1: #inicjacja gry od początku
			window.blit(f4, (0, 0))
			#ustawienie postaci i liczników
			pooh.rect.centerx = 850
			pooh.rect.centery = 650
			poohSprite.draw(window)
			miodkiSprite.draw(window)
			#beesSprite.empty()
			livesSprite.draw(window)
			wynikSprite.draw(window)
			wynik.wynik = 0
			for i in range(4):
				bees = Bees()
				beesSprite.add(bees)
			#hunnySprite.empty()
			#RAMKA
			window.blit(licznik_miodu_text_render, (140, 365))
			window.blit(zycia_text_render, (225, 465))
			window.blit(punkty_text_render, (185, 265))
			rekord_text_render = sprawdz_rekord()
			window.blit(rekord_text_render, (185, 200))
			pygame.display.flip()
			start_tlo = 0
		beetime += 1
		if beetime == 500:
			beetime = 0
			beesSprite.add(Bees())
		hunnytime += 1
		if hunnytime == 400:
			hunnytime = 0
			hunnySprite.add(Hunny())
		if pygame.sprite.groupcollide(poohSprite, hunnySprite, 0, 1):
			mniam = pygame.mixer.Sound('hunnyh.wav')
			mniam.play()
			miodkiSprite.update()
			miodkiSprite.clear(window, f4)
			miodkiSprite.draw(window)
			wynikSprite.update()
			wynikSprite.clear(window, f4)
			wynikSprite.draw(window)
			lista_w = naj_wyniki()
			if wynik.wynik >= int(lista_w[0]) and rekord_pobity == 0:
				win = pygame.mixer.Sound('winner.wav')
				win.play()
				rekord_pobity = 1
			pygame.display.flip()
		if pygame.sprite.groupcollide(poohSprite, beesSprite, 0, 1):
			livesSprite.update()
			livesSprite.clear(window,f4)
			livesSprite.draw(window)
			pygame.display.flip()
			if live.live == 0:
				stan = 'przegrana'
			else:
				bzz = pygame.mixer.Sound('bz.wav')
				bzz.play()
				
		poohSprite.update()
		beesSprite.update()
		poohSprite.clear(window, f4)
		beesSprite.clear(window, f4)
		hunnySprite.clear(window, f4)
		poohSprite.draw(window)	
		beesSprite.draw(window)
		hunnySprite.draw(window)
		pygame.display.flip()