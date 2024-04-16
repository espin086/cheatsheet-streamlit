import time
import streamlit as st
import pandas as pd

# Load the iris dataset
iris = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)

# Title
st.title("Streamlit Basics")
st.code('st.title("Streamlit Basics")')

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.code('st.sidebar.title("Sidebar")')
st.sidebar.markdown("---")
st.sidebar.write("This is a sidebar")
st.sidebar.code('st.sidebar.write("This is a sidebar")')
st.sidebar.title("Sidebar Button")
st.sidebar.markdown("---")
st.sidebar.button("Sidebar Button")
st.sidebar.code('st.sidebar.button("Sidebar Button")')
st.sidebar.title("KPIs")
st.sidebar.markdown("---")
st.sidebar.metric("KPI", 200, 3)
st.sidebar.code('st.sidebar.metric("KPI", 200, 3)')

# Header, Subheader, Text, Markdown

st.header("Header")
st.code('st.header("Header")')
st.markdown("---")
st.subheader("Subheader")
st.code('st.subheader("Subheader")')
st.markdown("---")
st.text("Text")
st.code('st.text("Text")')
st.markdown("---")
st.code("for i in range(8): foo()")


# Displaying Text
st.markdown("---")
st.metric("KPIs", 100, 2)
st.code('st.metric("KPIs", 100, 2)')

st.header("User Input")
st.markdown("---")

st.title("Enter Text")
st.markdown("---")
user_input = st.text_input("Enter Text", "Default Text")
st.code('user_input = st.text_input("Enter Text", "Default Text")')


st.title("Select Single Option")
st.markdown("---")
option = st.selectbox("Select Option", ["Option 1", "Option 2"])
st.write("Selected Option:", option)
st.code('option = st.selectbox("Select Option", ["Option 1", "Option 2"])')

st.title("Select Multiple Options")
st.markdown("---")
options = st.multiselect("Select Options", ["Option 1", "Option 2", "Option 3"])
st.code(
    'options = st.multiselect("Select Options", ["Option 1", "Option 2", "Option 3"])'
)

st.title("File Uploader")
st.markdown("---")
uploaded_file = st.file_uploader("Upload File", type=["csv", "txt"])
st.code('uploaded_file = st.file_uploader("Upload File", type=["csv", "txt"])')


st.title("Creating a Form")
st.markdown("---")
with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

st.code(
    """with st.form(key="my_form"):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login") """
)


st.title("Controlling Run of Program")
st.markdown("---")
# Button
if st.button("Run Button"):
    st.write("Run button clicked")
st.code('if st.button("Run Button"): st.write("Run button clicked")')

st.title("Two Columns Layout")
st.markdown("---")

tab1, tab2 = st.columns(2)
with tab1:
    if st.button("Tab 1"):
        st.write("Tab 1 Content")
with tab2:
    if st.button("Tab 2"):
        st.write("Tab 2 Content")

st.code(
    """
tab1, tab2 = st.columns(2)
with tab1:
    if st.button("Tab 1"):
        st.write("Tab 1 Content")
with tab2:
    if st.button("Tab 2"):
        st.write("Tab 2 Content")
        """
)

st.title("Expand and Collapse")
st.markdown("---")
expander = st.expander("Expand")
expander.write("Expanded Content")
st.code('expander = st.expander("Expand")')

st.title("Progress Bar")
st.markdown("---")
if st.button("Show Progress Bar"):
    p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        p_bar.progress(i + 1)

st.code(
    """
p_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        p_bar.progress(i + 1)

"""
)

st.title("Checkbox")
st.markdown("---")
st.checkbox("Check me out")
st.code('st.checkbox("Check me out")')

st.title("Radio Button")
st.markdown("---")
st.radio("Pick one:", ["nose", "ear"])
st.code('st.radio("Pick one:", ["nose", "ear"])')

st.title("Slider")
st.markdown("---")
st.slider("Slide me", min_value=0, max_value=10)
st.code('st.slider("Slide me", min_value=0, max_value=10)')


st.title("Slide to Select")
st.markdown("---")
st.select_slider("Slide to select", options=[1, "2"])
st.code('st.select_slider("Slide to select", options=[1, "2"])')

st.title("Enter Number")
st.markdown("---")
st.number_input("Enter a number")
st.code('st.number_input("Enter a number")')


st.title("Text Area")
st.markdown("---")
st.text_area("Area for textual entry")
st.code('st.text_area("Area for textual entry")')

st.title("Input Date")
st.markdown("---")
st.date_input("Date input")
st.code('st.date_input("Date input")')

st.title("Input Time")
st.markdown("---")
st.time_input("Time entry")
st.code('st.time_input("Time entry")')

st.title("Camera Input")
st.markdown("---")
st.camera_input("Take a picture!")
st.code('st.camera_input("Take a picture!")')

st.title("Display progress and status")
# Show a spinner during a process
with st.spinner(text="In progress"):
    time.sleep(3)
    st.success("Done")
st.code(
    """
with st.spinner(text="In progress"):
    time.sleep(3)
    st.success("Done")
"""
)


st.balloons()
st.code("st.balloons()")
st.snow()
st.code("st.snow()")
st.toast("Mr Stay-Puft")
st.code('st.toast("Mr Stay-Puft")')
st.error("Error message")
st.code('st.error("Error message")')
st.warning("Warning message")
st.code('st.warning("Warning message")')
st.info("Info message")
st.code('st.info("Info message")')
st.success("Success message")
st.code('st.success("Success message")')

st.title("Displaying Data")
st.markdown("---")
st.dataframe(iris)
st.code("st.dataframe(iris)")


import plotly.express as px

# Plotting the iris data
st.title("Scatterplot")
fig = px.scatter(iris, x="sepal_length", y="sepal_width", color="species")
st.plotly_chart(fig)
st.code(
    """fig = px.scatter(iris, x="sepal_length", y="sepal_width", color="species")"""
)

# Plotting a histogram using Plotly
st.title("Histogram")
fig = px.histogram(iris, x="sepal_length")
st.plotly_chart(fig)
st.code("""fig = px.histogram(iris, x="sepal_length")""")

# Plotting a line chart using Plotly
st.title("Line Chart")
fig = px.line(iris, x="sepal_length", y="sepal_width", color="species")
st.plotly_chart(fig)
st.code("""fig = px.line(iris, x="sepal_length", y="sepal_width", color="species")""")

# Plotting a boxplot using Plotly
st.title("Boxplot")
fig = px.box(iris, x="species", y="sepal_width")
st.plotly_chart(fig)
st.code("""fig = px.box(iris, x="species", y="sepal_width")""")

# Plotting a bar chart using Plotly
st.title("Bar Chart")
fig = px.bar(iris, x="species", y="sepal_length")
st.plotly_chart(fig)
st.code("""fig = px.bar(iris, x="species", y="sepal_length")""")

# Plotting a scatter matrix using Plotly
st.title("Scatter Matrix")
fig = px.scatter_matrix(
    iris,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
)
st.plotly_chart(fig)
st.code(
    """fig = px.scatter_matrix(iris, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species")"""
)

# Plotting a 3D scatter plot using Plotly
st.title("3D Scatter Plot")
fig = px.scatter_3d(
    iris, x="sepal_length", y="sepal_width", z="petal_length", color="species"
)
st.plotly_chart(fig)
st.code(
    """fig = px.scatter_3d(iris, x="sepal_length", y="sepal_width", z="petal_length", color="species")"""
)

# Plotting a heatmap using Plotly
st.title("Heatmap")
fig = px.imshow(iris.corr())
st.plotly_chart(fig)
st.code("""fig = px.imshow(iris.corr())""")

# Plotting a pie chart using Plotly
st.title("Pie Chart")
fig = px.pie(iris, names="species")
st.plotly_chart(fig)
st.code("""fig = px.pie(iris, names="species")""")
