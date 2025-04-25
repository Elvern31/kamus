import random

def tebak_tebakan():
    pertanyaan = [
        {"tebak": "Apa yang selalu naik tapi gak pernah turun?", "jawaban": "umur"},
        {"tebak": "Kenapa sampah gak bisa jadi selebriti?", "jawaban": "Karena dia gak punya fans."},
        {"tebak": "Apa yang berwarna hijau dan sering ada di sampah?", "jawaban": "Lettuce (selada)"}, 
        {"tebak": "Apa yang sering dibuang, tapi gak bisa hilang?", "jawaban": "Waktu"},
        {"tebak": "Apa yang kalau dikumpulin jadi sampah, tapi bisa jadi barang berharga?", "jawaban": "Kardus bekas"}
    ]
    
    print("Selamat datang di tebak-tebakan sampah!")
    score = 0
    
    for tanya in pertanyaan:
        print(f"Tebak-tebakan: {tanya['tebak']}")
        jawaban_user = input("Jawabanmu: ").lower()
        
        if jawaban_user == tanya['jawaban']:
            print("Benar banget! 🎉")
            score += 1
        else:
            print(f"Salah! Jawabannya adalah: {tanya['jawaban']}")
    
    print(f"Skormu adalah {score}/{len(pertanyaan)}. Terima kasih sudah main! 🤙")

# Jalankan permainan
tebak_tebakan()
