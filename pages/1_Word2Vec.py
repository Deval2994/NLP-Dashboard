import streamlit as st

st.set_page_config(page_title="Word2Vec", layout="wide", initial_sidebar_state="collapsed")

# Load CSS from external file
with open("styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("# 🔤 Word2Vec – CBOW & Skip-Gram", unsafe_allow_html=True)
st.markdown("<p style='color: #00d4ff; font-family: Space Mono; font-size: 1.2rem;'>Words as Dense Vectors</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ===== WHAT IS WORD2VEC =====
st.markdown("## 🎯 What is Word2Vec?")
st.markdown("""
<div class='concept-box'>
    <div class='concept-title'>Core Idea</div>
    <p>
    Word2Vec represents words as <span class='highlight'>continuous vectors</span> in a high-dimensional space. 
    The magic happens when you discover that <span class='highlight'>similar words have similar vectors</span>. 
    Such as 🍺beer,  🍷wine, 🍸alcohol can be treated similarly.
</div>
""", unsafe_allow_html=True)


# ===== VECTOR RELATIONSHIPS =====
st.markdown("## ✨ The Magic of Word Vectors")

st.markdown("""
<div class='concept-box' style='border-left-color: #ff006e; background: rgba(255, 0, 110, 0.08);'>
    <div class='concept-title' style='color: #ff006e;'>Vector Arithmetic</div>
    <p style='font-size: 1.15rem; margin-bottom: 1rem;'>
    <span class='highlight'>king − man + woman ≈ queen</span>
    </p>
    <p>
    This isn't magic—it's mathematics! Word vectors encode semantic relationships. When you subtract "man" 
    (masculine concept), add "woman" (feminine concept), and adjust "king" accordingly, you get close to "queen".
    </p>
    <p style='margin-top: 12px; color: #a1a8b8;'><strong>Other Examples:</strong></p>
    <p>
    • <span class='highlight'>Paris − France + Italy ≈ Rome</span><br>
    • <span class='highlight'>Apple − iPhone + Samsung ≈ Galaxy</span><br>
    • <span class='highlight'>Queen − Woman + Man ≈ King</span>
    </p>
</div>
""", unsafe_allow_html=True)


# ===== Heading: TWO APPROACHES =====
st.markdown("## 🔀 Two Approaches to Word Embedding")

# CBOW Section
st.markdown("""
<div class='concept-box'>
    <div class='comparison-title'>📊 CBOW (Continuous Bag of Words)</div>
    <p><strong>Goal:</strong> Predict the <span class='highlight'>target word</span> using the <span class='highlight'>context words</span></p>
    <p style='margin-top: 12px;'>
    Imagine you're reading a sentence and someone covers up one word. Can you guess what it is based on the surrounding words? 
    That's essentially what CBOW does!
    </p>"""

            +


    """
    <div class='example-box'>
    Context: "The quick brown ___ jumped over the fence"<br>
    CBOW learns: [quick, brown, jumped, over] → [fox]
    </div>"""

            +


    """
     <div class='concept-title' style='color: #00d4ff;'>Why CBOW?</div>
        <p>
        ✓ <strong>Faster to train</strong> – processes context as a bag (order doesn't matter)<br>
        ✓ <strong>Better for smaller datasets</strong> – fewer samples to learn from<br>
        ✓ <strong>Good for frequent words</strong> – common context patterns are easier to capture
        </p>
</div>
""", unsafe_allow_html=True)


# ===== CBOW IMAGE SECTION =====
st.markdown("""
<div class='image-container'>
Example Sentence: <strong>Watch Campusx for</strong> Data Science
    <div class='image-wrapper'>
""", unsafe_allow_html=True)

st.image("images/image_1.png")

st.markdown("""
    </div>
    <div class='image-caption'>CBOW Neural Network Architecture</div>
    <div class='image-description'>
        Input layer receives context words → Hidden layer processes embeddings → 
        Output layer predicts target word using SoftMax and backpropagation
    </div>
</div>
""", unsafe_allow_html=True)


# Skip-Gram Section
st.markdown("""
<div class='concept-box'>
    <div class='comparison-title'>🎯 Skip-Gram</div>
    <p><strong>Goal:</strong> Predict the <span class='highlight'>context words</span> using the <span class='highlight'>target word</span></p>
    <p style='margin-top: 12px;'>
    Opposite approach! Given a single word, Skip-Gram tries to predict what words might appear around it. 
    It's like asking: "If I know this word, what other words are likely nearby?"
    </p>"""

            +
            
    """<div class='example-box'>
    Word: "fox"<br>
    Skip-Gram learns: [fox] → [the, quick, brown, jumped, over, ...]
    </div>"""

            +


    """
    <div class='comparison-title'>Why Skip-Gram?</div>
    <p>
    ✓ <strong>Better for rare words</strong> – generates more training samples<br>
    ✓ <strong>Captures word relationships better</strong> – learns nuanced semantic connections<br>
    ✓ <strong>Produces higher-quality embeddings</strong> – often preferred in practice
    </p>
</div>
""", unsafe_allow_html=True)

# ===== COMPARISON TABLE =====
st.markdown("## 📊 CBOW vs Skip-Gram")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='background: rgba(0, 212, 255, 0.1); border: 2px solid #00d4ff; border-radius: 8px; padding: 20px;'>
        <h3 style='color: #00d4ff; margin-top: 0;'>CBOW</h3>
        <p><strong>Input:</strong> Context words</p>
        <p><strong>Output:</strong> Target word</p>
        <p><strong>Speed:</strong> ⚡ Fast</p>
        <p><strong>Best for:</strong> Large corpora</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='background: rgba(124, 58, 237, 0.1); border: 2px solid #7c3aed; border-radius: 8px; padding: 20px;'>
        <h3 style='color: #7c3aed; margin-top: 0;'>Skip-Gram</h3>
        <p><strong>Input:</strong> Target word</p>
        <p><strong>Output:</strong> Context words</p>
        <p><strong>Speed:</strong> 🔄 Slower</p>
        <p><strong>Best for:</strong> Quality embeddings</p>
    </div>
    """, unsafe_allow_html=True)


# ===== FOOTER =====
st.markdown("<hr style='border-color: rgba(0, 212, 255, 0.2); margin: 60px 0;'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("streamlit_app.py", label="🏠 Home")

with col2:
    st.page_link("pages/2_pos_tagging.py", label="🏷️ POS Tagging →")

with col3:
    pass