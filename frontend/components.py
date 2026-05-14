import streamlit as st

def load_css():
    try:
        with open('frontend/style.css', 'r') as f:
            css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("CSS file not found")

def show_header():
    st.markdown("""
        <div class="main-header fade-in">
            <div class="header-badge"><span class="dot"></span>AI Powered</div>
            <h1>📚 AI <em>Study Companion</em></h1>
            <p>Upload any document — get summaries, quizzes &amp; key insights instantly</p>
        </div>
    """, unsafe_allow_html=True)

def show_stats_strip():
    st.markdown("""
        <div class="stat-strip">
            <div class="stat-box slide-left">
                <div class="num">6+</div>
                <div class="lbl">AI TOOLS</div>
            </div>
            <div class="stat-box scale-in">
                <div class="num">PDF</div>
                <div class="lbl">&amp; MORE</div>
            </div>
            <div class="stat-box slide-right">
                <div class="num">⚡</div>
                <div class="lbl">INSTANT</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_all_features():
    features = [
        ("📝", "Summary", "Concise bullet points"),
        ("📖", "Overview", "Deep topic breakdown"),
        ("❓", "MCQ Quiz", "Practice questions"),
        ("📋", "Short Q&A", "Quick revision pairs"),
        ("⭐", "Key Points", "Top takeaways"),
        ("📚", "Vocabulary", "Hard words explained"),
        ("🎯", "Topics", "Main & sub-topics"),
        ("💡", "Study Tips", "Personalised advice"),
    ]

    st.markdown('<span class="section-label slide-left">⚡ Everything you can do</span>', unsafe_allow_html=True)
    
    # Using grid layout with columns
    cols = st.columns(4, gap="small")
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 4]:
            st.markdown(f"""
                <div class="feature-card scale-in">
                    <div class="feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
            """, unsafe_allow_html=True)
        # New row after every 4 items
        if (i + 1) % 4 == 0 and i + 1 < len(features):
            cols = st.columns(4, gap="small")

def show_feature_card(icon, title, description):
    st.markdown(f"""
        <div class="feature-card scale-in">
            <span class="feature-icon">{icon}</span>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    """, unsafe_allow_html=True)

def show_upload_prompt():
    st.markdown("""
        <div class="upload-area fade-in">
            <div class="upload-icon-wrap">📄</div>
            <h3>Drop your study material here</h3>
            <p>or click the button below to browse files</p>
            <div class="file-pills">
                <span class="file-pill">PDF</span>
                <span class="file-pill">PPTX</span>
                <span class="file-pill">PNG</span>
                <span class="file-pill">JPG</span>
                <span class="file-pill">JPEG</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def show_quiz_card(question, options, q_num):
    display_question = question
    if len(question) > 3 and question[0] == 'Q' and question[1].isdigit():
        dot_idx = question.find('.')
        if dot_idx != -1:
            display_question = question[dot_idx + 1:].strip()

    st.markdown(f"""
        <div class="quiz-card">
            <div class="quiz-q-label">📝 Question {q_num + 1}</div>
            <div class="quiz-q-text">{display_question}</div>
        </div>
    """, unsafe_allow_html=True)

    return st.radio(
        f"q{q_num}",
        options=list(options.keys()),
        format_func=lambda x: f"{x})  {options[x]}",
        key=f"q_{q_num}",
        label_visibility="collapsed",
    )

def show_result_card(title):
    st.markdown(f"""
        <div class="result-card">
            <h3>✨ {title}</h3>
        </div>
    """, unsafe_allow_html=True)

def show_score_card(correct, total):
    percent = round((correct / total) * 100) if total else 0
    emoji = "🎉" if percent >= 80 else ("👍" if percent >= 50 else "📖")
    st.markdown(f"""
        <div class="score-card">
            <div class="score-num">{correct}/{total}</div>
            <div class="score-sub">{percent}% correct {emoji}</div>
        </div>
    """, unsafe_allow_html=True)