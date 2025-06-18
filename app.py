import streamlit as st
import random

st.set_page_config(page_title="AutoDocs AI", layout="centered")

st.title("AutoDocs AI")
st.markdown("""
A simple prototype to simulate automated meeting summaries using AI.
Submit your raw meeting notes below, and AutoDocs AI will generate a concise summary.
""")

st.subheader("📝 Enter Meeting Notes")
meeting_notes = st.text_area("Paste raw meeting notes or talking points:", height=250)

if st.button("Generate AI Summary"):
    if meeting_notes.strip():
        # Simulate AI summary generation
        mock_summaries = [
            "Key decisions made. Follow-up actions assigned.",
            "Project progress reviewed. Risks discussed.",
            "Client feedback addressed. Next sprint planned.",
            "Team blockers surfaced. Goals re-aligned."
        ]
        summary = random.choice(mock_summaries)
        st.success("AI-Generated Summary")
        st.write(summary)

        with st.expander("📤 Email This Summary (simulated)"):
            st.text_input("To:", value="team@example.com")
            st.text_area("Email Body:", value=summary)
            st.button("Send Email (Simulated)")
    else:
        st.warning("Please enter meeting notes to generate a summary.")
