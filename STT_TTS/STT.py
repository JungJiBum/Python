'''
mp3 to wav를 하기위해서 여러 작업을 진행함
폴더 내 ffmpeg.exe가 없을때 에러가 나타남
RuntimeWarning: Couldn't find ffmpeg or avconv
    - defaulting to ffmpeg, but may not work
위 같은 에러 발생하여 ffmpeg 파일(3ea)업로드


'''
from pydub import AudioSegment
import speech_recognition as sr
def convert():
    src = "text_ko.mp3"
    dst = "test.wav"
    audSeg = AudioSegment.from_mp3(src)
    audSeg.export(dst,format="wav")

convert()
r = sr.Recognizer()

with sr.AudioFile('test.wav') as source:
    audio = r.record(source, duration=10)

To_Text = r.recognize_google(audio_data=audio, language='ko-KR')
print(To_Text)