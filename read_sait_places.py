from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from calcul import Calculator
from calendatura import CalendarWindow
from table_results import Window7, Window8, Window9, Window10, Window11
from table_results import Window12, Window13, Window14, Window15, Window16
from table_results import Window17, Window18, Window1, Window2, Window3
from table_results import Window4, Window5, Window6

SCREEN_SIZE = [1920, 1080]
font = QFont("Times New Roman", 24)
font1 = QFont("Times New Roman", 12)

# Создаются классы с текстом, картинками и кнопками, отличается только текст!
# Всё остальное однотипно


class BeachMin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Грузия(Тбилиси)")
        self.table.setGeometry(150, 0, 300, 50)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(550, 10, 100, 30)
        self.button1.clicked.connect(self.open_window1)

        self.table_text = QLabel(self)
        self.table_text.setFont(font1)
        self.table_text.setWordWrap(True)
        self.table_text.setText("- Билеты в одну сторону для взрослого "
                                "обойдутся приблизительно от 8350 рублей, "
                                "смотря в какой месяц.\n"
                                "- Детям от 2 до 11 лет предоставляется "
                                "скидка 30‑50% от стоимости взрослого "
                                "билета. \n"
                                "- Дети, которым меньше двух лет могут "
                                "летать по России это бесплатно, а за "
                                "границу — со скидкой 90%.")
        self.table_text.setGeometry(420, 30, 400, 150)
        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("- Хороший отель 'Pushkin 10', за одного "
                                 "взрослого 1062 рубля(за сутки).\n"
                                 "- Если вы путешествуете с домашним животным,"
                                 " то этот отель вам подойдёт 'Agora' "
                                 "примерно за 2000 рублей(за сутки).\n"
                                 "- Так же там есть замечательные рестораны, "
                                 "где можно отведать много блюд по недорогой "
                                 "цене.")
        self.table_text1.setGeometry(520, 150, 400, 200)

        self.pixmap = QPixmap('image_jpg/Gruzia.jpg')
        self.image = QLabel(self)
        self.image.setGeometry(1, 50, 400, 300)
        self.image.setPixmap(self.pixmap)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Черногория(Бечичи)")
        self.table2.setGeometry(150, 390, 350, 50)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window2)

        self.pixmap1 = QPixmap('image_jpg/Behihi.jpg')
        self.image1 = QLabel(self)
        self.image1.setGeometry(500, 460, 550, 200)
        self.image1.setPixmap(self.pixmap1)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("- Билеты в одну сторону для взрослого "
                                 "обойдутся приблизительно от 5000 рублей, "
                                 "смотря в какой месяц.\n"
                                 "- Детям от 2 до 11 лет предоставляется "
                                 "скидка 30‑50% от стоимости взрослого "
                                 "билета. \n"
                                 "- Дети, которым меньше двух лет могут "
                                 "летать по России это бесплатно, а за "
                                 "границу — со скидкой 90%.")
        self.table_text2.setGeometry(10, 400, 400, 200)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("- Хороший отель 'Apartments Ivanovic', "
                                 "за двоих оплата 3100 рублей(за сутки).\n"
                                 "Так же этот отель позволяет взять "
                                 "с собой домашнее животноею")
        self.table_text3.setGeometry(70, 500, 400, 200)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window1(self):
        self.window1 = Window1()
        self.window1.show()

    def open_window2(self):
        self.window2 = Window2()
        self.window2.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class BeachAvg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Тайланд(Джомтьен)")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap2 = QPixmap('image_jpg/Dzhomten.jpg')
        self.image2 = QLabel(self)
        self.image2.setGeometry(1, 50, 400, 300)
        self.image2.setPixmap(self.pixmap2)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window3)

        self.table_text = QLabel(self)
        self.table_text.setFont(font1)
        self.table_text.setWordWrap(True)
        self.table_text.setText("-Билет на самолёт для одного от 35000 рублей."
                                "\n"
                                "- Детям от 2 до 11 лет предоставляется "
                                "скидка 30‑50% от стоимости взрослого "
                                "билета. \n"
                                "- Дети, которым меньше двух лет могут "
                                "летать по России это бесплатно, а за "
                                "границу — со скидкой 90%.")
        self.table_text.setGeometry(430, 30, 400, 150)
        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("- Хороший отель рядом с море "
                                 "'Jomtien Palm Beach Hotel & Resort', "
                                 "за двоих около 6000 рублей.\n"
                                 "- На соседнем пляже, есть отель, "
                                 "который разрешает иметь с собой домашнего "
                                 "питомца 'Rabbit Resort',"
                                 " за двоих около 11000 рублей")
        self.table_text1.setGeometry(420, 150, 400, 200)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Египет(Макади Бей)")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap3 = QPixmap('image_jpg/MakadiBeyjpg.jpg')
        self.image3 = QLabel(self)
        self.image3.setGeometry(500, 470, 400, 200)
        self.image3.setPixmap(self.pixmap3)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window4)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("- Билет на одного стоит 37 503 рублей.\n"
                                 "- Детям от 2 до 11 лет предоставляется "
                                 "скидка 30‑50% от стоимости взрослого "
                                 "билета. \n"
                                 "- Дети, которым меньше двух лет могут "
                                 "летать по России это бесплатно, а за "
                                 "границу — со скидкой 90%.")
        self.table_text2.setGeometry(10, 400, 400, 200)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("- Хороший отель рядом с пляжем "
                                 "'Old Palace Resort Sahl Hasheesh' за двоих"
                                 " оплата от 13000 рублей.")
        self.table_text3.setGeometry(70, 500, 400, 200)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window3(self):
        self.window3 = Window3()
        self.window3.show()

    def open_window4(self):
        self.window4 = Window4()
        self.window4.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class BeachMax(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) США(Гавайи)")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap4 = QPixmap('image_jpg/Gavayi.jpg')
        self.image4 = QLabel(self)
        self.image4.setGeometry(1, 60, 400, 300)
        self.image4.setPixmap(self.pixmap4)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window5)

        self.table_text = QLabel(self)
        self.table_text.setFont(font1)
        self.table_text.setWordWrap(True)
        self.table_text.setText("-Билет на самолёт для одного за 48 дней "
                                "до вылета , примерно 52 205 рублей . "
                                "Максимальная цена по направлению из Москвы в "
                                "Гонолулу — за 24 дня до вылета , "
                                "примерно 842 930 рублей."
                                "\n"
                                "- Детям от 2 до 11 лет предоставляется "
                                "скидка 30‑50% от стоимости взрослого "
                                "билета. \n"
                                "- Дети, которым меньше двух лет могут "
                                "летать по России это бесплатно, а за "
                                "границу — со скидкой 90%.")
        self.table_text.setGeometry(430, 30, 400, 200)
        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("- Хороший отель рядом с море 'Four Seasons'"
                                 ", за двоих оплата около 108000 рублей, так "
                                 "же этот отель разрешает брать с "
                                 "собой домашних животных.")
        self.table_text1.setGeometry(430, 150, 400, 200)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Дубай(Jumeirah Beach)")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap5 = QPixmap('image_jpg/JumeiraHBeach.jpg')
        self.image5 = QLabel(self)
        self.image5.setGeometry(500, 440, 450, 250)
        self.image5.setPixmap(self.pixmap5)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window6)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText(
            "- Билет на одного стоит от 35000 рублей рублей.\n"
            "- Детям от 2 до 11 лет предоставляется "
            "скидка 30‑50% от стоимости взрослого "
            "билета. \n"
            "- Дети, которым меньше двух лет могут "
            "летать по России это бесплатно, а за "
            "границу — со скидкой 90%.")
        self.table_text2.setGeometry(10, 400, 400, 200)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("- Хороший отель рядом с пляжем 'Mandarin "
                                 "Oriental Jumeira, Dubai', за двоих "
                                 "примерно 136000 рубелй .")
        self.table_text3.setGeometry(70, 500, 400, 200)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window5(self):
        self.window5 = Window5()
        self.window5.show()

    def open_window6(self):
        self.window6 = Window6()
        self.window6.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class FishingMin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Рыбалка у Иваныча")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap6 = QPixmap('image_jpg/FISHinIvan.jpg')
        self.image6 = QLabel(self)
        self.image6.setGeometry(440, 70, 300, 300)
        self.image6.setPixmap(self.pixmap6)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window7)

        self.table_text = QLabel(self)
        self.table_text.setFont(font1)
        self.table_text.setWordWrap(True)
        self.table_text.setText("Там всё предусмотренно, и предлагаются Домики"
                                " с кухней и комфортной спальней.\n"
                                "Стоимость аренды: Будни - 5000 ₽/сутки \n"
                                "Выходные/праздники - 6000 ₽/сутки")
        self.table_text.setGeometry(100, 40, 400, 100)
        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("Весенне-летний период\n"
                                 "- Пойманная рыба оплачивается по "
                                 "прейскуранту "
                                 "- по окончании рыбалки, улов взвешивается \n"
                                 "- В будние дни женщины и дети до 10 лет "
                                 "присутствуют по путевке рыбака, "
                                 "в выходные и праздничные дни - вход 500₽\n "
                                 "- Количество снастей на путевку - 2 шт.")
        self.table_text1.setGeometry(20, 120, 400, 200)

        self.table_text4 = QLabel(self)
        self.table_text4.setFont(font1)
        self.table_text4.setWordWrap(True)
        self.table_text4.setText("Осенне-зимний период(безлимит)\n"
                                 "- Дневная рыбалка с 7:00 до 19:00 - "
                                 "стоимость путевки 3500₽ с человека "
                                 "(можно рыбачить на две снасти)."
                                 "Дополнительная снасть 500₽. Запуск 4кг. "
                                 "форели на путевку ежедневно в 9:00 \n"
                                 "- Женщины и дети до 10 лет могут рыбачить "
                                 "на "
                                 "снасти рыбака бесплатно.\n - Живая форель"
                                 "из садка 900₽/кг")
        self.table_text4.setGeometry(720, 20, 400, 200)
        self.table_text5 = QLabel(self)
        self.table_text5.setFont(font1)
        self.table_text5.setWordWrap(True)
        self.table_text5.setText("Дополнительные услуги\n"
                                 "- Аренда подсачника - 100\n"
                                 "- Копчение рыбы - 300₽/шт.\n"
                                 "- Аренда садка - 100₽\n"
                                 "- Аренда снастей - 500₽\n"
                                 "- Чистка рыбы - 150₽./шт\n."
                                 "- Удочка для зимней ловли - 200₽\n"
                                 "- Аренда бура - 300₽\n"
                                 "- Аренда жерлиц, 1шт. - 200₽\n")
        self.table_text5.setGeometry(720, 220, 400, 200)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Рыбалка у Бородина")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap7 = QPixmap('image_jpg/FishinBorodino.jpg')
        self.image7 = QLabel(self)
        self.image7.setGeometry(580, 430, 520, 300)
        self.image7.setPixmap(self.pixmap7)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(550, 400, 100, 30)
        self.button2.clicked.connect(self.open_window8)

        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("1) 3 000 руб. С 5-00 до 20-00."
                                 "(Залог 500 руб обязательно). \n "
                                 "2) 1 500 руб. Действует С 12-00 до 20-00. "
                                 "(Залог 500 руб обязательно).\n 3) 500 руб. "
                                 "За 1 час рыбалки - действует с 12-00. \n"
                                 "На почасовой тариф перед рыбалкой вносится "
                                 "залог 2000 руб. Обязательно. "
                                 "Все тарифы без нормы вылова рыбы. Допустимо "
                                 "ТРИ ЛЮБЫХ СНАСТИ! Любые льготы на "
                                 "скидку отсутствуют. Кроме наших, "
                                 "раннее выданных или купленных скидочных "
                                 "карт, при предъявлении карты. "
                                 "Дополнительные снасти 500 руб за "
                                 "одну или 700 руб за 2 штуки допов.\n"
                                 "АРЕНДА ИНВЕНТАРЯ ! \n"
                                 "Удочка, спиннинг или донка - 500 "
                                 "руб. Садок - 200 руб. "
                                 "Подсак - 500 руб. Мангал - 500 руб. "
                                 "Сетка для барбекю - 500 руб. "
                                 "Шампур 1 шт - 50 руб.")
        self.table_text3.setGeometry(70, 350, 500, 400)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window7(self):
        self.window7 = Window7()
        self.window7.show()

    def open_window8(self):
        self.window8 = Window8()
        self.window8.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class FishingAvg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Золотые караси")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap8 = QPixmap('image_jpg/ZOLOTKARASI.jpg')
        self.image8 = QLabel(self)
        self.image8.setGeometry(10, 40, 740, 200)
        self.image8.setPixmap(self.pixmap8)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window9)

        self.table_text = QLabel(self)
        self.table_text.setFont(font1)
        self.table_text.setWordWrap(True)
        self.table_text.setText(
            "Рыболовная усадьба содержит множество удобст, "
            "котеджи, бани, рестораны, беседки и тд.\n"
            "Подробнее вы можете ознакомиться "
            "на их официальном сайте")
        self.table_text.setGeometry(300, 230, 400, 100)
        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("Высокая плотность зарыбления\n"
                                 "в Пн, Вт, Ср, Чт, Пт - Стоимость : "
                                 "3000 рублей\n"
                                 "в Сб, Вс и праздничные дни - "
                                 "Стоимость: 3000 рублей")
        self.table_text1.setGeometry(50, 250, 400, 200)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Sorola Village")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap9 = QPixmap('image_jpg/SOROLA.jpg')
        self.image9 = QLabel(self)
        self.image9.setGeometry(450, 450, 400, 200)
        self.image9.setPixmap(self.pixmap9)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window10)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("Стоимость аренды коттеджа на базе "
                                 "отдыха Ладожского озера «Sorola Village» "
                                 "начитается от 7000 рублей в сутки.\n "
                                 "Летом актуальна цена проката моторной "
                                 "лодки – за 12 часов 4 тыс. рублей, "
                                 "катера – 10 тыс. рублей за 2 часа. \n"
                                 "Прокат весельной лодки стоит всего 800 "
                                 "рублей. \n Цены на прокат плавательных "
                                 "средств"
                                 " зависят от мощности, размера и степени "
                                 "комфортабельности.\n"
                                 "Аренда удочки на 12 часов - 100 рублей.\n"
                                 "Аренда снегохода на час от 2500 рублей.")
        self.table_text2.setGeometry(10, 450, 400, 200)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window9(self):
        self.window9 = Window9()
        self.window9.show()

    def open_window10(self):
        self.window10 = Window10()
        self.window10.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class FishingMax(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Белый карп")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap10 = QPixmap('image_jpg/WhiteKarp.jpg')
        self.image10 = QLabel(self)
        self.image10.setGeometry(260, 190, 740, 200)
        self.image10.setPixmap(self.pixmap10)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window11)

        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("Основная зона( Щука,карп, "
                                 "Белый амур, окунь,Сом) "
                                 "Стоимость путевки на каждого мужчину "
                                 "Пн.-Чт. — 2000 руб./Пт.-Вс.-2500 руб. "
                                 "Норма вылова не превышает сумму — 2000 руб. "
                                 "Каждый вид рыбы считается отдельно, "
                                 "согласно прейскуранту "
                                 "Количество снастей — 3 шт. Доп снасть "
                                 "500 руб. "
                                 "Женщины и (дети до 14 лет) В сопровождении "
                                 "мужчин, принимают участие в ловли бесплатно"
                                 "!\n"
                                 "Стоимость выловленный рыбы\n "
                                 "Амур - 450 руб/кг \n"
                                 "Карп - 400 руб/кг \n"
                                 "Сом - 600 руб/кг \n"
                                 "Щука - 700 руб/кг")
        self.table_text1.setGeometry(30, 20, 400, 300)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Ихтиолог")
        self.table2.setGeometry(150, 390, 170, 50)

        self.pixmap11 = QPixmap('image_jpg/IXTIO.jpg')
        self.image11 = QLabel(self)
        self.image11.setGeometry(480, 440, 500, 250)
        self.image11.setPixmap(self.pixmap11)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window12)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("с 08:00 до 17:00 за 4000 рублей можно "
                                 "порыбачить")
        self.table_text2.setGeometry(10, 450, 320, 100)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("В данном клубе имеются котеджи"
                                 "(47 000 руб - будни, воскресенье. "
                                 "56 000 руб - пятница, суббота,) "
                                 "и рестораны, подробнее можете почитать "
                                 "на их официальном сайте ")
        self.table_text3.setGeometry(70, 500, 400, 100)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window11(self):
        self.window11 = Window11()
        self.window11.show()

    def open_window12(self):
        self.window12 = Window12()
        self.window12.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class SkiingMin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Нечкино")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap12 = QPixmap('image_jpg/Nechkino.jpg')
        self.image12 = QLabel(self)
        self.image12.setGeometry(650, 40, 400, 300)
        self.image12.setPixmap(self.pixmap12)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window13)

        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("разовый подъем (будни/выходные) — 150/200 "
                                 "рублей;\n"
                                 "1 час (только в будни) — 500 рублей; \n"
                                 "3 часа (только в выходные) — 1700 рублей;\n "
                                 "дневной тариф — 1500/2400 рублей; \n"
                                 "вечерний тариф (пн-чт 19:00-22:00) — 800 "
                                 "рублей за 3 часа; \n"
                                 "ночной тариф (пт/сб 21:00-00:00) — 800/1200 "
                                 "рублей за 3 часа.")
        self.table_text1.setGeometry(30, 20, 400, 300)

        self.table_text5 = QLabel(self)
        self.table_text5.setFont(font1)
        self.table_text5.setWordWrap(True)
        self.table_text5.setText("Рядом расположен неплохой отель "
                                 "'Отель Волна', стоимость от 4000 рублей")
        self.table_text5.setGeometry(120, 10, 400, 100)

        self.table_text4 = QLabel(self)
        self.table_text4.setFont(font1)
        self.table_text4.setWordWrap(True)
        self.table_text4.setText(
            "Также действуют совместные тарифы на прокат "
            "оборудования и ски-пасс: \n"
            "- «Часовой» (будни/выходняе) — 500/800 рублей "
            "(взрослый) и 400/650 рублей (детский); \n"
            "- «Оптимальный» (3 часа только в выходные) — "
            "2200 рублей и 1750 рублей;\n"
            "- «День» (будни/выходные) — 1500/3000 рублей "
            "(взрослый) и 1200/2400 рублей.")
        self.table_text4.setGeometry(250, 170, 400, 300)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Красная глинка")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap13 = QPixmap('image_jpg/Krasnaya-Glinka.jpg')
        self.image13 = QLabel(self)
        self.image13.setGeometry(700, 380, 400, 300)
        self.image13.setPixmap(self.pixmap13)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window14)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("По сменам: день с 09:00 до 17:00 "
                                 "(1500 рублей); вечер с 17:00 до 22:00 "
                                 "(1000 рублей); понедельник с 15:00 до 22:00 "
                                 "(1000 рублей); выходной день с 09:00 до "
                                 "20:00 (2600 рублей); два выходных дня "
                                 "(4000 рублей). \n"
                                 "По часам: 1 час — 400/700 рублей "
                                 "(будние/выходные и праздники); 2 часа — "
                                 "700/1100 рублей; 3 часа — 900/1500 рублей; "
                                 "3 часа детский (5–12 лет) — 500/700 рублей\n"
                                 "По подъемам: 1 подъем — 200 рублей; "
                                 "5 подъемов — 800 рублей; 10 подъемов — "
                                 "1300 рублей.\n"
                                 "Абонемент на неделю обойдется в 8000 "
                                 "рублей, на месяц — 20000 рублей.")
        self.table_text2.setGeometry(10, 350, 400, 400)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("Рядом расположен неплохой отель "
                                 "'Отель Ангел', стоимость от 4900 рублей")
        self.table_text3.setGeometry(410, 540, 300, 100)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window13(self):
        self.window13 = Window13()
        self.window13.show()

    def open_window14(self):
        self.window14 = Window14()
        self.window14.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class SkiingAvg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Бакуриани")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap14 = QPixmap('image_jpg/bakuriani.jpg')
        self.image14 = QLabel(self)
        self.image14.setGeometry(420, 40, 400, 200)
        self.image14.setPixmap(self.pixmap14)

        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("Ски-пасс, он же лифт-пасс, "
                                 "(на обывательском языке означает абонемент, "
                                 "позволяющий лыжникам пользоваться "
                                 "подъёмниками) обойдётся в 343 рубля  "
                                 " за разовый подъём\n"
                                 "три подъема — 860 рублей в любой день.")
        self.table_text1.setGeometry(30, 0, 400, 200)

        self.table_text5 = QLabel(self)
        self.table_text5.setFont(font1)
        self.table_text5.setWordWrap(True)
        self.table_text5.setText("Однодневный ски-пасс обойдется в 1891 рубля "
                                 "для взрослых и 962 рубля для детей "
                                 "(6-12 лет).\n"
                                 " Ски-пасс на 6 дней — 8699 и 4366 рублей "
                                 "соответственно.\n"
                                 "Вечерний абонемент, с 17.00 до 21.30, "
                                 "составляет 1031 рубля для взрослых, "
                                 "687 рублей для детей.")
        self.table_text5.setGeometry(30, 65, 400, 300)

        self.table_text4 = QLabel(self)
        self.table_text4.setFont(font1)
        self.table_text4.setWordWrap(True)
        self.table_text4.setText("Что касается аренды лыж, то на Дидвели "
                                 "за один час пользования спортинвентарём "
                                 "придётся заплатить 343 рубля, порядка "
                                 "515–687 "
                                 "рублей за день.\nсноуборд — 1031 рубелй "
                                 "в день. \n"
                                 "Если вы решите воспользоваться услугами "
                                 "инструктора, будьте готовы отдать ещё "
                                 "1031–1719 рублей за обучение.")
        self.table_text4.setGeometry(30, 190, 400, 300)

        self.table_text6 = QLabel(self)
        self.table_text6.setFont(font1)
        self.table_text6.setWordWrap(True)
        self.table_text6.setText(
            "Довольно близко находится превосходный отель "
            "'Villa Mtashi Bakuriani' за 11800 рублей")
        self.table_text6.setGeometry(400, 120, 400, 300)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window15)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Хацвали")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap15 = QPixmap('image_jpg/XACVALI.jpg')
        self.image15 = QLabel(self)
        self.image15.setGeometry(420, 430, 550, 250)
        self.image15.setPixmap(self.pixmap15)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(500, 400, 100, 30)
        self.button2.clicked.connect(self.open_window16)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("Стоимость ski-pass составляет "
                                 "примерно 687 рублей "
                                 "Если покупать абонемент на несколько "
                                 "дней, то курорт любезно предоставит скидку\n"
                                 "Стоимость обучения катанию у "
                                 "инструктора – 687 рублей за час. "
                                 "Цена за 1 день – 1719 рублей.\n"
                                 "Аренда лыж и сноубордов — 859 рубелй на"
                                 " 1 день.")
        self.table_text2.setGeometry(10, 300, 400, 400)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("Рядом расположен хороший отель 'Suntower' "
                                 "за 4700 рублей")
        self.table_text3.setGeometry(10, 400, 500, 400)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window15(self):
        self.window15 = Window15()
        self.window15.show()

    def open_window16(self):
        self.window16 = Window16()
        self.window16.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()


class SkiingMax(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setWindowTitle('Информация о курорте')

        self.table = QLabel(self)
        self.table.setFont(font)
        self.table.setText("1) Клостер")
        self.table.setGeometry(150, 0, 350, 50)

        self.pixmap16 = QPixmap('image_jpg/Kloster.jpg')
        self.image16 = QLabel(self)
        self.image16.setGeometry(490, 0, 500, 490)
        self.image16.setPixmap(self.pixmap16)

        self.table_text1 = QLabel(self)
        self.table_text1.setFont(font1)
        self.table_text1.setWordWrap(True)
        self.table_text1.setText("Рядом расположен замечательный отель "
                                 "'Hotel Vereina' за 49600 рублей")
        self.table_text1.setGeometry(30, 50, 400, 150)

        self.table_text5 = QLabel(self)
        self.table_text5.setFont(font1)
        self.table_text5.setWordWrap(True)
        self.table_text5.setText("Клостерс считается курортом-спутником "
                                 "Давоса, есть смысл приобретать ски-пасс "
                                 "на объединённую зону катания. А это 307 "
                                 "км разноуровневых трасс, 55 подъёмников, "
                                 "обслуживающих 6 зон катания: Мадриса"
                                 ", Парсенн, Якобсхорн"
                                 ", Пиша и Ринехорн"
                                 ". Стоимость ски-пасса при "
                                 "этом увеличивается не слишком сильно: "
                                 "взрослые за день платят 70 CHF, подростки "
                                 "— 49 CHF, дети — 28 CHF.")
        self.table_text5.setGeometry(70, 100, 400, 300)

        self.button1 = QPushButton('Выбрать', self)
        self.button1.setGeometry(480, 10, 100, 30)
        self.button1.clicked.connect(self.open_window17)

        self.table2 = QLabel(self)
        self.table2.setFont(font)
        self.table2.setText("2) Куршеваль")
        self.table2.setGeometry(150, 390, 350, 50)

        self.pixmap17 = QPixmap('image_jpg/courchevel.jpg')
        self.image17 = QLabel(self)
        self.image17.setGeometry(520, 430, 500, 250)
        self.image17.setPixmap(self.pixmap17)

        self.table_text2 = QLabel(self)
        self.table_text2.setFont(font1)
        self.table_text2.setWordWrap(True)
        self.table_text2.setText("Для взрослых – 629/547 евро, для "
                                 "детей - 503,20/437,60 евро."
                                 "Дети до 5 лет катаются бесплатно "
                                 "(необходим документ, подтверждающий "
                                 "возраст ребенка)."
                                 "При покупке скипасса на семью "
                                 "(2 взрослых+ 2 детей) через Интернет"
                                 ", предоставляются скидки "
                                 "до 20%."
                                 "Стоимость 2 взрослых и 2 детских "
                                 "скипассов на 6 дней – 864 евро")
        self.table_text2.setGeometry(10, 300, 400, 400)
        self.table_text3 = QLabel(self)
        self.table_text3.setFont(font1)
        self.table_text3.setWordWrap(True)
        self.table_text3.setText("Рядом расположен отель 'Les Suites de "
                                 "la Potinière', классический номер за "
                                 "86000 рублей")
        self.table_text3.setGeometry(10, 400, 500, 400)

        self.calculator = QPushButton('Открыть Калькулятор', self)
        self.calculator.setGeometry(1150, 300, 200, 100)
        self.calculator.clicked.connect(self.calculatre)
        self.calculator.setFont(font1)

        self.button2 = QPushButton('Выбрать', self)
        self.button2.setGeometry(390, 400, 100, 30)
        self.button2.clicked.connect(self.open_window18)

        self.calenda = QPushButton("Открыть Календарь", self)
        self.calenda.setGeometry(1150, 400, 200, 100)
        self.calenda.clicked.connect(self.calendare)
        self.calenda.setFont(font1)

    def calendare(self):
        self.cal = CalendarWindow()
        self.cal.show()

    def open_window17(self):
        self.window17 = Window17()
        self.window17.show()

    def open_window18(self):
        self.window18 = Window18()
        self.window18.show()

    def calculatre(self):
        self.calc = Calculator()
        self.calc.show()
