# 将文本隐藏在图片中和读取图片中隐藏的文本
from PIL import Image

def hideInPic(Pic, string, newname):	# 将字符串以方便读取的形式隐藏进图片，要求以字符串形式传入图片名、需要隐藏的文本及新图片名
	numList = sToI(string)
	image = Image.open('%s' % Pic)
	changeRGB(image, numList, newname)
	return None

def readPic(Pic):	# 读取图片中隐藏的文本
	L = []
	num = index = 0
	image = Image.open('%s' % Pic)
	w, h = image.size
	u, j, m = image.getpixel((0, 0))
	u = u % 10
	for y in range(1, u+1):
		r, g, b = image.getpixel((0, y))
		num = num * 10 + (r % 10) 
	for y in range(0, h):
		for x in range(1, w):
			index = index + 1
			r, g, b = image.getpixel((x, y))
			asc = r % 10 * 100 + g % 10 * 10 + b % 10
			L.append(chr(asc))
			if  index == num:
				return ''.join(L)

class inputError(ValueError):
    pass

def sToI(string):	# 将字符串转换为ASCLL值列表
	l=[]
	for x in string:
		l.append(ord(x))
	return l

def theKey(numList, image):	# 将字符串长度隐藏进图片
	length = len(numList)
	num = len(str(length))
	r, g, b = image.getpixel((0, 0))
	r = r // 10 * 10 + num
	image.putpixel((0, 0), (r, g, b))
	for y in range(1, num+1):
		r, g, b = image.getpixel((0, y))
		r = r // 10 * 10 + int(str(length)[y-1])
		image.putpixel((0, y), (r, g, b))
	return None

def changeRGB(image, numList, name):	# 将字符串隐藏进图片
	index = 0
	num = len(numList)
	w, h = image.size
	theKey(numList, image)
	for y in range(0, h):
		for x in range(1, w):
			n = numList[index]
			index = index + 1
			if n < 1000 and n >= 0:
				r = n // 100
				g = n // 10 % 10
				b = n % 10
				u, j, m = image.getpixel((x, y))
				r = u // 10 * 10 + r
				g = j // 10 * 10 + g
				b = m // 10 * 10 + b
				r, g, b = errorPrevent(r, g, b)
				image.putpixel((x, y), (r, g, b))
			else:
				raise inputError('invalid value: %s' % 'only support ascll 0~999')
			if index == num:
				return image.save("%s.bmp" % name)

def errorPrevent(r, g, b):		# 防止像素RGB值超过255出现错误
	for x in (r, g, b):
		if x >255:
			x = x - 10
	return (r, g, b)