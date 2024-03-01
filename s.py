# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import ST7735 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import unicodedata
from unidecode import unidecode
import pygame


def unicode_to_english(unicode_text):
    try:
        # Use unidecode to convert Unicode to ASCII representation
        english_text = unidecode(unicode_text)
        return english_text

    except Exception as e:
        print(f"Error converting Unicode to English: {e}")
        return None


def normalize_text(input_text, normalization_form='NFC'):
    normalized_text = unicodedata.normalize(normalization_form, input_text)
    return normalized_text


def func(st, st1, st2, st3):

    WIDTH = 128
    HEIGHT = 160
    SPEED_HZ = 16000000

    MESSAGE = st

    # Raspberry Pi configuration.
    DC = 24
    RST = 25
    SPI_PORT = 0
    SPI_DEVICE = 0

# BeagleBone Black configuration.
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Create TFT LCD display class.
    disp = TFT.ST7735(
        DC,
        rst=RST,
        spi=SPI.SpiDev(
            SPI_PORT,
            SPI_DEVICE,
            max_speed_hz=SPEED_HZ))

# Initialize display.
    disp.begin()

    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(
        "/home/barath/Desktop/arial-unicode-ms.ttf", 20)

    size_x, size_y = draw.textsize(st, font)

    text_x = 100
    text_y = (60 - size_y) // 2
    text_y2 = text_y + size_y + 5
    text_y3 = text_y2 + size_y + 5
    text_y4 = text_y3 + size_y + 5

    t_start = time.time()
    i = 0
    # Define the total time
    total_time = 5  # seconds

    # Get start time
    start = time.time()

    while True:
        x = (time.time() - t_start) * 100
        x %= (size_x + 160)
        draw.rectangle((0, 0, 128, 160), (128, 128, 128))
        draw.text((int(text_x - x), text_y), st,
                  font=font, fill=(255, 255, 255))

        draw.text((int(text_x - x), text_y2), st1,
                  font=font, fill=(255, 255, 255))
        draw.text((int(text_x - x), text_y3), st2,
                  font=font, fill=(255, 255, 255))

        draw.text((int(text_x - x), text_y4), st3,
                  font=font, fill=(255, 255, 255))
        disp.display(img)
        i += 1

        # Check if time exceeded
        current = time.time()
        elapsed = current - start
        if elapsed >= total_time:
            break


# A tuple containing all the language and codes of the language
dic = ('afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu', 'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')

# Capture Voice


def speak(text):
    # Detect language of the provided text
    translator = Translator()
    detected_lang = translator.detect(text)
    lang_code = detected_lang.lang  # Get the detected language code

    # Using Google-Text-to-Speech (gTTS) to create speech
    speech = gTTS(text=text, lang=lang_code, slow=False)

    # Save the speech as a temporary audio file
    speech.save("temp_audio.mp3")

    # Play the speech using the playsound module
    playsound("temp_audio.mp3")

    # Remove the temporary audio file
    os.remove("temp_audio.mp3")

    return lang_code


def take_command():
    # import pyttsx3
    # engine = pyttsx3.init()
    # engine.setProperty('rate', 150)
    # engine.setProperty('volume', 0.5)
    # engine.setProperty('voice', 'english+f4')
    # engine.say("Hello")
    # engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("/home/barath/Desktop/beep.mp3")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        # func("RECOGNIZING")
        query = r.recognize_google(audio)
        speak("The user said")
        l = speak(query)
        # func("The User said: ")
        # func(query)
    except Exception as e:
        speak("Say that again, please...")
        return "None", "None"
    return query, l


def get_language_choice(message):
    speak(message)
    time.sleep(1)
    language_choice, _ = take_command()
    while language_choice == "None":
        language_choice, _ = take_command()
    language_choice = language_choice.lower()

    return language_choice


speak("speak")
time.sleep(1)
query, inp_lancode = take_command()
print(inp_lancode)
while query == "None":
    query, inp_lancode = take_command()

print(inp_lancode)
# Input from user for destination language
to_lang = get_language_choice(
    "Please specify the destination language you want to translate to:")

while to_lang not in dic:
    speak("Language in which you are trying to convert is currently not available, please specify another language.")
    to_lang = get_language_choice(
        "Please specify the destination language you want to translate to:")

# Map the destination language to the corresponding language code
to_lang_code = dic[dic.index(to_lang) + 1]

# Invoking Translator
translator = Translator()
text1 = translator.translate(
    query, dest=inp_lancode)

# Translating from src to dest
text_to_translate = translator.translate(
    query, dest=to_lang_code)

text = text_to_translate.text

speak(text)
print(query)
print(text1.text)
print(text_to_translate.pronunciation)
print(text)
if text_to_translate.pronunciation == None:
    func(query, text1.text, text, " ")
else:
    s = unicode_to_english(text_to_translate.pronunciation)
    func(query, text1.text, s, text)

# here i want to ask the user if they want to listen again if yes code should play audio again else say thank you


def ask_to_replay():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("/home/barath/Desktop/beep.mp3")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        if query.lower() == "yes" or query.lower() =='s':
            return True
        else:
            return False
    except:
        speak("Sorry, I didn't get that. Please say yes or no.")
        return ask_to_replay()


while True:
    speak("Do you want to listen again?")
    time.sleep(1)

    if ask_to_replay():
        if text_to_translate.pronunciation == None:
            func(query, text1.text, text, " ")
        else:
            s = unicode_to_english(text_to_translate.pronunciation)
            func(query, text1.text, s, text)
        speak(text)
    else:
        speak("Thank you, have a nice day!")
        break
