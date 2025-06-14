import streamlit as st
import requests
import pandas as pd
import os

BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")
BACKEND_PORT = os.getenv("BACKEND_PORT", "5000")
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}/tasks"

st.title("To-Do List App")

# Form to Add Tasks
st.subheader("Add a New Task")
with st.form("add_task"):
    name = st.text_input("Task Name", "")
    category = st.text_input("Category", "")
    description = st.text_area("Description", "")
    deadline = st.date_input("Deadline")
    priority = st.selectbox("Priority", [1, 2, 3, 4, 5])

    submitted = st.form_submit_button("Add Task")
    if submitted:
        response = requests.post(BACKEND_URL, json={
            "name": name,
            "category": category,
            "description": description,
            "deadline": str(deadline),
            "priority": priority
        })
        st.rerun()

# Fetch and Display Tasks
st.subheader("Task List")
tasks = requests.get(BACKEND_URL).json()

if tasks:
    df = pd.DataFrame(tasks)
    st.dataframe(df, hide_index=True, use_container_width=True)
else:
    st.write("No tasks found.")
