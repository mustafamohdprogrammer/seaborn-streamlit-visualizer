# 🍽️ Seaborn + Streamlit Visualizer App - Tips Dataset

An interactive data visualization dashboard built with **Seaborn** and **Streamlit** that allows users to explore the classic `tips` dataset through dynamic plot selection and customization.

---

## 📊 Features

✅ View dataset head, column data types, and summary statistics  
✅ Choose from multiple Seaborn plot types:
- Scatter Plot
- Line Plot
- Bar Plot
- Box Plot
- Violin Plot
- Histogram
- KDE Plot
- Count Plot
- Strip Plot
- Regression Plot

✅ Customize plots with:
- X-axis and Y-axis
- Hue (grouping variable)

✅ Download the generated plot as a PNG file

---

## 📁 Project Structure

```
seaborn-streamlit-visualizer/
│
├── app.py                  # Main Streamlit app
├── tips_dataset.csv        # Dataset used in the app
├── output/                 # Screenshots of the app
│   ├── Output_1.png
│   ├── Output_2.png
│   ├── Output3.png
│   ├── Output_4.png
│   ├── Output_5.png
│   └── Output_6.png
└── README.md               # Project documentation
```

---

## 🧾 About the Dataset

The `tips` dataset is a built-in dataset in Seaborn that contains information about tips received by waiters in a restaurant. It includes features such as:

- `total_bill`: Total bill (cost of the meal)
- `tip`: Tip given
- `sex`: Gender of the person paying the bill
- `smoker`: Whether the person is a smoker
- `day`: Day of the week
- `time`: Lunch or Dinner
- `size`: Size of the dining party

---

## 🚀 How to Run This Project

### 🔧 Requirements

Install the necessary libraries:

```bash
pip install streamlit pandas seaborn matplotlib
```

### ▶️ Start the App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

---

## 🖼️ App Screenshots

| Dashboard Overview | Plot Configuration |
|--------------------|--------------------|
| ![](output/Output_1.png) | ![](output/Output_2.png) |

| Column Data Types | Summary Statistics |
|-------------------|--------------------|
| ![](output/Output3.png) | ![](output/Output_4.png) |

| KDE Plot | Dataset Head |
|----------|--------------|
| ![](output/Output_5.png) | ![](output/Output_6.png) |

---

## 💡 Use Cases

This app is ideal for:
- Beginners learning **Seaborn** and **Streamlit**
- Quickly exploring datasets visually
- Creating downloadable charts for presentations or reports

---

## 📥 Download

Clone the repository and run the app:

```bash
git clone https://github.com/your-username/seaborn-streamlit-visualizer.git
cd seaborn-streamlit-visualizer
streamlit run app.py
```

---

## 🧠 Author

**Mohd Mustafa**  
*Python | Data Visualization | Streamlit Enthusiast*

[LinkedIn Profile](https://www.linkedin.com/in/mustafa1622/)

---


## 🙏 Acknowledgements

- [Seaborn](https://seaborn.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
