from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class MyApp(App): 
    def build(self):
        self.title = "My Calculator"
        
        root_widget = BoxLayout(orientation = "vertical")

        output = Label(size_hint_y=1)
        button_symbols=('1', '2', '3', '+',
                        '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/','**', '(', ')', '=')
        
        button_grid = GridLayout(cols = 4, size_hint_y = 2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text = symbol, background_color = "blue"))

        clear_button = Button(text = 'Clear', background_color = "blue")

        #print text of buttons
        def print_text(instance):
            output.text += instance.text
        for button in button_grid.children[1:]:
            button.bind(on_press=print_text)
        
        def resize_text(label, new_height):
            label.font_size = 0.5*label.height
        output.bind(height = resize_text)

        #evaluate result
        def result(instance):
            try:
                output.text = str(eval(output.text))
            except SyntaxError:
                output.text = 'Python syntax error!'
        button_grid.children[0].bind(on_press = result)

        def clear_label(instance):
            output.text = ''
        clear_button.bind(on_press  = clear_label)

        root_widget.add_widget(output)
        root_widget.add_widget(button_grid)
        button_grid.add_widget(clear_button)

        return root_widget
    
MyApp().run()
