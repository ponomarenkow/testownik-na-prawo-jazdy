import settings

strings = {
    "PL": {
        "title": "Testownik na prawko",
        "loading": "Ładowanie...",
        "question nr": "Pytanie nr ",
        "range": "Zakres: ",
        "points": "Wartość punktowa: ",
        "repeats": "Pozostało powtórzeń: ",
        "learned": "Opanowane pytania: ",
        "video": "Rozpocznij wideo",
        "yes": "Tak",
        "no": "Nie",
        "next": "Następne",
        "end": "Koniec nauki!",
        "media error": "Nie udało się załadować multimedium.",
        "settings": "Ustawienia",
        "category": "Kategoria: ",
        "lang": "Język: ",
        "save": "Zapisz",
        "save error": "Błąd przy próbie otwarcia pliku zapisu.",
        "questions error": "Nie udało się otworzyć pliku z pytaniami.",
        "podstawowy": "podstawowy",
        "specjalistyczny": "specjalistyczny",
        "lang error": "Nie odnaleziono tłumaczenia dla języka. Wybierz jeden z: ",
        "category error": "Nie odnaleziono kategorii. Wpisz istniejącą kategorię prawa jazdy.",
        "numeric error": "Wartość musi być liczbą naturalną.",
        "font": "Rozmiar czcionki: ",
        "initial repeats": "Liczba początkowych powtórzeń: ",
        "added repeats": "Liczba powtórzeń dodawanych po błędzie: ",
        "restart": "Powtórz najtrudniejsze"
    },
    "EN": {
        "title": "Testownik for driver's license",
        "loading": "Loading...",
        "question nr": "Question nr ",
        "range": "Range: ",
        "points": "Point value: ",
        "repeats": "Remaining repeats: ",
        "learned": "Mastered questions: ",
        "video": "Start video",
        "yes": "Yes",
        "no": "No",
        "next": "Next",
        "end": "Questions finished!",
        "media error": "Failed to load multimedium.",
        "settings": "Settings",
        "category": "Category: ",
        "lang": "Language: ",
        "save": "Save",
        "save error": "Failed to open the save file.",
        "questions error": "Failed to open the questions file.",
        "podstawowy": "fundamental",
        "specjalistyczny": "specialized",
        "save": "Save",
        "lang error": "Translation for the language not found. Choose one from: ",
        "category error": "Category not found. Enter existing Polish driving license category.",
        "numeric error": "The value must be a natural number.",
        "font": "Font size: ",
        "initial repeats": "Number of initial repeats: ",
        "added repeats": "Number of repeats added after a mistake: ",
        "restart": "Repeat difficult ones"
    },
    "D": {
        "title": "Testownik für den Führerschein",
        "loading": "Wird geladen...",
        "question nr": "Frage Nr. ",
        "range": "Bereich: ",
        "points": "Punktwert: ",
        "repeats": "Verbleibende Wiederholungen: ",
        "learned": "Beherrschte Fragen: ",
        "video": "Video starten",
        "yes": "Ja",
        "no": "Nein",
        "next": "Nächste",
        "end": "Fragen abgeschlossen!",
        "media error": "Medien konnten nicht geladen werden.",
        "settings": "Einstellungen",
        "category": "Führerscheinklasse: ",
        "lang": "Sprache: ",
        "save error": "Speicherdatei konnte nicht geöffnet werden.",
        "questions error": "Fragen-Datei konnte nicht geöffnet werden.",
        "podstawowy": "Grundfragen",
        "specjalistyczny": "Spezialfragen",
        "save": "Speichern",
        "lang error": "Übersetzung für die Sprache nicht gefunden. Wählen Sie eine aus: ",
        "category error": "Führerscheinklasse nicht gefunden. Geben Sie eine vorhandene Führerscheinklasse ein.",
        "numeric error": "Der Wert muss eine natürliche Zahl sein.",
        "font": "Schriftgröße: ",
        "initial repeats": "Anzahl der anfänglichen Wiederholungen: ",
        "added repeats": "Anzahl der nach einem Fehler hinzugefügten Wiederholungen: ",
        "restart": "Schwierige wiederholen"
    },
    "UA": {
        "title": "Testownik для водійських прав",
        "loading": "Завантаження...",
        "question nr": "Питання № ",
        "range": "Розділ: ",
        "points": "Бали: ",
        "repeats": "Залишилося повторити: ",
        "learned": "Засвоєні питання: ",
        "video": "Відтворити відео",
        "yes": "Так",
        "no": "Ні",
        "next": "Наступне",
        "end": "Питання завершено!",
        "media error": "Не вдалося завантажити мультимедійні матеріали.",
        "settings": "Налаштування",
        "category": "Категорія: ",
        "lang": "Мова: ",
        "save error": "Не вдалося відкрити файл збереження.",
        "questions error": "Не вдалося відкрити файл із питаннями.",
        "podstawowy": "основні",
        "specjalistyczny": "спеціальні",
        "save": "Зберегти",
        "lang error": "Переклад для цієї мови не знайдено. Виберіть одну з доступних: ",
        "category error": "Категорію не знайдено. Введіть наявну категорію польського водійського посвідчення.",
        "numeric error": "Значення має бути натуральним числом.",
        "font": "Розмір шрифту: ",
        "initial repeats": "Кількість початкових повторень: ",
        "added repeats": "Кількість повторень, доданих після помилки: ",
        "restart": "Повторити складні"
    }
}

def get_string(string: str):
    try:
        if settings.lang == "PJM":
            return strings["PL"][string]    
        return strings[settings.lang][string]
    except:
        try:
            return strings["EN"][string]
        except:
            try:
                return strings["PL"][string]
            except:
                return ""

