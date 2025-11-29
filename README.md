# 📘 *Intelligent Career Guidance Recommendation System*

A machine-learning powered web application that predicts suitable career paths for students based on skills, interests, and academic background.

---

## 🚀 **Project Overview**

The **Intelligent Career Guidance Recommendation System** is designed to guide students in choosing the right career path using predictive ML models. It takes user inputs such as skills, interests, academic stream, and goals — and provides personalized role recommendations along with supporting career information.

This project includes:
✔ Machine Learning models (Bagging, XGBoost, custom ML pipeline)
✔ Python scripts for model training/testing
✔ A PHP-based front-end web application
✔ Pre-trained model file (`careerlast.pkl`)
✔ Templates, static assets, and role-wise career pages
✔ Database integration using PHP + MySQL

---

## 📂 **Project Structure**

```
INTELLIGENT-CAREER-CAMPUS-SYSTEM-1/
│
├── ABSTRACT.docx
├── README.md  (original)
├── bagging.py
├── bagging_xgboost.py
├── testapp.py
├── testmodel.py
├── careerlast.pkl     ← ML model file
│
├── *.php               ← All web pages (Login, Register, Dashboard, Career pages)
├── config.php          ← DB connection
├── static/             ← CSS, JS, Assets
├── templates/          ← HTML templates
├── phpmyadmin/         ← DB folder
│
└── venv/               ← Python virtual environment
```

---

## 🧠 **Machine Learning Components**

### ✔ **1. Training Scripts**

* **`bagging.py`**

  * Implements Bagging Classifier
  * Trains model with career dataset
  * Saves final model (`careerlast.pkl`)

* **`bagging_xgboost.py`**

  * Uses XGBoost for improved accuracy
  * Performs feature preprocessing + evaluation

* **`testmodel.py` / `testapp.py`**

  * Used to test predictions locally
  * Loads ML model and prints output

---

## 🌐 **Web Application Components (PHP)**

### 🔐 Authentication & Sessions

* `login.php`
* `register.php`
* `reset.php`
* `main.php`

### 📝 User Interaction Pages

* `courses.php`
* `contact.php`
* `blog.php`

### 🧭 Career Recommendation

* Model prediction integrated into:

  * `AI_ML_Specialist.php`
  * `Cyber_Security_analytics.php`
  * `Data_Analyst.php`
  * `Cloud_Engineer.php`
  * …and many more career-specific pages

### 🔧 Configuration

* `config.php` → MySQL database connection
* `phpmyadmin` folder → Database dump & structure

---

## 🎯 **Key Features**

### 💡 *1. Intelligent Career Prediction*

* Uses ML models to recommend the best-fit career.
* Based on student interests, skills, and data inputs.

### 🌐 *2. Fully Functional Website*

* Multi-page PHP application
* Login/Registration system
* Career pages with detailed info

### 📊 *3. Pre-trained ML Model Included*

* `careerlast.pkl` ensures ready-to-use prediction functionality.

### 🖼 *4. User-Friendly UI*

* Organized navigation
* Templates for readability
* Static assets included

### 🛠 *5. Easy to Extend*

* Add more careers
* Update training data
* Replace ML models anytime

---

## ⚙️ **Tech Stack**

### 🧑‍💻 Backend & ML

* Python
* Scikit-learn
* XGBoost
* Flask (for testing ML)

### 🌐 Frontend

* HTML
* CSS
* JavaScript
* Bootstrap (inside static folder)

### 🗄 Database

* MySQL
* phpMyAdmin

### 💾 Hosting Support

* XAMPP / WAMP
* Python virtual environment included

---

## 🚀 **How to Run This Project**

### **🔧 1. Setup Backend (ML Model)**

```bash
cd INTELLIGENT-CAREER-CAMPUS-SYSTEM-1
source venv/bin/activate   # or activate manually in Windows
python testapp.py
```

### **🌐 2. Setup Web Application**

1. Install **XAMPP**
2. Copy project folder into:

   ```
   C:/xampp/htdocs/
   ```
3. Start **Apache + MySQL**
4. Open browser:

   ```
   http://localhost/INTELLIGENT-CAREER-CAMPUS-SYSTEM-1/
   ```

---

## 🧪 **Dataset & Model**

* Career classification dataset (not included but model is pre-trained)
* Model accuracy improved with:

  * Bagging ensemble
  * XGBoost
  * Feature engineering

---

## 📄 **Included Documentation**

* **ABSTRACT.docx** - Project abstract
* **README.md** - Base project notes
* **credits.txt** - Contributor acknowledgments

---

## 🏆 **Ideal Use-Cases**

✔ Academic project submission
✔ Final year engineering project
✔ Career counseling systems
✔ AI recommendation system prototype

---

## 👥 **Contributors**

* Team project (as per credit file)
* Multiple modules created by team members:

  * ML Models
  * Web Frontend
  * Backend Integration
  * Documentation

