import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from translate import Translator
import tkinter as tk


def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def start_listening():
    global r
    global mic
    global said
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("말해보세요")
        r.adjust_for_ambient_noise(source)
        while True:
            audio = r.listen(source)
            try:
                said = r.recognize_google(audio, language="ko-KR")
                print("Your speech thinks like: ", said)
                translate(said)
            except Exception as e:
                print("Exception: " + str(e))


def translate(text):
    # 번역 부분(한글->영어로)
    translator = Translator(from_lang="ko", to_lang="en")
    translation = translator.translate(text)
    print(translation)


    # 텍스트 파일로 저장
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(text)


def exit_program():
    global mic
    mic.stop()


# UI 만들기
window = tk.Tk()
window.title("음성 인식 프로그램")

# 버튼 만들기
start_button = tk.Button(window, text="음성인식 시작", command=start_listening)
start_button.pack()

exit_button = tk.Button(window, text="종료", command=exit_program)
exit_button.pack()

window.mainloop()