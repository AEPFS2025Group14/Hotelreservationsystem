# Hotel Reservation System – AEP Projekt (FS2025)

## 🧾 Projektbeschreibung

Dieses Projekt wurde im Rahmen des Moduls *Anwendungsentwicklung mit Python* (AEP, FS2025) an der Hochschule für Wirtschaft FHNW umgesetzt.  
Ziel ist die exemplarische Implementierung eines Hotelreservierungssystems unter Einsatz moderner Python-Technologien, modularer Softwarearchitektur und relationaler Datenhaltung.

Das Projekt wurde vollständig mit PyCharm umgesetzt, inkl. Versionsverwaltung über GitHub. Eine Deepnote-Integration wurde nicht verwendet
> **Abstract:**  
Diese Arbeit demonstriert, wie sich reale Geschäftsprozesse – dargestellt durch User Stories – systematisch in Codestrukturen überführen lassen. Zum Einsatz kommen objektorientierte Programmierung, relationale Datenbanken (SQLite), Schichtentrennung (N-Tier Architektur) sowie Tools zur Visualisierung und PDF-Ausgabe.

🎥 [Hier klicken, um unsere Projektpräsentation anzusehen](https://link-zu-eurem-video)

> In diesem Video demonstrieren wir unsere Lösung wie in einer Live-Präsentation.  
> Wir zeigen exemplarisch zwei ausgewählte User Stories, die wir besonders gelungen finden, und erklären dabei jeweils die dahinterliegende Logik und den Code.  
> Zudem erläutern wir abwechselnd verschiedene Aspekte des Projekts, insbesondere unsere jeweiligen Beiträge.  
> Beide Teammitglieder sind in der Präsentation zu sehen.

---

## 👤 Rollen

### 👩‍💻 Daliah Beck  
**Rolle: Architektur, Datenmodellierung, Datenzugriff, Geschäftslogik, Dokumentation**

Daliah war verantwortlich für die technische Grundlage und den Aufbau des Hotelreservierungssystems. Ihr Fokus lag auf der initialen Projektstruktur, der Implementierung der Datenmodelle, dem Datenbankzugriff, zentraler Geschäftslogik sowie der vollständigen schriftlichen Dokumentation.

**Beiträge (basierend auf Commit-Verlauf):**

- **Projektsetup & Infrastruktur:**
  - Initialisierung des Repositories (`initial commit`, `.gitignore`, `requirements.txt`, Ordnerstruktur)
  - Einbindung und Organisation der SQLite-Datenbanken (`working_db.db`, `Script.sql`)
  - Git-Konfiguration für sauberen Workflow

- **Modellierung & Datenstruktur:**
  - Erstellung aller Model-Klassen (`Guest`, `Hotel`, `Room`, `Booking`, `Invoice`, `Facility`, `RoomType`)
  - Einbindung von Beziehungen entsprechend dem UML-Diagramm (inkl. Komposition/Aggregation)

- **Data Access & SQL:**
  - Entwicklung und Strukturierung sämtlicher `*_data_access.py`-Dateien
  - Zentrale SQL-Abfragen und Hilfsfunktionen in `SQL.py`
  - Verarbeitung hotel- und zimmerbezogener Daten über strukturierte SQL-Logik

- **Business Logic Layer:**
  - Aufbau der Geschäftslogik-Komponenten:
    - `invoice_manager.py`
    - `booking_manager.py`
    - `room_manager.py`
    - `room_type_manager.py`
  - Implementierung erweiterter Abläufe wie Rechnungslogik, Validierungen, Datenroutinen
  - User Story 5 & 6 

- **Zusätzliche Features & Utility:**
  - Implementierung von `email_sender.py` zur optionalen Buchungsbestätigung per E-Mail
  - Anpassung und Strukturpflege der Utility-Funktionen (`utils/`)

- **Fehlerbehandlung & Konfliktlösung:**
  - Commit am **26.05.2025**: Lösung von Merge-Konflikten und Integration von Hotfixes
  - Verbesserung der Abfragen für spezifische Hotels und Zimmerzuordnung

- **Dokumentation:**
  - Verfasserin der **README.md-Dokumentation**

### 👩 Katharina Hagen  
**Rolle: User Stories, UI/UX, Testing, Versionskontrolle, CLI-Interaktion**

Katharina war für die iterative Entwicklung der User Stories, die Gestaltung der Benutzerführung sowie für Eingabelogik, Testing und Repository-Pflege zuständig. Sie arbeitete kontinuierlich an der Verbesserung der funktionalen Abläufe und sorgte für eine konsistente Ausführung der Anforderungen in der CLI.

**Beiträge (basierend auf Commit-Verlauf):**

- **User Stories (konzeptionell und technisch):**
  - Umsetzung, Überarbeitung und Verbesserung von:
    - **User Story 1–4** (Hotels anzeigen, filtern, Zimmerdetails, Buchung)
    - **Überarbeitung User Story 5 & 6** 
      → *siehe Commit „userstory 5 und 6 verbessert“ am 08.06.2025 – 18:48*
    - **User Story 7 & 8** (dynamische Preise, Buchungsübersicht)
    - **User Story 9 & 10** (Admin-Reports & Datenpflege)
    - Überarbeitung von **User Story 3** (08.06.2025 – 22:59)
  - Korrektur und Feinschliff von Eingabelogik & Datenabfragen im Rahmen dieser Stories

- **UI- & CLI-Interaktion:**
  - Gestaltung der Benutzerführung im CLI
  - Eingabevalidierung & Fehlerbehandlung über `Inputs.py` und eigene Utils
  - Umsetzung und Verknüpfung der Eingabeflüsse mit Business-Logik

- **Testing & Konfliktlösung:**
  - Wiederholtes Refactoring, Testing und Reviews während der Story-Phasen
  - Pflege des konsistenten Codes zwischen Modellierung, Datenzugriff und Logik
  - Merge-Koordination & Konfliktlösungen mit Pull Requests

- **Technische Unterstützung:**
  - Erweiterung von `sql.py` mit spezifischen Abfragen (z. B. Zimmerfilter)
  - Unterstützung bei der Modellintegration & Datenbankabgleich (`model: guest, hotel, room` etc.)


- **Tutorials / Demo** – Daliah Beck, Katharina Hagen  
- **Coaches (extern)** – Charuta Pande, Phillip Gachnang

---

## 🛠️ Tools & Technologien

- **Python 3.10+** – Hauptsprache der Applikation
- **SQLite** – lokale relationale Datenbank
- **pandas** – Verarbeitung tabellarischer Daten (z. B. Rechnungsdetails, Gästeauswertung)
- **matplotlib** – visuelle Darstellung (z. B. Zimmerauslastung, Umsatztrend)
- **fpdf** – Erzeugung von PDF-Buchungsbestätigungen
- **Jupyter Notebook** – explorative Datenanalyse und Funktionsdemos
- **Visual Paradigm** – UML-Klassendiagramm (Designphase)

---

## 🧠 Architektur (N-Tier Modell)

Die Applikation folgt einer **mehrschichtigen Architektur (N-Tier)** zur logischen Trennung und besseren Wartbarkeit. Diese umfasst:

### 1. `database/`  
SQLite-Datenbanken + SQL-Skripte zur Strukturdefinition und Initialbefüllung.

### 2. `model/`  
Objektorientierte Repräsentation aller Entitäten (`Hotel`, `Room`, `Guest`, `Booking`, …) mit klaren Attributen, Methoden und Konstruktoren.

### 3. `data_access/`  
Jede Klasse kümmert sich um eine Entität (z. B. `booking_data_access.py`), führt SQL-Operationen aus und basiert auf einer gemeinsamen `base_data_access.py`.

### 4. `business_logic/`  
Implementiert Geschäftsregeln, Validierungen und komplexe Abläufe wie die Rechnungserstellung (`invoice_manager.py`) oder Zimmerverfügbarkeitsprüfung.

### 5. `ui/` und `utils/`  
- `ui/`: Eingabeprüfung und Konsoleninteraktion (CLI)
- `utils/`: PDF-Export, E-Mail-Versand, SQL-Hilfen

### 6. Root-Level  
- `main.py`: Einstiegspunkt der Anwendung (CLI)
- `Hotelreservation.ipynb`: Notebook zur Analyse & Visualisierung
- `requirements.txt`, `README.md`, `.gitignore`, `LICENSE`

---

## 📐 Klassendiagramm

Das Klassendiagramm zeigt die Beziehungen der zentralen Entitäten im System – inklusive:

- **Komposition:** `Hotel` → `Room`, `Guest` → `Booking`
- **Aggregation:** `Room` → `RoomType`, `Facility`
- **Assoziationen:** `Booking` ↔ `Invoice`

![img_1.png](img_1.png)

> Erstellt mit Visual Paradigm. Das Diagramm diente als Grundlage für die Implementierung aller modellbasierten Klassen.

---

## 📖 Anleitung zur Nutzung der Applikation (CLI)

### Voraussetzungen

- **Python 3.10 oder höher**
- Lokale Entwicklungsumgebung (z. B. PyCharm oder VS Code)
- Abhängigkeiten aus `requirements.txt` (sofern verwendet)

### 1. Projektstruktur vorbereiten

Stelle sicher, dass die Projektstruktur wie folgt vorhanden ist:

/Hotelreservationsystem

├── main.py

├── database/

│ └── hotel_reservation_sample.db

├── data_access/

├── business_logic/

├── model/

├── utils/

└── ...

### 2. Virtuelle Umgebung (empfohlen)

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Anwendung starten
Im Hauptverzeichnis:
```bash
python main.py
```
Daraufhin erscheint im Terminal:

HOTEL RESERVIERUNGSSYSTEM
1. Hotels in einer Stadt anzeigen
2. Verfügbare Zimmer anzeigen
3. Zimmer buchen
4. Rechnung erstellen

### 4. Mögliche Aktionen im CLI

| Option | Beschreibung                                                                     |
| ------ | -------------------------------------------------------------------------------- |
| `1`    | Zeigt alle Hotels in einer bestimmten Stadt                                      |
| `2`    | Listet verfügbare Zimmer in einem Hotel für ein bestimmtes Datum                 |
| `3`    | Bucht ein Zimmer für einen Gast (Eingabe von Gast-ID und Zimmer-ID erforderlich) |
| `4`    | Erstellt eine Rechnung für eine bestehende Buchung                               |

### 5. Erweiterte Funktionen (im Code enthalten, nicht direkt im Menü)
Hotelverwaltung (Admin):

add_hotel(), update_hotel(), delete_hotel() direkt in main.py aufrufbar

Buchung stornieren:

cancel_booking(booking_id)

PDF-Buchungsbestätigung generieren:

create_booking_confirmation() aus utils/pdf_export.py

Bewertungen:

Tabelle Review wird automatisch erstellt, wenn main.py gestartet wird

### 6. Validierung
Alle Eingaben (z. B. Stadtname, Sterne, Gästezahl) werden durch Funktionen in Inputs.py validiert. Ungültige Eingaben lösen ValueError mit passenden Meldungen aus.

> **Abstract:**  
> Hinweis: Es wird keine Notebook-Demo verwendet. Die gesamte Anwendung läuft über eine strukturierte Kommandozeilenoberfläche (CLI) und ist vollständig mit Python und SQLite implementiert.

---

## 🔍 Annahmen & Interpretationen

- **Preiskalkulation:**  
  Der Preis pro Nacht wird direkt aus der Spalte `price_per_night` in der Tabelle `Room` übernommen. Es gibt keine dynamische oder saisonale Preisgestaltung. Der Gesamtbetrag (`total_amount`) ergibt sich durch Multiplikation mit der Anzahl Nächte.


- **Rechnungserstellung:**  
  Eine Rechnung (`Invoice`) wird immer genau einer Buchung (`Booking`) zugeordnet. Der Ausstellungszeitpunkt erfolgt automatisch über `CURRENT_TIMESTAMP`.


- **Stornierungslogik:**  
  Eine Buchung kann nur storniert werden, wenn das Check-In-Datum in der Zukunft liegt. Stornierte Buchungen (Feld `is_cancelled`) verursachen standardmäßig **keine Kosten**, außer es ist eine Stornogebühr definiert (optional über Logik im `BookingManager`).


- **Bewertungen:**  
  Bewertungen werden über die Tabelle `Review` verwaltet. Es wird angenommen, dass **ein Gast pro Hotel genau eine Bewertung** abgeben kann.


- **Eingabevalidierung:**  
  Alle Benutzereingaben (Stadt, Sterne, Gästezahl) werden über dedizierte Funktionen validiert. Städte außerhalb der vordefinierten Liste (`Zürich`, `Luzern`, `Bern`, `Genève`, `Basel`) sind nicht zulässig.


- **Pro Buchung nur ein Zimmer:**  
  Eine Buchung bezieht sich immer auf ein einzelnes Zimmer (1:1 Beziehung). Für mehrere Zimmer müssen mehrere Buchungen erstellt werden.


- **Keine Authentifizierung:**  
  Es gibt keine Login-/Rollenverwaltung. Admin-Funktionen (Hotelpflege, PDF-Export, Stornierung) sind im Code direkt aufrufbar und daher nicht zugriffsgeschützt.


- **Demo-Daten:**  
  Alle Daten (Hotels, Gäste, Zimmer etc.) wurden aus der mitgelieferten `working_db.db` initial geladen. Diese Daten dienen Test- und Demonstrationszwecken.

> Diese Annahmen wurden bewusst getroffen, um den Fokus auf Geschäftslogik, Datenbankanbindung und funktionale Umsetzung gemäß den AEP-Vorgaben zu legen.

---

## 💡 Hervorzuhebende Codebeispiele

Im Rahmen der Umsetzung verschiedener User Stories wurden eine Reihe technischer Lösungen implementiert, die besonders hervorzuheben sind:

### 🔍 1. Dynamische Hotel- und Zimmerfilter (User Story 1.5)

Hotels können anhand einer Kombination aus Stadt, Zeitraum, Sternebewertung und Gästeanzahl gesucht werden. Die Kombination dieser Parameter führt zu einer präzisen Verfügbarkeitssuche:

```python
hotels = hotel_da.search_hotel_combinated(
    city=city_input,
    check_in_date=check_in,
    check_out_date=check_out,
    min_stars=min_stars,
    max_guests=guest_count
)
```
### 🧾 2. Preisberechnung & Rechnungserstellung (User Story 5)

Die Rechnung wird basierend auf dem Zimmerpreis pro Nacht und der Aufenthaltsdauer erstellt und automatisch mit einem Zeitstempel versehen:

```python
total_amount = room.price_per_night * nights
invoice = invoice_da.create_new_invoice(
    booking=booking,
    total_amount=total_amount,
    issue_date=issue_date
)
```
### ❌ 3. Stornierung mit automatischer Rechnungskorrektur (User Story 6)

Bereits fakturierte Buchungen können storniert und auf null gesetzt werden – inklusive Prüfung, ob bereits eine Stornierung erfolgt ist:

```python
if booking.is_cancelled:
    print("Diese Buchung wurde bereits storniert.")
else:
    success = booking_mgr.cancel_booking_by_id(booking_id)
    invoice_da.update_invoice_total(invoice["invoice_id"], 0.00)
```

### 📊 4. Datenvisualisierung: Beliebteste Zimmertypen (User Story 9)

Mit pandas und matplotlib wurde ein Balkendiagramm zur Darstellung der gebuchten Zimmertypen erstellt:

```python
query = """
SELECT rt.description AS room_type, COUNT(*) AS total_bookings
FROM Booking b
JOIN Room r ON b.room_id = r.room_id
JOIN Room_Type rt ON r.type_id = rt.type_id
WHERE b.is_cancelled = 0
GROUP BY rt.description
"""
df = pd.read_sql_query(query, conn)
df.plot(kind="bar", x="room_type", y="total_bookings")
```

### 📈 5. Umsatzanalyse nach Monaten (User Story 10)

Der monatliche Umsatz wird über SQL extrahiert und als Liniendiagramm visualisiert:

```python
query = """
SELECT strftime('%Y-%m', check_in_date) AS month, SUM(total_amount) AS revenue
FROM Booking
WHERE is_cancelled = 0
GROUP BY month
"""
df = pd.read_sql_query(query, conn)
df.plot(kind="line", x="month", y="revenue", marker='o')
```
> **Abstract:**  
Diese Codebeispiele stehen exemplarisch für die Verbindung aus datenbankzentrierter Logik, robuster Geschäftsverarbeitung und benutzerfreundlicher Darstellung.

---

## 🧠 Reflexion

Zu Beginn des Projekts waren wir ursprünglich zu dritt in einer Gruppe. Nachdem sich die Gruppenkonstellation geändert hatte, haben wir (Daliah Beck und Katharina Hagen) das Projekt als Zweierteam eigenständig neu aufgesetzt – mit dem klaren Ziel, eine robuste und vollständig funktionsfähige Lösung für ein Hotelreservierungssystem zu entwickeln.

Anstatt auf bestehende Strukturen zurückzugreifen, haben wir uns bewusst dafür entschieden, das Projekt komplett neu zu starten. Dadurch konnten wir alle zentralen Komponenten – von der Architektur über die Datenbank bis hin zur Business-Logik und den User Stories – selbst gestalten und tiefgehend verstehen. Diese Herangehensweise hat unser Verständnis für die einzelnen Schichten eines Softwaresystems deutlich gestärkt.

Auch wenn der verfügbare Zeitrahmen durch den späten Neustart naturgemäss enger war, haben wir diese Herausforderung als Chance genutzt: Wir haben uns schnell organisiert, klare Verantwortlichkeiten definiert und uns auf ein strukturiertes Vorgehen konzentriert. Gerade in dieser intensiven Phase konnten wir unsere Fähigkeiten in Planung, technischer Umsetzung und Zusammenarbeit besonders weiterentwickeln.

Besonders wertvoll war dabei die konsequente Trennung von Verantwortlichkeiten in unserer N-Tier-Architektur. Das Projekt ermöglichte uns, theoretisches Wissen direkt in die Praxis zu überführen: Wir haben relationales Datenbankdesign mit SQL umgesetzt, datengetriebene Python-Module gebaut, Validierung und Fehlerbehandlung strukturiert integriert, und analytische Visualisierungen mit `pandas` und `matplotlib` realisiert.

Die Tatsache, dass wir die volle Kontrolle über alle Komponenten hatten, erlaubte es uns, technische Entscheidungen mit Verständnis und Absicht zu treffen – von der Modellierung bis hin zur CLI-Interaktion. Besonders stolz sind wir darauf, dass wir sämtliche Minimal-User-Stories erfolgreich umsetzen konnten, einschliesslich erweiterter Funktionen wie PDF-Export, Bewertungslogik und dynamischer Preisberechnung.

Insgesamt blicken wir auf ein Projekt zurück, das nicht nur unsere technischen Fähigkeiten weiterentwickelt hat, sondern uns auch gezeigt hat, wie effektiv kollaboratives Arbeiten in einem strukturierten, selbstgesteuerten Rahmen sein kann. Die Entscheidung, alles eigenständig zu erarbeiten, hat uns nicht nur gefordert, sondern vor allem bestärkt – in unserer Kompetenz, in unserer Klarheit und in unserem Vertrauen in lösungsorientiertes Software-Engineering.
