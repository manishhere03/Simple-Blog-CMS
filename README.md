# ✍️ Simple Blog CMS

**A simple CRUD (Create, Read, Update, Delete) content management system for a blog, developed using the high-performance Python framework, FastAPI.**

This project demonstrates proficiency in building robust, high-speed backend APIs, data modeling, and integrating front-end functionality for a real-world application.

## 🚀 Key Features

* **RESTful API Development:** Built a complete API using **FastAPI** to manage blog posts and user content.
* **CRUD Operations:** Full implementation of core features for a blog platform:
    * **C**reate: New blog posts.
    * **R**ead: Retrieve individual posts and all posts.
    * **U**pdate: Modify existing posts.
    * **D**elete: Remove posts.
* **Data Validation:** Utilized **Pydantic** models to define data schemas, ensuring strict data validation and type hinting for all incoming and outgoing API requests.
* **Automatic Documentation:** Leveraged FastAPI's built-in support for **Swagger UI** (OpenAPI) to provide live, interactive documentation for all endpoints.
* **Front-End Integration:** The site features basic front-end components (likely HTML/JavaScript or a simple React integration) to demonstrate the consumption of the API for a complete user experience.

## 🛠️ Technology Stack

| Category | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI** | High-performance, async Python web framework. |
| **Data Schemas** | **Pydantic** | Used for data validation, serialization, and deserialization. |
| **Programming Language**| **Python** | Primary language for API logic. |
| **Database** | (Mention your specific DB here - e.g., **SQLite, PostgreSQL, MongoDB**) | Used for persistence of blog post data. |
| **Frontend/UI** | (Mention your UI technology - e.g., **HTML/CSS/JS** or **React.js**) | Simple user interface to interact with the API endpoints. |

## ⚙️ How to Run Locally

### Prerequisites

* Python (3.7+)
* `pip` (Python package installer)
* `uvicorn` (ASGI server to run FastAPI)

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone <YOUR_GITHUB_REPO_URL>
    cd <PROJECT_FOLDER_NAME>
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install fastapi uvicorn pydantic python-multipart
    ```

4.  **Run the Server:**
    ```bash
    uvicorn main:app --reload
    ```

The API will be accessible at `http://127.0.0.1:8000`.

### API Documentation

View the interactive API documentation at:
🔗 **`http://127.0.0.1:8000/docs`**

---
*Created by Manish Soni*