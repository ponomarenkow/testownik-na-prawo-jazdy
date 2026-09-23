from PySide6.QtWidgets import QMainWindow, QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QPushButton, QWidget, QScrollArea, QFrame, QLineEdit
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget   
from PySide6.QtCore import Slot, QUrl, Qt
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor, QMovie
import pandas as pd
from random import randint
import re
import settings
from strings import get_string
from loading import load_save, save_exists, filter_out, new_from_diff

class QuestionPage(QMainWindow):

    def __init__(self, parent=None):
        super(QuestionPage, self).__init__(parent)
        self.setWindowTitle(get_string("title"))
        self.resize(settings.max_width, 800)

        settings.load()
        new_save = not save_exists()

        self.questions, self.save, self.diff_quest = load_save()
        self.initial_number = len(self.questions)

        self.settings = SettingsScreen(parent=self)

        if new_save:
            settings.first_run = True
            self.settings.show()

        self.init_question_screen()


        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0, 0))
        self.widget.setPalette(palette)
        self.widget.setAutoFillBackground(True)
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.widget)
        self.scroll.setWidgetResizable(True)
        self.setCentralWidget(self.scroll)


    def init_question_screen(self):

        self.question = QLabel(get_string("loading"), wordWrap=True)
        font = self.question.font()
        font.setPointSize(settings.font_size)
        self.question.setFont(font)
        self.question_nr = QLabel(get_string("question nr") + "-")
        self.question_nr.setFont(font)
        self.range = QLabel(get_string("range") + "-")
        self.range.setFont(font)
        self.points = QLabel(get_string("points") + "-")
        self.points.setFont(font)
        self.repeats = QLabel(get_string("repeats") + "-")
        self.repeats.setFont(font)
        self.learned = QLabel(get_string("learned") + str(self.initial_number - len(self.save)) + "/" + str(self.initial_number))
        self.learned.setFont(font)

        self.media = QLabel("")
        self.media.setMaximumHeight(settings.max_media_height)

        self.video_container = QVBoxLayout()
        self.video = QVideoWidget()
        self.video.setFixedSize(settings.media_width, int((settings.media_width * 9) /16))
        self.play_widget = QWidget()
        self.play_button = QPushButton(get_string("video"))
        self.play_button.setFont(font)
        self.play_button.clicked.connect(self.play_video)
        self.play_layout = QHBoxLayout()
        self.play_layout.addStretch(1)
        self.play_layout.addWidget(self.play_button)
        self.play_layout.addStretch(1)
        self.play_widget.setLayout(self.play_layout)
        self.video_container.addWidget(self.video)

        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video)
        self.media_player.positionChanged.connect(self.position_changed)

        self.yes_button = QPushButton(get_string("yes"))
        self.yes_button.setFont(font)
        self.yes_button.clicked.connect(self.check_t)

        self.no_button = QPushButton(get_string("no"))
        self.no_button.setFont(QFont(font))
        self.no_button.clicked.connect(self.check_n)

        self.a_button = QPushButton("A")
        self.a_button.setFont(QFont(font))
        self.a_button.clicked.connect(self.check_a)
        
        self.b_button = QPushButton("B")
        self.b_button.setFont(QFont(font))
        self.b_button.clicked.connect(self.check_b)
        
        self.c_button = QPushButton("C")
        self.c_button.setFont(QFont(font))
        self.c_button.clicked.connect(self.check_c)

        self.next_button = QPushButton(get_string("next"))
        self.next_button.setFont(QFont(font))
        self.next_button.clicked.connect(self.show_question)

        self.next = QWidget()
        self.next_layout = QHBoxLayout()
        self.next_layout.addStretch(1)
        self.next_layout.addWidget(self.next_button)
        self.next_layout.addStretch(1)
        self.next.setLayout(self.next_layout)

        self.restart_button = QPushButton(get_string("restart"))
        self.restart_button.setFont(QFont(font))
        self.restart_button.clicked.connect(self.restart)

        self.restart_widget = QWidget()
        self.restart_layout = QHBoxLayout()
        self.restart_layout.addStretch(1)
        self.restart_layout.addWidget(self.restart_button)
        self.restart_layout.addStretch(1)
        self.restart_widget.setLayout(self.restart_layout)

        self.settings_button = QPushButton(get_string("settings"))
        self.settings_button.setFont(QFont(font))
        self.settings_button.clicked.connect(self.settings.show)
        
        self.settings_layout = QHBoxLayout()
        self.settings_layout.addWidget(self.settings_button)
        self.settings_layout.addStretch(1)

        self.buttons = {
            "A": self.a_button,
            "B": self.b_button,
            "C": self.c_button,
            "T": self.yes_button,
            "N": self.no_button
        }

        self.question_layout = QVBoxLayout()
        self.question_layout.setAlignment(Qt.AlignTop)
        self.question_layout.addWidget(self.question)
        self.question_layout.addWidget(self.media)
        self.question_layout.addLayout(self.video_container)
        self.question_layout.setContentsMargins(20, 0, 20, 0)
        self.question_widget = QWidget()
        self.question_widget.setMaximumWidth(settings.max_width)
        self.question_widget.setLayout(self.question_layout)

        self.info_layout = QVBoxLayout()
        self.info_layout.setAlignment(Qt.AlignTop)
        self.info_layout.addWidget(self.question_nr)
        self.info_layout.addWidget(self.range)
        self.info_layout.addWidget(self.points)
        self.info_layout.addWidget(self.repeats)
        self.info_layout.addWidget(self.learned)
        self.info_layout.addStretch(1)
        self.info_layout.addLayout(self.settings_layout)
        self.info_layout.setContentsMargins(20, 0, 20, 0)

        self.separator = QFrame()
        self.separator.setFrameStyle(QFrame.VLine | QFrame.Plain)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.question_widget)
        self.layout.addWidget(self.separator)
        self.layout.addLayout(self.info_layout)


        self.yesno = QWidget()
        self.ynlayout = QHBoxLayout()
        self.ynlayout.addStretch(1)
        self.ynlayout.addWidget(self.yes_button)
        self.ynlayout.addWidget(self.no_button)
        self.ynlayout.addStretch(1)
        self.yesno.setLayout(self.ynlayout)

        self.answer_a = QLabel("A. ", wordWrap=True)
        self.answer_a.setFont(font)
        self.answer_b = QLabel("B. ", wordWrap=True)
        self.answer_b.setFont(font)
        self.answer_c = QLabel("C. ", wordWrap=True)
        self.answer_c.setFont(font)

        self.abc_buttons = QHBoxLayout()
        self.abc_buttons.addStretch(1)
        self.abc_buttons.addWidget(self.a_button)
        self.abc_buttons.addWidget(self.b_button)
        self.abc_buttons.addWidget(self.c_button)
        self.abc_buttons.addStretch(1)

        self.abc_answers = QVBoxLayout()
        self.abc_answers.addWidget(self.answer_a)
        self.abc_answers.addWidget(self.answer_b)
        self.abc_answers.addWidget(self.answer_c)

        self.abc = QWidget()
        self.abc_layout = QVBoxLayout()
        self.abc_layout.addLayout(self.abc_answers)
        self.abc_layout.addLayout(self.abc_buttons)
        self.abc.setLayout(self.abc_layout)


    def update_language(self):
        self.setWindowTitle(get_string("title"))
        self.play_button.setText(get_string("video"))
        self.yes_button.setText(get_string("yes"))
        self.no_button.setText(get_string("no"))
        self.next_button.setText(get_string("next"))
        self.settings_button.setText(get_string("settings"))
        self.set_question()
        self.update_learned()
        if not pd.isnull(self.current_question["Odpowiedź A"]):
            self.answer_a.setText("A. " + self.current_question["Odpowiedź A" + settings.lang_tag])
            self.answer_b.setText("B. " + self.current_question["Odpowiedź B" + settings.lang_tag])
            self.answer_c.setText("C. " + self.current_question["Odpowiedź C" + settings.lang_tag])


    def set_question(self):
        self.question_nr.setText(get_string("question nr") + str(int(self.current_question["Numer pytania"])))
        try:
            rang = str(self.current_question["Zakres struktury"]).lower()
            if rang == "specajlistyczny":
                rang = "specjalistyczny"
            self.range.setText(get_string("range") + get_string(rang))
        except:
            self.range.setText(get_string("range") + str(self.current_question["Zakres struktury"]).lower())
        self.points.setText(get_string("points") + str(int(self.current_question["Liczba punktów"])))
        self.repeats.setText(get_string("repeats") + str(self.chosen["Repeats"]))
        self.question.setText(self.current_question["Pytanie" + settings.lang_tag])


    def update_font(self):
        font = self.question.font()
        font.setPointSize(settings.font_size)
        self.question.setFont(font)
        self.play_button.setFont(font)
        self.yes_button.setFont(font)
        self.no_button.setFont(font)
        self.next_button.setFont(font)
        self.restart_button.setFont(font)
        self.settings_button.setFont(font)
        self.learned.setFont(font)
        self.question_nr.setFont(font)
        self.range.setFont(font)
        self.points.setFont(font)
        self.repeats.setFont(font)
        self.a_button.setFont(font)
        self.b_button.setFont(font)
        self.c_button.setFont(font)
        self.answer_a.setFont(font)
        self.answer_b.setFont(font)
        self.answer_c.setFont(font)


    @Slot()
    def show_question(self):

        self.answerable = True
        self.question_layout.removeWidget(self.next)
        self.next.setParent(None)

        for key, button in self.buttons.items():
            button.setStyleSheet('')

        if len(self.save) == 0:
            self.question.setText(get_string("end"))
            self.question_layout.removeWidget(self.abc)
            self.abc.setParent(None)
            self.question_layout.removeWidget(self.yesno)
            self.yesno.setParent(None)
            self.question_layout.removeWidget(self.next)
            self.next.setParent(None)
            self.media_player.stop()
            self.video.hide()
            self.video_container.removeWidget(self.play_widget)  
            self.play_widget.setParent(None)
            self.movie = QMovie("source/finished.gif")
            self.media.setMovie(self.movie)
            self.movie.start()
            settings.first_run = True
            settings.save()
            if len(self.diff_quest) > 0:
                self.question_layout.addWidget(self.restart_widget)
            return
        
        self.current = randint(0, len(self.save) - 1)
        self.save.iloc[self.current, self.save.columns.get_loc("Repeats")] -= 1
        self.chosen = self.save.iloc[self.current]
        self.current_question = self.questions.loc[self.questions["Lp"] == self.chosen["Lp"]]
        self.current_question = self.current_question.iloc[0]
        self.correct = self.current_question["Poprawna odp"]

        self.set_question()

        if pd.isnull(self.current_question["Odpowiedź A"]):
            self.question_layout.removeWidget(self.abc)
            self.abc.setParent(None)
            self.question_layout.addWidget(self.yesno)
        else:
            self.question_layout.removeWidget(self.yesno)
            self.yesno.setParent(None)
            self.answer_a.setText("A. " + self.current_question["Odpowiedź A" + settings.lang_tag])
            self.answer_b.setText("B. " + self.current_question["Odpowiedź B" + settings.lang_tag])
            self.answer_c.setText("C. " + self.current_question["Odpowiedź C" + settings.lang_tag])
            self.question_layout.addWidget(self.abc)

        if not pd.isnull(self.current_question["Media"]):
            try:
                if ".jpg" in self.current_question["Media"]:
                    self.video.hide()
                    self.video_container.removeWidget(self.play_widget)
                    self.play_widget.setParent(None)
                    self.play_widget.hide()  
                    pixmap = QPixmap("multimedia/do_pytan/" + self.current_question["Media"])
                    if pixmap.width() > pixmap.height() + 10:
                        pixmap = pixmap.scaledToWidth(settings.media_width)
                    else:
                        pixmap = pixmap.scaledToHeight(settings.max_media_height)
                    self.media.setPixmap(pixmap)
                else:
                    self.media.clear()
                    self.media_player.setSource(QUrl.fromLocalFile("multimedia/do_pytan/"  + self.current_question["Media"]))   
                    self.video.resize(settings.media_width, int((settings.media_width * 9) /16)) 
                    self.video.show()  
                    self.video_container.addWidget(self.play_widget) 
                    self.play_widget.show()
                    self.media_player.play()
                    self.media_player.pause() 
            except:
                self.media.setText(get_string("media error"))
        else:
            self.media.clear()
            self.media_player.stop()
            self.video.hide()
            self.video_container.removeWidget(self.play_widget)  
            self.play_widget.setParent(None)

    def update_learned(self):
        self.learned.setText(get_string("learned") + str(self.initial_number - len(self.save)) + "/" + str(self.initial_number))

    @Slot()
    def restart(self):
        self.save = new_from_diff(self.diff_quest)
        self.question_layout.removeWidget(self.restart_widget)
        self.restart_widget.setParent(None)
        self.diff_quest = pd.DataFrame({"Lp": []})
        self.diff_quest.to_csv(settings.diff_path, index=False)
        self.initial_number = len(self.save)
        self.update_learned()
        self.show_question()


    @Slot()
    def play_video(self):
        self.media_player.play()


    @Slot(int)
    def position_changed(self, position):
        if self.media_player.duration() > 0 and position >= self.media_player.duration() - 1000:
            self.media_player.pause()



    @Slot()
    def check(self, answer):

        if not self.answerable:
            return

        if answer == self.correct:
            if self.save.iloc[self.current, self.save.columns.get_loc("Repeats")] == 0:
                self.save.drop(self.save.index[self.current], inplace=True)
                self.update_learned()
        else:
            self.save.iloc[self.current, self.save.columns.get_loc("Repeats")] += settings.added_repeats
            self.buttons[answer].setStyleSheet('QPushButton {background-color: red;}')
            self.repeats.setText(get_string("repeats") + str(self.save.iloc[self.current, self.save.columns.get_loc("Repeats")]))
            self.diff_quest.loc[len(self.diff_quest)] = self.chosen["Lp"]
            self.diff_quest.to_csv(settings.diff_path, index=False)
        
        self.buttons[self.correct].setStyleSheet('QPushButton {background-color: green;}')
        self.question_layout.addWidget(self.next)
        self.answerable = False
        self.save.to_csv(settings.save_path, index=False)

    @Slot()
    def check_a(self):
        self.check("A")

    @Slot()
    def check_b(self):
        self.check("B")

    @Slot()
    def check_c(self):
        self.check("C")

    @Slot()
    def check_t(self):
        self.check("T")
        
    @Slot()
    def check_n(self):
        self.check("N")





class SettingsScreen(QDialog):
    
    def __init__(self, parent):
        super(SettingsScreen, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle(get_string("settings"))
        self.layout = QFormLayout()

        self.category_input = QLineEdit(settings.category)
        if not settings.first_run:
            self.category_input.setReadOnly(True)
        self.cat_error = QLabel(get_string("category error"), wordWrap=True)
        red_font = self.cat_error.palette()
        red_font.setColor(self.cat_error.foregroundRole(), Qt.red)
        self.cat_error.setPalette(red_font)

        self.lang_input = QLineEdit(settings.lang)
        self.lang_error = QLabel(get_string("lang error") + self.detect_translations() + ".", wordWrap=True)
        # red_font = self.lang_error.palette()
        # red_font.setColor(self.lang_error.foregroundRole(), Qt.red)
        self.lang_error.setPalette(red_font)

        self.init_input = QLineEdit(str(settings.initial_repeats))
        self.init_error = QLabel(get_string("numeric error"))
        self.init_error.setPalette(red_font)

        self.added_input = QLineEdit(str(settings.added_repeats))
        self.added_error = QLabel(get_string("numeric error"))
        self.added_error.setPalette(red_font)

        self.font_input = QLineEdit(str(settings.font_size))
        self.font_error = QLabel(get_string("numeric error"))
        self.font_error.setPalette(red_font)

        self.save = QHBoxLayout()
        self.save_button = QPushButton(get_string("save"))
        self.save_button.clicked.connect(self.save_settings)
        self.save.addStretch(1)
        self.save.addWidget(self.save_button)
        self.save.addStretch(1)

        # font = self.save_button.font()
        # font.setPointSize(settings.font_size)
        # self.save_button.setFont(font)

        self.layout.addRow(get_string("category"), self.category_input)
        self.layout.addRow(get_string("lang"), self.lang_input)
        self.layout.addRow(get_string("initial repeats"), self.init_input)
        self.layout.addRow(get_string("added repeats"), self.added_input)
        self.layout.addRow(get_string("font"), self.font_input)
        self.layout.addRow(self.save)
        self.setLayout(self.layout)


    def detect_translations(self):
        langs = "PL"
        for column in self.parent.questions:
            if "Pytanie [" in column:
                langs += ", "
                tag = re.search('''\[.+\]''', column).group()
                langs += tag.lstrip("[").rstrip("]")
        return langs


    def save_settings(self):

        self.layout.takeRow(self.cat_error)
        self.cat_error.setParent(None)
        self.layout.takeRow(self.lang_error)
        self.lang_error.setParent(None)
        self.layout.takeRow(self.init_error)
        self.init_error.setParent(None)
        self.layout.takeRow(self.added_error)
        self.added_error.setParent(None)
        self.layout.takeRow(self.font_error)
        self.font_error.setParent(None)

        validated = True
        added_rows = 0

        test_questions = filter_out(self.category_input.text())
        if len(test_questions) == 0:
            self.layout.insertRow(1 + added_rows, self.cat_error)
            added_rows += 1
            validated = False

        if self.lang_input.text() not in ["PL", "PJM"]:
            try:
                first = self.parent.questions.iloc[0]
                test = first["Pytanie [" + self.lang_input.text() + "]"]
            except:
                self.layout.insertRow(2 + added_rows, self.lang_error)
                validated = False

        if not self.init_input.text().isdecimal() or int(self.init_input.text()) == 0:
            self.layout.insertRow(3 + added_rows, self.init_error)
            added_rows += 1
            validated = False

        if not self.added_input.text().isdecimal() or int(self.added_input.text()) == 0:
            self.layout.insertRow(4 + added_rows, self.added_error)
            added_rows += 1
            validated = False

        if not self.font_input.text().isdecimal() or int(self.font_input.text()) == 0:
            self.layout.insertRow(5 + added_rows, self.font_error)
            added_rows += 1
            validated = False

        if not validated:
            return
        
        settings.first_run = False
        if settings.lang != self.lang_input.text():
            settings.lang = self.lang_input.text()
            test = get_string("yes")
            if test == "":
                settings.lang = "EN"
            settings.update_lang_tag(self.lang_input.text())
            self.parent.update_language()
        if settings.category != self.category_input.text():
            settings.category = self.category_input.text()
            self.parent.questions, self.parent.save, self.parent.diff_quest = load_save(force_new=True)
            self.parent.initial_number = len(self.parent.questions)
            self.parent.update_learned()
            self.parent.show_question()
        settings.initial_repeats = int(self.init_input.text())
        settings.added_repeats = int(self.added_input.text())
        if settings.font_size != int(self.font_input.text()):
            settings.font_size = int(self.font_input.text())
            self.parent.update_font()
        settings.save()
        self.hide()