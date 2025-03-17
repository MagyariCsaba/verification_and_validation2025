# Alkalmazotti Menedzsment Rendszer - Tesztelési Projekt

Ez a repository egy egyszerű alkalmazotti menedzsment rendszer egységtesztjeit tartalmazza, amely egy szoftvertesztelési kurzus keretében készült.

## Projekt áttekintés

A projekt célja egy már meglévő kódbázis egységtesztelése Python és pytest segítségével. A rendszer a következő fő komponensekből áll:

- `Employee`: Alkalmazotti adatokat tároló adatosztály
- `RelationsManager`: Alkalmazottak és fejlesztési csapatok kezelése
- `EmployeeManager`: Alkalmazotti fizetések számítása és értesítések kezelése

## Telepítés

1. Python 3.x telepítése szükséges

2. Virtuális környezet létrehozása:

   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # VAGY
   venv\Scripts\activate  # Windows
  

4. Függőségek telepítése:
   
   pip install pytest
   

## Fájlstruktúra


./
├── employee.py                # Alkalmazott adatosztály
├── relations_manager.py       # Alkalmazotti kapcsolatok kezelése
├── employee_manager.py        # Fizetések számítása
├── test_relations_manager.py  # RelationsManager tesztek
├── test_employee_manager.py   # EmployeeManager tesztek
└── README.md                  # Ez a fájl


## Tesztek futtatása

Az összes teszt futtatása:

pytest -v


Egy specifikus tesztfájl futtatása:

pytest -v test_relations_manager.py


Egy specifikus teszt futtatása:

pytest -v test_relations_manager.py::test_john_doe_is_team_leader


## Tesztelési követelmények

A projekt a következő tesztelési követelményeket valósítja meg:

### RelationsManager tesztek:
- Ellenőrzi, hogy van-e John Doe nevű csapatvezető, akinek a születési dátuma 1970.01.31.
- Ellenőrzi, hogy John Doe csapattagjai Myrta Torkelson és Jettie Lynch.
- Biztosítja, hogy Tomas Andre nem tagja John Doe csapatának.
- Ellenőrzi, hogy Gretchen Walford alapfizetése 4000$.
- Biztosítja, hogy Tomas Andre nem csapatvezető, és ellenőrzi mi történik, ha megpróbáljuk lekérni a csapattagjait.
- Biztosítja, hogy Jude Overcash nincs tárolva az adatbázisban.

### EmployeeManager tesztek:
- Ellenőrzi egy olyan alkalmazott fizetését, aki nem csapatvezető, és akit 1998.10.10-én vettek fel 1000$ alapfizetéssel.
- Ellenőrzi egy csapatvezető fizetését, akinek 3 tagból áll a csapata, 2008.10.10-én vették fel és az alapfizetése 2000$.
- Biztosítja, hogy a fizetésszámítás és e-mail értesítés a megfelelő információkkal történik (név és üzenet).

## Dokumentáció

A teljes projekt dokumentációja a `Szoftvertesztelés.pdf` fájlban található, amely tartalmazza:
- A választott egységteszt keretrendszer leírását
- A tesztelési repository struktúráját
- Minden egyes fejlesztett egységteszt részletes leírását
