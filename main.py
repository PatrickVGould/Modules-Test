import streamlit as st

# Define the modules and their activities
modules = {
    "Module 1": [
        "Activity 1.1",
        "Activity 1.2",
        "Activity 1.3",
    ],
    "Module 2": [
        "Activity 2.1",
        "Activity 2.2",
        "Activity 2.3",
    ],
    "Module 3": [
        "Activity 3.1",
        "Activity 3.2",
        "Activity 3.3",
    ],
}

def render_activity(activity):
    if activity == "Activity 1.1":
        st.write("This is the content for Activity 1.1.")
        # Add any relevant Streamlit components for the activity
    elif activity == "Activity 1.2":
        st.write("This is the content for Activity 1.2.")
        # Add any relevant Streamlit components for the activity
    # Continue with other activities in a similar manner

st.title("Online Text-based Modules")
st.write("Select a module and activity from the sidebar.")

# Display the modules and activities in the sidebar
selected_module = st.sidebar.selectbox("Select a module", list(modules.keys()))
selected_activity = st.sidebar.selectbox("Select an activity", modules[selected_module])

# Render the selected activity
render_activity(selected_activity)
