"""
HMM & Viterbi Algorithm Visualization
Personal Notes Dashboard - Presentation Style
"""

import streamlit as st

# ===== PAGE CONFIGURATION =====
st.set_page_config(page_title="HMM & Viterbi Algorithm", layout="wide", initial_sidebar_state="collapsed")

# ===== LOAD EXTERNAL CSS =====
with open("styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# ===== HEADER SECTION =====
st.markdown("# 🤖 HMM & Viterbi Algorithm", unsafe_allow_html=True)
st.markdown(
    "<p style='color: #ffa300; font-family: Space Mono; font-size: 1.2rem;'>Hidden Markov Model for POS Tagging</p>",
    unsafe_allow_html=True)

# ===== HMM VISUALIZATION SECTION =====
st.markdown("""
## Architecture
* The lines represent the probability. 
* The red lines shows probability of word having that POS (Emission Probability).
* Rest shows probability of next what POS can be (Transition Probability).
"""
)

st.image("images/image_3.png", width='stretch')

# ===== VITERBI ALGORITHM SECTION =====
st.markdown("## Viterbi Algorithm")

st.markdown("""
### Brute Force vs Viterbi

**Brute Force (Simple Idea):**
- Check every possible tag sequence and pick the best one
- But this becomes extremely slow because the number of possibilities grows very fast

**Viterbi (Great Idea):**
- Instead of checking all possibilities, it keeps only the best path at each step
- This makes finding the best tag sequence fast and efficient

**Why Viterbi?**
It's not magic, but very logical - it's about being smart and not checking unnecessary paths.
""")

# ===== PRACTICAL EXAMPLE SECTION =====
st.markdown("### Example: \"will will google cube\"")

st.markdown("""
## Normal Life (Brute Force) - Check ALL possibilities:
- Path 1: M → N → N → N = 1/5 × 3/5 × 5/10 × 3/16 = (3⁴ = 81 loops)
- Path 2: M → N → V → N = 1/5 × 3/5 × 0 × 3/16 = ❌ ZERO (wasted effort!)
- Path 3: M → V → N → N = 1/5 × 0 × 5/10 × 3/16 = ❌ ZERO (wasted effort!)
- ... and 78 more paths to check!

## Mentos Life (Viterbi) - Smart elimination:
""")
st.image("images/image_4.png", width='stretch')

# Create visual comparison
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Step 1: what come after start? and Word is "will"**
    ```
          start  will  calc
   P(n)   0.6   0.2   0.12   ✗
   P(m)   0.4   0.5   0.20   ✓
   P(v)    0                 ✗
    ```
    Keep only M!
    """)

with col2:
    st.markdown("""
    **Step 2: what come after M? and Word is "will"**
    ```
            M   will  calc
   P(n)   1.0   0.2   0.2    ✓
   P(m)    0                 ✗
   P(v)    0                 ✗
    ```
    Keep only M→N!
    """)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    **Step 3: what come after N? and Word is "google"**
    ```
            N    google    calc
   P(n)    0                   ✗ 
   P(m)    0                   ✗
   P(v)   0.5    0.4     0.20  ✓    
    ```
    Keep only M→N→V!
    """)

with col4:
    st.markdown("""
    **Step 4: what come after V? and Word is "cube"**
    ```
            V   cube  calc
   P(n)   1.0   0.3   0.3    ✓
   P(m)    0                 ✗
   P(v)    0                 ✗
    ```
    Keep only M→N→V→N!
    """)

st.markdown("""
## We got the POS sequence M→N→V→N in just 4 step.
""")

st.markdown("""
**Result:**
- Brute Force: 81 loops + wasted checks
- Viterbi: Only 4 steps with smart elimination! ⚡

🎯 **That's the power of Viterbi - eliminate zeros early and keep only the best paths!**
""")


# ===== NAVIGATION SECTION =====
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("🏠 Home", width='content'):
    st.switch_page("streamlit_app.py")