# cheatsheet-streamlit

A single-file Streamlit app that demonstrates most of the common Streamlit API in one scrollable page. Every widget is rendered live and immediately followed by an `st.code()` block showing the exact call that produced it, so you can read the page and copy the snippet you need. The data examples use the seaborn iris CSV, pulled straight from GitHub at startup, and the charts are built with Plotly Express.

All of it lives in `basics.py`.

## What the cheatsheet covers

**Text and layout**
- `st.title`, `st.header`, `st.subheader`, `st.text`, `st.markdown` for page structure and horizontal rules
- `st.code` for rendering the source of each example
- `st.columns(2)` for a two-column layout, each column holding its own button
- `st.expander` for collapsible content
- `st.sidebar.*` for a sidebar with a title, text, a button, and a metric

**Metrics and status**
- `st.metric` for a KPI with a delta value, in both the main page and the sidebar
- `st.progress` driven by a loop with `time.sleep`
- `st.spinner` wrapping a slow block, ending in `st.success`
- `st.error`, `st.warning`, `st.info`, `st.success` for message boxes
- `st.balloons`, `st.snow`, `st.toast` for the visual effects

**User input**
- `st.text_input` and `st.text_area` for free text
- `st.number_input` for numeric entry
- `st.selectbox` for one choice, `st.multiselect` for several
- `st.checkbox` and `st.radio`
- `st.slider` with min and max, and `st.select_slider` over a list of options
- `st.date_input` and `st.time_input`
- `st.file_uploader` restricted to csv and txt
- `st.camera_input` for a webcam capture
- `st.button` used to gate whether a block runs
- `st.form` with `st.form_submit_button`, batching a username and password field into one submit

**Data and charts**
- `st.dataframe` on the iris DataFrame
- `st.plotly_chart` with Plotly Express figures: `px.scatter`, `px.histogram`, `px.line`, `px.box`, `px.bar`, `px.scatter_matrix`, `px.scatter_3d`, `px.imshow` on a correlation matrix, and `px.pie`

## Requirements

- Python 3
- `streamlit`
- `pandas`
- `plotly`

There is no requirements.txt in the repo, and no version pins.

## Installation

```bash
git clone https://github.com/espin086/cheatsheet-streamlit.git
cd cheatsheet-streamlit
pip install streamlit pandas plotly
```

## Usage

```bash
streamlit run basics.py
```

Streamlit opens the page in your browser. An internet connection is needed on startup because the iris CSV is read from a raw GitHub URL.

Two things to expect while the page loads: the spinner example sleeps for 3 seconds on every rerun, and the heatmap calls `iris.corr()` on a DataFrame that still has the string `species` column, which recent pandas versions reject unless the frame is narrowed to numeric columns first.

## License

MIT. See [LICENSE](LICENSE).
