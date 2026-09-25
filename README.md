# Testownik na prawo jazdy
*English below!* 

*Deutsch weiter unten!*

*Українська нижче!*

Program wspomagający naukę do teoretycznego egzaminu na prawo jazdy z oficjalnej bazy Ministerstwa w formie inspirowanej [Testownikiem PWr](https://github.com/TestownikiPWR/testownik-electron). Pozwala opanować wszystkie dostępne pytania dla dowolnej kategorii prawa jazdy. 

> [!NOTE]
> Program wymaga pobrania multimediów do pytań, które na obecny moment zajmują ponad 9 GB pamięci. Tłumaczenia na PJM to dodatkowe 10,5 GB.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9d4eb923-aaaa-49e5-840b-3d820988c635" />

<sub> GenAI disclaimer: przy tworzeniu programu konsultowano modele genAI przy rozwiązywaniu błędów, przy których wyszukiwanie w internecie zawiodło. Wygenerowane fragmenty kodu są nie większe, niż te brane z tutoriali lub odpowiedzi na forach. GenAI zostało użyte także do tłumaczeń na ukraiński i niemiecki. </sub>

## Instalacja
Najpierw zainstaluj pythona i wymagane moduły, jeśli ich nie posiadasz. Program był tworzony na wersjach podanych w nawiasach, ale może być kompatybilny z innymi.
- Python (3.14.3)
- PySide6 (6.11.1)
- pandas (3.0.1)

Sklonuj lub pobierz repozytorium. Ze [strony Ministerstwa Infrastruktury](https://www.gov.pl/web/infrastruktura/prawo-jazdy) pobierz aktualną bazę pytań, zmień nazwę pliku na `baza_pytan.xlsx` i umieść go w folderze `pytania`. Następnie pobierz wszystkie multimedia do pytań, rozpakuj je i umieść bezpośrednio w `multimedia/do_pytan`. Jeśli chcesz korzystać z tłumaczeń na język migowy, analogicznie pobierz je i umieść w `multimedia/PJM`. Program możesz uruchomić z terminala, a na Windowsie także poprzez plik `run.bat` (jeśli nie działa, spróbuj zmienić komendę z `python` na `python3`). 

## Jak to działa
Zasada jest bardzo prosta. W losowej kolejności wyświetlają ci się pytania dla twojej kategorii prawa jazdy, a po udzieleniu przez ciebie odpowiedzi pokazywana jest prawidłowa. Początkowo każde pytanie ma się pojawić dwa razy, ale jeśli odpowiesz źle, zostaną dodane kolejne dwa powtórzenia, żeby to pytanie lepiej ci się utrwaliło. I tak odpowiadasz, aż opanujesz wszystkie pytania. Czy to skuteczne? Powiem tyle, uczyłam się głównie z tego i zdałam za pierwszym razem ;)

## Testownik for Polish driver's license
A program for learning theory for Polish driver's license exam, using the official question base from the Ministry. It's form is inspired by [PWr's Testownik](https://github.com/TestownikiPWR/testownik-electron). It allows to master all available questions for any driver's license category.

> [!NOTE]
> For the program to work, it's necessary to download multimedia for questions, which as of now take up more than 9 GB of memory. PJM translations take up additional 10.5 GB.

<sub> GenAI disclaimer: while making the program, genAI models were consulted in solving errors that internet search did not help with. Generated code fragments are no larger than the ones taken from tutorials or answers on forums. GenAI was also used for translations to Ukrainian and German. </sub>

### How to install
First install python and necessary modules, unless you already have them. The program was created with versions in brackets, but it may be compatible with others.
- Python (3.14.3)
- PySide6 (6.11.1)
- pandas (3.0.1)

Clone or download the repository. From [Ministry's of Infrastructure site](https://www.gov.pl/web/infrastruktura/prawo-jazdy) download the question base, rename the file to `baza_pytan.xlsx` and place it in the folder `pytania`. Next download all multimedia for questions, unpack them and place directly in `multimedia/do_pytan`. If you want to use Polish Sign Language, download the translations as well and place them in `multimedia/PJM`. You may run the program from console, and on Windows also through `run.bat` (if it doesn't work, try changing the command from `python` to `python3`).

### How does it work
The rule is simple. THe questions from your category are shown to you in random order, and after answering the correct answer is shown. Initially every question is supposed to appear two times, but if you answer incorrectly, two additional repeats are added to help you remember this question better. And you go on until you learn all the questions. Is it effective? I'll say this, I was learning mainly from this and I passed on the first try ;)

## Testownik für den Führerschein in Polen
*Der Text wurde mit ChatGPT übersetzt. Die Übersetzung wurde vor der Veröffentlichung überprüft, aber die Sprachkenntnisse des Autors sind begrenzt, sodass möglicherweise einige Fehler unbemerkt geblieben sind.*

Ein Programm zum Lernen der Theorie für die polnische Führerscheinprüfung, das die offizielle Fragen-Datenbank des Ministeriums verwendet. Seine Form ist von [Testownik der PWr](https://github.com/TestownikiPWR/testownik-electron) inspiriert. Es ermöglicht, alle verfügbaren Fragen für jede Führerscheinklasse zu lernen und zu beherrschen.

> [!NOTE]
> Damit das Programm funktioniert, müssen die Multimediadateien für die Fragen heruntergeladen werden. Diese benötigen derzeit mehr als 9 GB Speicherplatz.

<sub> GenAI-Hinweis: Bei der Entwicklung des Programms wurden GenAI-Modelle zur Lösung von Fehlern konsultiert, bei denen eine Internetsuche nicht weitergeholfen hat. Die generierten Codefragmente sind nicht größer als diejenigen, die aus Tutorials oder Antworten in Foren übernommen wurden. GenAI wurde außerdem für die Übersetzungen ins Ukrainische und Deutsche verwendet. </sub>

### Installation
Installiere zunächst Python und die benötigten Module, sofern du sie nicht bereits hast. Das Programm wurde mit den in Klammern angegebenen Versionen erstellt, ist aber möglicherweise auch mit anderen Versionen kompatibel.
- Python (3.14.3)
- PySide6 (6.11.1)
- pandas (3.0.1)

Klone oder lade das Repository herunter. Lade von der [Website des Ministeriums für Infrastruktur](https://www.gov.pl/web/infrastruktura/prawo-jazdy) die Fragen-Datenbank herunter, benenne die Datei in `baza_pytan.xlsx` um und lege sie im Ordner `pytania` ab. Lade anschließend alle Multimediadateien für die Fragen herunter, entpacke sie und lege sie direkt in `multimedia/do_pytan`. Du kannst das Programm über die Konsole starten, unter Windows außerdem über `run.bat` (falls dies nicht funktioniert, versuche, den Befehl von `python` in `python3` zu ändern).

### Wie funktioniert es?
Die Regel ist einfach. Die Fragen aus deiner Führerscheinklasse werden dir in zufälliger Reihenfolge angezeigt. Nach deiner Antwort wird die richtige Antwort angezeigt. Zunächst soll jede Frage zweimal erscheinen. Wenn du jedoch falsch antwortest, werden zwei zusätzliche Wiederholungen hinzugefügt, damit du dir diese Frage besser einprägen kannst. So machst du weiter, bis du alle Fragen beherrschst. Ist das effektiv? Ich sage nur so viel: Ich habe hauptsächlich auf diese Weise gelernt und die Prüfung beim ersten Versuch bestanden ;)

## Testownik для водійських прав в Польщі
*Текст перекладено за допомогою ChatGPT. Перед публікацією переклад було перевірено, але знання мови автора обмежені, тому деякі помилки могли залишитися непоміченими.*

Програма для вивчення теорії перед іспитом на водійські права в Польщі, яка використовує офіційну базу питань Міністерства. Її формат натхненний [Testownik від PWr](https://github.com/TestownikiPWR/testownik-electron). Програма дає змогу опанувати всі доступні питання для будь-якої категорії водійських прав.

> [!NOTE]
> Для роботи програми необхідно завантажити мультимедійні матеріали для питань, які наразі займають понад 9 ГБ пам'яті.

<sub> Примітка щодо GenAI: під час створення програми моделі GenAI використовувалися для пошуку рішень помилок, які не вдалося вирішити за допомогою пошуку в інтернеті. Згенеровані фрагменти коду не більші за фрагменти, взяті з навчальних посібників або відповідей на форумах. GenAI також використовувався для перекладу українською та німецькою мовами. </sub>

### Як встановити
Спочатку встановіть Python та необхідні модулі, якщо вони ще не встановлені. Програма створювалася з використанням версій, зазначених у дужках, але може бути сумісною і з іншими версіями.
- Python (3.14.3)
- PySide6 (6.11.1)
- pandas (3.0.1)

Клонуйте або завантажте репозиторій. На [сайті Міністерства інфраструктури](https://www.gov.pl/web/infrastruktura/prawo-jazdy) завантажте базу питань, перейменуйте файл на `baza_pytan.xlsx` і помістіть його до папки `pytania`. Потім завантажте всі мультимедійні матеріали для питань, розпакуйте їх і помістіть безпосередньо до `multimedia/do_pytan`. Запустити програму можна через консоль, а у Windows також за допомогою `run.bat` (якщо це не працює, спробуйте змінити команду з `python` на `python3`).

### Як це працює
Правило просте. Питання з обраної вами категорії показуються у випадковому порядку, а після відповіді відображається правильна відповідь. Спочатку кожне питання має з'явитися двічі, але якщо ви відповісте неправильно, додаються ще два повторення, щоб допомогти вам краще запам'ятати це питання. Так триває доти, доки ви не опануєте всі питання. Чи ефективно це? Скажу лише одне: я вчилася переважно за допомогою цієї програми й склала іспит з першої спроби ;)
