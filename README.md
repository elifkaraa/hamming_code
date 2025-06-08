# 🧮 Hamming SEC-DED Simülatörü
## 📌 Proje Tanımı
Bu proje, Hamming SEC-DED (Single Error Correction – Double Error Detection) kodlama ve düzeltme simülatörüdür. Projede Python dili ve Tkinter kütüphanesi kullanılmıştır.

Kullanıcı:

8,16 veya 32 bitlik bir veri girişi yapararak bu veriye ait Hamming kodunu oluşturabilir,
Hata ekleyebilir,
Hata tespiti ve düzeltme yapabilir.
## ⚙️ Fonksiyonlar
### - input_kontrol(data): 
Kullanıcının girdiği verinin sadece 0 ve 1 karakterlerinden oluşup oluşmadığını ve uzunluğunun 8, 16 veya 32 bit olup olmadığını kontrol eder.
 Çıktı: True (geçerli), False (geçersiz)
### - gerekli_parity_sayisi(m):
Verinin uzunluğuna (m) göre Hamming kodunda gereken parite biti sayısını hesaplar.
### - parite_kontrol(parity_pos, uzunluk): 
Belirli bir parite biti pozisyonu (parity_pos) için, hangi bitlerin o parite biti tarafından kontrol edildiğini listeler.
### - parite_hesaplama(hamming, pozisyon):
Verilen pozisyon listesindeki bitleri XOR'layarak parite bitinin değerini hesaplar.
### - hamming_olustur(data): 
Kullanıcının verdiği veri bitlerini alır, gerekli parite bitlerini ekleyerek Hamming kodunu oluşturur. Genel parite bitini de hesaplar.
### - hamming_hesapla(): 
Arayüzden veriyi alır, geçerliğini kontrol eder, Hamming kodunu oluşturur ve ekranda gösterir.
### - hata_uret():  
Kullanıcının belirttiği pozisyonda (1-index) Hamming kodunda yapay bir hata oluşturur.
### - düzelt_ve_göster():
Hamming kodundaki hatayı tespit eder, tek bit hatası varsa düzeltir, çift bit hatası varsa kullanıcıya bildirir, genel parite hatasını düzeltir.
### - göster_hamming(hamming): 
Hamming kodunun bit pozisyonları ve değerlerini okunabilir şekilde arayüzde gösterir.
## Grafik Arayüz (GUI) 
Program, Tkinter kütüphanesi kullanılarak oluşturulmuş basit ve kullanıcı dostu bir grafik arayüz sunar. Bu arayüz, Hamming SEC-DED kodunun oluşturulması, hata eklenmesi ve düzeltilmesi işlemlerini kolaylaştırır.

 ### Arayüz Öğeleri:
- **Veri Girişi**: Kullanıcının 8, 16 veya 32 bit uzunluğunda ikili veri girmesi için metin kutusu.

- **Kod Hesaplama Butonu**: Girilen veriye göre Hamming kodunu hesaplar.

- **Kodlu Veri Gösterimi**: Oluşturulan Hamming kodunu ve bit pozisyonlarını gösteren etiket.

- **Hata Pozisyonu Girişi**: Hata eklemek istediği bit pozisyonunu kullanıcıdan alan metin kutusu.

- **Hata Ekle Butonu**: Belirtilen pozisyonda kodda hata oluşturur (bit tersler).

- **Hata Tespit & Düzelt Butonu**: Kodda bulunan hatayı tespit eder ve tek bit hatasını düzeltir.

- **Sonuç Etiketi**: Hata durumu ve düzeltme sonuçları hakkında bilgi verir.
  ### Metotlar:
**hamming_hesapla()**:Arayüzden alınan veriyi doğrular, Hamming kodunu oluşturur ve ekranda gösterir.

**hata_uret()**:Kullanıcının belirttiği pozisyonda Hamming kodunda hata oluşturur ve sonucu gösterir.

**düzelt_ve_göster()**:Kodda hata varsa tespit eder; tek bit hatasını düzeltir, çift hata varsa uyarır ve sonucu arayüzde bildirir.
# #🔍 Kullanım Senaryosu
**1**:Kullanıcı 8, 16 veya 32 bit uzunluğunda, örneğin "11010101" gibi bir ikili veri girer.

**2**:"Hamming Kodu Oluştur" butonuna basar.

**3**:Uygulama, girdiye göre 13 veya uygun uzunlukta Hamming SEC-DED kodunu hesaplar ve gösterir.

**4**:Kullanıcı, "Hata Oluştur" kısmına bir pozisyon numarası (örneğin: 5) girer.

**5**:Belirtilen pozisyondaki bit terslenerek hata enjekte edilir.

**6**:"Düzelt ve Göster" butonuna basılır.

**7**:Sistem hatayı tespit eder ve tek bitlik hataları düzeltir; çift bitli hatalar varsa uyarı verir.
## 🎥 Demo & Kaynak
🔗 Demo Videosu: https:https://youtu.be/bakLMbq16XY
🧷 GitHub Linki: 



