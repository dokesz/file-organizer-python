# file-organizer-python
Ez a projekt egy beadandó a Széchenyi István Egyetem (SZE) Linux ismeretek (GKNB_MSTM028) nevű órájára.

Ez egy Python kód, amely figyeli a Letöltések mappát, és automatikusan áthelyezi a fájlokat a Dokumentumok mappába fájlkiterjesztés alapján. Ha már létezik egy fájl ugyanazzal a névvel, a script módosítja az újonnan másolt fájl nevét, hogy elkerülje a névütközést. A watchdog könyvtárat használom a mappák változásainak figyelésére.

Kód felépítése:

- Szükséges modulok importálása.
- Definiál egy DownloadFolderHandler osztályt, amely a FileSystemEventHandler osztályból származik
- Az osztály on_modified metódusa válaszol a mappa módosulásaira.
- A get_new_filename függvény segítségével hozok letre egy egyedi nevet az újonnan másolt fájlnak (mögé ír egy számot pluszban), abban az estben, ha már létezik ilyen nevű fájl (mivel ilyenkor felülírja csak, tehát a régit törölné) 
- Szükséges beállítani a kiindulási és cél útvonalakat (ez bármi lehet, tesztelési szempontból célszerű létrehozni ehhez egy új mappát)
- watchdog Observer elindítása, amely figyeli a kiindulási útvonalat és ha változás történik meghívja DownloadFolderHandler osztály on_modified metódusát
- A kód végtelen ciklusban fut, amíg a felhasználó meg nem szakítja CTRL+C lenyomásával.

A használata előtt győződjön meg róla, hogy telepítette a watchdog csomagot a Python környezetébe. Ha még nem telepítette, futtassa ezt a parancsot:

 `pip install watchdog`
