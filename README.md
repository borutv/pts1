# pts1
Domaca uloha 1

Program uchováva zoznam učastníkov a ich aktuálny stav bodov v sútaži. Po spustení si program od užívateľa vypýta heslo. Potom program čaká na príkazy od užívateľa, ktoré následne vykoná.

points <name:string> <number:int> Pridá hráčovi bodov. Číslo môže byť aj záporné. Ak hráč ešte nie je evidovaný pridá ho do zoznamu s bodmi.

reduce <number:int> Zníži počet bodov každého hráča o %. Výsledok sa zaokrúhli na celé čísla nadol.

junior <name:string> Označí, že hráč je junior

ranking Vypíše celé poradie. Hráčov zoradíme podľa počtu bodov.

ranking junior Vypíše poradie medzi juniormi.

quit Ukončí program.

Ak užívateľ zadá príkazy points, reduce, junior, a quit systém si najprv vypýta password a príkaz vykoná iba v prípade, že password je správny.
