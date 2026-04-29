import streamlit as st
import calendar
import datetime
import json
import os

st.title("📅 Smart Calendar Web App")

year = st.number_input("Enter Year", 2000, 2100, datetime.date.today().year)
month = st.number_input("Enter Month", 1, 12, datetime.date.today().month)

cal = calendar.month(year, month)
st.text(cal)

# ---- Event System ----
st.subheader("➕ Add Event")

date = st.text_input("Enter date (DD-MM-YYYY)")
event = st.text_input("Event description")

if st.button("Save Event"):
    new_event = {"date": date, "event": event}

    if os.path.exists("events.json"):
        with open("events.json", "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(new_event)

    with open("events.json", "w") as f:
        json.dump(data, f)

    st.success("Event Saved!")

# ---- Show Events ----
st.subheader("📌 Saved Events")

if os.path.exists("events.json"):
    with open("events.json", "r") as f:
        data = json.load(f)

    for e in data:
        st.write(f"📅 {e['date']} → {e['event']}")