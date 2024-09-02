import streamlit as st


st.set_page_config(page_icon="👨‍💻", layout="wide")


page_bg_gradient = """
<style>
.stApp {
    background: linear-gradient(to right, #003135, #024950, #964737); /* Dark Teal, Deep Blue Teal, Rust gradient */
}

/* CSS for hamburger menu sidebar */
.sidebar-menu {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 250px;
    background-color: #003135;
    color: white;
    z-index: 1000;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.3);
}

.sidebar-menu a {
    display: block;
    color: white;
    text-decoration: none;
    margin: 10px 0;
}

.sidebar-menu a:hover {
    background-color: #024950;
    padding: 10px;
}

.sidebar-menu.active {
    display: block;
}

.sidebar-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    width: 50px;
    background-color: #024950;
    color: white;
    cursor: pointer;
    border-radius: 50%;
    position: fixed;
    top: 20px;
    left: 20px;
    z-index: 1000;
}
</style>
"""


st.markdown(page_bg_gradient, unsafe_allow_html=True)


st.markdown("""
<div class="sidebar-toggle">☰</div>
<div class="sidebar-menu" id="menu">
    <a href="#home" onclick="toggleSidebar()">Home</a>
    <a href="#educational" onclick="toggleSidebar()">Educational Journey</a>
    <a href="#skills" onclick="toggleSidebar()">Skills</a>
    <a href="#certificates" onclick="toggleSidebar()">Certificates</a>
    <a href="#projects" onclick="toggleSidebar()">Projects</a>
    <a href="#extracurricular" onclick="toggleSidebar()">Extracurricular Activities</a>
    <a href="#hobbies" onclick="toggleSidebar()">Hobbies and Interests</a>
    <a href="#contact" onclick="toggleSidebar()">Contact Information</a>
</div>
<script>
function toggleSidebar() {
    var menu = document.getElementById('menu');
    menu.classList.toggle('active');
}
</script>
""", unsafe_allow_html=True)


with st.sidebar:
    st.image(r"C:\Users\dawn\OneDrive\Pictures\Camera Roll\FORMAL PIC 2X2.png", width=300)  # Wider profile image in sidebar
    st.header("Dawn Marie D. Gumagay")
    st.write("""
    I am a 4th Year BSIT student at CIT-U. My journey in technology has been a transformative experience, shaping my skills and deepening my understanding of IT's impact on our lives.
    """)


st.title("Dawn Marie D. Gumagay's Portfolio")


menu = st.sidebar.selectbox(
    "Choose a section",
    ["Home", "Educational Journey", "Skills", "Certificates", "Projects", "Extracurricular Activities", "Hobbies and Interests", "Contact Information"]
)

if menu == "Home":
    st.header("Welcome to my portfolio!")
    st.write("""
    Welcome to my portfolio! Here you will find information about my educational journey, skills, certifications, projects, extracurricular activities, and hobbies.
    """)

elif menu == "Educational Journey":
    st.subheader("Educational Journey")
    st.write("""
    - **2021:** Began my BSIT journey at CIT-U during the pandemic. The start was challenging with online learning, but with the help of my instructors, I managed to learn meaningful skills in my 1st year.
    - **2021 - Present:** Engaged in various projects, ranging from simple tasks to the most challenging and meaningful projects that have greatly contributed to my growth in IT.
    - **2025:** Anticipated graduation year, manifesting success and ready to take on new challenges in the professional world.
    """)

elif menu == "Skills":
    st.subheader("Skills")
    st.write("""
    - **Development Languages:** Java, C, Python, JavaScript
    - **Front-end Technology:** HTML, JavaScript, ReactJS
    - **Backend Technology:** Java, Spring Boot
    - **Database and Cache:** MySQL, SQL Server, XAMPP
    - **Data Analysis:** Excel, Python
    - **Soft Skills:** 
      - 🕒 **Punctuality:** Ensuring tasks are completed on time
      - 🗂️ **Organization:** Keeping projects and assignments well-structured
      - 🗣️ **Communication:** Effective in both written and verbal exchanges
      - 🧩 **Adaptability:** Quick to learn and apply new skills in different environments
    - **Languages:** 
      - 🇬🇧 **English:** Native or Bilingual Proficiency
      - 🇯🇵 **Japanese:** Elementary Proficiency
      - 🇪🇸 **Spanish:** Elementary Proficiency
      - 🇨🇳 **Chinese:** Elementary Proficiency
    """)

elif menu == "Certificates":
    st.subheader("Certificates")
    st.write("""
    - 🎓 **Information Representation and Data Organization** (01/2022 - Present)
    - 🎓 **HCIA-Storage Course** (01/2022)
    - 🎓 **HCIP-Storage Course** (02/2022)
    - 🎓 **HCIE-Storage Course** (03/2022)
    - 🎓 **Theoretical Understanding of PHP** (04/2023)
    - 🎓 **Theoretical and Practical Understanding of SQL** (04/2023)
    - 🎓 **Intro to Programming (Python)** (08/2023)
    - 🎓 **Pandas Course** (09/2023)
    - 🎓 **Data Visualization Course** (09/2023)
    """)

elif menu == "Projects":
    st.subheader("Projects")
    st.write("""
    - 💬 **Forum: My Own Touch (10/15/2023):** Developed a user-friendly UI/UX for a Forum Application.
    - 🎲 **Bingo Game (09/2023):** Created a BINGO game using JavaScript and React.js framework.
    - 🎲 **Bingo Game URLs:**
      - [Game Board URL](#) (HEelhJos is the Game Code)
      - [Get Card URL](#) (Returns JSON-encoded data for the game card)
      - [Check Card Win](#) (Validates the player's card to determine if it's a winning card)
    - 📊 **Data Visualization (09/2023):** Analyzed a dataset and transformed it into meaningful data visualization.
    - 🗃️ **Queueing System (09/2023):** Developed a basic Queueing System using JavaScript and React.js.
    - 🍔 **Food Delivery System (01/2023 - 05/2023):** Created a Food Delivery System using HTML, SQL, and Database.
    - 📚 **WikangWali Application (2023):** An application for young students to learn the Filipino language.
    - 🛤️ **JeepCodes (10/18/2023):** Designed a program to decode Jeep Codes, outputting routes and highlighting common places for multiple codes.
    - 🚀 **Wildcat One Tap (02/2024 - Present):** Capstone project allowing students to report accidents and post content within the campus community. Developed using Java and Spring Boot. [GitHub Repository](https://github.com/dawnmarie-gumagay/THETECHHIVE_FRONTEND.git)
    - 🎨 **ColorHarmony (04/2024):** Created a tool to generate visually harmonious color palettes from images. Uses Python Imaging Library and KMeans from sklearn.cluster.
    - 📄 **NLP Project – Text Summarizer (05/2024):** Developed a text summarization algorithm producing concise and informative summaries. [GitHub Repository](https://github.com/dawnmarie-gumagay/CHIKABEBS_TEXTSUMMARIZER.git)
    - 🧩 **Build Your Own Machine Learning Model (03/2024):** Built a machine learning model for diagnosing breast cancer tumors.
    """)

elif menu == "Extracurricular Activities":
    st.subheader("Extracurricular Activities")
    st.write("""
    - **Supreme Student Government (2023 - 2024):** 
      - **Role:** IT Representative
      - **Responsibilities:** Addressed the concerns and needs of the Technologian Body through the Committee on Technologian Concerns, focusing on enhancing IT infrastructure and student experience.
    """)
    st.image(r"C:\Users\dawn\Downloads\4.png", caption="Extracurricular Activity 1", width=300)
    st.image(r"C:\Users\dawn\Downloads\5.jpeg", caption="Extracurricular Activity 2", width=300)
    st.video(r"C:\Users\dawn\Downloads\6.mp4")
    st.image(r"C:\Users\dawn\Downloads\8.jpeg", caption="Extracurricular Activity 3", width=300)

elif menu == "Hobbies and Interests":
    st.subheader("Hobbies and Interests")
    st.write("""
    I have a passion for painting, which allows me to express my creativity and unwind. Here are some of my paintings:
    """)
    st.image(r"C:\Users\dawn\Downloads\1.jpg", caption="Painting 1", width=300)
    st.image(r"C:\Users\dawn\Downloads\2.jpg", caption="Painting 2", width=300)
    st.image(r"C:\Users\dawn\Downloads\3.jpg", caption="Painting 3", width=300)
    st.image(r"C:\Users\dawn\Downloads\7.jpeg", caption="Additional Hobby", width=300)

    st.write("""
    In addition to painting, I have a deep interest in:
    - Coding and App Development
    - Data Visualization
    - Statistical Analysis
    - Cybersecurity
    - Artificial Intelligence
    - Language and Literature
    """)

elif menu == "Contact Information":
    st.subheader("Contact Information")
    st.write("""
    - **Email:** [gumagaydawnmarie14@gmail.com](mailto:gumagaydawnmarie14@gmail.com)
    - **Phone Number:** 09060447327
    - **GitHub:** [dawnmarie-gumagay](https://github.com/dawnmarie-gumagay)
    """)

