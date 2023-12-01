import numpy as np
def odkoduj_jeden_element(przyklad, ktory_el):
	dlugosc_jednej_czesci = 2**ktory_el
	polowa = (dlugosc_jednej_czesci//2)
	ile_czesci = len(przyklad)//dlugosc_jednej_czesci
	przyklad_podzielony = przyklad.reshape((ile_czesci, dlugosc_jednej_czesci))

	count_rozne = 0
	count_takie_same = 0
	for czesc in przyklad_podzielony:
		i = 0
		while i < polowa:
			if czesc[i] == czesc[i + polowa]:
				count_takie_same += 1
			else:
				count_rozne += 1
			i += 1
	if count_rozne < count_takie_same: return 0
	elif count_rozne > count_takie_same: return 1

def czy_zanegowane(przyklad, odkodowana_wiadomosc):
	przyklad_podzielony = np.copy(przyklad)
	ile_zmiennych = len(odkodowana_wiadomosc)
	i = ile_zmiennych

	while i > 0:
		if odkodowana_wiadomosc[i-1] == 1:
			dlugosc_jednej_czesci = 2 ** (i-1)
			ile_czesci = len(przyklad) // dlugosc_jednej_czesci
			przyklad_podzielony = przyklad.reshape((ile_czesci, dlugosc_jednej_czesci))
			for x in range(1, len(przyklad_podzielony), 2):
				for y in range(len(przyklad_podzielony[x])):
					przyklad_podzielony[x][y] = not przyklad_podzielony[x][y]
			przyklad_podzielony = przyklad_podzielony.flatten()
		i-=1
	jedynki = np.count_nonzero(przyklad_podzielony)
	zera = len(przyklad_podzielony) - jedynki
	return jedynki > zera



def odkoduj(przyklad, ile_zmiennych):
	result = []
	for i in range(1, ile_zmiennych + 1):
		result.append(odkoduj_jeden_element(przyklad, i))
	if czy_zanegowane(przyklad, result):
		print([1]+result[::-1])
	else:
		print([0]+result[::-1])
def uruchom(sciezka):
	with open(sciezka) as my_file:
		t = my_file.read().rstrip().split('\n')
	przyklady = t[3:]

	dlugosc_wiadomosci = int(t[0])
	ile_zmiennych = dlugosc_wiadomosci - 1
	# ile_przykladow = int(t[1])
	# max_zmienionych_bitow = int(t[2])
	for przyklad in przyklady:
		przyklad_array = np.array(list(przyklad), dtype=np.int8)
		odkoduj(przyklad_array, ile_zmiennych)


if __name__ == '__main__':
	sciezka1 = "messages7.in.txt"
	sciezka2 = "messages13.in.txt"
	sciezka3 = "messages16.in.txt"

	uruchom(sciezka1)
	uruchom(sciezka2)
	uruchom(sciezka3)