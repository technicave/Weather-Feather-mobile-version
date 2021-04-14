import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
import requests, json



class MyApp(MDApp):
    def build(self):
        return Builder.load_file("my.kv")

    def find(self):
        api_key = "4f8046e62675c481877f2a005634ca86"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        # city_name = self.root.ids.location.text
        complete_url = base_url + "appid=" + api_key + "&q=" + self.root.ids.location.text   

        try:
            respons = requests.get(complete_url)
            x = respons.json()
      
            
            if x["cod"] != "404" : 
                y = x["main"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                self.root.ids.weathers.text = weather_description

            else:
                self.root.ids.weathers.text = "City Not Found"

        except:
            self.root.ids.weathers.text = "Check Internet!"
      

    
    def clear(self):
        self.root.ids.location.text = ""
        self.root.ids.weathers.text = "Enter City name"


if __name__ == "__main__":
    MyApp().run()
