from kivymd.app import MDApp
from kivymd.uix.screen import Screen,MDScreen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton ,MDRoundFlatButton,MDFillRoundFlatButton,MDTextButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
import json
import helpers
import generate
import pyperclip



"""This program is account and password management software in python language combined with kivy """
"xu li viet hoa cua ng dung : unfulfilled"

class VPassWord(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Purple"
        screen = Screen()
        wimg = Image(source = 'icons8-password-window-100.png',
                    pos_hint ={'center_x': 0.5, 'center_y': 0.85},
                     )
        self.name_web = Builder.load_string(helpers.name)
        self.username = Builder.load_string(helpers.username_input)
        self.password = Builder.load_string(helpers.password_input)

        #ADD Button
        button_add = MDFillRoundFlatButton(text='ADD',
                                       pos_hint={'center_x': 0.3, 'center_y': 0.28},
                                       on_release = self.save_pass
                                       )
        #Search Button
        button_sreach = MDFillRoundFlatButton(text='Search',
                                       pos_hint={'center_x': 0.7, 'center_y': 0.28},
                                       on_release=self.search_pass
                                              )
        #CREAT Password Button
        button_creat = MDFillRoundFlatButton(text='Creat',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.2},
                                       on_release = self.generate,
                                       theme_text_color=  "Secondary"
                                              )
        help_button = MDTextButton(text ='Help?',
                                   pos_hint={'center_x': 0.8, 'center_y': 0.05},
                                   on_release = self.help_fun)
        screen.add_widget(wimg)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(self.name_web)

        # screen.add_widget(button_show)

        screen.add_widget(button_add)
        screen.add_widget(button_sreach)
        screen.add_widget(button_creat)
        screen.add_widget(help_button)
        return screen

    #function that save pass word
    def save_pass_wordisTrue(self,obj):
        """if save pass return is Ok"""
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        self.close_dialog(obj)



    def save_pass(self,obj):
        """Get info and confirm info with user ."""
        web_name = self.name_web.text
        name = self.username.text
        pass_ = self.password.text
        global new_data
        new_data= {
            web_name:
                {
                    "Account": name,
                    "pass": pass_
                }

        }

        #if wb box and username box empty
        if len(web_name) == 0 or len(pass_) == 0:
            self.dialog = MDDialog(
                title = "ERROR",
                text = "Please dont leave any fields empty!",
                size_hint=(0.8, 1),
                buttons = [MDFlatButton(text='Close', on_release=self.close_dialog)]
            )
            self.dialog.open()
        else:
            #confirm ifo
            self.dialog = MDDialog(
                title = "Confirm",
                size_hint=(0.8, 1),
                text = f"There are the details enterd :\nEmail:{name}\n"
                        f"PassWord: {pass_} ",
                buttons = [MDFlatButton(text='No', on_release=self.close_dialog),
                           MDFlatButton(text='Yes', on_release=self.save_pass_wordisTrue)
                           ]
            )
            self.dialog.open()


    #Fuction that user can find password of account
    def search_pass(self,obj):
        """Search pass when uesrs enter web name"""
        web = self.name_web.text
        acc = self.username.text
        if web ==  "":
            self.dialog = MDDialog(
                title = "Error",
                text = "Pls Enter User Name!",
                size_hint=(0.8, 1),
                buttons = [MDFlatButton(text='Close', on_release=self.close_dialog)
                       ]
            )
            self.dialog.open()
        else:
            try:
                with open(file="data.json") as data_file:
                    data = json.load(data_file)
                    pass_w = data[web]["pass"]
            except KeyError:
                self.dialog = MDDialog(
                    title="Error",
                    text="Cant find this user . Once more time enter the username or web name",
                    size_hint=(0.8, 1),
                    buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)
                             ]
                )
                self.dialog.open()
            else:
                with open(file="data.json") as data_file:
                    data = json.load(data_file)
                    pass_w = data[web]["pass"]
                    self.dialog = MDDialog(
                        title = web + " of pass is ",
                        text = pass_w,
                        size_hint=(0.8, 1),
                        buttons = [MDFlatButton(text='Close', on_release=self.close_dialog)

                               ]
                    )
                    pyperclip.copy(pass_w)

                self.dialog.open()


    #Random pass word
    def generate(self,obj):
        """Ramdom passWord with sysbomls , alp , numbers"""
        web =  self.name_web.text
        name = self.username.text
        pass_word = generate.generate_password()
        n_data= {
            web:
                {
                    "Account": name,
                    "pass": pass_word
                }

        }
        if len(web) == 0 or len(name) == 0:
            self.dialog = MDDialog(
                title = "ERROR",
                text =  "Please fill in the information of the website and user name ",
                size_hint = (0.8,1 ),
                buttons = [MDFlatButton(text='Close', on_release=self.close_dialog)]

            )
            self.dialog.open()
        else:
            try:
                with open(file = "data.json", mode = "r") as data_file :
                    data = json.load(data_file)
            except :
                with open(file = "data.json", mode = "w") as data_file :
                    json.dump(n_data, data_file, indent=4)

            else:
                data.update(n_data)
                with open(file="data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            self.dialog = MDDialog(title='Notification',
                                   text=f"you have successfully generated password with {name} user . "
                                        f"If you want to see show pass . Please click close and press find " ,
                                   size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
                                            )
            self.dialog.open()

    #close function
    def help_fun(self,obj):
        self.dialog = MDDialog(title = 'Help',
                               text = "*My app helps you manage your accounts and passwords. And it can help you create strong passwords that prevent hacking.\n"
                                        "\n*First of all, if you want to save the password of an account, please enter the account application name and password then press the ADD button.\n"
                                        "\n*If you want to find the password that you have saved, just enter the website name and press find\n"
                                        "\n*If you want to create a strong password, enter your account name and application name then Create. the app will automatically save for you\n"
                                        "\n*Finally, if you have any questions, please contact: nguyenhuuvu286@gmail.com ",
                               size_hint = (0.8, 1),
                               buttons = [MDFlatButton(text='Close', on_release=self.close_dialog)]
        )

        self.dialog.open()



    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog




VPassWord().run()


