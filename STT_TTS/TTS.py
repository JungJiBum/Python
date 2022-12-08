# https://scribblinganything.tistory.com/522?category=918711
from gtts import gTTS
from playsound import playsound

# text= input("영어 입력 : ")
test=  input("한국어 입력 : ")

# text_to_voice = gTTS(text=text, lang="en")
# text_to_voice.save("C:/Users/tec/Desktop/python/Python/STT_TTS/text_en.mp3")

# text_to_voice1 = gTTS(text=text, lang="fr")
# text_to_voice1.save("C:/Users/tec/Desktop/python/Python/STT_TTS/text_fr.mp3")

test_to_voice = gTTS(text=test,lang='ko')
test_to_voice.save("C:/Users/tec/Desktop/python/Python/STT_TTS/text_ko.mp3")


# playsound("C:/Users/tec/Desktop/python/Python/STT_TTS/text_en.mp3")
# playsound("C:/Users/tec/Desktop/python/Python/STT_TTS/text_fr.mp3")
playsound("C:/Users/tec/Desktop/python/Python/STT_TTS/text_ko.mp3")
