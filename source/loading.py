import pandas as pd
import traceback
import settings
from strings import strings

def save_exists():
    try:
        save = pd.read_csv(settings.save_path)
    except pd.errors.EmptyDataError, FileNotFoundError: 
        return False
    except Exception:
        print(traceback.format_exc())
        print(strings[settings.lang]["save error"])
    if len(save) == 0:
        return False
    return True

def load_save(force_new=False):
    save = pd.DataFrame({"Lp": []})
    questions = filter_out(settings.category)
    diff_quest = pd.DataFrame({"Lp": []})
    try:
        save = pd.read_csv(settings.save_path)
    except pd.errors.EmptyDataError, FileNotFoundError:
        save = new_save(questions)
    except Exception:
        print(traceback.format_exc())
        print(strings[settings.lang]["save error"])
    try:
        diff_quest = pd.read_csv(settings.diff_path)
    except pd.errors.EmptyDataError, FileNotFoundError:
        diff_quest.to_csv(settings.diff_path, index=False)
    if len(save) == 0 or force_new:
        save = new_save(questions)
    if force_new:
        diff_quest = pd.DataFrame({"Lp": []})
    return questions, save, diff_quest

def new_save(questions):
    save = pd.DataFrame({"Lp": []})
    save["Lp"] = questions.loc[:, "Lp"]
    save["Repeats"] = settings.initial_repeats
    save.to_csv(settings.save_path, index=False)
    return save

# creates new save from the list of the difficult questions (the ones where user made any errors when answering)
def new_from_diff(diff_quest):
    save = pd.DataFrame({"Lp": []})
    save["Lp"] = diff_quest.loc[:, "Lp"]
    save["Repeats"] = settings.initial_repeats
    save.to_csv(settings.save_path, index=False)
    return save

# returns only the questions matching selected driving license category
def filter_out(category: str):
    try:
        data = pd.read_excel("pytania/baza_pytan.xlsx")
        counts = data.count()
        questions_nr = counts["Pytanie"]
        idxs = []
        for i in range(0, questions_nr):
            categories = data.loc[i, "Kategorie"]
            if category in categories.split(","):
                idxs.append(i)
        filtered = data.loc[idxs]
        return filtered
    except Exception:
        print(traceback.format_exc())
        print(strings[settings.lang]["questions error"])