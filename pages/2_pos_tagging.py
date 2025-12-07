"""
POS Tagging - Demo and Educational Content
Display-only examples of POS tagging without user interaction
"""

import streamlit as st
import pandas as pd

# ===== PAGE CONFIGURATION =====
# Set up the Streamlit page with title and layout settings
st.set_page_config(page_title="POS Tagging", layout="wide", initial_sidebar_state="collapsed")

# ===== LOAD EXTERNAL CSS =====
# Load custom CSS styles from styles.css file to style the application
with open("styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# ===== HEADER SECTION =====
# Display the main title and subtitle with custom styling
st.markdown("# 📝 POS Tagging – HMM & Viterbi", unsafe_allow_html=True)
st.markdown(
    "<p style='color: #ffa300; font-family: Space Mono; font-size: 1.2rem;'>Grammatical Labeling with Intelligence</p>",
    unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ===== CONCEPT EXPLANATION SECTION =====
# Display information about what POS tagging is
st.markdown("## 🎯 What is POS Tagging?")
st.markdown("""
<div class='concept-box'>
    <div class='concept-title'>The Basic Idea</div>
    <p>
    POS (Part-of-Speech) tagging assigns <span class='highlight'>grammatical labels</span> to each word in a sentence. 
    Is "bank" a noun (riverbank) or a verb (to bank money)? Context matters!
    </p>
</div>
""", unsafe_allow_html=True)

# ===== POS TAGGING EXPLAINED SECTION =====
st.markdown("## 📚 Understanding POS Tags")
st.markdown("""
**Part-of-Speech (POS) tags** are labels that identify the grammatical role of each word in a sentence.

### The Three POS Categories in This Project:
*  You can even do it by yourself, I have created user interaction. scroll to the end and click on 'interactive Tagging' or from menu click 'user POS Tagging' *
1. **Noun (N)** 🟢 - Words that represent people, places, things, or ideas
   - Examples: *dog, city, happiness, Deval*

2. **Verb (V)** 🟠 - Words that represent actions or states
   - Examples: *run, jump, is, loves, can*

3. **Modal Auxiliary (M)** 🔴 - Words that express possibility, obligation, permission, or ability
   - Examples: *can, could, will, would, should, may*
""", unsafe_allow_html=True)

# ===== EXAMPLE SENTENCES SECTION =====
st.markdown("## 📖 Example POS Tagged Sentences")

# Example 1
st.markdown("### Example 1: Simple Sentence")
example1_words = ["Deval", "loves", "google"]
example1_tags = ["Noun", "Verb", "Noun"]
example1_colors = {"Noun": "#2ecc71", "Verb": "#ffa300", "Modal Auxiliary": "#e74c3c"}

cols = st.columns(len(example1_words), gap="small")
for word, tag, col in zip(example1_words, example1_tags, cols):
    with col:
        color = example1_colors[tag]
        text_color = "#000" if tag != "Modal Auxiliary" else "#fff"
        st.markdown(
            f"""
            <div style='
                background-color: {color};
                color: {text_color};
                padding: 12px 15px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 1rem;
                text-align: center;
                font-family: Space Mono, monospace;
            '>
                {word}<br/>
                <span style='font-size: 0.8rem; opacity: 0.9;'>{tag}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# Example 2
st.markdown("### Example 2: Modal Auxiliary Sentence")
example2_words = ["Can", "google", "help"]
example2_tags = ["Modal Auxiliary", "Noun", "Verb"]

cols = st.columns(len(example2_words), gap="small")
for word, tag, col in zip(example2_words, example2_tags, cols):
    with col:
        color = example1_colors[tag]
        text_color = "#000" if tag != "Modal Auxiliary" else "#fff"
        st.markdown(
            f"""
            <div style='
                background-color: {color};
                color: {text_color};
                padding: 12px 15px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 1rem;
                text-align: center;
                font-family: Space Mono, monospace;
            '>
                {word}<br/>
                <span style='font-size: 0.8rem; opacity: 0.9;'>{tag}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# Example 3
st.markdown("### Example 3: Complex Sentence")
example3_words = ["Will", "juliet", "love", "google"]
example3_tags = ["Modal Auxiliary", "Noun", "Verb", "Noun"]

cols = st.columns(len(example3_words), gap="small")
for word, tag, col in zip(example3_words, example3_tags, cols):
    with col:
        color = example1_colors[tag]
        text_color = "#000" if tag != "Modal Auxiliary" else "#fff"
        st.markdown(
            f"""
            <div style='
                background-color: {color};
                color: {text_color};
                padding: 12px 15px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 1rem;
                text-align: center;
                font-family: Space Mono, monospace;
            '>
                {word}<br/>
                <span style='font-size: 0.8rem; opacity: 0.9;'>{tag}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# ===== PROBABILITY TABLES SECTION =====
st.markdown("## 📊 Emission Probability Example")
st.markdown("""
The **emission probability** shows the likelihood of a word appearing with a specific POS tag.
Based on the examples above:
""")

# Sample emission probability table
emission_data = {
    "Word": ["deval", "google", "loves", "can", "will", "juliet"],
    "P(Noun)": [0.5, 0.5, 0.0, 0.0, 0.0, 0.5],
    "P(Verb)": [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
    "P(Modal Aux)": [0.0, 0.0, 0.0, 1.0, 1.0, 0.0]
}

emission_df = pd.DataFrame(emission_data)


# Style the emission probability table
def style_prob(val):
    if val == 0:
        return 'color: #e74c3c; font-weight: bold;'
    else:
        return 'color: #2ecc71; font-weight: bold;'


styled_emission_df = emission_df.style.format({
    "P(Noun)": "{:.1f}",
    "P(Verb)": "{:.1f}",
    "P(Modal Aux)": "{:.1f}"
}).map(style_prob, subset=["P(Noun)", "P(Verb)", "P(Modal Aux)"]).set_properties(**{"text-align": "center"})

st.dataframe(styled_emission_df, width='stretch', hide_index=True)

# ===== TRANSITION PROBABILITY SECTION =====
st.markdown("## 🔀 Transition Probability Example")
st.markdown("""
The **transition probability** shows the likelihood of a POS tag appearing after another POS tag.
Based on the examples above:
""")

# Sample transition probability table
transition_data = {
    "Current POS": ["start", "Noun", "Verb", "Modal Aux"],
    "→ Noun": [0.0, 0.0, 0.5, 1.0],
    "→ Verb": [0.0, 0.5, 0.0, 0.0],
    "→ Modal Aux": [0.5, 0.0, 0.0, 0.0],
    "→ End": [0.5, 0.5, 0.5, 0.0]
}

transition_df = pd.DataFrame(transition_data)

styled_transition_df = transition_df.style.format({
    "→ Noun": "{:.1f}",
    "→ Verb": "{:.1f}",
    "→ Modal Aux": "{:.1f}",
    "→ End": "{:.1f}"
}).map(style_prob, subset=["→ Noun", "→ Verb", "→ Modal Aux", "→ End"]).set_properties(**{"text-align": "center"})

st.dataframe(styled_transition_df, width='stretch', hide_index=True)

# ===== HOW IT WORKS SECTION =====
st.markdown("## ⚙️ How POS Tagging Works")
st.markdown("""
1. **Training Phase**: Learn probabilities from tagged sentences
   - Emission probabilities: P(word | POS tag)
   - Transition probabilities: P(POS tag₂ | POS tag₁)

2. **Tagging Phase**: Use HMM (Hidden Markov Model) with Viterbi algorithm
   - Find the most likely sequence of POS tags for a sentence
   - Uses both emission and transition probabilities

# This is not the end **
""", unsafe_allow_html=True)

if st.button("→ Continue to Hidden Markov Model & Viterbi Algo", width='stretch'):
    st.switch_page("pages/4_HMM_&_Viterbi_Algo.py")

# ===== NAVIGATION SECTION =====
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("## 🚀 Ready to Tag Your Own Sentences?")

col1, col2 = st.columns(2)

with col1:
    if st.button("→ Interactive Tagging", width='stretch'):
        st.switch_page("pages/3_user_POS_Tagging.py")

with col2:
    if st.button("← Back to Home", width='stretch'):
        st.switch_page("streamlit_app.py")