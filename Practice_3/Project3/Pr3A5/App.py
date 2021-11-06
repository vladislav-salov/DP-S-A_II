import PySimpleGUI as PSG
from Tree import Tree

class App:
    def __init__(self):
        default_tree = '12.12 0.987 24.01 -3.14 -99.99 0.5 13.21'
        self.tree = Tree(default_tree)
        self.calculate_average_left = PSG.Text(font=("Times New Roman", 12), text_color='white', background_color='#000030')
        self.calculate_average_right = PSG.Text(font=("Times New Roman", 12), text_color='white', background_color='#000030')
        self.show_hor = PSG.Text(str(self.tree), font=("Times New Roman", 12), text_color='white', background_color='#000030')
        self.layout = [
            [PSG.In(key='_ELEMENTS_', default_text=default_tree, font=("Times New Roman", 12), text_color='black'), PSG.Button(key='_CREATE_', button_text='Создать дерево', font=("Times New Roman", 12), button_color=('white', 'darkblue'))],
            [PSG.Text('Среднее арифметическое левого поддерева:', font=("Times New Roman", 12), text_color='white', background_color='#000030'), self.calculate_average_left],
            [PSG.Text('Среднее арифметическое правого поддерева:', font=("Times New Roman", 12), text_color='white', background_color='#000030'), self.calculate_average_right],
            [PSG.Button(key='_DELETE_', button_text='Удалить дерево', font=("Times New Roman", 12), button_color=('white', 'darkblue'))],
            [PSG.Text('Дерево (повёрнутое справа налево):', font=("Times New Roman", 12), text_color='white', background_color='#000030'), self.show_hor],
        ]

    def run(self):
        app = PSG.Window('Идеальное сбалансированное дерево', self.layout, background_color='#000030')
        while True:
            event, values = app.read()

            if event == PSG.WIN_CLOSED:
                break
            elif event == '_CREATE_':
                self.tree = Tree(values['_ELEMENTS_'])
                self.show_hor.update(str(self.tree))
                self.calculate_average_left.update(str(self.tree.calculate_average(values['_ELEMENTS_'])[0]))
                self.calculate_average_right.update(str(self.tree.calculate_average(values['_ELEMENTS_'])[1]))
            elif self.tree is not None:
                if event == '_DELETE_':
                    self.tree.delete()
                    self.show_hor.update(str(self.tree))
                    self.calculate_average_left.update('')
                    self.calculate_average_right.update('')

application = App()
application.run()
