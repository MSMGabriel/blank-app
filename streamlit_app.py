import streamlit as st

st.set_page_config(page_title="News Sentiment App", page_icon="📰")

st.title("News Sentiment App is Back Online! 🎉")
st.write(
    "We're excited to announce that the News Sentiment App is now back online!\n "
    "\nYou can access it here: [News Sentiment App](https://news.concretumgroup.com/)\n "
    "\nIf you need any assistance, please contact us at **Mohamed@concretumgroup.com** or **Carlo@concretumgroup.com**."
)

# Embed website preview
st.write(
    "Preview [News Sentiment App](https://news.concretumgroup.com/)"
)
st.markdown(
    """
    <iframe src="https://news.concretumgroup.com/" width="100%" height="600"></iframe>
    """,
    unsafe_allow_html=True
)
