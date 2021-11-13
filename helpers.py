name = """
MDTextField:
    hint_text: "Name of web or application"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "application"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.67}
    size_hint_x:None
    width:250
"""

username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "account-outline"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.53}
    size_hint_x:None
    width:250
"""

password_input = """
MDTextField:
    hint_text: "PassWord"
    helper_text: "Enter PassWord"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.39}
    size_hint_x:None
    width:250
    password: True
    multiline: False
"""

