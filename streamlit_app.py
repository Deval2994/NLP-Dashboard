import streamlit as st

st.set_page_config(page_title="NLP Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Load CSS from external file
with open("styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# ===== HEADER SECTION =====
st.markdown("# 🧠 NLP Learning Dashboard", unsafe_allow_html=True)
st.markdown("<p class='hero-text'>Master Natural Language Processing Concepts</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ===== MAIN CONTENT CARDS =====
st.markdown("<div style='margin-top: 60px;'>", unsafe_allow_html=True)

# Card 0: Your Journey
st.markdown("""
<div class='card'>
    <div class='card-title'>Reason to Create This Page</div>
    <div class='card-text'>
        I created this webpage to demonstrate my understanding of complete NLP. 
        I am showcasing my knowledge mainly through two end concepts: 
        <b><span class='highlight'>Word2Vec</span></b> and <b><span class='highlight'>POS tagging</span></b>.
        <br><br>
        Beyond these, I have also covered several foundational and advanced NLP topics, including:
        <span class='highlight'>heuristic approaches</span>, 
        <span class='highlight'>WordNet</span>, 
        the <span class='highlight'>OMCS project by MIT</span>, 
        <span class='highlight'>ML/DL approaches</span> for NLP, 
        the <span class='highlight'>NLP pipeline</span>, 
        <span class='highlight'>One-Hot Encoding (OHE)</span>, 
        <span class='highlight'>Bag of Words (BoW)</span>, 
        <span class='highlight'>n-grams</span>, 
        <span class='highlight'>TF-IDF</span>, 
        <span class='highlight'>Word2Vec</span>, 
        <span class='highlight'>POS tagging</span>, 
        <span class='highlight'>Large Language Models (LLMs)</span>, 
        <span class='highlight'>probability concepts</span>, 
        and <span class='highlight'>neural networks (CNNs & RNNs)</span>.
        <br><br>
        It is obvious that if I understand <span class='highlight'>Word2Vec</span> and <span class='highlight'>POS tagging</span> in depth, 
        then I have already grasped all the foundational concepts mentioned above—from 
        <span class='highlight'>LLMs</span>, 
        <span class='highlight'>CNNs</span>, 
        and <span class='highlight'>RNNs</span> 
        to probabilistic approaches such as 
        <span class='highlight'>Hidden Markov Models</span> and the 
        <span class='highlight'>Viterbi algorithm</span>.
    </div>
</div>
""", unsafe_allow_html=True)




# Card 1: What is NLP
st.markdown("""
<div class='card'>
    <div class='card-title'>✨ What is NLP?</div>
    <div class='card-text'>
        Natural Language Processing is the intersection of linguistics and machine learning. 
        It enables computers to understand, interpret, and generate human language in meaningful ways.
    </div>
</div>
""", unsafe_allow_html=True)

# Card 2: Topics Covered
st.markdown(f"""
<div class='card'>
    <div class='card-title'>📚 Topics Covered</div>
    <div class='card-text'>
        <strong style='color: #00d4ff;'>Word2Vec (CBOW & Skip-Gram)</strong><br>
        Learn how words are transformed into dense vector representations that capture semantic relationships.
        <br><br>
        <strong style='color: #7c3aed;'>POS Tagging (HMM & Viterbi)</strong><br>
        Understand how Hidden Markov Models and the Viterbi algorithm assign grammatical tags to words.
    </div>
</div>
""", unsafe_allow_html=True)


# ===== NAVIGATION BUTTONS =====
st.markdown("<div style='text-align: center; margin: 40px 0;'>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)


with col1:
    st.page_link("pages/1_Word2Vec.py", label="Word2Vec", icon="🧠")

with col2:
    st.page_link("pages/2_pos_tagging.py", label=" POS Tagging", icon="🏷️")


st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("<div style='text-align: center; margin-top: 80px; padding: 40px; color: #64748b; font-size: 0.95rem;'>", unsafe_allow_html=True)
st.markdown("Built with ❤️ for NLP Learning | Powered by Streamlit")
st.markdown("</div>", unsafe_allow_html=True)