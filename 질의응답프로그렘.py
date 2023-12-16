import time
import winsound
import webbrowser

print("안녕 만나서 반가워요~")
winsound.Beep(600, 500)
time.sleep(1)
name = input("당신의 이름이 뭐에요? ")
print("아~ 당신의 이름은",name,"이군요~만나서 반가워요")
winsound.Beep(600, 500)
time.sleep(1)
year = int(input("몇 년도에 태어났나요?"))
age = 2022 - year + 1
print("아~ 당신은 올 해",age,"살 이군요")
winsound.Beep(600, 500)
time.sleep(1)
food = input("좋아하는 음식이 뭐에요?")
print("아~ 당신은",food,"을 좋아하는군요")
winsound.Beep(600,500)
print("궁금한 것이 있으면 무엇이든 물어보세요")
question=input()
url="www.google.co.kr/search?q="+question
webbrowser.open(url)
input()
