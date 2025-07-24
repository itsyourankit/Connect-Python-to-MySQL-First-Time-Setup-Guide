# Connect-Python-to-MySQL-First-Time-Setup-Guide
This project demonstrates how to connect Python to a MySQL database using SQLAlchemy and PyMySQL, and load data using a basic ETL pipeline.

📦 Requirements
Before you start, make sure you have:

✅ Python 3.7+

✅ MySQL Server installed (e.g., MySQL Workbench)

✅ A MySQL database created

✅ pip (Python package manager)

🛠️ Step 1: Install Required Python Packages
pip install pandas sqlalchemy pymysql requests

🧑‍💻 Step 2: Create a MySQL Database
Login to MySQL and run:

sql
CREATE DATABASE my_database;
📁 Step 3: Update Your Python Script
Set your database credentials in the load() function:

python
user = 'root'
password = 'your_password'
host = 'localhost'
port = 3306
database = 'my_database'
📄 Step 4: Run the Python Script
im sharing my python script, you can refer...everything is mention with code
