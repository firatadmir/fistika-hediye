import streamlit as st
import time  # Bekleme süresi eklemek için
from PIL import Image, ImageOps


# Sayfa ayarları
st.set_page_config(page_title="FISTIKIMIN DOĞUM GÜNÜ İÇİN", page_icon="📼", layout="centered")

# --- TÜM SAYFALAR İÇİN GEÇERLİ GÜNCELLENMİŞ TASARIM (CSS, BUTON, KUTU VE FOTOĞRAFLAR) ---
st.markdown("""
    <style>
    /* 1. Arka Plan Görseli */
    .stApp {
        background-image: url("https://static.vecteezy.com/system/resources/previews/074/774/108/non_2x/seamless-pattern-with-a-koi-fish-pond-koi-carps-seamless-pattern-with-golden-red-and-black-koi-carps-on-background-of-water-waves-for-wrapping-paper-scrapbooking-textile-fabric-vector.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* 2. Güvenli Yazı Ayarları (Beyaz, Kalın ve Gölgeli) */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #FFFFFF !important;
        font-family: 'Trebuchet MS', 'Comic Sans MS', sans-serif !important; 
        font-weight: 800 !important; 
        text-shadow: 2px 2px 5px rgba(0,0,0,0.9) !important;
    }

    /* 3. Video Oynatıcı Boyutu */
    video {
        max-height: 40vh !important;
        width: auto !important;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
    }

    /* 4. BUTONLARI ORTALAMA */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* 5. BUTON TASARIMI (%20 Daha Büyük ve Oval/Tatlı Şekil) */
    div.stButton > button {
        background: linear-gradient(135deg, #FF7F50 0%, #FF4500 100%) !important; 
        color: #FFFFFF !important; 
        font-family: 'Trebuchet MS', sans-serif !important;
        font-size: 18px !important; 
        font-weight: bold !important;
        padding: 12px 38px !important; 
        border-radius: 30px !important; 
        border: none !important;
        box-shadow: 0px 5px 15px rgba(255, 69, 0, 0.4) !important; 
        transition: all 0.3s ease !important; 
    }

    div.stButton > button:hover {
        transform: translateY(-3px) scale(1.03); 
        box-shadow: 0px 8px 20px rgba(255, 69, 0, 0.6) !important;
        background: linear-gradient(135deg, #FF6347 0%, #FF1493 100%) !important; 
    }

    div.stButton > button:active {
        transform: translateY(1px) scale(0.98); 
    }

    /* 6. SAYFA GEÇİŞ EFEKTİ */
    @keyframes yumusakGecis {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    .block-container {
        animation: yumusakGecis 0.6s ease-out forwards; 
    }

    /* 7. YAZMA KUTULARINI ÖZELLEŞTİRME */
    div[data-testid="stTextInput"] input {
        background-color: #FFF0F5 !important; 
        color: #2F4F4F !important; 
        font-family: 'Trebuchet MS', sans-serif !important;
        font-size: 16px !important; 
        font-weight: 600 !important;
        padding: 12px 20px !important; 
        border-radius: 20px !important; 
        border: 2px solid #FFB6C1 !important; 
        box-shadow: inset 0px 2px 5px rgba(0, 0, 0, 0.05) !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #FF69B4 !important; 
        box-shadow: 0px 0px 10px rgba(255, 105, 180, 0.6) !important; 
        background-color: #FFFFFF !important; 
        color: #000000 !important;
    }

    /* --- YENİ EKLENEN KISIM: 8. FOTOĞRAFLARI YUMUŞAK KÖŞELİ YAPMA --- */
    div[data-testid="stImage"] img {
        border-radius: 20px !important; /* Fotoğrafların köşelerini ovalleştirir */
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4) !important; /* Fotoğrafların altına şık, koyu bir gölge ekler */
        transition: transform 0.3s ease !important; /* İleride ufak efektler eklersek yumuşak geçsin diye */
    }
    
    </style>
""", unsafe_allow_html=True)

# Oturum (Session) durumu kontrolü
if 'asama' not in st.session_state:
    st.session_state.asama = 0

# Başlık
st.title("SENİ CKO SEVİOMMMMM ")
st.write("---")

# 0. Aşama: Karşılama Ekranı
if st.session_state.asama == 0:
    st.subheader("İYİ Kİ DOĞDUN GÜZELLER GÜZELİMMMM")
    st.write("bunları sen gül diye yapıom")
    
    # CSS İLE YÜKSEKLİK KISITLAMASI
    st.markdown("""
        <style>
        /* Video oynatıcıyı hedef alıp yüksekliğini kısıtlıyoruz */
        video {
            max-height: 40vh !important; /* Ekran yüksekliğinin maksimum %40'ı kadar yer kapla */
            width: auto !important; /* En-boy oranını bozmamak için genişliği serbest bırak */
            border-radius: 15px; /* Hediyeye yakışır yumuşak köşeler :) */
        }
        </style>
    """, unsafe_allow_html=True)

    # Ekranı yine 3 sütuna bölüyoruz (Videonun ortada kalması için)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        video_alani = st.empty()
        
        if 'bekleme_yapildi' not in st.session_state:
            video_alani.info("Sürpriz yükleniyor, lütfen bekle...")
            time.sleep(2)
            st.session_state.bekleme_yapildi = True
        
        video_alani.video("dg_video1.mp4", autoplay=True)
    
    with col2:
        st.write("") 
        if st.button("BURAYA TIKLA"):
            st.session_state.asama = 1
            st.rerun()

# 1. Aşama: İlk Soru
elif st.session_state.asama == 1:
    
    # Doğru cevabı oturuma (session) kaydediyoruz
    if 'soru1_dogru' not in st.session_state:
        st.session_state.soru1_dogru = False

    # EĞER HENÜZ DOĞRU CEVAP VERİLMEDİYSE SORUYU GÖSTER
    if not st.session_state.soru1_dogru:
        st.subheader("Sana anılarımız ve şakalarımızdan oluşan minik bir test hazırladım.")
        
        cevap_1 = st.text_input("SORU 1(Kolay): Görgüsüzlüğün kişiyi gülünç duruma düşüreceğini \n"
        "anlatan sözde,kekliği taklit ederken kendi yürüyüşünü şaşıran hangisidir \n"
        "(İPUCU D...)")
        
        if st.button("Cevapla"):
            if "kaplumbağa" in cevap_1.lower(): 
                st.session_state.soru1_dogru = True
                st.rerun() # Doğruysa ekranı yenileyip sadece alt bloğu çalıştırır
            elif cevap_1 == "":
                st.warning("Cevabını yaz")
            else:
                st.error("SEN BENİ SEVMİON 😭😭 (saka)")
                
    # EĞER CEVAP DOĞRUYSA (SORU EKRANDAN GİDER, SADECE BUNLAR GELİR)
    else:
        st.success(" DABİ Kİİ☕")
        
        # 1. Ses Oynatıcı en üstte (success mesajının hemen altında)
        st.audio("trollselcuk_son.mp3", format="audio/mp3")
        
        st.write("---") # Estetik bir ayırıcı çizgi
        
        # İki resmi yan yana eşit alan kaplayacak şekilde koyuyoruz
        img_col1, img_col2 = st.columns([1, 1])
        
        # Hedeflenen boyut (Genişlik, Yükseklik) - İkisini de 500x500 kare yapıyoruz
        hedef_boyut = (500, 500) 
        
        with img_col1:
            # 1. Fotoğrafı aç, bozmadan merkezden kırparak boyutlandır ve ekrana bas
            img1 = Image.open("troll_selcuk_selcuk.png")
            img1_kirpilmis = ImageOps.fit(img1, hedef_boyut)
            st.image(img1_kirpilmis, use_container_width=True)
            
        with img_col2:
            # 2. Fotoğrafı aç, bozmadan merkezden kırparak boyutlandır ve ekrana bas
            img2 = Image.open("troll_selcuk_teyze.png")
            img2_kirpilmis = ImageOps.fit(img2, hedef_boyut)
            st.image(img2_kirpilmis, use_container_width=True)
            
        st.write("---")
        
        # 3. İleri gitme butonu en altta
        if st.button("Dİnledikten sonra buraya tıkla"):
            st.session_state.asama = 2
            st.rerun()

# 2. Aşama: Nostalji Ara Sayfası (Soru yok, sadece anı)
elif st.session_state.asama == 2:
    st.subheader("MİNİK BİR ANI MOLASI 🐧💞")
    
    st.write("Her bir anımız o kadar güzel ki... Değil bu siteye bir ömre sığmaz bana verdiğin mutluluk ve huzur ahu gözlüm")
    st.audio("dg_ses1.mpeg", format="audio/mpeg")
    st.write("---")
    
    hedef_boyut = (500, 500) # Hepsini kusursuz 500x500 kare yapıyoruz
    
    # --- 1. SATIR (Üstteki İki Fotoğraf) ---
    satir1_col1, satir1_col2 = st.columns([1, 1])
    
    with satir1_col1:
        img1 = Image.open("dg_fotograf1.jpg")
        img1 = ImageOps.exif_transpose(img1) 
        img1_kirpilmis = ImageOps.fit(img1, hedef_boyut)
        st.image(img1_kirpilmis, use_container_width=True)
        
    with satir1_col2:
        img2 = Image.open("dg_fotograf2.jpg")
        img2 = ImageOps.exif_transpose(img2)
        img2_kirpilmis = ImageOps.fit(img2, hedef_boyut)
        st.image(img2_kirpilmis, use_container_width=True)
        
    st.write("") # Üst ve alt satır arasına minik estetik bir boşluk bırakır
    
    # --- 2. SATIR (Alttaki İki Fotoğraf) ---
    satir2_col1, satir2_col2 = st.columns([1, 1])
    
    with satir2_col1:
        img3 = Image.open("dg_fotograf3.jpg")
        img3 = ImageOps.exif_transpose(img3) 
        img3_kirpilmis = ImageOps.fit(img3, hedef_boyut)
        st.image(img3_kirpilmis, use_container_width=True)
        
    with satir2_col2:
        img4 = Image.open("dg_fotograf4.jpg")
        img4 = ImageOps.exif_transpose(img4)
        img4_kirpilmis = ImageOps.fit(img4, hedef_boyut)
        st.image(img4_kirpilmis, use_container_width=True)
        
    st.write("---")
    
    if st.button("İVİTT TESTİMİZE DEVAM EDELİMM"):
        st.session_state.asama = 3
        st.rerun()


# 3. Aşama: İkinci Soru
elif st.session_state.asama == 3:
    
    # Doğru cevabı oturuma (session) kaydediyoruz
    if 'soru2_dogru' not in st.session_state:
        st.session_state.soru2_dogru = False

    # EĞER HENÜZ DOĞRU CEVAP VERİLMEDİYSE SORUYU GÖSTER
    if not st.session_state.soru2_dogru:
        st.subheader("Soru 2(Orta):Bizim favorimiz olan ve senin kaçırıp eve getirmek istediğin kedinin adı nedir? \n (İpucu : Dombili)")
        
        # Kendi sorunu buraya yazabilirsin
        cevap_2 = st.text_input("Buraya yaz")
        
        if st.button("Cevapla"):
            # Doğru cevabı buraya küçük harflerle yaz
            if "mig-29" in cevap_2.lower():
                st.session_state.soru2_dogru = True
                st.rerun()
            elif cevap_2 == "":
                st.warning("Bir tahminde bulunmalısın.")
            else:
                st.error("AMA.. 😭😭")
                
    # EĞER CEVAP DOĞRUYSA (SORU GİDER, SADECE FOTOĞRAFLAR GELİR)
    else:
        st.success("AFERİN BENİM GEYİKEE")
        st.write("---")
        
        # İlk sorudaki gibi ekranı 2 eşit sütuna bölüyoruz
        img_col1, img_col2 = st.columns([1, 1])
        hedef_boyut = (500, 500) # İkisini de 500x500 mükemmel kare yapıyoruz
        
        with img_col1:
            # UYARI: Eğer fotoğrafların uzantısı .png ise koddaki .jpg kısmını değiştirmeyi unutma!
            img1 = Image.open("dg_mig29_1.jpg") 
            img1_kirpilmis = ImageOps.fit(img1, hedef_boyut)
            st.image(img1_kirpilmis, use_container_width=True)
            
        with img_col2:
            img2 = Image.open("dg_mig29_2.jpg")
            img2_kirpilmis = ImageOps.fit(img2, hedef_boyut)
            st.image(img2_kirpilmis, use_container_width=True)
            
        st.write("---")
        
        # 4. Aşama'ya geçiş butonu
        if st.button("Bir sonraki soru için tıkla"):
            st.session_state.asama = 4
            st.rerun()

# 4. Aşama: Üçüncü Soru (Kiraz Ağacı)
elif st.session_state.asama == 4:
    
    if 'soru3_dogru' not in st.session_state:
        st.session_state.soru3_dogru = False

    # EĞER HENÜZ DOĞRU CEVAP VERİLMEDİYSE
    if not st.session_state.soru3_dogru:
        st.subheader("Soru 3(Orta): Senlen beraber yaptığımız ve yaparken benim sinirden alnımda damar çıkartan ama sonunda bitirdiğimizde cko güzel olan şey \n (İpucu: bunu bulursun ya sana güveniom)")
        
        cevap_3 = st.text_input("Buraya yaz")
        
        if st.button("Cevapla"):
            # Doğru cevabı buraya yaz
            if "kiraz ağacı" in cevap_3.lower():
                st.session_state.soru3_dogru = True
                st.rerun()
            elif cevap_3 == "":
                st.warning("Hadi ama, boş bırakmak yok!")
            else:
                st.error("AMA BUNU BİLMEN GEREKİO :((")
                
    # EĞER CEVAP DOĞRUYSA
    else:
        st.success("SEN HER SEYİ HATIRLAYAN 1 GEYİKSİN")
        st.write("---")
        
        # Tek bir fotoğrafı şıkça ORTALAMAK için ekranı 3'e bölüyoruz
        # Ortadaki sütuna daha fazla alan (2 birim) veriyoruz
        sol_bosluk, orta_alan, sag_bosluk = st.columns([1, 2, 1])
        
        with orta_alan:
            st.image("dg_kirazagaci.jpg", use_container_width=True)
            
        st.write("---")
        
        # Artık bir sonraki adım "Final" olacağı için asama'yı 4 yapıyoruz
        if st.button("MUHTESEM GEYİK(BURAYA TIKLA)"):
            st.session_state.asama = 5
            st.rerun()

# 5. Aşama: YENİ 2. Anı Molası (4 Fotoğraftan Oluşan Sekans)
elif st.session_state.asama == 5:
    st.subheader("Birlikte Geçen Harika Zamanlar... 💖")
    st.write("Zaman akıp giderken seninle biriktirdiğimiz her anı,ruhumun en değerli melodisi.")
    st.audio("dg_ses2.mpeg", format="audio/mpeg")
    st.write("---")
    
    hedef_boyut = (500, 500) # Kusursuz kare simetrisi için
    
    # --- 1. SATIR (Üstteki İki Fotoğraf) ---
    satir1_col1, satir1_col2 = st.columns([1, 1])
    
    with satir1_col1:
        img1 = Image.open("dg_fotograf5.jpg") # Buraya kendi fotoğraf ismini yazabilirsin
        img1 = ImageOps.exif_transpose(img1) # Sağa/sola dönmeyi engeller
        img1_kirpilmis = ImageOps.fit(img1, hedef_boyut)
        st.image(img1_kirpilmis, use_container_width=True)
        
    with satir1_col2:
        img2 = Image.open("dg_fotograf6.jpg")
        img2 = ImageOps.exif_transpose(img2)
        img2_kirpilmis = ImageOps.fit(img2, hedef_boyut)
        st.image(img2_kirpilmis, use_container_width=True)
        
    st.write("") # İki satır arası estetik boşluk
    
    # --- 2. SATIR (Alttaki İki Fotoğraf) ---
    satir2_col1, satir2_col2 = st.columns([1, 1])
    
    with satir2_col1:
        img3 = Image.open("dg_fotograf7.jpg")
        img3 = ImageOps.exif_transpose(img3)
        img3_kirpilmis = ImageOps.fit(img3, hedef_boyut)
        st.image(img3_kirpilmis, use_container_width=True)
        
    with satir2_col2:
        img4 = Image.open("dg_fotograf8.jpg")
        img4 = ImageOps.exif_transpose(img4)
        img4_kirpilmis = ImageOps.fit(img4, hedef_boyut)
        st.image(img4_kirpilmis, use_container_width=True)
        
    st.write("---")
    
    # Buradaki buton artık büyük finale (6. aşamaya) götürecek
    if st.button("VEEE FİNAL SORUSUU"):
        st.session_state.asama = 6
        st.rerun()

# 6. Aşama: Dördüncü Soru (Final Soru)
elif st.session_state.asama == 6:
    st.subheader("Soru 4(İmkansız):Senlen tanıştığımız gün gittiğimiz tiyatro oyununun adı neydi?")
    
    # Track if this final question is answered correctly
    if 'soru6_dogru' not in st.session_state:
        st.session_state.soru6_dogru = False

    # EĞER HENÜZ DOĞRU CEVAP VERİLMEDİYSE
    if not st.session_state.soru6_dogru:
        st.write("1 TANEMMM (bir)")
        
        # Son sorunun metnini ve doğru cevabı buraya yaz
        cevap_6 = st.text_input("Bulabilirsin ben sana inaniom")
        if st.button("BURAYA TIKLA"):
            # Doğru cevabı buraya küçük harflerle yaz (örneğin: 'kazandibi')
            if "bitmeyecek öykü" in cevap_6.lower():
                st.session_state.soru6_dogru = True
                st.rerun() # Refresh to hide question, show photo
            elif cevap_6 == "":
                st.warning("Bu son soru, boş bırakmak yok!")
            else:
                st.error("Bu zor olduğu için ipucu veriom: B... Ö...")
                
    # EĞER CEVAP DOĞRUYSA (Görseller ve Büyük Final butonu)
    else:
        st.success("SENİ CKO SEVİOM İYİ Kİ DOGDUNNN <3")
        st.write("---")
        
        # Tek bir fotoğrafı şıkça ORTALAMAK için ekranı 3'e bölüyoruz
        # Ortadaki sütuna daha fazla alan (2 birim) veriyoruz
        sol_bosluk, orta_alan, sag_bosluk = st.columns([1, 2, 1])
        
        with orta_alan:
            # ! UPDATE: Klasöründeki o özel fotoğrafın ismini buraya yaz (örneğin: dg_last_photo.jpg)
            img_last = Image.open("dg_tiyatro.jpg") # Uzantısını kontrol et (.jpg veya .png)
            img_last = ImageOps.exif_transpose(img_last)
            st.image(img_last, use_container_width=True)
            
        st.write("---")
        
        # Buradaki buton artık gerçekten Final (7. aşamaya) götürecek
        if st.button("Sürprizi görme zamanı geldiiii "):
            st.session_state.asama = 7
            st.rerun()

# 7. Aşama: Final (Yeni Numara)
elif st.session_state.asama == 7:
    st.balloons() # Ekranda balonlar uçurur 🎉
    st.subheader("AFERİN BENİM GEYİKİMEEEE TÜM TESTİ ÇÖZDÜNNN")
    st.write("💞💞💞")
    
    st.write("---")
    
    # --- 1. SATIR (Üstteki İki GIF/MP4) ---
    satir1_col1, satir1_col2 = st.columns([1, 1])
    
    with satir1_col1:
        # autoplay, loop ve muted parametreleri videoyu kusursuz bir GIF'e dönüştürür
        st.video("dg_gif1.mp4", autoplay=True, loop=True, muted=True)
        
    with satir1_col2:
        st.video("dg_gif2.mp4", autoplay=True, loop=True, muted=True)
        
    st.write("") # İki satır arası estetik boşluk
    
    # --- 2. SATIR (Alttaki İki GIF/MP4) ---
    satir2_col1, satir2_col2 = st.columns([1, 1])
    
    with satir2_col1:
        st.video("dg_gif3.mp4", autoplay=True, loop=True, muted=True)
        
    with satir2_col2:
        st.video("dg_gifson.mp4", autoplay=True, loop=True, muted=True)
        
    st.write("---")
    
    # Final sürprizi için tatlı bir dokunuş
    st.info("Artık hediyeyi açma zamanıııı 🐧💞")