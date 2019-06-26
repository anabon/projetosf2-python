import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.clock import Clock


class RootWidget(FloatLayout):

    def __init__(self,**kwargs):
        super(RootWidget,self).__init__(**kwargs)
        try:

            import mysql.connector

            conn = mysql.connector.connect(
         user='ana1',
         password='123',
         host='177.94.244.189',
         database='f2software',
         port=3306)


            cur = conn.cursor()

            query = ("SELECT nome, idade FROM pessoas LIMIT 10")

            cur.execute(query)
                        
            _str=''
            for (v1, v2) in cur:
                _str= _str + "{}, {}\n".format(v1, v2)

            cur.close()

            conn.close()
            self.ids.lbl.text= _str
             
        except Exception as e:
            self.ids.lbl.text=str(e)

            
class MysqlTest(App):
    def build(self):
       return RootWidget()


if __name__ == '__main__':
    myapp = MysqlTest()
    myapp.run()
