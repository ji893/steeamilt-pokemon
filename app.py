import streamlit as st

st.set_page_config(
page_title="안정호 포켓몬 도감",
page_icon="./images/monsterball.png"
)
st.title("streamlit 포켓몬 도감")

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

pokemons = [
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


example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}
auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
	...

pokemon = {
    "name": "누오",
    "types": ["물", "땅"],
    "image_url": "https://static.wikia.nocookie.net/pokemon/images/4/48/%EB%88%84%EC%98%A4_%EA%B3%B5%EC%8B%9D_%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8.png/revision/latest?cb=20170406075557&path-prefix=ko"
}



for i in range(0, len(pokemons), 3):
    row_pokemons = pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1 :
        name = st.text_input(label="포켓몬 이름")
    with col2:
        types = st.multiselect(
        label="포켓몬 속성",
        options=type_emoji_dict.keys(),
        max_selections=2
    )
    image_url = st.text_input(label="포켓몬 이미지 URL")
    submit = st.form_submit_button(label="Submit")
    if submit:
        pokemons.append(
            {
            "name": name,
            "types": types,
            "image_url": image_url if image_url else "./images/default.png"
            }
    )
        
initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://i.namu.wiki/i/R9GjiUEKY9snXwP9mqXDRsHkZ0yK5GVoJtFHEMCamYe5jd4FeIrcMMU6ZRuMnJ0Pckci7qhOhWhXLqqoRNfovfVysbJVtiO1J2aiwwlf6Xi-_KHpXCnkchch9GxvW5zVKf_5PeTtSQD5xm6yLrdMdw.webp",
    },
    ...
]

# session_state에 키 값 체크, 없으면 초기값 할당
if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons



    
    submit_button = st.form_submit_button(label="제출")

# 포켓몬 목록을 출력하는 코드
# for loop에서 pokemon 객체를 확인해봅니다
for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            
            # pokemon이 제대로 정의되었는지 확인
            if isinstance(pokemon, dict) and 'name' in pokemon:
                # f-string 안에서 pokemon의 'name'을 사용
                with st.expander(label=f"**{i+j+1}. {pokemon['name']}**", expanded=True):
                    st.image(pokemon["image_url"])
                    emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                    st.subheader(f"/".join(emoji_types))
                    
                    delete_button = st.button(label="삭제", key=f"delete_{i+j}", use_container_width=True)
                    if delete_button:
                        # print("삭제 버튼 누르셨네요.")
                        del st.session_state.pokemons[i+j]
                        st.rerun()



