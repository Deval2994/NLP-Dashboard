# 🧠 NLP Learning Dashboard

An interactive **Streamlit-based dashboard** designed to help learners understand core Natural Language Processing (NLP) concepts through clear explanations and modern visual design.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Project Pages](#project-pages)
- [File Descriptions](#file-descriptions)
- [Design & Styling](#design--styling)
- [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)

---

## 🎯 Project Overview

This dashboard is an **educational tool** for learning NLP concepts. It provides:

- **Clear Explanations** – Conceptual understanding without heavy mathematics
- **Modern UI/UX** – Beautiful, interactive design with smooth animations
- **Organized Navigation** – Easy-to-navigate pages for different topics
- **Extensible Structure** – Easy to add new topics and content

The project focuses on **conceptual understanding** rather than implementation, making it beginner-friendly for anyone new to NLP.

---

## ✨ Features

✅ **Interactive Dashboard** – Multi-page Streamlit application  
✅ **Modern Design** – Custom CSS with gradients, animations, and glassmorphism  
✅ **Responsive Layout** – Works on desktop and mobile devices  
✅ **Modular Code** – Separated HTML/CSS from Python for easy maintenance  
✅ **Clean Navigation** – Easy page switching with intuitive buttons  
✅ **Visual Components** – Cards, badges, concept boxes, and diagrams  

---

## 📁 Project Structure

```
NLP-Learning-Dashboard/
│
├── streamlit_app.py          # Main home page (entry point)
├── styles.css                # All CSS styling & design
├── README.md                 # This file
│
└── pages/
    ├── 1_Word2Vec.py         # Word2Vec concepts (CBOW & Skip-Gram)
    └── 2_POS_Tagging.py      # POS Tagging (HMM & Viterbi)
```

---

## 🚀 Installation & Setup

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Step 1: Clone or Download the Project

```bash
git clone <repository-url>
cd NLP-Learning-Dashboard
```

### Step 2: Install Dependencies

```bash
pip install streamlit
```

### Step 3: Verify File Structure

Ensure your folder looks like this:

```
project/
├── pages/
│   ├── 1_Word2Vec.py                   # Educational content (read-only)
│   ├── 2_pos_tagging.py              # Interactive tagging interface
│   ├── 3_user_POS_Tagging.py
│   └── 4_HMM_&_Viterbi_Algo.py           # HMM & Viterbi visualization
├── mathematical_calculation.py             # Core calculations module
├── streamlit_app.py                          # Main home page
├── styles.css                              # Custom styling
├── images/
│   ├── image_1.png
│   ├── image_2.png
│   ├── image_3.png                         
│   └── image_4.png                         
└── README.md                               
```

---

## ▶️ How to Run

Navigate to the project directory and run:

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### Keyboard Shortcuts

- `q` – Quit the app
- `r` – Rerun the app

---

## 📄 Project Pages

### 🏠 **Home Page** (`streamlit_app.py`)

The landing page of the dashboard featuring:

- **Welcome Section** – Title and hero text
- **Navigation Buttons** – Links to all major topics
- **Info Cards** – What is NLP, Topics Covered, Your Learning Journey
- **Beautiful Gradient Background** – Modern glassmorphic design

### 🔤 **Word2Vec Page** (`pages/1_Word2Vec.py`)

Covers word embedding concepts:

- **What is Word2Vec?** – Introduction to word vectors
- **CBOW (Continuous Bag of Words)** – Context predicts target word
- **Skip-Gram** – Target word predicts context
- **Comparison Section** – Side-by-side differences
- **Vector Relationships** – Examples like "king - man + woman ≈ queen"

**Key Concepts Explained:**
- Word embeddings capture semantic relationships
- CBOW is faster, Skip-Gram produces better quality
- Vector arithmetic reveals semantic patterns

### 📝 **POS Tagging Page** (`pages/2_POS_Tagging.py`)

Explains Part-of-Speech tagging with Hidden Markov Models:

- **What is POS Tagging?** – Grammatical labeling of words
- **Common POS Tags** – NOUN, VERB, ADJ, ADV, etc.
- **Hidden Markov Model (HMM)** – Transition and emission probabilities
- **Viterbi Algorithm** – Finding the most likely tag sequence
- **Complete Example** – Step-by-step walkthrough

**Key Concepts Explained:**
- POS tagging requires understanding context
- HMM models sequential dependencies
- Viterbi algorithm efficiently finds optimal paths

---

## 🎨 File Descriptions

### `streamlit_app.py`

**Purpose:** Main entry point of the application

**What it does:**
- Sets up the Streamlit page configuration
- Loads CSS styling from `styles.css`
- Creates the home page with navigation
- Displays welcome cards and information

**Key Components:**
- Page layout configuration
- CSS import logic
- Navigation buttons using `st.page_link()`
- Card-based content layout

---

### `styles.css`

**Purpose:** All visual design and styling

**What it contains:**
- Font imports (Poppins, Outfit, Space Mono)
- Color schemes and gradients
- Component styling (cards, buttons, badges)
- Animations (fade-in, hover effects)
- Responsive design utilities

**Key Sections:**
- **Typography** – Font families and sizes
- **Colors** – Gradients and color variables
- **Components** – Cards, buttons, boxes, badges
- **Animations** – Fade, pulse, hover effects
- **Page-specific Styles** – Word2Vec and POS Tagging unique colors

**Why Separate?**
- Easier to maintain and update design
- Reusable across all pages
- Non-programmers can edit styling
- Cleaner code organization

---

### `pages/1_Word2Vec.py`

**Purpose:** Educational page on Word2Vec embeddings

**Content Focus:**
- Conceptual explanation of word vectors
- CBOW vs Skip-Gram comparison
- Real-world examples
- Vector arithmetic demonstrations

**Design Elements:**
- Cyan/Purple color scheme (#00d4ff, #7c3aed)
- Concept boxes with left borders
- Comparison boxes for side-by-side learning
- Example boxes with visual highlighting

---

### `pages/2_POS_Tagging.py`

**Purpose:** Educational page on POS Tagging and HMM

**Content Focus:**
- POS tagging fundamentals
- Hidden Markov Model probabilities
- Viterbi algorithm explanation
- Step-by-step examples

**Design Elements:**
- Orange/Red color scheme (#ffa300, #ff006e)
- Tag badges for visual POS representation
- Probability bars for visual explanation
- Flow diagrams for algorithm walkthrough

---

## 🎨 Design & Styling

### Color Scheme

| Element | Color | Usage |
|---------|-------|-------|
| **Background** | Linear Gradient (#0f172a → #1e293b → #0f4c75) | Main background |
| **Primary** | #00d4ff (Cyan) | Word2Vec theme |
| **Secondary** | #7c3aed (Purple) | Accents, highlights |
| **Accent** | #ffa300 (Orange) | POS Tagging theme |
| **Text** | #cbd5e1 (Light Slate) | Body text |

### Typography

- **Headings** – Outfit (bold, modern)
- **Body** – Poppins (readable, clean)
- **Code/Monospace** – Space Mono (technical elements)

### Key Design Features

🎨 **Glassmorphism** – Semi-transparent cards with blur effects  
✨ **Gradient Text** – Multi-color text for visual interest  
🎯 **Hover Effects** – Interactive cards that lift and glow  
⚡ **Animations** – Smooth fade-in and transition effects  
📱 **Responsive** – Adapts to different screen sizes  

---

## 🚀 Future Enhancements

### Planned Features

- [ ] **Word2Vec Visualization** – Interactive vector space visualization
- [ ] **Algorithm Animation** – Step-by-step Viterbi algorithm visualization
- [ ] **Interactive Examples** – Users input their own text for tagging
- [ ] **Code Implementation** – Show actual code for training embeddings
- [ ] **Quiz Section** – Test understanding with interactive quizzes
- [ ] **Additional Topics** – Add NER, Sentiment Analysis, Language Models
- [ ] **Dark Mode Toggle** – User preference for theme
- [ ] **Resource Links** – Links to papers, tutorials, and datasets

### How to Extend

1. **Add New Topic** – Create `pages/3_NewTopic.py`
2. **Update Navigation** – Add link in `streamlit_app.py`
3. **Maintain Styling** – Use existing CSS classes from `styles.css`
4. **Test Locally** – Run with `streamlit run streamlit_app.py`

---

## 💻 Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Programming language |
| **Streamlit** | Web framework for dashboards |
| **CSS3** | Styling and animations |
| **HTML** | Markup (embedded in Streamlit) |
| **Google Fonts** | Modern typography |

### Why Streamlit?

- ✅ Fast prototyping
- ✅ No web development experience needed
- ✅ Beautiful default components
- ✅ Easy to add interactivity
- ✅ Perfect for data science/ML projects

---

## 📚 Learning Resources

If you want to dive deeper into these topics:

- **Word2Vec Original Paper** – [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
- **Hidden Markov Models** – [HMM Tutorial](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- **Viterbi Algorithm** – [Dynamic Programming for Sequences](https://en.wikipedia.org/wiki/Viterbi_algorithm)
- **Streamlit Docs** – [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

## 🤝 Contributing

To improve this project:

1. Fork or clone the repository
2. Make changes to the files
3. Test locally with `streamlit run streamlit_app.py`
4. Submit your improvements

**Areas for Contribution:**
- Add new NLP topics
- Improve explanations
- Create visualizations
- Fix bugs or issues
- Add interactive examples

---

## 📝 License

This project is open source and available for educational purposes.

---

## ❓ Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'streamlit'`

**Solution:**
```bash
pip install streamlit
```

### Issue: CSS file not loading

**Solution:**
- Make sure `styles.css` is in the same directory as `streamlit_app.py`
- Check file name spelling (case-sensitive on Linux/Mac)

### Issue: Pages not showing in navigation

**Solution:**
- Ensure page files are in `pages/` folder
- File names must start with numbers (e.g., `1_Word2Vec.py`)
- Restart Streamlit app

### Issue: Slow performance

**Solution:**
- Streamlit automatically reruns on file changes
- Press `r` to manually rerun
- Check internet connection for font loading

---

## 📧 Questions or Feedback?

If you have questions about this project or want to contribute, feel free to reach out!

---

## 🙏 Acknowledgments

- Built with **Streamlit** for interactive dashboards
- Styled with modern **CSS** design principles
- Educational content inspired by NLP research papers
- Designed for beginners learning NLP concepts

---

**Happy Learning! 🚀**
