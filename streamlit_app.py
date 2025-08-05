import streamlit as st
import random
import time
from streamlit_autorefresh import st_autorefresh

# --- Sayfa Ayarları ---
st.set_page_config(page_title="Bil Bakalım Ben Kimim", layout="wide")

# --- Otomatik Yenileme (her 1 sn) ---
st_autorefresh(interval=1000, key="auto_refresh")

# --- Veri Listesi ---
items = [
    "Elma", "Armut", "Çekiç", "Tavuk", "Kedi", "Köpek", "At", "Tornavida", "Kalem", "Defter",
    "Karpuz", "Aslan", "Kaplan", "Ayı", "Fare", "Gitar", "Piyano", "Televizyon", "Telefon", "Bilgisayar",
    "Haluk Bilginer", "Ajda Pekkan", "Tarkan", "Cem Yılmaz", "Nusret", "Simit", "Menemen", "Klavye", "Fare (Mouse)"
    # Buraya 1000+ öğelik liste eklenebilir
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
