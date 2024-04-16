import time
import streamlit as st

# Title
st.title("Streamlit Basics")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.markdown("---")
st.sidebar.write("This is a sidebar")
st.sidebar.title("Sidebar Button")
st.sidebar.markdown("---")
st.sidebar.button("Sidebar Button")
st.sidebar.title("KPIs")
st.sidebar.markdown("---")
st.sidebar.metric("Sidebar Metric", 200, 3)

# Header, Subheader, Text, Markdown
st.header("Display Text")
st.markdown("---")
st.header("Header")
st.subheader("Subheader")
st.text("Text")
st.markdown("Markdown")

# Displaying Text
st.metric("Metric", 100, 2)

st.header("User Input")
st.markdown("---")

st.title("Enter Text")
st.markdown("---")
user_input = st.text_input("Enter Text", "Default Text")
st.write("User Input:", user_input)

st.title("Select Single Option")
st.markdown("---")
option = st.selectbox("Select Option", ["Option 1", "Option 2"])
st.write("Selected Option:", option)

st.title("Select Multiple Options")
st.markdown("---")
options = st.multiselect("Select Options", ["Option 1", "Option 2", "Option 3"])

st.title("File Uploader")
st.markdown("---")
uploaded_file = st.file_uploader("Upload File", type=["csv", "txt"])

st.title("Controlling Run of Program")
st.markdown("---")
# Button
if st.button("Run Button"):
    st.write("Run button clicked")

st.title("Two Columns Layout")
st.markdown("---")

tab1, tab2 = st.columns(2)
with tab1:
    if st.button("Tab 1"):
        st.write("Tab 1 Content")
with tab2:
    if st.button("Tab 2"):
        st.write("Tab 2 Content")

st.title("Expand and Collapse")
st.markdown("---")
expander = st.expander("Expand")
expander.write("Expanded Content")

st.title("Progress Bar")
st.markdown("---")
if st.button("Show Progress Bar"):
    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        p_bar.progress(i + 1)
