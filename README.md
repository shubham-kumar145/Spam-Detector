# 📧 Spam Email Detector

An AI-powered **Spam Email Detection Web App** built using **Machine Learning (KNN)** and deployed with **Streamlit**.
This application analyzes email content and predicts whether it is **Spam** or **Not Spam** in real-time.

🔗 **Live App:**
https://spams-detector.streamlit.app/

---

# 🚀 Features

* 📩 Real-time Email Spam Detection
* 🤖 Machine Learning Based Prediction
* 📊 Confidence Score Display
* 🎨 Clean & Professional UI
* ⚡ Fast and Lightweight Deployment
* 🔍 Word & Character Count Analysis

---

# 🧠 Machine Learning Model

This project uses:

* **Algorithm:** K-Nearest Neighbors (KNN)
* **Vectorization:** TF-IDF Vectorizer
* **Preprocessing:** Text Cleaning & Tokenization
* **Model Serialization:** Pickle (.pkl)

### Model Files

| File             | Description                               |
| ---------------- | ----------------------------------------- |
| `model.pkl`      | Trained KNN spam detection model          |
| `vectorizer.pkl` | TF-IDF vectorizer for text transformation |

These files are loaded during runtime to perform predictions without retraining.

---

# 🏗️ Project Structure

```
Spam-detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ How It Works

1. User enters email content
2. Text is cleaned and processed
3. Vectorizer converts text into numerical format
4. Trained KNN model predicts spam or safe
5. Confidence score displayed

---

# 📊 Prediction Flow

```
User Input
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorizer
     ↓
KNN Model
     ↓
Spam / Not Spam Prediction
```

---

# 🛠️ Tech Stack

### Machine Learning

* Python
* Scikit-learn
* Numpy
* Pandas

### Deployment

* Streamlit
* Streamlit Cloud

### Model Handling

* Pickle

---

# 📦 Installation (Run Locally)

Clone repository

```bash
git clone https://github.com/shubham-kumar145/Spam-Detector.git
```

Navigate to folder

```bash
cd Spam-Detector
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run app

```bash
streamlit run app.py
```

---

# 📸 App Preview

* Input Email Text
* Click Analyze
* Get Spam Detection Result

---

# 🎯 Use Cases

* Email filtering
* Phishing detection
* Message moderation
* AI learning project
* Resume ML project

---

# 📈 Future Improvements

* Deep Learning Model
* NLP Advanced Preprocessing
* Multi-language Support
* Model Retraining
* Dataset Expansion

---

# 👨‍💻 Author

**Shubham Kumar**

* GitHub: https://github.com/shubham-kumar145
* LinkedIn: https://linkedin.com/in/shubham-kumar145
* Portfolio: https://shubhamkumar.me

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share with others!

---

# 📄 License

This project is open-source and available under the **MIT License**.
