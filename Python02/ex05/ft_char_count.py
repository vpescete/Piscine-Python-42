import sys

def	char_count(stringa) -> None:
	diz = {}
	for i in stringa:
		diz[i] = diz.get(i, 0) + 1
	chiavi_ordinate = list(diz.keys())
	chiavi_ordinate.sort()
	diz_sorted = {k: diz[k] for k in chiavi_ordinate}
	for lettera, conteggio in diz_sorted.items():
		print(f"{lettera} = {conteggio}")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error! No string given")
	char_count(sys.argv[1])
	