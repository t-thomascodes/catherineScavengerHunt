import streamlit as st

# Set page config
st.set_page_config(page_title="Birthday Hunt", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
        background-image: url('https://static.vecteezy.com/system/resources/previews/017/719/340/non_2x/white-hearts-on-bright-pink-background-seamless-pattern-seamless-love-heart-design-background-seamless-pattern-on-valentine-s-day-the-seamless-texture-with-hart-vector.jpg');
        background-size: cover;
        background-repeat: repeat;
        background-attachment: fixed;
        color: #333333; /* Darker gray for better contrast */
    }
    .stApp {
        background-color: rgba(255, 230, 240, 0.9);
        backdrop-filter: blur(3px);
        max-width: 100%;
        margin: auto;
        padding: 1em;
    }
    .stButton>button {
        background-color: #ffb6c1;
        color: #333333;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.8em 1.5em;
        margin: 0.5em 0;
        width: 100%;
        display: block;
    }
    .stTextInput>div>div>input {
        background-color: white;
        color: #333333;
        border-radius: 5px;
        padding: 0.6em;
        font-size: 1.0em;
    }
    .stTextInput label {
        color: #333333;
        font-size: 1.3em;
    }
    .stMarkdown, .stCaption {
        color: #333333;
        font-size: 1.3em;
    }
    .stCaption {
        color: #333333 !important;
        font-style: italic;
        font-size: 1.2em !important;
    }
    /* Additional selectors to ensure hint text is dark */
    .stCaption *, div[data-testid="stCaption"], div[data-testid="stCaption"] * {
        color: #333333 !important;
    }
    .stAlert[data-testid="stAlert-success"] {
        background-color: #e0ffe0 !important;
        color: #0a4d0a !important;
        border: 2px solid #b3ffb3;
        font-size: 1.1em;
        font-weight: 500;
    }
    h1 {
        text-align: center;
        font-size: 2.5em !important;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 0
for i in range(9):  # Initialize state for each step
    if f"show_hint_{i}" not in st.session_state:
        st.session_state[f"show_hint_{i}"] = False
    if f"complete_step_{i}" not in st.session_state:
        st.session_state[f"complete_step_{i}"] = False

# Define steps
steps = [
    {
        "title": "Step #1",
        "content": "Happy Birthday, baby. I love you so much. I told you this weekend would be full of surprises — but today, you’ll have to uncover them yourself.",
        "input_prompt": "We are going to ______ Island. Think of where we spent almost an hour waiting for a butterfly to land on you.",
        "hint": "Hint: He was a president.",
        "answer": "roosevelt",
        "success_message": "Surprise! We’re going to Roosevelt Island — for a scavenger hunt. If you can solve all the clues, you’ll unlock a special surprise."
    },
    {
        "title": "Step #2",
        "content": "Think of where the nerds go. The place for people who would say 'Erm actually 🤓...'",
        "input_prompt": "Where do the nerds go? Take a picture at the place.",
        "hint": "Hint: At one of the Ivies.",
        "answer": "picture taken",
        "success_message": "Beautiful picture! On to the next challenge."
    },
    {
        "title": "Step #3",
        "content": "You taught me how to drive in the parking lot of a building that looked like this. What year was it opened to the public?",
        "input_prompt": "What year was the building opened to the public?",
        "hint": "Hint: Think of the building near your house — maybe right across the street.",
        "answer": "1856",
        "success_message": "You're killing it. Next stop!"
    },
    {
        "title": "Step #4",
        "content": "I used to be trapped by this feeling. But every time I talk to you, you give me freedom from ______.",
        "input_prompt": "What feeling do I give you freedom from?",
        "hint": "Hint: Roosevelt talked about this — and it might be carved on a rock in the South.",
        "answer": "fear",
        "success_message": "Beautiful. You bring freedom just by being you. Let's keep going."
    },
    {
        "title": "Step #5",
        "content": "Time to get something that refreshes you and glows you up. Where do we get this?",
        "input_prompt": "Where do we get something that refreshes you?",
        "hint": "Hint: Come onnnn... you know this.",
        "answer": "starbucks",
        "success_message": "Drink secured. Glow initiated."
    },
    {
        "title": "Step #6",
        "content": "We’ve got the blanket... but we’re missing something. Go buy food at the Roosevelt Island Farmers Market.",
        "button": "Food Bought",
        "success_message": "Snacks secured."
    },
    {
        "title": "Step #7",
        "content": "If your emoji were a shape, what would it be?",
        "input_prompt": "What shape would your emoji be?",
        "hint": "Hint: Think of tentacles.",
        "answer": "octagon",
        "success_message": "Eight sides, infinite charm. Next!"
    },
    {
        "title": "Step #8",
        "content": "To end this journey, let’s go somewhere we haven’t been before. You represent this to me — guiding me through rough tides. What symbol is this?",
        "input_prompt": "What symbol guides through rough tides?",
        "hint": "Hint: We couldn’t go here in New Hampshire... remember? It was closed.",
        "answer": "lighthouse",
        "success_message": "You made it — just like you always do."
    },
    {
        "title": "Final Message 💌",
        "content": "I love you so much, baby. Every step of this was a little reflection of how deeply I care about you. You’re my light, my calm, my best friend — and this day wouldn’t be complete without reminding you that loving you is the best adventure I’ve ever had.",
        "button": "Restart"
    }
]

def next_page():
    st.session_state.page += 1

def reveal_hint(step_idx):
    st.session_state[f"show_hint_{step_idx}"] = True

# Render the current step
current = st.session_state.page

# Step 0
if current == 0:
    step = steps[0]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_0").strip().lower()
    if st.button("Submit", key="submit_0"):
        if user_input == step["answer"]:
            st.session_state.complete_step_0 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_0"):
        reveal_hint(0)
    if st.session_state.show_hint_0:
        st.caption(step["hint"])
    if st.session_state.complete_step_0:
        st.button("Next", key="next_0", on_click=next_page)

# Step 1
elif current == 1:
    step = steps[1]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_1").strip().lower()
    if st.button("Submit", key="submit_1"):
        if user_input == step["answer"]:
            st.session_state.complete_step_1 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_1"):
        reveal_hint(1)
    if st.session_state.show_hint_1:
        st.caption(step["hint"])
    if st.session_state.complete_step_1:
        st.button("Next", key="next_1", on_click=next_page)

# Step 2
elif current == 2:
    step = steps[2]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_2").strip().lower()
    if st.button("Submit", key="submit_2"):
        if user_input == step["answer"]:
            st.session_state.complete_step_2 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_2"):
        reveal_hint(2)
    if st.session_state.show_hint_2:
        st.caption(step["hint"])
    if st.session_state.complete_step_2:
        st.button("Next", key="next_2", on_click=next_page)

# Step 3
elif current == 3:
    step = steps[3]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_3").strip().lower()
    if st.button("Submit", key="submit_3"):
        if user_input == step["answer"]:
            st.session_state.complete_step_3 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_3"):
        reveal_hint(3)
    if st.session_state.show_hint_3:
        st.caption(step["hint"])
    if st.session_state.complete_step_3:
        st.button("Next", key="next_3", on_click=next_page)

# Step 4
elif current == 4:
    step = steps[4]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_4").strip().lower()
    if st.button("Submit", key="submit_4"):
        if user_input == step["answer"]:
            st.session_state.complete_step_4 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_4"):
        reveal_hint(4)
    if st.session_state.show_hint_4:
        st.caption(step["hint"])
    if st.session_state.complete_step_4:
        st.button("Next", key="next_4", on_click=next_page)

# Step 5
elif current == 5:
    step = steps[5]
    st.title(step["title"])
    st.markdown(step["content"])
    if st.button(step["button"], key="button_5"):
        st.session_state.complete_step_5 = True
        st.success(step["success_message"])
        next_page()

# Step 6
elif current == 6:
    step = steps[6]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_6").strip().lower()
    if st.button("Submit", key="submit_6"):
        if user_input == step["answer"]:
            st.session_state.complete_step_6 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_6"):
        reveal_hint(6)
    if st.session_state.show_hint_6:
        st.caption(step["hint"])
    if st.session_state.complete_step_6:
        st.button("Next", key="next_6", on_click=next_page)

# Step 7
elif current == 7:
    step = steps[7]
    st.title(step["title"])
    st.markdown(step["content"])
    user_input = st.text_input(step["input_prompt"], key="input_7").strip().lower()
    if st.button("Submit", key="submit_7"):
        if user_input == step["answer"]:
            st.session_state.complete_step_7 = True
            st.success(step["success_message"])
        else:
            st.warning("Hmm... that doesn't seem quite right. Try again or get a hint.")
    if st.button("Show Hint", key="hint_7"):
        reveal_hint(7)
    if st.session_state.show_hint_7:
        st.caption(step["hint"])
    if st.session_state.complete_step_7:
        st.button("Next", key="next_7", on_click=next_page)

# Step 8 (Final Message)
elif current == 8:
    step = steps[8]
    st.title(step["title"])
    st.markdown(step["content"])
    if st.button(step["button"], key="restart_8"):
        st.session_state.page = 0
        for i in range(9):
            st.session_state[f"show_hint_{i}"] = False
            st.session_state[f"complete_step_{i}"] = False