import random

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

available = ["__"] * 5
result = 0


class MenuWindow(Screen):
    pass


class HelpWindow(Screen):
    pass


class ChooseWindow(Screen):
    counter = 0
    my_text = StringProperty("YOUR NUMBERS : \n __  __  __  __  __")

    def small_number(self):
        if self.counter < 5:
            nums = " "
            a = random.randint(1, 9)
            available[self.counter] = a
            self.counter += 1
            for i in range(len(available)):
                nums += str(available[i]) + "   "
            self.my_text = "YOUR NUMBERS: \n " + nums
        if self.counter >= 5:
            self.ids.small_button.disabled = True
            self.ids.big_button.disabled = True
            self.ids.start_button.disabled = False

    def big_number(self):
        if self.counter < 5:
            nums = " "
            a = random.randint(10, 99)
            available[self.counter] = a
            self.counter += 1
            for i in range(len(available)):
                nums += str(available[i]) + "   "
            self.my_text = "YOUR NUMBERS: \n " + nums

        if self.counter >= 5:
            self.ids.small_button.disabled = True
            self.ids.big_button.disabled = True
            self.ids.start_button.disabled = False

    def reset_choose(self):
        global available
        self.counter = 0
        available = ["_"] * 5
        self.my_text = "YOUR NUMBERS : \n __  __  __  __  __"
        self.ids.small_button.disabled = False
        self.ids.big_button.disabled = False
        self.ids.start_button.disabled = True


class CalculationWindow(Screen):
    calculation_text = StringProperty('')
    btn0_text = StringProperty('')
    btn1_text = StringProperty('')
    btn2_text = StringProperty('')
    btn3_text = StringProperty('')
    btn4_text = StringProperty('')

    soln = 0
    num_turn = True
    btnids = ['btn0', 'btn1', 'btn2', 'btn3', 'btn4']

    def numbers_turn(self):
        for i in self.btnids:
            if i == 'btn0':
                self.ids.btn0.disabled = True
            elif i == 'btn1':
                self.ids.btn1.disabled = True
            elif i == 'btn2':
                self.ids.btn2.disabled = True
            elif i == 'btn3':
                self.ids.btn3.disabled = True
            elif i == 'btn4':
                self.ids.btn4.disabled = True
        self.ids.add.disabled = False
        self.ids.minus.disabled = False
        self.ids.multiply.disabled = False
        self.ids.divide.disabled = False
        self.ids.equals.disabled = False
        self.ids.submit.disabled = False

        self.num_turn = False

    def number_not_turn(self):
        for i in self.btnids:
            if i == 'btn0':
                self.ids.btn0.disabled = False
            elif i == 'btn1':
                self.ids.btn1.disabled = False
            elif i == 'btn2':
                self.ids.btn2.disabled = False
            elif i == 'btn3':
                self.ids.btn3.disabled = False
            elif i == 'btn4':
                self.ids.btn4.disabled = False

        self.ids.add.disabled = True
        self.ids.minus.disabled = True
        self.ids.multiply.disabled = True
        self.ids.divide.disabled = True
        self.ids.equals.disabled = True
        self.ids.submit.disabled = True

        self.num_turn = True

    def button_press(self, btn):
        self.calculation_text = self.calculation_text + btn.text

        if len(self.btnids) == 0:
            self.ids.add.disabled = True
            self.ids.minus.disabled = True
            self.ids.multiply.disabled = True
            self.ids.divide.disabled = True
            self.ids.equals.disabled = False
            self.ids.submit.disabled = False

        if self.num_turn and btn.text != ")" and btn.text != "(":
            self.numbers_turn()

        elif not self.num_turn  and btn.text != ")" and btn.text != "(":
            self.number_not_turn()

    def calculate(self):
        try:
            self.soln = round(eval(self.calculation_text), 2)
            self.calculation_text = str(self.soln)
        except ValueError:
            self.reset_calculation()

    def reset_goal(self):
        self.goal = random.randint(100, 999)

    def submit_calculation(self):
        global result
        try:
            self.soln = eval(self.calculation_text)
            result = self.goal - self.soln
        except ValueError:
            self.reset_calculation()

    def button_disable(self, btn):
        if btn.btn_id == 'btn0':
            self.ids.btn0.disabled = True
            self.btnids.remove('btn0')
        elif btn.btn_id == 'btn1':
            self.ids.btn1.disabled = True
            self.btnids.remove('btn1')
        elif btn.btn_id == 'btn2':
            self.ids.btn2.disabled = True
            self.btnids.remove('btn2')
        elif btn.btn_id == 'btn3':
            self.ids.btn3.disabled = True
            self.btnids.remove('btn3')
        elif btn.btn_id == 'btn4':
            self.ids.btn4.disabled = True
            self.btnids.remove('btn4')

        if len(self.btnids) == 0:
            self.ids.add.disabled = True
            self.ids.minus.disabled = True
            self.ids.multiply.disabled = True
            self.ids.divide.disabled = True
            self.ids.equals.disabled = False
            self.ids.submit.disabled = False

    def reset_calculation(self):
        self.calculation_text = ''
        self.ids.goal.text = "GOAL : " + str(self.goal)
        self.num_turn = True
        self.btnids = ['btn0', 'btn1', 'btn2', 'btn3', 'btn4']

        self.btn0_text = str(available[0])
        self.btn1_text = str(available[1])
        self.btn2_text = str(available[2])
        self.btn3_text = str(available[3])
        self.btn4_text = str(available[4])

        self.ids.btn0.disabled = False
        self.ids.btn1.disabled = False
        self.ids.btn2.disabled = False
        self.ids.btn3.disabled = False
        self.ids.btn4.disabled = False

        self.ids.open.disabled = False
        self.ids.close.disabled = False
        self.ids.add.disabled = True
        self.ids.minus.disabled = True
        self.ids.multiply.disabled = True
        self.ids.divide.disabled = True
        self.ids.equals.disabled = True
        self.ids.submit.disabled = True


class ResultWindow(Screen):
    result_label = StringProperty("You were 7 Off!!")

    def update_result(self):
        self.result_label = "You were " + str(result) + " Off!!"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('TheClosest.kv')


class TheClosestApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    TheClosestApp().run()
