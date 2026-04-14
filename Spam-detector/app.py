import streamlit as st
import pickle

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📧",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ---- Global ---- */
body { font-family: 'Segoe UI', sans-serif; }

/* ---- Hero banner ---- */
.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px;
    padding: 2.5rem 2rem 2rem;
    text-align: center;
    margin-bottom: 1.8rem;
    color: white;
}
.hero h1 { font-size: 2.2rem; font-weight: 700; margin: 0.3rem 0 0; letter-spacing: -0.5px; }
.hero p  { font-size: 1rem; color: #a0aec0; margin: 0.4rem 0 0; }

/* ---- Text area label ---- */
.section-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #4a5568;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}

/* ---- Result cards ---- */
.result-spam {
    background: #fff5f5; border: 1px solid #feb2b2;
    border-radius: 12px; padding: 1.2rem 1.5rem;
    display: flex; align-items: center; gap: 14px;
}
.result-safe {
    background: #f0fff4; border: 1px solid #9ae6b4;
    border-radius: 12px; padding: 1.2rem 1.5rem;
    display: flex; align-items: center; gap: 14px;
}
.result-icon { font-size: 2rem; }
.result-title { font-size: 1.15rem; font-weight: 700; }
.result-sub   { font-size: 0.88rem; color: #718096; margin-top: 2px; }
.spam-text    { color: #c53030; }
.safe-text    { color: #276749; }

/* ---- Stats bar ---- */
.stats-row {
    display: flex; gap: 12px; margin-top: 1.5rem;
}
.stat-card {
    flex: 1; background: #f7fafc; border: 1px solid #e2e8f0;
    border-radius: 10px; padding: 0.75rem 1rem; text-align: center;
}
.stat-num  { font-size: 1.5rem; font-weight: 700; color: #2d3748; }
.stat-lbl  { font-size: 0.78rem; color: #718096; margin-top: 2px; }

/* ---- Predict button override ---- */
div.stButton > button {
    width: 100%; height: 3rem;
    background: linear-gradient(90deg, #667eea, #764ba2);
    color: white; font-weight: 600; font-size: 1rem;
    border: none; border-radius: 10px;
    transition: opacity 0.2s;
}
div.stButton > button:hover { opacity: 0.88; }

/* ---- Divider ---- */
hr { border: none; border-top: 1px solid #e2e8f0; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
# def load_artifacts():
#     model      = pickle.load(open("model.pkl", "rb"))
#     vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
#     return model, vectorizer

# model, vectorizer = load_artifacts()
import os

@st.cache_resource
def load_artifacts():
    base_path = os.path.dirname(__file__)

    model_path = os.path.join(base_path, "model.pkl")
    vectorizer_path = os.path.join(base_path, "vectorizer.pkl")

    model = pickle.load(open(model_path, "rb"))
    vectorizer = pickle.load(open(vectorizer_path, "rb"))

    return model, vectorizer

# ── Hero section ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div style="font-size:2.4rem;">📧</div>
    <h1>Spam Email Detector</h1>
    <p>Paste any email content below and let AI decide instantly</p>
</div>
""", unsafe_allow_html=True)

# ── Input section ─────────────────────────────────────────────────────────────
st.markdown('<p class="section-label">Email Content</p>', unsafe_allow_html=True)
email = st.text_area(
    label="email_input",
    label_visibility="collapsed",
    placeholder="Paste or type the email text here…",
    height=200,
)

word_count = len(email.split()) if email.strip() else 0
char_count = len(email)
col1, col2, col3 = st.columns([2, 1, 1])
with col2: st.caption(f"Words: **{word_count}**")
with col3: st.caption(f"Chars: **{char_count}**")

st.markdown("")  # spacing

predict_btn = st.button("🔍  Analyze Email", use_container_width=True)

# ── Prediction ────────────────────────────────────────────────────────────────
if predict_btn:
    if not email.strip():
        st.warning("⚠️ Please enter some email text before analyzing.")
    else:
        with st.spinner("Analyzing…"):
            data       = vectorizer.transform([email])
            prediction = model.predict(data)
            proba      = model.predict_proba(data)[0] if hasattr(model, "predict_proba") else None

        st.markdown("<hr>", unsafe_allow_html=True)

        if prediction[0] == 1:
            st.markdown("""
            <div class="result-spam">
                <div class="result-icon">🚨</div>
                <div>
                    <div class="result-title spam-text">Spam Detected</div>
                    <div class="result-sub">This email shows strong signs of spam or phishing.</div>
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-safe">
                <div class="result-icon">✅</div>
                <div>
                    <div class="result-title safe-text">Looks Safe</div>
                    <div class="result-sub">No spam indicators were found in this email.</div>
                </div>
            </div>""", unsafe_allow_html=True)

        # Confidence bar (only if model supports predict_proba)
        if proba is not None:
            spam_conf = round(proba[1] * 100, 1)
            safe_conf = round(proba[0] * 100, 1)
            st.markdown(f"""
            <div class="stats-row">
                <div class="stat-card">
                    <div class="stat-num spam-text">{spam_conf}%</div>
                    <div class="stat-lbl">Spam confidence</div>
                </div>
                <div class="stat-card">
                    <div class="stat-num safe-text">{safe_conf}%</div>
                    <div class="stat-lbl">Safe confidence</div>
                </div>
                <div class="stat-card">
                    <div class="stat-num" style="color:#2d3748">{word_count}</div>
                    <div class="stat-lbl">Words analyzed</div>
                </div>
            </div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Powered by a trained ML classifier · Results are probabilistic, not guaranteed")
