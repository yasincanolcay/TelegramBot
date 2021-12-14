#code=utf8
from datetime import datetime
import requests
import tkinter
from tkinter import *
from threading import Thread

#https://api.telegram.org/bot/getUpdates  - tarayıcıda api hareketlerini izlemek ve id numarası almak için kullanın


#-------------------------------------------#
#telegrama gönder fonksiyonu
def gonder():
    #iş yükü parçacıgı için
    def thread1():
        ap = 'https://api.telegram.org/bot-Kendiapiniz-/sendMessage'#istek yollarken kullanın-bot'dan sonra api yazın
        covid19="https://pomber.github.io/covid19/timeseries.json"#covid19 bilgilerini buradan çekiniz
        #istek yollar
        durum = requests.get(covid19)
        #gelen cevabı json olarak çevirir
        jsoncevir = durum.json()
        #cevap içinden türkiye bilgilerini alır
        kacgun = len(jsoncevir["Turkey"])
        #en son güncel olan bilgiye ulaşır
        turkey = jsoncevir["Turkey"][kacgun-1]
        #bu verilerden istediklerimizi çekelim
        tarih = turkey["date"]
        vaka = turkey["confirmed"]
        olum = turkey["deaths"]
        iyilesme = turkey["recovered"]
        #bunları bir yerde toparlayalım
        mesaj = "{} Tarihli covid19 bilgileri aşagıdaki gibidir\nvaka sayısı:{}\nölüm sayısı:{}\niyileşme sayısı:{}".format(tarih,vaka,olum,iyilesme)
        # ve buınları telegrama yollayalım
        requests.post(url="https://api.telegram.org/bot-Kendiapiniz-/sendMessage",data={"chat_id":"Kendi chat id numaranız","text":mesaj}).json()
        #daha sonra ekranda yazdıralım
        label1["text"] = mesaj

    #thread ile fonksiyonu başlatır
    th = Thread(target=thread1)
    th.start()
#-------------------------------------------#
#tasarım kodları
top = Tk()
top.title("telegram bot")#pencere baslıgı
top.geometry("400x200+150+150")#pencere genislikxyukseklik+x ekseni+y ekseni
top.resizable(False,False)#kullanıcı pencereyi buyutmesin - sabit boyut
frame = Frame(top,bg="dodgerblue")#frame pencere icine,arkaplan rengi
frame.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)#frame x ekseni, y ekseni, genislik, yukseklik

label1 = Label(font="Arial 12 bold",bg="dodgerblue",fg="black")#label font,arkaplan,yazı rengi
label1.pack()# aktif et

btn = Button(text="Gonder",font="Arial 12 bold",bg="green",fg="white",command=gonder)#buton,yazı,font,arkarenk,yazırengi,komut
btn.pack()#butonu aktif et



#pencere kapanmaması icin dongu
top.mainloop()
