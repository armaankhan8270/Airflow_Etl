
```markdown
📰 News ETL Pipeline using Apache Airflow & PostgreSQL

A production-grade, fully local ETL pipeline that extracts real-time tech news from NewsAPI, transforms the data, and loads it into a PostgreSQL database — all orchestrated using Apache Airflow.

> ❌ No cloud tools. ✅ 100% Open Source. 🐳 Dockerized. 🛠️ Real-world setup.

---

 📌 Features

- ⏰ **Daily ETL Scheduling** with Apache Airflow
- 🧪 **Data Cleaning & Normalization** during transformation
- 🗃️ **Structured Storage** into PostgreSQL
- 🔁 **Retry logic & Logging** with Airflow DAGs
- 📦 **Dockerized** for easy setup and consistent environments

---

 🧱 Project Structure


```markdown

news\_etl\_pipeline/
├── dags/
│   └── news\_etl\_dag.py         # Main DAG definition
│
├── extract.py                  # Extract data from NewsAPI
├── transform.py                # Clean and normalize article data
├── load.py                     # Load data into PostgreSQL
│
├── docker-compose.yml          # Runs Airflow + PostgreSQL + Scheduler
├── requirements.txt            # Python dependencies
├── .env                        # API keys and DB credentials
└── README.md                   # You're here

````

---

# ⚙️ Setup Instructions

# 1. Clone the Repository

```bash
git clone https://github.com/armaankhan8270/news-etl-pipeline.git](https://github.com/armaankhan8270/Airflow_Etl
cd news-etl-pipeline
````

### 2. Add Environment Variables

Create a `.env` file in the root directory:

```env
NEWS_API_KEY=your_news_api_key
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=news_db
```

> 🔑 You can get a free NewsAPI key from [https://newsapi.org/](https://newsapi.org/)

### 3. Start the Services

```bash
docker-compose up --build
```

This will launch:

* Airflow Webserver on `http://localhost:8080`
* PostgreSQL on `localhost:5432`

### 4. Initialize Airflow

In a new terminal:

```bash
docker exec -it airflow_webserver airflow db init
docker exec -it airflow_webserver airflow users create \
  --username admin --firstname Armaan --lastname Khan \
  --role Admin --email your@email.com --password admin
```

### 5. Trigger the DAG

* Visit `http://localhost:8080`
* Login using the credentials above
* Enable and trigger `news_etl_dag`

---

## 📊 Pipeline Overview

### 🔹 Extract

Pulls top tech headlines from NewsAPI and saves raw JSON.

### 🔹 Transform

Cleans and normalizes article data (removes HTML tags, filters empty fields, formats dates).

### 🔹 Load

Pushes cleaned articles into a `tech_news` table in PostgreSQL.

---

## 📈 Future Enhancements

* [ ] Sentiment Analysis on Articles
* [ ] Streamlit Dashboard for News Visualization
* [ ] Switch to Airflow 2.8+ and production-ready metadata DB
* [ ] Test coverage and logging improvements

---

## 💡 Why This Project?

This project was built to simulate real-world, production-level ETL pipelines without relying on cloud platforms. Ideal for aspiring data engineers, it demonstrates:

* ✅ Clean DAG structure
* ✅ Modular Python scripts
* ✅ Real API + Real Database + Real Orchestration

---

## 📣 Connect With Me

I'm Armaan Khan, a 22-year-old Data Engineer passionate about building robust data systems and sharing what I learn.

* 🌐 [Portfolio](https://armaanswiftserve.netlify.app/)
* 💼 [LinkedIn](https://linkedin.com/in/armaankhan8270)
* 🐙 [GitHub](https://github.com/armaankhan8270)

Feel free to fork the project, give it a ⭐ if you found it helpful, or connect to discuss more about data engineering!

---

> “Code more, rely less. Master the building blocks before the cloud.” ☁️❌💻✅

```

---

