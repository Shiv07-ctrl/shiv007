import streamlit as st

# Page Title
st.set_page_config(page_title="My Introduction", page_icon="👋")
st.title("👋 Welcome to My Introduction Website")
# About Me
st.header("🧑 About Me")
st.write("""
Hello! My name is **Shiv Pithva**.  
I’m passionate about **learning coding**, building websites, and creating cool tech projects using **Python and Streamlit**.
""")

# Hobbies Section
st.header("🎯 Hobbies")
st.markdown("""
- 💻 Coding
- 📚 Reading
- 🎵 Listening to music
- 🌍 Exploring new technologies
- 🏞️ Traveling
- 🚗 Driving       
""")

# Contact Info
st.header("📬 Contact")
st.write("You can reach me at: [your-shivpithva07@gmail.com](mailto:your-email@example.com)")

# Footer
st.markdown("---")
st.markdown("© 2025 Shiv Pithva | Built with ❤️ using Streamlit")


 