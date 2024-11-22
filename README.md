# **BackOps.AI** - Revolutionizing Backend Operations with AI 💡

### 🏆 2024 Luddy Hackathon Winner, Indiana University Bloomington 🏆

---

## 📘 Overview

**BackOps.AI** is an intelligent assistant engineered to streamline backend database operations using natural language inputs. By harnessing the power of advanced Language Models (LLMs), it translates user instructions into structured JSON, facilitating efficient execution of operations such as:

- Insertions
- Updates
- Deletions  

![Screenshot 2024-11-18 171524](https://github.com/user-attachments/assets/8a10da9f-0892-41cd-8640-c7a34a73a21c)

### 🎬 [Watch the demo video](https://www.youtube.com/watch?v=TdIGMo6VuT8)
### 🔗 [Link to Project Report](https://drive.google.com/drive/folders/1mE6HK-6n0comwxLJTuwpMKVVOPnnRyOG)
---



### 🛠️ Core Functionalities

- **Natural Language Command Parsing:** Converts user queries into actionable database operations.  
- **In-Memory Database Design:** Efficiently manages key-value data with attributes like creation and update timestamps.  
- **Real-Time Analytics:** Monitors system usage, providing visualized metrics for performance evaluation.  

---

### 💻 Backend Implementation

- **Prompt Design:**  
  - Utilized few-shot prompting to handle various command types (insert, delete, update, create).  

- **In-Memory Database:**  
  - Attributes include:
    - **Key**
    - **Value**
    - **Created Datetime**
    - **Updated Datetime**  

- **Audit Trail:**  
  - Logs every query and tracks database changes for enhanced transparency and trend analysis.  

---

### 🎨 UI/UX Design

Developed an intuitive web interface allowing users to:  
- Submit natural language queries.  
- Visualize database manipulations in real-time.  
- Monitor system performance through interactive dashboards.  

---

### 📊 Advanced Analytics

- **Query Logs:** Tracks all queries executed for analysis and debugging.  
- **KPI Tracking:** Monitors key metrics, such as:  
  - Total Insertions, Deletions, Updates.  
  - Success/Failure percentages.  

- **7-Day Activity Overview:** Provides historical insights with graphical representations.  

---

### 🔍 Testing & Validation

- **Extensive Testing:** Evaluated system responses to diverse prompts.  
- **Performance Audits:** Documented outcomes to identify and improve edge cases.  

---
### 🔮 Future Work  

We aim to expand **BackOps.AI** with the following features:  

1. **Speech Input Support:** Enable the AI agent to process speech commands for performing database operations, along with adding multilingual support for wider global accessibility.
2. **Developer Log Access:** Allow developers to directly download log files from the web interface for easier monitoring and troubleshooting.
3. **Cloud Database Integration:** Expand compatibility by integrating BackOps.AI with cloud-based databases for seamless operations in distributed environments.      
4. **Role-Based Access Control (RBAC):** Implement robust security through role-based access control, ensuring fine-grained permissions for different user roles.    

---

>### Steps to Run this Project:

1. Clone this repo.
2. Create virtual environment using python `venv` command.
3. Activate virtual environment.
4. Install all dependencies using `pip install -r requirements.txt`.
5. Create a `.env file` and store the key of your LLM there which you can import in `llm.py` to make it work
5. Go to `app` directory using `cd AI-agent-operating-backend-system/app`.
6. Run `uvicorn main:app --reload` to start your application.

## 🤝 Collaborators  

| Name             | Email            |  
|------------------|------------------|  
| **Dev Patel**    | dap3@iu.edu      |  
| **Dhruv Bhanderi** | dbhander@iu.edu |  
| **Yash Vyas**    | yashvyas@iu.edu  |  
| **Dhwanit Pandya** | dhpandya@iu.edu |  

