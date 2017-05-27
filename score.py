hraci = {}
juniors = []


def usporiadaj():
    return [(poc, hraci[poc]) for poc in sorted(hraci, key=hraci.get, reverse=True)]


# dekorator
#overi si heslo a pokracuje s funkciou ak je spravne
def check(function):
    def wrapper(*args, **kwargs):
        check = raw_input("Zadaj heslo: ")
        if(check == password):
            return function(*args, **kwargs)
        else:
            print("Nespravne heslo")
            return False
    return wrapper


# prida hracovi 'name' skore 'number' ak existuje hrac 'name' inak prida hraca 'name' so skore 'number'
@check
def points(name, number):
    if name in hraci:
        hraci[name] += number
    else:
        hraci[name] = number


# zmensi skore vsetkym hracom o per %
@check
def reduce(per):
    for i in hraci:
        hraci[i] = int(hraci[i] * (1.0 - (per / 100)))


# prida hraca medzi juniorov
@check
def junior(name):
    if not name in juniors:
        juniors.append(name)
        if not name in hraci:
            hraci[name] = 0


# usporiada vsetkych hracov podla skore a vypise ich
def ranking():
    print('Ranking vsetkych hracov:')
    s = usporiadaj()
    for h, ss in s:
        print(h,' ',ss)


# same as ranking, but with juniors only
def ranking_junior():
    print('Ranking juniorov:')
    s = usporiadaj()
    for h, ss in s:
        if h in juniors:
            print(h,' ',ss)


# koniec
@check
def end():
    quit()


# nastavit heslo
password = raw_input("Nastav si prosim ta heslo: ")


while True:

    cmd = raw_input("Zadaj prikaz: ").split()

    if cmd[0] == "points":
        points(cmd[1], int(cmd[2]))
    elif cmd[0] == "reduce":
        reduce(float(cmd[1]))
    elif cmd[0] == "junior":
        junior(cmd[1])
    elif cmd[0] == "ranking":
        if len(cmd)>1:
            ranking_junior()
        else:
            ranking()
    elif cmd[0] == "quit":
        end()