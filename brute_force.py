import numpy as np

def unpackbits(x, num_bits):
	xshape = list(x.shape)

	x = x.reshape([-1, 1])
	mask = 2 ** np.arange(num_bits, dtype=x.dtype).reshape([1, num_bits])
	return (x & mask).astype(bool).astype(int).reshape(xshape + [num_bits])
def liczby_binarne(ile_zmiennych):
	dlugosc_wyniku = 2 ** ile_zmiennych
	wyn = unpackbits(np.arange(dlugosc_wyniku, dtype=np.uint16), ile_zmiennych)
	return wyn


LICZBY_BINARNE = {6: liczby_binarne(6), 12: liczby_binarne(12), 15: liczby_binarne(15), 5:liczby_binarne(5)}

def tablica_prawdy(ile_zmiennych, czy_zanegowane, duplikaty_index):
	wyn = []
	for i in LICZBY_BINARNE[ile_zmiennych]:

		xor = 0
		for j in range(ile_zmiennych):
			if i[j] and duplikaty_index[j]:
				xor = xor ^ 1

		if czy_zanegowane:
			xor = not xor

		wyn.append(xor)
	return wyn


def porownaj(l1, l2, max_zmienionych):
	czy_niezmienione = np.array(l1) == np.array(l2)
	return np.count_nonzero(czy_niezmienione==0) <= max_zmienionych


def mozliwosci(ile_zmiennych, przyklad, max_zmienionych):
	# mozliwosci
	for x in LICZBY_BINARNE[ile_zmiennych]:
		# Bez negacji
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 0, x)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return 0, *x[::-1]
		# Z negacją
		mozliwy_szyfr = tablica_prawdy(ile_zmiennych, 1, x)
		if porownaj(mozliwy_szyfr, przyklad, max_zmienionych):
			return 1, *x[::-1]


def odkoduj(dlugosc_jednej_wiadomosci, ile_wiadomosci, max_zmienionych_bitow, przyklady):
	ile_zmiennych = dlugosc_jednej_wiadomosci - 1

	i = 0
	while i < ile_wiadomosci:
		przyklad = [int(x) for x in przyklady[i]]
		print(f"{mozliwosci(ile_zmiennych, przyklad, max_zmienionych_bitow)}")
		i += 1


def uruchom(sciezka):
	with open(sciezka) as my_file:
		t = my_file.read().rstrip().split('\n')
	przyklady = t[3:]

	dlugosc_wiadomosci = int(t[0])
	ile_przykladow = int(t[1])
	max_zmienionych_bitow = int(t[2])

	odkoduj(dlugosc_jednej_wiadomosci=dlugosc_wiadomosci, ile_wiadomosci=ile_przykladow,
			max_zmienionych_bitow=max_zmienionych_bitow, przyklady=przyklady)

if __name__ == '__main__':
	sciezka1 = "messages7.in.txt"
	sciezka2 = "messages13.in.txt"
	sciezka3 = "messages16.in.txt"

	# uruchom(sciezka1)
	# uruchom(sciezka2)
	# uruchom(sciezka3)

