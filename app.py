import streamlit as st 

# App title
st.title("Growth Mindset Challenge 🎉")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Sidebar heading
st.sidebar.header("Manage your task")

# Text input for new task
new_task = st.sidebar.text_input("Add a new task:", placeholder="Enter your task here...")

if st.sidebar.button("Add task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success("Task added successfully!")
    else:
        st.warning("Task cannot be empty!")

# Display tasks
st.subheader("Your TO-DO List")

if not st.session_state.tasks:
    st.info("No task added yet. Start by adding a task from the sidebar.")
else:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])

        # Mark as completed
        completed = col1.checkbox(f"**{task['task']}**", task["completed"], key=f"check_{index}")
        if completed != task["completed"]:
            st.session_state.tasks[index]["completed"] = completed

        # Edit task
        new_task_input = st.text_input("Edit task", task["task"], key=f'edit_{index}')
        if col2.button("Edit", key=f"edit_button_{index}"):
            if new_task_input and new_task_input != task["task"]:
                st.session_state.tasks[index]["task"] = new_task_input
                st.rerun()

        # Delete task
        if col3.button("Delete", key=f"delete_{index}"):
            del st.session_state.tasks[index]
            st.rerun()

# Clear all tasks
if st.button("Clear all tasks"):
    st.session_state.tasks = []
    st.success("All tasks deleted successfully!")

# Footer
st.markdown("---")
st.caption("Stay organized and productive with this simple TO-DO List App")
