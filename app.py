import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="안정호 포켓몬 도감",
    page_icon="./images/monsterball.png"
)
st.title("🐾 Streamlit 포켓몬 도감")

# 타입 이모지 매핑
type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

# 초기 포켓몬 리스트
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

# session_state에 pokemons 없으면 초기화
if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons.copy()

# ✅ 예시 데이터 추가 버튼
example = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}
if st.toggle("예시 포켓몬 추가 (알로라 디그다)"):
    if all(p["name"] != example["name"] for p in st.session_state.pokemons):
        st.session_state.pokemons.append(example)
        st.success("알로라 디그다가 추가되었습니다!")
        st.rerun()
    else:
        st.info("알로라 디그다는 이미 추가되어 있습니다.")

# 🔽 포켓몬 추가 폼
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름")
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=type_emoji_dict.keys(),
        )
    image_url = st.text_input(label="포켓몬 이미지 URL")
    submit = st.form_submit_button(label="등록")

    if submit:
        if not name or not types:
            st.warning("이름과 속성은 필수 항목입니다.")
        else:
            st.session_state.pokemons.append(
                {
                    "name": name,
                    "types": types,
                    "image_url": image_url if image_url else "./images/default.png"
                }
            )
            st.success(f"{name} 이(가) 추가되었습니다!")
            st.rerun()

# 📋 포켓몬 목록 출력
st.subheader("등록된 포켓몬 목록")
for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[t]} {t}" for t in pokemon["types"]]
                st.subheader(" / ".join(emoji_types))

                if st.button("❌ 삭제", key=f"delete_{i+j}", use_container_width=True):
                    del st.session_state.pokemons[i + j]
                    st.rerun()
