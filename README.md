# Portfolio-Prüfung für Programmierung 1: Staubsaugerroboter

## Hintergrund
Das Unternehmen "Storverk AB" ist ein Hersteller von Haushaltsgeräten. Für das neue akkubetriebene Modell "RoboSaug+Wisch 3000" wurde sich dazu entschieden, die komplette Logik, Kollisionserkennung und Wegfindung des Roboters auf einer neuen Plattform mit Java zu implementieren. Das unternehmensinterne Team aus Elektrotechnikern kümmert sich um die Anbindung der Sensorik, benötigt allerdings Ihre Unterstützung bei der Implementierung des Kontrollprogramms.

Da der "RoboSaug+Wisch 3000" noch nicht vollständig entwickelt ist, stellt Ihnen Ihr Auftraggeber ein Python-Programm bereit, das die Simulation von verschiedenen Räumen und Gegenständen ermöglicht. Zusätzlich lässt sich dadurch der Energiebedarf simulieren, sodass eine rechtzeitige Rückkehr des Roboters zur Ladestation möglich ist.

## Aufgabenstellung
Machen Sie sich mit der Funktionsweise des Python-Programms vertraut. "Übersetzen" Sie anschließend dieses Programm in ein objektorientiertes Java-Programm. Übernehmen und erweitern Sie auf dieser Basis Ihre `Roboter`-Klasse mit dem zur Erfüllung der Anforderungen des Auftragsgebers nötigen Logik.

**Hinweis:** Der Staubsaugerroboter wird von unabhängigen Instituten vor der Markteinführung geprüft - dabei wird auch die Codequalität beachtet! Zudem soll der Roboter auf die unterschiedlichsten Situationen und Raum-Designs reagieren können und **immer** einen sauberen Raum hinterlassen.

## Organisatorisches

### Teambildung
- 2er- bis 3er-Teams
- Anmeldung der Teams bis **Freitag, 27.11.2020, 18:00 Uhr (CET)** per E-Mail
- Pro Team **eine** Mail mit Liste der Mitglieder
- Studierende, die bis zum 27.11.2020, 18:00 Uhr (CET) nicht in einem Team gemeldet wurden, werden per Zufall Teams zugewiesen

### Abstimmungstermin
- Pro Gruppe ein Termin, bei dem der jeweilige Zwischenstand besprochen wird
- Ziel: Prüfung der Eigenständigkeit sowie andererseits wollen wir Tipps bzw. Beratung durch den Dozenten
- Der Zeitpunkt darf von der Gruppe selbst bestimmt werden.
- Die Bearbeitung muss zu diesem Zeitpunkt noch nicht vollständig sein.
- Jedes Gruppenmitglied muss teilnehmen und etwas (sinnvolles) zur Diskussion beitragen

### Abgabe
- Spätestens am **23.12.2020 um 23:59 Uhr (CET)** über Moodle
- ZIP-Datei mit Quellcode (`.java`-Dateien) und Dokumentation (PDF)
- Moodle-Abgabe (ein/e Verantwortliche/r pro Team)
- Namen und Matrikelnummern der Teammitglieder auf Deckblatt der Dokumentation nennen

## Bewertungskriterien

### Dokumentation
- **Sprache:** Deutsch
- **Deckblatt:** Namen und Matrikelnummern der Teammitglieder
- **Umfang:** Keine Vorgabe für minimale oder maximale Seitenanzahl, ca. 10 Seiten sind realistisch
- **Ziel:** Gesamtkonzept beschreiben
  - Klassendiagramm (UML) mit Klassen, Attributen, Methoden, Sichtbarkeiten und Beziehungen
  - Vorgehen und Umsetzung von Roboter-Logik beschreiben und erklären
  - Entscheidungen (z. B. für Datenstrukturen) erklären

### Funktionalität
Es sind mehrere Räume mit aufsteigender Schwierigkeit in Form von Textdateien vorgegeben. Ihr Java-Programm sollte möglichst viele dieser Test-Räume lösen können.

Genauer wird in der in Java vorgegebenen Main-Methode ein Roboter, ein Raum und ein Logger erzeugt. Dann wird in einer Schleife der Roboter so lange nach seinem jeweils nächsten Schritt gefragt, bis er über seine `isDone()`-Methode signalisiert, dass er fertig ist.

Der Roboter soll in jedem Schritt die zu fahrende Differenz in x- und y-Richtung liefern, wobei es immer nur erlaubt ist, einen Schritt in jede Richtung zu machen.
Es wird erwartet, dass durch den Roboter ein Weg angegeben wird (und am Ende im Logger steht), der den gesamten Raum säubert und der auch mit der vorhandenen Akku-Kapazität gefahren werden kann (siehe Python-Vorgabe).

→ Details ergeben sich aus Python-Code. Das Verständnis des vorgegebenen Codes gehört zur Aufgabe dazu!

| Symbol | Beschreibung |
| :--- | :--- |
| ` ` | Freiraum |
| `D` | Dreck, Staub |
| `S` | Ladestation |
| `R` | Roboter |
| `W` | Wand, Hindernis |

### Codequalität
- Einheitliche Formatierung (Klammern, Einrückung usw.)
- Sinnvolle Kommentare im Code
  - Kurzbeschreibungen der wichtigsten Methoden ("**was** macht die Methode?")
  - an komplizierten Stellen Erklärungen der Funktionsweise ("**wie** wird das in der Methode umgesetzt?")
- (Sinnvolle) Anwendung von Prinzipien der Objektorientierung
- Verwendung adäquater Datentypen
- Sinnvolle Attributs- und Methodennamen
- Namenskonventionen und Schreibweisen beachten


## Deadlines
- Anmeldung der Teams bis **Freitag, 27.11.2020, 18:00 Uhr (CET)** per E-Mail
- Terminvereinbarung zu **verpflichtendem** Abstimmungstermin bis spätestens 18.12.2020
- Abgabe von Dokumentation und Code spätestens am **23.12.2020 um 23:59 Uhr (CET)** über Moodle
