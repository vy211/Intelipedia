import speech_recognition as sr
def rec():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Somthing:')
        audio=r.listen(source)
        print('time over')
    try:
        txt=r.recognize_google(audio)
        return txt

    except:
        pass
#rec()
