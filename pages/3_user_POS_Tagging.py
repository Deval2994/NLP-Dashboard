"""
probability of getting VERB after NOUN :  st.write(st.session_state.transition_probability_table['Noun']['Verb'])

Forf `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.
2025-12-06 20:02:58.773 Please replace `use_container_width` with `width`.

`use_container_width` will be removed after 2025-12-31.

For `use_container_width=True`, use `width='stretch'`. For `use_container_width=False`, use `width='content'`.

"""

import streamlit as st
import pandas as pd
from mathematical_calculation import (
    update_pos_count,
    calculate_emission_probability,
    calculate_transition_count,
    calculate_transition_probability
)

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

# ===== INTERACTIVE POS TAGGING SECTION HEADING =====
st.markdown("## ✏️ Interactive POS Tagging")
st.markdown("###### In this dashboard we are considering only 3 POS: *  Verb, Noun & Modal Auxiliary*")
st.markdown("###### you at least need to enter 5 sentences")

# ===== SESSION STATE INITIALIZATION =====
# Initialize session state variables to persist data across page reruns
# These variables will store data throughout the user's session

# Stores the list of words from the current sentence being tagged
if 'words' not in st.session_state:
    st.session_state.words = []

# Stores the POS tags for each word (e.g., {0: "Noun", 1: "Verb", ...})
if 'pos_tags' not in st.session_state:
    st.session_state.pos_tags = {}

# Stores all sentences that have been completely tagged
# Each sentence contains: {"words": [...], "tags": {...}}
if 'all_tagged_sentences' not in st.session_state:
    st.session_state.all_tagged_sentences = []

# Stores the count of each POS tag for each word
# Format: {"word": {'n': count, 'v': count, 'm': count}}
if 'pos_count' not in st.session_state:
    st.session_state.pos_count = {}

# Stores the calculated emission probability table
# Format: {"word": {'n': probability, 'v': probability, 'm': probability}}
if 'emission_probability_table' not in st.session_state:
    st.session_state.emission_probability_table = {}

# ===== DISPLAY PREVIOUSLY TAGGED SENTENCES =====
# Show all sentences that have been tagged so far with colored POS labels
if st.session_state.all_tagged_sentences:
    st.markdown("### 📋 Tagged Sentences")

    # Loop through each tagged sentence
    for idx, sentence in enumerate(st.session_state.all_tagged_sentences, 1):
        words = sentence["words"]  # Get the words from the sentence
        tags = sentence["tags"]  # Get the POS tags from the sentence

        st.markdown(f"**Sentence {idx}:**")

        # Create columns equal to the number of words for side-by-side display
        cols = st.columns(len(words), gap="small")

        # Display each word with its POS tag in a colored box
        for word_idx, (word, col) in enumerate(zip(words, cols)):
            with col:
                tag = tags.get(word_idx, "Untagged")  # Get the tag for this word

                # Set color based on POS tag
                # Noun = Green, Verb = Orange, Modal Auxiliary = Red
                if tag == "Noun":
                    color = "#2ecc71"
                    text_color = "#000"
                elif tag == "Verb":
                    color = "#ffa300"
                    text_color = "#000"
                elif tag == "Modal Auxiliary":
                    color = "#e74c3c"
                    text_color = "#fff"
                else:
                    color = "#333"
                    text_color = "#fff"

                # Display the word and its POS tag in a colored box
                st.markdown(
                    f"""
                    <div style='
                        background-color: {color};
                        color: {text_color};
                        padding: 10px 15px;
                        border-radius: 6px;
                        font-weight: bold;
                        font-family: Space Mono, monospace;
                        text-align: center;
                    '>
                        {word}<br/>
                        <span style='font-size: 0.8rem; opacity: 0.9;'>{tag}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ===== INPUT SECTION (Only shown when no words are currently being tagged) =====
if not st.session_state.words:
    # Text input field for user to enter a sentence
    sentence_input = st.text_input(
        "Enter a sentence to tag parts of speech:",
        placeholder="Example: The cat is sleeping",
        key="sentence_input"
    )

    # Button to split the sentence into words and start tagging
    if st.button("Split & Tag", width='content'):
        if sentence_input.strip():
            # Split the input sentence into individual words
            st.session_state.words = sentence_input.strip().split()

            # Initialize POS tags for each word as None (not yet selected)
            st.session_state.pos_tags = {i: None for i in range(len(st.session_state.words))}

            # Rerun the script to show the tagging interface
            st.rerun()
        else:
            st.warning("Please enter a sentence!")

# ===== TAGGING INTERFACE (Only shown when words are being tagged) =====
else:
    # Check if all words have been assigned a POS tag
    all_tagged = all(tag != "Select POS" and tag is not None for tag in st.session_state.pos_tags.values())

    # Display words with dropdown menus for POS selection
    st.markdown("<div class='pos-tags-container'>", unsafe_allow_html=True)

    # Create columns equal to the number of words for side-by-side dropdowns
    cols = st.columns(len(st.session_state.words), gap="small")

    # Create dropdown for each word
    for idx, (word, col) in enumerate(zip(st.session_state.words, cols)):
        with col:
            # Dropdown to select POS tag for this word
            pos_tag = st.selectbox(
                f"Word {idx + 1}",
                options=["Select POS", "Noun", "Verb", "Modal Auxiliary"],
                index=0,
                key=f"pos_dropdown_{idx}",
                label_visibility="collapsed"
            )

            # Determine color based on selected POS tag
            if pos_tag == "Noun":
                color = "#2ecc71"
                text_color = "#000"
            elif pos_tag == "Verb":
                color = "#ffa300"
                text_color = "#000"
            elif pos_tag == "Modal Auxiliary":
                color = "#e74c3c"
                text_color = "#fff"
            else:
                color = "#333"
                text_color = "#fff"

            # Display the word in a colored box that changes color as user selects POS
            st.markdown(
                f"""
                <div style='
                    background-color: {color};
                    color: {text_color};
                    padding: 12px 15px;
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: 1.1rem;
                    text-align: center;
                    font-family: Space Mono, monospace;
                    transition: all 0.3s ease;
                '>
                    {word}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Store the selected POS tag in session state
            st.session_state.pos_tags[idx] = pos_tag

    st.markdown("</div>", unsafe_allow_html=True)

    # ===== NEXT BUTTON (Only shown when all words are tagged) =====
    # Show "Next" button only after user has selected POS for all words
    if all_tagged:
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Next", width='stretch', type="primary"):
            # ===== STORE TAGGED SENTENCE =====
            # Create a dictionary with the current sentence and its tags
            tagged_sentence = {
                "words": st.session_state.words,
                "tags": st.session_state.pos_tags.copy()
            }
            # Add this sentence to the list of all tagged sentences
            st.session_state.all_tagged_sentences.append(tagged_sentence)

            # ===== UPDATE POS COUNT =====
            # Call the update_pos_count function from mathematical_calculation.py
            # This updates the count of how many times each word appears with each POS tag
            st.session_state.pos_count = update_pos_count(
                st.session_state.pos_count,
                st.session_state.words,
                st.session_state.pos_tags
            )

            # ===== CLEAR FOR NEXT SENTENCE =====
            # Clear the words and tags to reset for the next sentence
            st.session_state.words = []
            st.session_state.pos_tags = {}

            # Rerun the script to show the input field again
            st.rerun()
    else:
        # Show info message if not all words are tagged yet
        st.info("👉 Tag all words before proceeding to the next sentence")

# ===== MOVE FORWARD SECTION (Only shown after 5+ sentences are tagged) =====
# Check if at least 5 sentences have been tagged and no current tagging is in progress
if len(st.session_state.all_tagged_sentences) >= 5 and not st.session_state.words:
    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("Move Forward", width='stretch', type="primary", key="move_forward_btn"):
        # ===== CALCULATE EMISSION PROBABILITY =====
        # Call the calculate_emission_probability function from mathematical_calculation.py
        # This calculates the probability of each word appearing with each POS tag
        st.session_state.emission_probability_table = calculate_emission_probability(st.session_state.pos_count)

        # Display success message with count of tagged sentences
        st.success(f"✅ Successfully tagged {len(st.session_state.all_tagged_sentences)} sentences!")

        # ===== DISPLAY POS COUNT DICTIONARY =====
        # Show the raw POS count data in JSON format
        st.markdown("### 📊 POS Count Dictionary")
        st.json(st.session_state.pos_count)

        # ===== DISPLAY EMISSION PROBABILITY TABLE =====
        st.markdown("### 📈 Emission Probability Table")

        # Create table data from the emission probability dictionary
        table_data = []
        for word in sorted(st.session_state.emission_probability_table.keys()):
            probs = st.session_state.emission_probability_table[word]
            table_data.append({
                "Word": word.capitalize(),
                "T=10 (Noun)": probs['n'],  # Probability of this word being a Noun
                "T=5 (Verb)": probs['v'],  # Probability of this word being a Verb
                "T=2 (Modal Aux)": probs['m']  # Probability of this word being Modal Auxiliary
            })

        # Convert table data to Pandas DataFrame
        df = pd.DataFrame(table_data)

        # ===== STYLING FUNCTION =====
        # Function to color cells: red for zeros, green for non-zeros
        def style_probability(val):
            if val == 0:
                return 'color: #e74c3c; font-weight: bold; text-align: center;'
            else:
                return 'color: #2ecc71; font-weight: bold; text-align: center;'

        # ===== FORMAT AND STYLE THE TABLE =====
        # Format probabilities to 1 decimal place and apply colors
        styled_df = df.style.format({
            "T=10 (Noun)": "{:.1f}",
            "T=5 (Verb)": "{:.1f}",
            "T=2 (Modal Aux)": "{:.1f}"
        }).map(style_probability, subset=["T=10 (Noun)", "T=5 (Verb)", "T=2 (Modal Aux)"]).set_properties(
            **{"text-align": "center"})

        # Display the styled table in Streamlit
        st.dataframe(styled_df, width='stretch', hide_index=True)

        # ===== CALCULATE TRANSITION TABLES =====
        # Calculate transition count table from all tagged sentences
        st.session_state.transition_count_table = calculate_transition_count(
            st.session_state.all_tagged_sentences
        )

        # Calculate transition probability table from transition counts
        st.session_state.transition_probability_table = calculate_transition_probability(
            st.session_state.transition_count_table
        )

        # ===== DISPLAY TRANSITION PROBABILITY TABLE =====
        st.markdown("### 🔀 Transition Probability Table")

        # Create table data from transition probability table
        transition_prob_data = []
        for pos in st.session_state.transition_probability_table.keys():
            transition_prob_data.append({
                "Current POS": pos,
                "→ Noun": st.session_state.transition_probability_table[pos]["Noun"],
                "→ Verb": st.session_state.transition_probability_table[pos]["Verb"],
                "→ Modal Aux": st.session_state.transition_probability_table[pos]["Modal Auxiliary"],
                "→ End": st.session_state.transition_probability_table[pos]["end"]
            })

        # Convert to DataFrame
        transition_prob_df = pd.DataFrame(transition_prob_data)

        # ===== STYLING FUNCTION FOR TRANSITION PROBABILITY =====
        # Function to color cells: red for zeros, green for non-zeros
        def style_transition_probability(val):
            if val == 0:
                return 'color: #e74c3c; font-weight: bold; text-align: center;'
            else:
                return 'color: #2ecc71; font-weight: bold; text-align: center;'

        # ===== FORMAT AND STYLE TRANSITION PROBABILITY TABLE =====
        # Format probabilities to 1 decimal place and apply colors
        styled_transition_prob_df = transition_prob_df.style.format({
            "→ Noun": "{:.1f}",
            "→ Verb": "{:.1f}",
            "→ Modal Aux": "{:.1f}",
            "→ End": "{:.1f}"
        }).map(style_transition_probability, subset=["→ Noun", "→ Verb", "→ Modal Aux", "→ End"]).set_properties(
            **{"text-align": "center"})

        # Display the styled table in Streamlit
        st.dataframe(styled_transition_prob_df, width='stretch', hide_index=True)

        # ===== NAVIGATION BUTTONS =====
        st.markdown("<br><br>", unsafe_allow_html=True)
