import PySimpleGUI as PSG
from Tree import Tree

class App:
    def __init__(self):
        default_tree = 'a&b hello x0y0z0 c0x0 abc012 34de'
        self.tree = Tree(default_tree)
        self.level = PSG.Text(font=("Times New Roman", 12), text_color='black', background_color='#ffb300')
        self.count_digits_from_left = PSG.Text(font=("Times New Roman", 12), text_color='black', background_color='#ffb300')
        self.show_hor = PSG.Text(str(self.tree), font=("Times New Roman", 12), text_color='black', background_color='#ffb300')
        self.show_vert = PSG.Text(str(self.tree.print_vert()), font=("Times New Roman", 12), text_color='black', background_color='#ffb300')
        self.layout = [
            [PSG.In(key='_ELEMENTS_', default_text=default_tree, font=("Times New Roman", 12), text_color='black'), PSG.Button(key='_CREATE_', button_text='Создать дерево', font=("Times New Roman", 12), button_color=('orange', 'brown'))],
            [PSG.Text('Кол-во цифр в левом поддереве:', font=("Times New Roman", 12), text_color='black', background_color='#ffb300'), self.count_digits_from_left],
            [PSG.In(key='_ELEMENT_'), PSG.Button(key='_LEVEL_', button_text='Найти уровень элемента', font=("Times New Roman", 12), button_color=('orange', 'brown')), PSG.Text('Элемент найден на уровне:', font=("Times New Roman", 12), text_color='black', background_color='#ffb300'), self.level],
            [PSG.Button(key='_DELETE_', button_text='Удалить дерево', font=("Times New Roman", 12), button_color=('orange', 'brown'))],
            [PSG.Text('Дерево (гор.):', font=("Times New Roman", 12), text_color='black', background_color='#ffb300'), self.show_hor],
            [PSG.Text('Дерево (верт.):', font=("Times New Roman", 12), text_color='black', background_color='#ffb300'), self.show_vert]
        ]

    def run(self):
        app = PSG.Window('Идеальное сбалансированное дерево', self.layout, background_color='#ffb300')

        while True:
            event, values = app.read()

            if event == PSG.WIN_CLOSED:
                break
            elif event == '_CREATE_':
                self.tree = Tree(values['_ELEMENTS_'])
                self.count_digits_from_left.update(str(self.tree.count_digits_from_left(values['_ELEMENTS_'])))
                self.show_hor.update(str(self.tree))
                self.show_vert.update(str(self.tree.print_vert()))
            elif self.tree is not None:
                if event == '_LEVEL_':
                    self.level.update(str(self.tree.level(values['_ELEMENT_'], values['_ELEMENTS_'])))
                if event == '_DELETE_':
                    self.tree.delete()
                    self.show_hor.update(str(self.tree))
                    self.show_vert.update(str(self.tree))

application = App()
application.run()
