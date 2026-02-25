# ==========================================
# AI Examiner – Streamlit Web App
# ==========================================

import streamlit as st
import matplotlib.pyplot as plt
import string

# ---------- SCORING FUNCTIONS ----------

def logic_score(reasoning):
    positive_keywords = [
        "because", "therefore", "as a result",
        "this will lead to", "hence"
    ]
    negative_keywords = ["but", "however", "although"]

    reasoning = reasoning.lower()
    score = 0

    for w in positive_keywords:
        if w in reasoning:
            score += 8

    for w in negative_keywords:
        if w in reasoning:
            score -= 5

    return max(0, min(score, 25))


def risk_score(reasoning):
    risk_keywords = [
        "risk", "drawback", "downside", "challenge",
        "may fail", "could lead to", "possible loss",
        "uncertainty", "limitation"
    ]

    reasoning = reasoning.lower()
    score = 0

    for w in risk_keywords:
        if w in reasoning:
            score += 5

    return min(score, 20)


def bias_score(reasoning):
    absolute_words = ["always", "never", "everyone", "no one", "guaranteed"]
    emotional_words = ["obviously", "clearly", "definitely", "best", "worst", "useless"]

    reasoning = reasoning.lower()
    score = 15

    for w in absolute_words:
        if w in reasoning:
            score -= 3

    for w in emotional_words:
        if w in reasoning:
            score -= 2

    return max(score, 0)


def completeness_score(scenario, reasoning):
    scenario = scenario.lower().translate(str.maketrans("", "", string.punctuation))
    reasoning = reasoning.lower().translate(str.maketrans("", "", string.punctuation))

    scenario_words = set(scenario.split())
    reasoning_words = set(reasoning.split())

    stopwords = {
        "the", "is", "are", "a", "an", "and", "to", "of",
        "in", "on", "for", "with", "as", "by", "this",
        "that", "will", "be"
    }

    scenario_words -= stopwords
    reasoning_words -= stopwords

    if not scenario_words:
        return 0

    common = scenario_words.intersection(reasoning_words)
    return min(int((len(common) / len(scenario_words)) * 20), 20)


def ethics_score(reasoning):
    ethical_flags = [
        "only", "exclude", "reject", "deny",
        "prioritize younger", "fire", "terminate",
        "remove support", "no impact",
        "does not matter", "irrelevant"
    ]

    reasoning = reasoning.lower()
    score = 20

    for w in ethical_flags:
        if w in reasoning:
            score -= 4

    return max(score, 0)


def score_decision(data):
    return {
        "Logic": logic_score(data["reasoning"]),
        "Risk": risk_score(data["reasoning"]),
        "Bias": bias_score(data["reasoning"]),
        "Completeness": completeness_score(data["scenario"], data["reasoning"]),
        "Ethics": ethics_score(data["reasoning"])
    }


def generate_explanations(scores):
    explanations = []

    explanations.append(
        "Logic is weak: reasoning lacks clear cause–effect explanation."
        if scores["Logic"] < 10 else
        "Logic is strong: reasoning shows clear cause–effect."
    )

    explanations.append(
        "Risk is ignored: decision does not mention downsides."
        if scores["Risk"] < 5 else
        "Risk is acknowledged in the reasoning."
    )

    explanations.append(
        "Bias detected: emotional or absolute language used."
        if scores["Bias"] < 10 else
        "Reasoning is objective and neutral."
    )

    explanations.append(
        "Incomplete reasoning: scenario not fully addressed."
        if scores["Completeness"] < 8 else
        "Reasoning sufficiently covers the scenario."
    )

    explanations.append(
        "Ethical concerns detected in decision."
        if scores["Ethics"] < 10 else
        "No major ethical issues detected."
    )

    return explanations


def decision_verdict(total):
    if total >= 60:
        return "Good Decision"
    elif total >= 40:
        return "Risky Decision"
    else:
        return "Poor Decision"


# ---------- STREAMLIT UI ----------

st.set_page_config(page_title="AI Examiner", layout="centered")

st.title("🧠 AI Examiner – Decision Quality Evaluation")
st.write("Evaluate the *quality of reasoning* behind decisions, not just outcomes.")

scenario = st.text_area("📌 Scenario", height=100)
decision = st.text_area("✅ Decision Taken", height=80)
reasoning = st.text_area("📝 Reasoning", height=120)

if st.button("Evaluate Decision"):
    if scenario.strip() == "" or reasoning.strip() == "":
        st.warning("Please enter both scenario and reasoning.")
    else:
        data = {
            "scenario": scenario,
            "decision": decision,
            "reasoning": reasoning
        }

        scores = score_decision(data)
        total_score = sum(scores.values())
        verdict = decision_verdict(total_score)

        st.subheader("📊 Score Breakdown")
        for k, v in scores.items():
            st.write(f"**{k}:** {v}")

        st.subheader("🎯 Total Score")
        st.success(f"{total_score} / 100")

        st.subheader("🧾 Final Verdict")
        st.info(verdict)

        st.subheader("🧠 Explanation")
        explanations = generate_explanations(scores)
        for e in explanations:
            st.write("•", e)

        # Visualization
        st.subheader("📈 Decision Quality Visualization")
        fig, ax = plt.subplots()
        ax.bar(scores.keys(), scores.values())
        ax.set_ylim(0, 25)
        ax.set_ylabel("Score")
        ax.set_title("Decision Quality Breakdown")
        st.pyplot(fig)
