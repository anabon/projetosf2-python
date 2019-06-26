# textInput.kv
<MainScreen>
    orientation: 'vertical'

    # Third section title
    Label:
        size_hint: (1, .1)
        text: 'Setup Connection'
        font_size: 25

    # Third section Box
    BoxLayout:
        size_hint: (1, .2)
        padding: [100, 0, 100, 0]
        BoxLayout:
            Label:
                size_hint: (.2, 1)
                text: 'Host'
            TextInput:
                height: self.minimum_height
                multiline: False
                text: 'localhost'
            Label:
                size_hint: (.2, 1)
                text: ''
            Label:
                size_hint: (.2, 1)
                text: 'Port'
            TextInput:
                size_hint: (.2, 1)
                multiline: False
                text: '502'
