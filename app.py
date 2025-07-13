import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("tips_dataset.csv")

tips = load_data()
sns.set_theme(style="whitegrid")

# App title
st.title("🍽️ Seaborn Visualizer App - Tips Dataset")
st.write("An interactive data visualization dashboard using Seaborn and Streamlit.")

# Dataset overview section
st.subheader("📄 Dataset Overview")
with st.expander("View Dataset Head"):
    st.dataframe(tips.head())
with st.expander("View Column Data Types"):
    st.write(tips.dtypes)
with st.expander("View Summary Statistics"):
    st.write(tips.describe(include='all'))

# Sidebar configuration
st.sidebar.header("🔧 Plot Configuration")

plot_types = {
    "Scatter Plot": "scatter",
    "Line Plot": "line",
    "Bar Plot": "bar",
    "Box Plot": "box",
    "Violin Plot": "violin",
    "Count Plot": "count",
    "Regression Plot": "reg",
    "Histogram": "hist",
    "Strip Plot": "strip",
    "KDE Plot": "kde"
}

plot_choice = st.sidebar.selectbox("Select Plot Type", list(plot_types.keys()))
x_axis = st.sidebar.selectbox("X-Axis", tips.columns)
y_axis = st.sidebar.selectbox("Y-Axis (optional)", [""] + list(tips.columns))
hue_choice = st.sidebar.selectbox("Hue (optional)", [""] + list(tips.columns))

# Plotting function
def create_plot():
    fig, ax = plt.subplots(figsize=(8, 6))
    plot_kind = plot_types[plot_choice]
    
    plot_args = {
        "data": tips,
        "x": x_axis,
        "ax": ax
    }

    if y_axis: plot_args["y"] = y_axis
    if hue_choice: plot_args["hue"] = hue_choice

    try:
        if plot_kind == "scatter":
            sns.scatterplot(**plot_args)
        elif plot_kind == "line":
            sns.lineplot(**plot_args)
        elif plot_kind == "bar":
            sns.barplot(**plot_args)
        elif plot_kind == "box":
            sns.boxplot(**plot_args)
        elif plot_kind == "violin":
            sns.violinplot(**plot_args)
        elif plot_kind == "count":
            plot_args.pop("y", None)
            sns.countplot(**plot_args)
        elif plot_kind == "reg":
            sns.regplot(x=x_axis, y=y_axis, data=tips, ax=ax, scatter_kws={'s': 40}, line_kws={"color": "red"})
        elif plot_kind == "hist":
            sns.histplot(**plot_args, kde=True, bins=20)
        elif plot_kind == "strip":
            sns.stripplot(**plot_args, jitter=True)
        elif plot_kind == "kde":
            sns.kdeplot(**plot_args, fill=True)
        
        ax.set_title(f"{plot_choice} - {x_axis} vs {y_axis if y_axis else 'Frequency'}")
        st.pyplot(fig)

        return fig
    except Exception as e:
        st.error(f"Error rendering plot: {e}")
        return None

# Display plot
fig = create_plot()

# Download button
if fig:
    buffer = BytesIO()
    fig.savefig(buffer, format="png")
    st.download_button(
        label="📥 Download Plot as PNG",
        data=buffer.getvalue(),
        file_name="seaborn_plot.png",
        mime="image/png"
    )
