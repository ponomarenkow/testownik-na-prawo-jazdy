import json

category = "B"
lang = "PL"
lang_tag = ""
save_path = "saves/save.csv"
diff_path = "saves/difficult.csv"
first_run = True
initial_repeats = 2
added_repeats = 2
max_width = 1000
media_width = 800
max_media_height = 600
font_size = 16

def save():
    global category, lang, lang_tag, first_run, initial_repeats, added_repeats, font_size
    with open("saves/settings.json", "w") as save:
        jsn = {}
        jsn["category"] = category
        jsn["lang"] = lang
        jsn["lang_tag"] = lang_tag
        jsn["first_run"] = str(first_run)
        jsn["initial_repeats"] = initial_repeats
        jsn["added_repeats"] = added_repeats
        jsn["font_size"] = font_size
        json.dump(jsn, save, indent=4)

def load():
    global category, lang, lang_tag, first_run, initial_repeats, added_repeats, font_size
    try:
        with open("saves/settings.json") as sav:
            jsn = json.load(sav)
            category = jsn["category"]
            lang = jsn["lang"]
            lang_tag = jsn["lang_tag"]
            first_run = (jsn["first_run"] == "True")
            initial_repeats = jsn["initial_repeats"]
            added_repeats = jsn["added_repeats"]
            font_size = jsn["font_size"]
    except:
        save()

def update_lang_tag(lng = lang):
    global lang_tag
    if lng == "PL" or lng == "PJM":
        lang_tag = ""
    else:
        lang_tag = " [" + lng + "]"
