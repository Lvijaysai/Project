# 📚 Quiz Score Analyzer

A Django-based web application designed to streamline the process of grading and analyzing student quiz scores. Users can upload a CSV file containing student data, and the application instantly generates detailed statistics, grade distributions, and a color-coded leaderboard.

## ✨ Features

* **CSV Upload:** Simple drag-and-drop interface for uploading score data.
* **Automatic Grading:** Automatically assigns letter grades (A-F) based on score thresholds.
* **Statistical Analysis:** Instantly calculates:
    * Average (Mean) Score
    * Median Score
    * Highest & Lowest Scores
    * Grade Distribution Breakdown
* **Visual Leaderboard:** Displays students in a table with color-coded high scores:
    * 🏆 **Gold:** Scores > 90
    * 🥈 **Silver:** Scores 80 - 89
    * ⚪ **Standard:** Scores < 80
* **Responsive UI:** Modern, dark-themed interface built with CSS Grid/Flexbox.

## 🛠️ Technologies Used

* **Backend:** Python 3, Django 5.2
* **Frontend:** HTML5, CSS3
* **Utilities:** Python `statistics` module, `python-dotenv`

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

* Python 3.10+ installed on your machine.

### Installation
    
1.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**
    Create a `.env` file in the root directory (next to `manage.py`) and add the following:
    ```env
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    ```

4.  **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

## 📂 CSV File Format

To analyze scores, your CSV file **must** have headers named `Name` and `Score` (case-sensitive).

**Example `scores.csv`:**
```csv
Name,Score
Alice Smith,95
Bob Jones,82
Charlie Brown,65
David Lee,74
Eve Davis,91
