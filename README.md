<p align="center">
  <img src="https://img.shields.io/badge/ML-Recommendation%20System-blue" />
  <img src="https://img.shields.io/badge/Framework-Scikit--learn-orange" />
  <img src="https://img.shields.io/badge/Frontend-Streamlit-red" />
  <img src="https://img.shields.io/badge/Build-uv-green" />
  <img src="https://img.shields.io/badge/License-MIT-brightgreen" />
  <img src="https://img.shields.io/badge/Container-Docker-informational" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-yellow" />
</p>

# Books Recommendation System

## Overview
A production-ready, end-to-end book recommendation system built using collaborative filtering and Nearest Neighbors. The system processes raw book, user, and rating datasets, performs EDA, feature engineering, builds a recommendation engine, and serves real-time suggestions through a deployable application. The project demonstrates practical ML engineering skills, including model training, serialization, modular code design, and containerized deployment.

## Key Features
- Collaborative filtering using user–item rating matrix.
- Pivot-table transformation and sparse matrix optimisation.
- NearestNeighbors-based similarity search for generating top-N recommendations.
- Image URL extraction for displaying book covers.
- Serialized model artifacts for fast inference.
- Streamlit UI for interactive recommendations.
- Docker-ready structure for deployment.

## Tech Stack
- **Python**, **NumPy**, **Pandas**, **Scikit-learn**
- **Streamlit** for UI  
- **Joblib / Pickle** for model persistence  
- **Docker** for packaging  
- **Jupyter Notebook** for experimentation  

## How the System Works
1. **Data Cleaning & Normalisation**  
   - Fix encodings, remove malformed rows, rename columns.

2. **Filtering & Feature Engineering**  
   - Keep users with ≥200 ratings.  
   - Keep books with ≥50 ratings.  
   - Merge datasets, generate final rating matrix.

3. **Pivot Table + Sparse Matrix**  
   - Construct user–book matrix.  
   - Convert to CSR sparse format for efficient similarity search.

4. **Model Training**  
   - Fit `NearestNeighbors(algorithm="brute")` on sparse matrix.  
   - Store book indices, titles, and poster URLs.

5. **Inference Logic**  
   - Given a book title → fetch its vector → return top-N similar books + images.

6. **Streamlit UI**  
   - Dropdown selection  
   - Display recommended books with covers

7. **Artifacts**  
   Stored in `/artifacts`:
   - `dataset/`
   - `serialized_object/`
   - `trained_model/`

---

## Dataset
The system uses publicly available book-ratings data (users, books, ratings).  
Three primary CSV files are processed:
- **Books.csv**
- **Users.csv**
- **Book-Ratings.csv**

## How It Works
1. **Data Cleaning & Merging**  
   - Load all three CSVs, clean malformed rows, unify column formats.  
   - Merge books + ratings on ISBN and users + ratings on User-ID.

2. **Filtering & Feature Engineering**  
   - Retain users with ≥200 ratings to avoid sparse noise.  
   - Retain books with ≥50 ratings for quality signals.  
   - Construct a **user–book pivot matrix**.

3. **Sparse Matrix + Model Training**  
   - Convert pivot table to CSR sparse matrix.  
   - Train `NearestNeighbors(algorithm="brute")` for similarity search.

4. **Inference Logic**  
   - Given a book, compute nearest similar books using K-NN.  
   - Extract corresponding names + large cover image URLs.

5. **UI Layer (Streamlit)**  
   - Dropdown with all book titles  
   - Display recommended books with cover images

## Running Locally
```bash
uv sync
python main.py
streamlit run app.py
docker build -t book_recommendation:latest .
docker run -p 8501:8501 book_recommendation:latest

