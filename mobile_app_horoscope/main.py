from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder


data = 'Овен – человек-огонь. Он постоянно находится в действии и стремится к своим целям с завидным упорством ' \
       'и энтузиазмом. При этом склонен не замечать желаний и мнений окружающих, действуя только в своих интересах'
data2 = 'У Тельца огромный запас внутренней силы. Она проявляется в повышенной работоспособности, терпеливости и ' \
        'независимости представителей этого знака зодиака. Телец солидно выглядит, у него крепкое телосложение и ' \
        'отменное здоровье'
data3 = 'Близнецы – люди действия. Их натуре свойственно постоянное движение вперед, генерация новых идей и ' \
        'воплощение их в жизнь. Они способны заниматься несколькими делами одновременно и не терпят однообразия.'
data4 = 'Луна, которая управляет Раком, наделяет его чувствительностью и мягкостью. Это дает ему хорошее понимание ' \
        'людей и тонкую душевную организацию. При этом он не остается уязвимым.'
data5 = 'Лев – яркая личность. Ему свойственна большая жизненная сила, оптимизм и величественность в словах и делах.' \
        ' Этому знаку зодиака многое по плечу. Он часто добивается высокого положения в обществе' \
        ' и руководящих должностей'
data6 = 'Дева рассудительна, экономна. Доводит дела до логического завершения. Стремится держать свою жизнь в ' \
        'идеальном порядке. Часто придирается к мелочам и тратит много времени на самоанализ и контроль ситуации.'
data7 = 'Весы – символ уравновешенности и движения к совершенству. Это превосходные стратеги и прекрасные работники.' \
        ' Предпочитают обдумывать каждый шаг, поэтому зачастую действуют медленно и осторожно.'
data8 = 'Скорпион – человек с железной волей. Он умеет ставить перед собой цели и достигает их, несмотря на любые ' \
        'препятствия. Это прямолинейная личность. Он всегда говорит то, что думает.'
data9 = 'Стрелец – мыслитель и деятель в одном лице. Он находится в постоянном движении, много общается, интересуется' \
        ' окружающим миром. Из-за нелюбви к ограничениям и свободолюбия часто выступает против «системы».'
data10 = 'Козерог умеет добиваться своего. Он прокладывает себе дорогу в жизни медленно, но верно. Умеет обходить' \
         ' препятствия и достигает цели быстрее тех, кто «идет напролом».' \
         ' Его отличает сдержанность, серьезность и мягкость.'
data11 = 'Водолей – реалист, который старается изменить мир к лучшему. Поскольку им управляют сразу две планеты,' \
         ' его характер является неоднозначным. Любимые занятия представителя этого знака ' \
         'зодиака – получение новых знаний и путешествия.'
data12 = 'Рыбы – знатоки человеческих душ. Они хорошо понимают людей, выслушивают их невзгоды и с радостью помогают' \
         ' советом. Представители этого знака зодиака не переносят одиночества и стараются как можно больше времени' \
         ' проводить в компании близких и родных'


class HoroscopeApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = None

    def zodiac_1(self, instance):
        self.data = instance.text
        self.lbl.text = str(data)

    def zodiac_2(self, instance):
        self.data = instance.text
        self.lbl.text = str(data2)

    def zodiac_3(self, instance):
        self.data = instance.text
        self.lbl.text = str(data3)

    def zodiac_4(self, instance):
        self.data = instance.text
        self.lbl.text = str(data4)

    def zodiac_5(self, instance):
        self.data = instance.text
        self.lbl.text = str(data5)

    def zodiac_6(self, instance):
        self.data = instance.text
        self.lbl.text = str(data6)

    def zodiac_7(self, instance):
        self.data = instance.text
        self.lbl.text = str(data)

    def zodiac_8(self, instance):
        self.data = instance.text
        self.lbl.text = str(data8)

    def zodiac_9(self, instance):
        self.data = instance.text
        self.lbl.text = str(data9)

    def zodiac_10(self, instance):
        self.data = instance.text
        self.lbl.text = str(data10)

    def zodiac_11(self, instance):
        self.data = instance.text
        self.lbl.text = str(data11)

    def zodiac_12(self, instance):
        self.data = instance.text
        self.lbl.text = str(data12)

    def build(self):
        self.data = ""
        bl = BoxLayout(orientation='vertical', padding=[10])
        gl = GridLayout(cols=3, padding=[2], spacing=1.2)

        self.lbl = Label(text="",
                         font_size=16,
                         text_size=(300, None),
                         )
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='Овен', background_normal='icon/oven.png', font_size=20, color='yellow',
                             on_press=self.zodiac_1))
        gl.add_widget(Button(text='Телец', background_normal='icon/telets.png', font_size=20, color='yellow',
                             on_press=self.zodiac_2))
        gl.add_widget(Button(text='Близнецы', background_normal='icon/bliznetsy.png', font_size=20, color='yellow',
                             on_press=self.zodiac_3))

        gl.add_widget(Button(text='Рак', background_normal='icon/rak.png', font_size=20, color='yellow',
                             on_press=self.zodiac_4))
        gl.add_widget(Button(text='Лев', background_normal='icon/lev.png', font_size=20, color='yellow',
                             on_press=self.zodiac_5))
        gl.add_widget(Button(text='Дева', background_normal='icon/deva.png', font_size=20, color='yellow',
                             on_press=self.zodiac_6))

        gl.add_widget(Button(text='Весы', background_normal='icon/vesy.png', font_size=20, color='yellow',
                             on_press=self.zodiac_7))
        gl.add_widget(Button(text='Скорпион', background_normal='icon/skorpion.png', font_size=20, color='yellow',
                             on_press=self.zodiac_8))
        gl.add_widget(Button(text='Стрелец', background_normal='icon/strelets.png', font_size=20, color='yellow',
                             on_press=self.zodiac_9))

        gl.add_widget(Button(text='Козерог', background_normal='icon/kozerog.png', font_size=20, color='yellow',
                             on_press=self.zodiac_10))
        gl.add_widget(Button(text='Водолей', background_normal='icon/vodolei.png', font_size=20, color='yellow',
                             on_press=self.zodiac_11))
        gl.add_widget(Button(text='Рыбы', background_normal='icon/ryby.png', font_size=20, color='yellow',
                             on_press=self.zodiac_12))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    HoroscopeApp().run()






