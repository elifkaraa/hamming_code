import tkinter as tk
from tkinter import messagebox

def input_kontrol(data): # inputun uzunluğunu ve 0 ve 1 lerden oluşup oluşmadığını ve boyutunu kontrol etmek için
    if(all(bit in '01' for bit in data)):
        if(len(data) == 8):
            return True
        elif(len(data) == 16):
            return True
        elif(len(data) == 32):
            return True
        else:
            return False
    else:
        return False

def gerekli_parity_sayisi(m):
    r = 0
    while 2 ** r < m + r + 1:
        r += 1
    return r

def parite_kontrol(parity_pos, uzunluk): #hangi bitlerin parite bitine bağlı olduğunu belirlemek için
    return [i for i in range(1, uzunluk) if (i & parity_pos) == parity_pos]

def parite_hesaplama(hamming, pozisyon): #bitleri XOR larız
    sonuc = 0
    for pos in pozisyon:
        if hamming[pos] is not None:
            sonuc ^= hamming[pos]
    return sonuc

def hamming_olustur(data):
    bits = list(map(int, data))
    m = len(bits)
    r = gerekli_parity_sayisi(m)
    total_len = m + r + 1
    parity_positions = [2**i for i in range(r)]
    parity_positions.append(total_len - 1)
    hamming = [None] * total_len
    j = 0
    for i in range(1, total_len):
        if i not in parity_positions:
            hamming[i] = bits[j]
            j += 1

    for p in parity_positions[:-1]:
        kontrol = parite_kontrol(p, total_len)
        hamming[p] = parite_hesaplama(hamming, kontrol)

    kontrol = [i for i in range(1, total_len - 1)]
    hamming[total_len - 1] = parite_hesaplama(hamming, kontrol)
    return hamming

def hamming_hesapla():
    global hamming_kodu, data_length
    data = entry.get()
    if not input_kontrol(data):
        messagebox.showerror("Hatalı Giriş","Lütfen 0 ve 1 lerden oluşan 8,16 veya 32 bit uzunluğunda değerler giriniz!")
        return
    data_length = len(data) 
    hamming_kodu = hamming_olustur(data)
    göster_hamming(hamming_kodu)

def hata_uret():
    if not hamming_kodu:
        messagebox.showwarning("Uyarı", "Önce Hamming kodunu oluşturun!")
        return
    try:
        pozisyon = int(error_entry.get())
        if 1 <= pozisyon < len(hamming_kodu):
            hamming_kodu[pozisyon] ^= 1  # Bit i tersliyoruz
            göster_hamming(hamming_kodu)
        else:
            messagebox.showerror("Hatalı Pozisyon", f"Pozisyon 1 ile {len(hamming_kodu) - 1} arasında olmalıdır.")
    except ValueError:
        messagebox.showerror("Hatalı Giriş", "Pozisyon sayısal bir değer olmalıdır!")

def göster_hamming(hamming):
    pos_str = "Pozisyon: " + " ".join(f"{i:>3}" for i in range(1, len(hamming)))
    bit_str = "Bit:      " + " ".join(f"{hamming[i]:>3}" for i in range(1, len(hamming)))
    output_text.set(pos_str + "\n" + bit_str)

def sendrom_hesapla(hamming, parity_pos):
    toplam_len = len(hamming)
    sendrom = 0
    for i, p in enumerate(parity_pos):
        kontrol_edilen = parite_kontrol(p, toplam_len)
        hesaplanan = parite_hesaplama(hamming, kontrol_edilen)
        if hesaplanan != hamming[p]:
            sendrom += p
    return sendrom

def düzelt_ve_göster():
    global hamming_kodu

    if not hamming_kodu:
        messagebox.showwarning("Uyarı", "Hamming kodu bulunamadı.")
        return

    code = ''.join(str(bit) for bit in hamming_kodu[1:])  # index 1'den itibaren, çünkü 0 kullanılmıyor
    n = len(code)
    
    
    r = 0 # r=Parity bit sayısı
    while (2 ** r) < n:
        r += 1
    syndrome = 0
    for i in range(r):
        parity_pos = 2 ** i
        count = 0
        for j in range(1, n):  
            if j & parity_pos:
                count += int(code[j - 1])
        if count % 2 != 0:
            syndrome += parity_pos

    overall_parity = int(code[-1])
    data_and_parity = code[:-1]
    calculated_overall = sum(int(b) for b in data_and_parity) % 2

    corrected = list(code)

    if syndrome == 0 and calculated_overall == overall_parity:
        messagebox.showinfo("Durum", "Hata yok.")
    elif syndrome != 0 and calculated_overall != overall_parity:
        pos = syndrome - 1
        if pos < len(corrected):
            corrected[pos] = '0' if corrected[pos] == '1' else '1'
            for i in range(1, len(corrected) + 1):
                hamming_kodu[i] = int(corrected[i - 1])
            göster_hamming(hamming_kodu)
            messagebox.showinfo("Düzeltildi", f"{pos + 1}. pozisyondaki hata düzeltildi.")
    elif syndrome != 0 and calculated_overall == overall_parity:
        messagebox.showerror("Çift Hata", "Çift bitli hata tespit edildi, düzeltilemez.")
    elif syndrome == 0 and calculated_overall != overall_parity:
        pos = len(corrected) 
        corrected[-1] = '0' if corrected[-1] == '1' else '1'
        for i in range(1, len(corrected) + 1):
            hamming_kodu[i] = int(corrected[i - 1])
        göster_hamming(hamming_kodu)
        messagebox.showinfo("Genel Parite", f"Genel parite biti ({pos}) düzeltildi.")
    else:
        messagebox.showerror("Beklenmedik", "Beklenmeyen bir durum oluştu.")



root = tk.Tk()
root.title("Hamming SEC-DED Simülatörü")

tk.Label(root, text="Veri (8,16,32 bit):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Hamming Kodu Oluştur", command=hamming_hesapla).pack(pady=5)
output_text = tk.StringVar()
tk.Label(root, textvariable=output_text, justify="left", font=("Courier", 10)).pack(pady=10)

tk.Label(root, text="Hata eklemek istediğiniz pozisyon:").pack() #kullanıcıdan hata girilicek pozisyonu alıyoruz
error_entry = tk.Entry(root)
error_entry.pack()

tk.Button(root, text="Hata Ekle", command=hata_uret).pack(pady=5) #
tk.Button(root, text="Düzelt ve Göster", command=düzelt_ve_göster).pack(pady=5)

hamming_kodu = []

root.mainloop()

