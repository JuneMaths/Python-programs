import urllib.request
import xml.etree.ElementTree as ET
import os
import datetime
from tkinter import *
import tkinter.ttk as ttk


# ## POBIERANIE DANYCH Z NBP
try:
	web = True
	local_filename, headers = urllib.request.urlretrieve(r'http://www.nbp.pl/kursy/xml/LastA.xml', # strona www.nbp.pl
			r'C:\Users\*\NBP_converter\the_last_rate.xml') # path to file
	with open(local_filename) as file:
		tree = ET.parse(file) #tworze z niego drzewo
		root = tree.getroot() #czytam drzewo i zapisuję uchwyt
		file.close()	

except(urllib.error.URLError):
	web = False
	print('No network connection')

if web == False:
	tree = ET.parse('the_last_rate.xml')
	root = tree.getroot()


# ## POBRANIE DATY NOTOWANIA
t = os.path.getmtime('the_last_rate.xml')
filetime = datetime.datetime.fromtimestamp(t)
filetime = '%i.%i.%i' % (filetime.day, filetime.month, filetime.year)


# ## SŁOWNIK DANYCH
DATA = {} #słownik
CODE = []
for position in root.findall('pozycja'): #szukam wszystkich pozycjii w drzewie
	code = position.find('kod_waluty').text
	name = position.find('nazwa_waluty').text
	conventer = int(position.find('przelicznik').text)
	course = float(position.find('kurs_sredni').text.replace(',', '.')) #zamieniam ',' na '.'
	CODE.append(code + '  -  ' + str(course))	#do zapisu combobox (dodaję aktualny course)
	DATA[code] = {'name' : name, 'conventer' : conventer, 'course' : course} #zapisuję słownik w słowniku

# ## PROJEKTOWANIE OKNA NBP
class NBP:
	def __init__(self, master, DATA, CODE):
		'''funkcja projektuje okno do conventera walut'''
		self.DATA = DATA	#DATA globalne
		
		self.lc1 = Label(master, text = 'TARGET CURRENCY:', bg = '#B0B6BA', fg = '#000000')
		self.lc1.grid(row = 1, column = 1, )
		self.chosen1 = StringVar()
		self.c1 = ttk.Combobox(master, width = 30, textvariable = self.chosen1)
		t = ("I'd like to get...", 'PLN')
		for i in range(len(CODE)):	#pętla wpisuje wartośli do combobox
			t = t + (CODE[i], )
		self.c1['values'] = t
		self.c1.current(0)	#domyślny pierwszy argument
		self.c1.grid(row = 2, column = 1, padx = 20)
			
		self.lc1 = Label(master, text = 'SOURCE CURRENCY:', bg = '#B0B6BA',fg = '#000000')
		self.lc1.grid(row = 3, column = 1)
		self.chosen2 = StringVar()
		self.c2 = ttk.Combobox(master, width = 30, textvariable = self.chosen2)	#width-szerokość okna
		t = ('I have got...', 'PLN')
		for i in range(len(CODE)):
			t = t + (CODE[i], )
		self.c2['values'] = t
		self.c2.current(0)
		self.c2.grid(row = 4, column = 1, padx = 20)	#padx-odstęp w poziomie

		self.l1 = Label(master, text = 'AMOUNT TO CONVERT:', bg = '#B0B6BA',fg = '#000000')
		self.l1.grid(row = 5, column = 1)	
		self.e1 = Entry(master, width = 30)
		self.e1.grid(row = 6, column = 1)

		self.l2 = Label(master, text = 'RESULT:', font = ('bold'), fg = '#000000', bg = '#B0B6BA')
		self.l2.grid(row = 4, column = 5)
		self.l3 = Label(master, text = '', font = ('bold'), fg = '#000000', bg = '#B0B6BA')
		self.l3.grid(row = 5,column=5)
				
		self.b1 = Button(master, text = 'CONVERT', command=self.przelicz, bg = '#91D3FF')
		self.b1.grid(row = 8, column = 1, padx = 20, pady = 20)	#pady-odstęp w pionie
			
		self.l5 = Label(master, text = '', fg = 'crimson', bg = '#B0B6BA') #Błąd
		self.l5.grid(row = 7, column = 1)

		self.l4 = Label(master, text = 'QUOTATION DATE: ' + str(filetime), fg = '#000000', bg = '#B0B6BA')
		self.l4.grid(row = 1, column = 5, padx = 20)

		self.btn = Button(master, text = "QUIT", command = quit, bg = '#91D3FF')
		self.btn.grid(row = 8, column = 5, padx = 10, pady = 10)


	# ## PRZELICZANIE courseÓW WALUT
	def przelicz(self):
		'''funkcja przelicza coursey walut'''	
		x_from = self.c2.get()
		x_from = x_from[:3]
		y_to = self.c1.get()
		y_to = y_to[:3]
		amount = self.e1.get()
		self.l3.configure(text = '')
		if x_from == 'I have got...' or y_to == "I'd like to get..." or type(amount) == str:	#jeżeli coś zostało źle uzupełnione
			self.l5.configure(text = 'Incorrectly entered data')
		amount = float(amount)
		if x_from == y_to:	#kiedy przeliczam z tej samej currency
			new_amount = amount
		elif x_from == 'PLN' and y_to != 'PLN':	#kiedy przeliczam z polskich
			y_to_course = float(DATA[y_to]['course'])
			y_to_conventer = int(DATA[y_to]['conventer'])
			new_amount = (amount * y_to_conventer) / y_to_course
		elif y_to == 'PLN' and x_from != 'PLN':	#kiedy przeliczam na polskie
			x_from_course = float(DATA[x_from]['course'])
			x_from_conventer = int(DATA[x_from]['conventer'])
			new_amount = (amount * x_from_course) / x_from_conventer
		else:	#kiedy przeliczam z obcej currency na inną
			x_from_course = float(DATA[x_from]['course'])
			x_from_conventer = int(DATA[x_from]['conventer'])
			y_to_course = float(DATA[y_to]['course'])
			y_to_conventer = int(DATA[y_to]['conventer'])
			PLN = (amount * x_from_course) / x_from_conventer
			new_amount = (PLN * y_to_conventer) / y_to_course
		self.l3.configure(text = str(round(new_amount, 2)))	#pojawia się wynik
		self.l5.configure(text = '')	#jeżeli wszystko dobrze to błąd nie wyskoczy (a jak był wcześniej to się resetuje)



# ## WYWOŁANIE OKNA
if __name__ == "__main__":	
	window = Tk()
	window.title('exchange rate converter')#tytuł okna
	window.geometry('+550+300')	#miejsce gdzie się pojawia okno
	window.configure(bg = '#B0B6BA') 	#tło okna
	n = NBP(window, DATA, CODE)
	window.mainloop() #pętla zdarzeń
