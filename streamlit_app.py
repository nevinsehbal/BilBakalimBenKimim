import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- Sayfa Ayarları ---
st.set_page_config(page_title="Bil Bakalım Ben Kimim", layout="wide")

# --- Otomatik Yenileme (her 1 sn) ---
st_autorefresh(interval=1000, key="auto_refresh")

items = [
    # --- Meyveler (50) ---
    "Elma", "Armut", "Şeftali", "Muz", "Çilek", "Ahududu", "Böğürtlen", "Kiraz", "Vişne", "Üzüm",
    "Nar", "Portakal", "Mandalina", "Limon", "Greyfurt", "Kavun", "Karpuz", "Avokado", "Hindistan Cevizi", "Ananas",
    "Mango", "Papaya", "Kivi", "Guava", "Kestane", "Fındık", "Mürdüm Erik", "Ayva", "Hurma", "Kumkuat",
    "Bergamot", "İncir", "Karpuz Çekirdeksiz", "Açai", "Goji", "Akdarı", "Yaban Mersini", "Kızılcık", "Goyavi", "Carambola",
    "Lime", "Frambuaz", "Tamarillo", "Yaban Üzümü", "Kahvaltılık Kiraz", "Kavun Tatlısı", "Zeytin", "Zencefil", "Anason", "Karanfil",

    # --- Sebzeler (50) ---
    "Domates", "Salatalık", "Biber", "Patlıcan", "Kabak", "Havuç", "Soğan", "Sarımsak", "Pırasa", "Lahana",
    "Brokoli", "Karnabahar", "Brüksel Lahanası", "Ispanak", "Roka", "Marul", "Kara Lahana", "Kereviz", "Turp", "Pancar",
    "Patates", "Şalgam", "Bamya", "Bezelye", "Mısır", "Fasulye", "Nohut", "Mercimek", "Bakla", "Enginar",
    "Kuşkonmaz", "Yer Elması", "Ayçiçeği Çekirdeği", "Soya Fasulyesi", "Şeker Pancarı", "Kereviz Sapı", "Biberiye", "Maydanoz", "Dereotu", "Nane",
    "Kişniş", "Kekik", "Adaçayı", "Fesleğen", "Kereviz Yaprağı", "Salata Marulu", "Kavun Kabuğu", "Turp Yaprağı", "Mantar", "Kuşkonmaz Sapı",

    # --- Hayvanlar (50) ---
    "Kedi", "Köpek", "At", "İnek", "Koyun", "Keçi", "Tavuk", "Horoz", "Ördek", "Kaz",
    "Hindi", "Güvercin", "Martı", "Penguen", "Balina", "Köpekbalığı", "Ahtapot", "Yunus", "Kaplumbağa", "Yılan",
    "Kartal", "Şahin", "Baykuş", "Tavşan", "Sincap", "Sıçan", "Geyik", "Turna", "Somon", "Alabalık",
    "Karides", "Istakoz", "Midye", "Kurbağa", "Semender", "Bukalemun", "Kertenkele", "Fil", "Aslan", "Kaplan",
    "Panter", "Leopar", "Jaguar", "Gergedan", "Zürafa", "Fil", "Panda", "Rakoon", "Sansar", "Vaşak",

    # --- Aletler ve Eşyalar (50) ---
    "Çekiç", "Tornavida", "Matkap", "Testere", "Maket Bıçağı", "Pense", "Kerpeten", "Anahtar", "İngiliz Anahtarı", "Lokma Takımı",
    "Allen Anahtarı", "Dremel", "Zımpara Makinesi", "Taşlama Makinesi", "Kürek", "Balyoz", "Rende", "Makas", "Kablo Soyucu", "Kumpas",
    "Cetvel", "Kelepçe", "Zımba", "Zımba Teli", "Ataç", "Dosya", "Defter", "Ajanda", "Post-It", "Hesap Makinesi",
    "Yazıcı", "Klavye", "Mouse", "Ekran", "Hoparlör", "Kulaklık", "Mikrofon", "Kamera", "Tripod", "Drone",
    "Sandaly e", "Masa", "Dolap", "Kitaplık", "Sehpa", "Koltuk", "Yatak", "Şilte", "Yastık", "Battaniye",

    # --- Ünlüler (100) ---
    "Tarkan", "Ajda Pekkan", "Sezen Aksu", "Cem Yılmaz", "Şener Şen", "Haluk Bilginer", "Beren Saat", "Kenan İmirzalioğlu", "Kıvanç Tatlıtuğ", "Fahriye Evcen",
    "Mehmet Günsür", "Nusret Gökçe", "Gülse Birsel", "Kenan Doğulu", "Sıla Gençoğlu", "Demet Akalın", "Hülya Avşar", "Acun Ilıcalı", "Yılmaz Erdoğan", "Murat Boz",
    "Hadise", "Ebru Gündeş", "Merve Boluğur", "Tolga Çevik", "Şahin Irmak", "Serenay Sarıkaya", "Cansu Dere", "Engin Akyürek", "Burak Özçivit", "Çağatay Ulusoy",
    "Demet Özdemir", "Hazal Kaya", "Bensu Soral", "Elçin Sangu", "Aslı Enver", "Kenan İmirzan", "Mahsun Kırmızıgül", "Tuba Büyüküstün", "Kadir İnanır", "Hakan Altıntop",
    "Kıvanç Tatlıtuğ", "Beren Gökyıldız", "Aleyna Tilki", "Hande Erçel", "Ezgi Mola", "Hazar Ergüçlü", "Melisa Sözen", "Murat Yıldırım", "Sarp Apak", "Nazan Kesal",
    "Levent Üzümcü", "Zafer Algöz", "Cansu Tosun", "Alperen Duymaz", "Murat Cemcir", "Cemre Baysel", "Özge Yağız", "Ediz Hun", "Selçuk Yöntem", "Fikret Kuşkan",
    "Okan Bayülgen", "Mehmet Aslantuğ", "Cenk Ertan", "Suat Sungur", "Müjde Ar", "Pelin Karahan", "Ebru Şahin", "Gizem Karaca", "Sıla Türkoğlu", "Kerem Bürsin",
    "Serkan Çayoğlu", "Burak Dakak", "Ayça Bingöl", "Nihan Akdoğan", "Begüm Birgören", "Merve Çağıran", "Nilay Duru", "Hatice Şendil", "Selin Şekerci", "Seda Bakan",
    "Aslıhan Gürbüz", "Ceyda Düvenci", "Melisa Döngel", "Hazal Filiz Küçükköse", "Miray Daner", "Alina Boz", "Gizem Emre", "Burcu Özberk", "Alp Navruz", "Selen Öztürk",

    # --- Günlük Eşyalar & Nesneler (100) ---
    "Telefon", "Bilgisayar", "Televizyon", "Radyo", "Saat", "Ayna", "Çanta", "Cüzdan", "Şemsiye", "Yağmurluk",
    "Mont", "Kazak", "Tişört", "Pantolon", "Etek", "Elbise", "Ayakkabı", "Sandalet", "Çorap", "Terlik",
    "Şapka", "Bere", "Eldiven", "Gözlük", "Güneş Gözlüğü", "Kol Saati", "Bileklik", "Kolye", "Küpe", "Yüzük",
    "Anahtar", "Anahtarlık", "Bavul", "Sırt Çantası", "Seyahat Çantası", "Saat Kordonu", "Film Kamerası", "GPS", "Dijital Fotoğraf Makinesi", "Projeksiyon",
    "Mutfak Robotu", "Buzdolabı", "Çamaşır Makinesi", "Bulaşık Makinesi", "Fırın", "Ocak", "Mikrodalga Fırın", "Tost Makinesi", "Fritöz", "Kahve Makinesi",
    "Çay Makinesi", "Su Isıtıcı", "Blender", "Mikser", "Tencere", "Tava", "Çatal", "Bıçak", "Kaşık", "Tabak",
    "Bardak", "Fincan", "Kesme Tahtası", "Rende", "Şişe Açacağı", "Makarna Süzgeci", "Sebze Soyacağı", "Süzgeç", "Damak Kaşığı", "Termos",
    "Mutfak Ölçü Kabı", "Kağıt Havlu", "Peçete Tutacağı", "Çöp Kovası", "Süpürge", "Paspas", "Elektrikli Süpürge", "Firçalayıcı", "Temizlik Bezi", "Deterjan",
    "Sabunluk", "Diş Fırçası", "Diş Macunu", "Havlu", "Banyo Dolabı", "Tuvalet Kağıdı", "Çamaşır Sepeti", "Dijital Terazi", "Küvet", "Duş Perdesi",

    # --- Taşıtlar (50) ---
    "Araba", "Bisiklet", "Motosiklet", "Otobüs", "Kamyon", "Kamyonet", "Minibüs", "Metro", "Tren", "Tramvay",
    "Uçak", "Helikopter", "Gemi", "Feribot", "Yelkenli", "Kano", "Deniz Motoru", "Jetski", "Kayık", "Römork",
    "Karavan", "Pikap", "Elektrikli Scooter", "Hoverboard", "Segway", "Skuter", "Traktör", "Zırhlı Araç", "Tank", "İtfaiye Aracı",
    "Ambulans", "Polis Aracı", "At Arabası", "Spor Araba", "SUV", "Hatchback", "Sedan", "Cabrio", "Roadster", "Kargo Uçağı",
    "Heliport", "Yolcu Gemisi", "Balon", "Paraşüt", "Jet Uçağı", "Hidroplan", "Limuzin", "Monoray", "Funtoş", "Drift Arabası",

    # --- Meslekler (50) ---
    "Avukat", "Doktor", "Hemşire", "Öğretmen", "Mühendis", "Mimar", "Muhasebeci", "Polis Memuru", "İtfaiyeci", "Pilot",
    "Hostes", "Garson", "Pastacı", "Aşçı", "Kasiyer", "Market Müdürü", "Barista", "Bartender", "Taksici", "Şoför",
    "Fotografçı", "Gazeteci", "Editör", "Yazılım Geliştirici", "Veri Analisti", "Proje Yöneticisi", "Pazarlama Uzmanı", "Satış Temsilcisi", "Danışman", "Psikolog",
    "Psikiyatrist", "Fizyoterapist", "Eczacı", "Veteriner", "Di̇ş Hekimi", "Fizikçi", "Kimyager", "Biyolog", "Matematikçi", "Arkeolog",
    "Tarihçi", "Sosyolog", "Antropolog", "Çevirmen", "Tercüman", "Çiftçi", "Bahçıvan", "Bahçıvan Yardımcısı", "Elektrikçi", "Sıvacı",

    # --- Mobilya (50) ---
    "Yatak", "Başlık", "Gardırop", "Şifonyer", "Komodin", "Çalışma Masası", "Kitap Rafı", "Büro Sandalyesi", "TV Ünitesi", "Kitaplık",
    "Yemek Masası", "Sandalye", "Bar Taburesi", "Puf", "Kanepe", "Kolçaklı Koltuk", "Berjer", "Oturma Grubu", "Kanepe Takımı", "Zigon Sehpa",
    "Orta Sehpa", "Konsol", "Portmanto", "Ayakkabılık", "Depolama Ünitesi", "Çok Amaçlı Dolap", "Bebek Beşiği", "Çocuk Masası", "Çocuk Sandalyesi", "Oyun Alanı Üniteli Dolap",
    "Bahçe Mobilyası", "Şezlong", "Masa Sandalye Takımı", "TV Sehpası", "Kitap Okuma Koltuğu", "Yüz Bakım Masası", "Makyaj Masası", "Ayakkabı Dolabı", "Portmanto Askısı", "Bebek Arabası",
    "Çamaşır Sepeti", "Malzeme Dolabı", "Dosya Dolabı", "Raf Ünitesi", "Çok Katlı Kitaplık", "Katlanır Masa", "Katlanır Sandalye", "Bar Masası", "Ofis Dolabı", "Köşe Koltuk",

    # --- Bitkiler & Çiçekler (50) ---
    "Gül", "Lale", "Orkide", "Karanfil", "Ayçiçeği", "Nergis", "Menekşe", "Begonya", "Sümbül", "Saksı Çiçeği",
    "Frezya", "Kasımpatı", "Zambak", "Şakayık", "Cam Gülü", "Yasemin", "Hanımeli", "Lavanta", "Biberiye", "Adaçayı",
    "Menekşe Otu", "Sardunya", "Petunya", "Kedi Otu", "Sarı Kantaron", "Çarkıfelek", "Antoryum", "Kaktüs", "Aloe Vera", "Paşa Kılıcı",
    "Kum Zambağı", "Kaz Ayağı", "Çin Şemsiyesi", "Barış Çiçeği", "Kamelya", "Fil Kulağı", "Philodendron", "Alyum", "Kasımpatı Türleri", "Kalp Çiçeği",
    "Guatro", "Dracaena", "Ficus", "Areka Palmiyesi", "Monstera", "Zamioculcas", "Maranta", "Begonya Türleri", "Hoya", "Tradescantia",

    # --- Spor Ekipmanları (50) ---
    "Futbol Topu", "Basketbol Topu", "Voleybol", "Tenis Raketi", "Tenis Topu", "Golf Sopası", "Golf Topu", "Beyzbol Sopası", "Beyzbol Topu", "Hentbol Topu",
    "Kricket Sopası", "Masa Tenisi Raketi", "Masa Tenisi Topu", "Beyzbol Eldiveni", "Boks Eldiveni", "Muay Thai Eldiveni", "Boks Torbası", "Ambalaj Eldiveni", "Kick Boks Torbası", "Atletizm Çivisi",
    "Koşu Bandı", "Ağırlık Sehpası", "Dambıl", "Halter", "Bar", "Plaka", "Squat Rafı", "Yoga Matı", "Pilates Topu", "Direnç Bandı",
    "Jimnastik Halteri", "Kondisyon Bisikleti", "Kürek Makinesi", "Step Tahtası", "Zıplama İpi", "Boks Çemberi", "Masa Tenisi Masası", "Bilardo Masası", "Futbol Kalesi", "Skateboard",
    "Kaykay", "Patinaj Paten", "Bisiklet Kaskı", "Koruyucu Dizlik", "Koruyucu Dirseklik", "Kayak Takımı", "Snowboard", "Sörf Tahtası", "Dalış Ekipmanı", "Yelken Takımı",

    # --- Müzik Aletleri (50) ---
    "Keman", "Violin", "Çello", "Kontrbas", "Gitar", "Bas Gitar", "Ukulele", "Mandolin", "Sitar", "Lute",
    "Bağlama", "Ud", "Kanun", "Santur", "Ney", "Kaval", "Fagot", "Klarnet", "Obua", "Flüt",
    "Trompet", "Trombon", "Korno", "Tuba", "Saksafon", "Duduk", "Mızıka", "Akordeon", "Piyano", "Elektrikli Klavye",
    "Djembe", "Davul", "Bongo", "Kese Davulu", "Timpani", "Tamburin", "Marakas", "Ziller", "Cajon", "Triangle",
    "Xilofon", "Marimba", "Vibrafon", "Glockenspiel", "Tabla", "Hang Drum", "Didgeridoo", "Theremin", "Harmonik", "Melodika",

    # --- Renkler (50) ---
    "Kırmızı", "Mavi", "Yeşil", "Sarı", "Turuncu", "Mor", "Pembe", "Beyaz", "Siyah", "Gri",
    "Kahverengi", "Bej", "Lacivert", "Mint Yeşili", "Turkuaz", "Zeytin Yeşili", "Bordo", "Lila", "Şeftali", "Krem",
    "Açık Mavi", "Açık Yeşil", "Kömür Karası", "Kirli Beyaz", "Sağlık Yeşili", "Deniz Mavisi", "Koral", "Mercan", "Lavanta", "Fıstık Yeşili",
    "Hardal Sarısı", "Çikolata Kahvesi", "Kahve Altı", "Gül Kurusu", "Pas Kırmızısı", "İnci Beyazı", "Antrasit", "Camgöbeği", "Kül Grisi", "Süt Beyazı",
    "Söğüt Yeşili", "Fildişi", "Kabak Çekirdeği Yeşili", "Kar Çiçeği Beyazı", "İnci Mavisi", "Gri Yeşil", "Saman Sarısı", "Kum Rengi", "Yosun Yeşili", "Gri Mavi",


        # --- Yabancı Ünlüler (150) ---
    # Aktör/Aktris (75)
    "Leonardo DiCaprio", "Brad Pitt", "Tom Hanks", "Johnny Depp", "Robert Downey Jr.", "Chris Hemsworth",
    "Chris Evans", "Will Smith", "Matt Damon", "George Clooney", "Tom Cruise", "Harrison Ford",
    "Leonardo DiCaprio", "Mark Wahlberg", "Christian Bale", "Ryan Gosling", "Ryan Reynolds", "Hugh Jackman",
    "Jake Gyllenhaal", "Tom Hardy", "Benedict Cumberbatch", "Denzel Washington", "Morgan Freeman",
    "Samuel L. Jackson", "Robert De Niro", "Al Pacino", "Jack Nicholson", "Anthony Hopkins",
    "Michael Caine", "Ian McKellen", "Jude Law", "Eddie Redmayne", "Daniel Craig", "Pierce Brosnan",
    "Jeremy Renner", "Channing Tatum", "Matthew McConaughey", "Robert Pattinson", "Christian Slater",
    "Colin Farrell", "Russell Crowe", "Nicolas Cage", "James McAvoy", "Adrien Brody", "Keanu Reeves",
    "Ryan Phillippe", "Val Kilmer", "Kurt Russell", "Sylvester Stallone", "Arnold Schwarzenegger",
    "Jason Statham", "Vin Diesel", "Dwayne Johnson", "Idris Elba", "Ben Affleck", "Zac Efron",
    "Heath Ledger", "Joaquin Phoenix", "Michael Fassbender", "Cillian Murphy", "Tom Selleck",
    "Owen Wilson", "Edward Norton", "James Franco", "Donald Sutherland", "Christopher Walken",
    "Samuel L. Jackson", "Russell Crowe", "Clint Eastwood", "Jeff Bridges", "John Travolta", "Mel Gibson",
    "Steve Carell", "Bill Murray", "Jim Carrey",

    # Şarkıcı/Müzisyen (75)
    "Beyoncé", "Madonna", "Taylor Swift", "Ariana Grande", "Lady Gaga", "Rihanna", "Katy Perry",
    "Billie Eilish", "Dua Lipa", "Adele", "Bruno Mars", "Justin Timberlake", "Justin Bieber", "Ed Sheeran",
    "Shawn Mendes", "Harry Styles", "Sam Smith", "The Weeknd", "Drake", "Nicki Minaj", "Cardi B",
    "Eminem", "Jay-Z", "Kanye West", "Kendrick Lamar", "Post Malone", "Coldplay", "Maroon 5",
    "Imagine Dragons", "OneRepublic", "Linkin Park", "Green Day", "U2", "Queen", "The Beatles",
    "Elton John", "Michael Jackson", "Prince", "Whitney Houston", "Celine Dion", "Mariah Carey",
    "Bruce Springsteen", "Bob Dylan", "Neil Young", "Bon Jovi", "Aerosmith", "AC/DC", "Metallica",
    "Guns N' Roses", "Red Hot Chili Peppers", "The Rolling Stones", "Pink Floyd", "Led Zeppelin",
    "Nirvana", "Pearl Jam", "The Killers", "Muse", "Coldplay", "R.E.M.", "U2", "Eagles", "Fleetwood Mac",
    "Kendrick Lamar", "Sia", "Lorde", "Miley Cyrus", "Selena Gomez", "Bruno Mars", "John Legend",
    "Sam Smith", "Zayn Malik", "Jason Derulo", "Calvin Harris", "David Guetta", "Marshmello", "Avicii",
    "Tiësto", "Armin van Buuren", "Martin Garrix", "The Chainsmokers", "Macklemore",

    # --- Sporcular (100) ---
    # Futbol (50)
    "Lionel Messi", "Cristiano Ronaldo", "Neymar Jr.", "Kylian Mbappé", "Mohamed Salah", "Kevin De Bruyne",
    "Robert Lewandowski", "Virgil van Dijk", "Sergio Ramos", "Luka Modrić", "Eden Hazard", "Harry Kane",
    "Erling Haaland", "Karim Benzema", "Sadio Mané", "Raheem Sterling", "Luis Suárez", "Zlatan Ibrahimović",
    "Paul Pogba", "Toni Kroos", "Sergio Agüero", "Antoine Griezmann", "Romelu Lukaku", "Romário",
    "Ronaldo Nazário", "Ronaldinho", "Diego Maradona", "Pelé", "Johan Cruyff", "Marco van Basten",
    "Fransesco Totti", "Andrés Iniesta", "Xavi Hernández", "Gianluigi Buffon", "Manuel Neuer",
    "David Beckham", "Frank Lampard", "Steven Gerrard", "Patrick Vieira", "Clarence Seedorf",
    "Iker Casillas", "Gerd Müller", "Miroslav Klose", "Zinedine Zidane", "Thierry Henry",
    "Gareth Bale", "Raúl González", "Fernando Torres",

    # Basketbol (25)
    "Michael Jordan", "LeBron James", "Kobe Bryant", "Shaquille O'Neal", "Magic Johnson", "Larry Bird",
    "Tim Duncan", "Kevin Durant", "Stephen Curry", "James Harden", "Giannis Antetokounmpo",
    "Kawhi Leonard", "Chris Paul", "Russell Westbrook", "Dirk Nowitzki", "Dwyane Wade", "Carmelo Anthony",
    "Allen Iverson", "Charles Barkley", "Hakeem Olajuwon", "Kevin Garnett", "Anthony Davis",
    "Steve Nash", "Paul Pierce", "Vince Carter",

    # Tenis (10)
    "Roger Federer", "Rafael Nadal", "Novak Djokovic", "Serena Williams", "Venus Williams",
    "Andy Murray", "Pete Sampras", "Andre Agassi", "Björn Borg", "Steffi Graf",

    # Diğer Sporlar (15)
    "Usain Bolt", "Michael Phelps", "Simone Biles", "Lewis Hamilton", "Valentino Rossi",
    "Lionel Messi", "Cristiano Ronaldo", "Max Verstappen", "Conor McGregor", "LeBron James",
    "Tom Brady", "Tiger Woods", "Lewis Hamilton", "Novak Djokovic", "Michael Phelps",

    # --- Ünlü Türk Yemekleri (150) ---
    "Döner", "İskender", "Mantı", "Kebap", "Adana Kebap", "Urfa Kebap", "Çöp Şiş", "Şiş Kebap", "Ali Nazik",
    "Testi Kebap", "Lahmacun", "Pide", "Kuşbaşılı Pide", "Kıymalı Pide", "Peynirli Pide", "Sucuklu Pide",
    "Kıymalı Börek", "Su Böreği", "Sigara Böreği", "Gül Böreği", "Paçanga Böreği", "Çiğ Börek",
    "Gözleme", "Katmer", "Künefe", "Baklava", "Kadayıf", "Tulumba", "Sütlaç", "Kazandibi",
    "Keşkül", "Aşure", "Muhallebi", "Tavuklu Pilav", "Etli Pilav", "Nohutlu Pilav", "Zeytinyağlı Yaprak Sarma",
    "Enginar Dolması", "Biber Dolması", "Kabak Dolması", "Kestane Şekeri", "Cevizli Reçel",
    "Acuka", "Humus", "Ezme", "Haydari", "Muhammara", "Tarator", "Çırpılmış Yoğurt",
    "Patlıcan Salatası", "Köz Patlıcan", "Şakşuka", "Atom", "Mücver", "İmam Bayıldı",
    "Kuzu Tandır", "Kuzu İncik", "Beğendi", "Hünkar Beğendi", "Karnıyarık", "İçli Köfte",
    "Sarma Köfte", "Çiğ Köfte", "Dalyan Köfte", "Kabak Mücveri", "Simit", "Pişi",
    "Lahmacun Dürüm", "Tost", "Balık Ekmek", "Midye Dolma", "Midye Tava",
    "Kokoreç", "Yaprak Döner", "Çevirme", "Tantuni", "Adana Usulü Tantuni", "Kilis Tavalısı",
    "Patlıcan Kebabı", "Soslu Patates", "Haydar Otlu Pidesi", "Bursa İskenderi", "Edirne Tava Ciğeri",
    "Antep Fıstıklı Baklava", "Şanlıurfa Çiğköfte", "Maraş Dondurması", "Van Kahvaltısı",
    "Karadeniz Pidesi", "Lahmacun İskender", "Tokat Kebabı", "Mantı Evi Mantısı", "Çorum Leblebisi",
    "İnegöl Köfte", "İzmir Boyoz", "Bülbül Yuvası", "Paça Çorbası", "Analı Kızlı Çorba",
    "Kelle Paça", "Yayla Çorbası", "Domates Çorbası", "Mercimek Çorbası", "Tavuk Çorbası",
    "Ezogelin Çorbası", "Düğün Çorbası", "Tarhana Çorbası", "Yayla Çorbası", "Tırnaklı Çorba",
    "Yoğurt Çorbası", "İşkembe Çorbası", "Terbiyeli Çorba", "Keşkek", "Höşmerim",
    "İçli Köfte Çeşitleri", "Karalahana Çorbası", "Bulgur Pilavı", "Şehriyeli Pilav", "Mısır Ekmeği",
    "Akıtma", "Gözleme Çeşitleri", "Çiğdem", "Kıtır", "Çekme Helva", "Un Helvası", "İrmik Helvası",
    "Semsek", "Şeker Pancarı Turşusu", "Lahana Turşusu", "Salatalık Turşusu", "Kanlıca Yoğurdu",
    "Kaymaklı Ekmek Kadayıfı", "Muhlama", "Kuymak", "Hamsi Tava", "Hamsi Buğulama",
    "Karalahana Sarması", "But Yemeği", "Güveç", "Kabak Çiçeği Dolması", "Alinazik"
]

# --- Session State ---
if "current_item" not in st.session_state:
    st.session_state.current_item = random.choice(items)

if "game_running" not in st.session_state:
    st.session_state.game_running = False

if "time_limit" not in st.session_state:
    st.session_state.time_limit = 60  # Varsayılan süre

if "timer_start" not in st.session_state:
    st.session_state.timer_start = None

if "timeout" not in st.session_state:
    st.session_state.timeout = False

# --- Süre Ayarı ---
col_time1, col_time2, col_time3 = st.columns([1, 2, 1])
with col_time1:
    if st.button("-10 sn") and st.session_state.time_limit > 30:
        st.session_state.time_limit -= 10
with col_time2:
    st.markdown(
        f"<div style='text-align:center; font-size:40px;'>{st.session_state.time_limit} sn</div>",
        unsafe_allow_html=True
    )
with col_time3:
    if st.button("+10 sn") and st.session_state.time_limit < 180:
        st.session_state.time_limit += 10

# --- Fonksiyonlar ---
def shuffle_item():
    st.session_state.current_item = random.choice(items)

def start_game():
    st.session_state.game_running = True
    st.session_state.timer_start = time.time()
    st.session_state.timeout = False
    shuffle_item()

# --- Butonlar ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("▶ Oyna", use_container_width=True):
        start_game()
with col2:
    if st.button("🔀 Karıştır", use_container_width=True):
        shuffle_item()

# --- Timer Hesaplama ---
if st.session_state.game_running:
    elapsed = time.time() - st.session_state.timer_start
    time_left = st.session_state.time_limit - int(elapsed)

    if time_left <= 0:
        st.session_state.game_running = False
        st.session_state.timeout = True
    else:
        st.markdown(
            f"<div style='text-align:center; font-size:30px;'>Kalan süre: {time_left} sn</div>",
            unsafe_allow_html=True
        )

# --- Ekran ---
if st.session_state.timeout:
    st.markdown(
        """
        <div style="background-color:red; height:400px; display:flex; justify-content:center; align-items:center; font-size:80px; font-weight:bold; color:white;">
            SÜRE BİTTİ!
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        f"""
        <div style="text-align:center; font-size:80px; font-weight:bold; margin-top:50px;">
            {st.session_state.current_item}
        </div>
        """,
        unsafe_allow_html=True
    )
