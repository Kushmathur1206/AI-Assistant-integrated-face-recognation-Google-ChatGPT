import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import AppOpener
import datetime
from bs4 import BeautifulSoup
import requests
import image
import qrcode
import openai
from config import apikey
import fr

x = fr.fc()
Name = x


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
def qr(text):
    qr = qrcode.QRCode(version=15,box_size=10,border=5)
    data = text
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill='black',back_color='white')
    image.save('QR.png')

headers = {'Enter your User-Agent'}

def weather(city):
    c1 = city
    city = city+" weather"
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}'f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='f'chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather1 = soup.select('#wob_tm')[0].getText().strip()
    say(f"The weather in {c1} is {weather1} °C and {info}")
def say(text):
    engine = pyttsx3.init()
    engine.say({text})
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return f"Some error occured. Sorry {Name}"

if __name__ == '__main__':
    print('PyCharm')
    say(f"Hello {Name}, I am Jarvis A-I")
    try:
        while True:
            print("listening")
            query = takeCommand()
            if query.lower() == "stop listening":
                say(f"Ok {Name}")
                break
            query1 = query.split(" ")

            if ("Open".lower() == query1[0].lower()) & ("website" == query1[1].lower()):
                site = query.split(" ", 2)[2].replace(" ","")

                webbrowser.open("https://"+site+".com")
                say(f"Opening {site} Sir")

            elif (("launch" == query1[0].lower())|("open" == query1[0].lower())):
                AppOpener.open(f"{query1[1]}")

            elif('the time' in query.lower()):
                strftime = datetime.datetime.now().strftime("%H %M"+" and "+"%S"+"seconds")
                say(f"Sir the time is {strftime}")

            elif('the date' in query.lower()):
                strfdate = datetime.datetime.now().strftime("%d  %m  %y")
                strfday = datetime.datetime.today().strftime("%A")
                say(f"Sir today is {strfday}, {strfdate}")

            elif('weather in' in query.lower()):
                i = query1.index('weather')+2
                weather(query1[i])

            elif('generate qr' in query.lower()):
                i = query1.index('saying')+1
                query2 = query.split(" ",i+1)
                qr(query2[i])
                say("Your QR Code is ready")

            elif ('google' == query1[0].lower()):
                s = query.split(" ",1)[1]
                s2 = f"https://www.google.com/search?q={s}"
                webbrowser.open(f"{s2}")

            elif "Using AI".lower() in query.lower():
                ai(query)




    except Exception as e:
        say(f"Some error occured. Sorry {Name}")
