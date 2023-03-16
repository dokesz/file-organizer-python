# file-organizer-python
Ez a projekt egy beadandó a Széchenyi István Egyetem (SZE) Linux ismeretek (GKNB_MSTM028) nevű órájára.

Ez egy Python script, amely figyeli a Letöltések mappát, és automatikusan áthelyezi a fájlokat a Dokumentumok mappába fájlkiterjesztés alapján. Ha már létezik egy fájl ugyanazzal a névvel, a script módosítja az újonnan másolt fájl nevét, hogy elkerülje a névütközést. A script a watchdog könyvtárat használja a mappák változásainak figyelésére.

Script felépítése:

Importálja a szükséges modulokat.
Definiál egy DownloadFolderHandler osztályt, amely a FileSystemEventHandler osztályból származik. Az osztály on_modified metódusa válaszol a mappa módosulásaira.
A get_new_filename függvény segít létrehozni egy egyedi nevet az újonnan másolt fájlnak, ha már létezik egy ugyanolyan nevű fájl a célkönyvtárban.
Beállítja a mappákat a Letöltések és Dokumentumok elérési útvonalaira. Ezeket a változókat a saját elérési útvonalaidra kell módosítani.
Inicializálja és elindítja a watchdog Observer-t, amely figyeli a Letöltések mappát, és hívja a DownloadFolderHandler osztály on_modified metódusát, amikor változás történik.
A script végtelen ciklusban fut, amíg a felhasználó meg nem szakítja CTRL+C lenyomásával.

At the command prompt, type `nano`.
