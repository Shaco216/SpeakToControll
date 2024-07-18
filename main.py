import speech_recognition as sr
import pyaudio
import enum

#https://www.youtube.com/watch?v=eykWtp-Bt8A

class Language(enum):
    german = "de-DE",
    english = "en-EN"

class SpeechToText():
    def print_mic_device_index(self):
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print("{1}, device_index{0}".format(index,name))

    def speech_to_text(self, device_index,language=Language.english):
        r = sr.Recognizer()
        with sr.Microphone(device_index=device_index) as source:
            print("Start Talking:")
            audio = r.listen(source)
            try:
                text = r.record(audio, language=language.value)
                print("You said: {}".format(text))
            except:
                print('Please try again.')

    def check_mic_device_index(self):
        SpeechToText.print_mic_device_index()

    def run_speech_to_text_english(self,device_index, language):
        SpeechToText.speech_to_text(device_index,language)

    if __name__ == '__main__':
        check_mic_device_index()