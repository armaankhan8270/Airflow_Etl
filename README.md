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
