import requests


			     #APINIZI YAZIN VE BU LINKI TARAYTICIDA ACIN
#https://api.telegram.org/botKENDIAPINIZ/getUpdates  - tarayıcıda api hareketlerini izlemek ve id numarası almak için kullanın

#-------------------------------------------#
#telegrama gönder fonksiyonu
def gonder():

    #BURAYA KENDİ APİNİZİ GİRİN----------BURAYA/
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

    #BURAYA KENDİ APİNİZİ GİRİN---------------------BURAYA/
    requests.post(url="https://api.telegram.org/bot-Kendiapiniz-/sendMessage",data={"chat_id":"Kendi chat id numaranız","text":mesaj}).json()

    #daha sonra ekranda yazdıralım
    print(mesaj)

#FONKSIYONU CALISTIRALIM VE BEKLEYELIM
gonder()

#videoda gosterilen yontemleri yapın, bu dosya telefon içindir
#bot olusturduktan sonra en ustte verdigim linki tarayıcıda acın ve 
#id numarasını videodaki gibi alın, daha sonra gerekli yerlere yapıstırın
#kendi chat id numaranız kısımlerına bu id yi yazın
#termuxa baslangıcta gereklı izinleri verin ve python3 kurun
#bununla alakalı bircok kaynak var google termux baslangıc ayarları diye arama yapın
   