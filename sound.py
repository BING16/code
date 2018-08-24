import wave
import numpy as np
import matplotlib.pyplot as plt
import numpy
import pylab
import time

def wavread(path):
	wavfile =  wave.open(path,"rb")   #--利用wave库的只读方式打开文件
	params = wavfile.getparams()   #--获取wav文件的参数（以tuple形式输出），依次为(声道数，采样精度，采样率，帧数，......)
	datawav = wavfile.readframes(params[3])   #--得到每一帧的声音数据，其形式为‘左右左右’依次混合排列，返回的值是二进制数据，在python中用字符串表示二进制数据
	framerate = wavfile.getframerate()
	wavfile.close()
	
	return np, datawav, params, framerate

def Plot_At(np, datawav, params):
	#--绘制波形图
	#--wave data get  -xlxw
	#--1.通过wav库获得night.wav的头文件中的信息，如采样率／声道数等等
	#--2.提取出DATA区域的信息，用numpy将string格式数据转化为数组
	#--3.通过判定声道数将DATA区域数据进行处理（对数组矩阵进行转换）
	#--4.得到每个绘制点的时间（x坐标）
	#--5.用matplotlib库提供的方法绘制出波形图
	
	#--振幅处理
	wavdata = np.fromstring(datawav,dtype = np.short)
	wavtime = np.arange(0, params[3]) * (1.0/params[2])
	if params[0]==2:   #--判断声道数
		wavdata.shape = -1,2   #--通过shape先改变矩阵的形状使数据变为两列分别为左右声道
		wavdata = wavdata.T   #--通过转置得到最终数据
		
		plt.title("Night.wav's Frames")
		plt.subplot(211)   #--（’行数‘‘列数’‘左到右上到下的顺序数’）
		plt.xlabel("Time(s)")
		plt.ylabel("Amplitude")
		plt.plot(wavtime, wavdata[0], color = 'green')   #--（x，y，颜色）
		
		plt.subplot(212)
		plt.xlabel("Time(s)")
		plt.ylabel("Amplitude")
		plt.plot(wavtime, wavdata[1])
		plt.show()
	else:
		plt.xlabel("Time(s)")
		plt.ylabel("Amplitude")
		plt.plot(wavtime, wavdata, color = 'green')
		plt.show()
	
    
def Plot_ft(np, datawav, params):
	#--频率处理
	waveData = np.fromstring(datawav,dtype = np.int16)#将字符串转化为int
	waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化
	waveData = np.reshape(waveData,[params[3],params[0]]).T
	
	plt.specgram(waveData[0],Fs = params[2], scale_by_freq = True, sides = 'default')
	plt.ylabel('Frequency(Hz)')
	plt.xlabel('Time(s)')
	plt.show()
	
def Plot_fs(np, datawav, params, framerate):
	#--测试频率依次为29.004, 30.004, 32.004, 251031, 
	N = framerate
	start = 0 #开始采样位置
	df = params[2]/(N-1) # 分辨率
	freq = [df*n for n in range(0,N)] #N个元素
	wavdata = np.fromstring(datawav,dtype = np.short)
	
	if params[0] == 2:   #--判断声道数
		wavdata.shape = -1,2   #--通过shape先改变矩阵的形状使数据变为两列分别为左右声道
		wavdata = wavdata.T   #--通过转置得到最终数据
		wave_data2 = wavdata[0][start:start+N]
	else:
		wave_data2 = wavdata[start:start+N]
		
	c = numpy.fft.fft(wave_data2)*2/N
	#常规显示采样频率一半的频谱
	d = int(len(c)/2)
	a = 0
	#仅显示频率在4000以下的频谱,此处有所修改
	while freq[d] > 4000:
		d -= 10
	while freq[a] < 20:
		a += 10
	
	return (freq[np.argmax(abs(c[a:d-1]))+a])
	#pylab.plot(freq[a:d-1],abs(c[a:d-1]),'r')
	#pylab.show()

def main():
	f = 20.0
	while(True):
		try:
			np, datawav, params, framerate = wavread('/home/qbj//test.wav')
			#np, datawav, params, framerate = wavread('/home/qbj/5/export/会话.wav')
			#Plot_At(np, datawav, params)
			#Plot_ft(np, datawav, params)
			f1 = Plot_fs(np, datawav, params, framerate)
			if f != f1:
				f = f1
				print(f)
		except:
			print("Wrong!")
	
main()
