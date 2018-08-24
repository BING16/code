# encoding: utf-8
import wave
from pyaudio import PyAudio,paInt16

framerate=8000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME = 0.232/0.232*3
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record(file):
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count < TIME:  #--控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file(file,my_buf)
    stream.close()

def record_time(time):
	TIME = time


if __name__ == '__main__':
    while(True):
		try:
			my_record('test.wav')
			print('Over!') 
		except:
			print('Wrong！')