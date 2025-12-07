talhaHesap = {
    'ad':'Talha Yilmaz',
    'hesapNo':147852369,
    'bakiye':10000,
    'ekHesap':3000
}
senaHesap = {
    'ad':'Senanur Kahraman Yilmaz',
    'hesapNo':369852147,
    'bakiye':12000,
    'ekHesap':4000
}

def paraCek(hNo,miktar):

    print(f"Merhaba {hNo['ad']}")
    if hNo['bakiye'] >= miktar:
        print("Paranizi alabilirsiniz.")
        hNo['bakiye'] -= miktar
        print(f"Kalan tutar = {hNo['bakiye']}")
    else:
        print(f"Bakiyeniz yetersiz. Bakiye = {hNo['bakiye']}")
        toplam = hNo['bakiye'] + hNo['ekHesap']
        if toplam >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanilsin mi (e/h) ? ")
            if ekHesapKullanimi == 'e':
                print("Paranizi alabilirsiniz.")
                hNo['bakiye'] = 0
                toplam = toplam - miktar
                print(f"Kalan bakiyeniz {hNo['bakiye']} ve ek hesabinizda kalan para = {toplam}")
            else:
                print(f"Iyi gunler dileriz.")
        else:
            print(f"Ek hesap dahil yetersiz para. Paraniz = {toplam}")

def paraYatir(hNo,miktar):
    print(f"Merhaba {hNo['ad']}")
    hNo['bakiye'] += miktar
    print(f"Guncel bakiyeniz: {hNo['bakiye']}")

tutar = int(input("Cekmek istediginiz ya da yatirmak istediginiz tutari giriniz: "))
paraCek(senaHesap,tutar)
paraCek(senaHesap,tutar)
paraCek(senaHesap,tutar)
paraCek(senaHesap,tutar)
paraYatir(senaHesap,tutar)