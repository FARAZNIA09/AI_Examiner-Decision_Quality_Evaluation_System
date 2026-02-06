# 🧠 AI Examiner – Decision Quality Evaluation System

## 🔍 Overview
**AI Examiner** is an AI-driven system that evaluates the **quality of decision-making** based on *reasoning* rather than outcomes.

Instead of predicting results, the system analyzes **how well a decision is reasoned**, using explainable and interpretable evaluation logic. It provides structured scores, human-readable explanations, and a final verdict to support better decision analysis.

---

## 🎯 Key Idea
> Good decisions are not defined only by outcomes, but by the quality of reasoning behind them.

AI Examiner focuses on **decision intelligence** and **explainable AI**, making it suitable for real-world applications where transparency and accountability matter.

---

## 🧩 Evaluation Dimensions
Each decision is evaluated across five independent dimensions:

- **Logical Consistency** – Checks cause–effect clarity in reasoning  
- **Risk Awareness** – Identifies acknowledgment of uncertainty or downsides  
- **Bias Detection** – Detects emotional or absolute language  
- **Completeness** – Measures how well reasoning addresses the given scenario  
- **Ethical Impact** – Flags potential stakeholder harm or unfair treatment  

Each dimension contributes to a structured score out of 100.

---

## ⚙️ Features
- Multi-dimensional decision quality scoring  
- Explainable feedback for each evaluation dimension  
- Final decision verdict: **Good / Risky / Poor**  
- Visual comparison of decision strengths and weaknesses  
- Interactive **Streamlit web application**

---

## 🛠️ Tech Stack
- **Python**
- **Rule-based NLP**
- **Streamlit**
- **Matplotlib**
- **Explainable AI principles**

---

## 🚀 How It Works
1. User provides a **scenario**, **decision**, and **reasoning**
2. System evaluates reasoning across five dimensions
3. Generates:
   - Individual scores  
   - Explainable feedback  
   - Final verdict  
   - Visual insights  

---

## ▶️ Run Locally

### 1️⃣ Install Dependencies
```bash
pip install streamlit matplotlib
