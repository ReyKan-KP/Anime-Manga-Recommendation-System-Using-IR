# Anime/Manga Recommendation System

## Description
This is an information retrieval system for Anime/Manga recommendations. It allows both new and existing users to enter Anime/Manga information and preferences, and get recommendations based on anime/manga descriptions, ratings, and user interactions. The system utilizes an Information Retrieval (IR) similarity algorithm to match user preferences to Anime/Manga in the dataset.

## Getting Started
Before you start using the system, make sure you have the necessary libraries installed. You can install them using pip:

```bash
pip install numpy pandas matplotlib beautifulsoup4
```



## Usage
- Run the script, and the system will prompt you to indicate whether you are an existing user or not.
- If you are an existing user, you will be asked to enter your User ID.
- Based on your input, you can either:
  - Enter the description of the Anime/Manga you'd like to read.
  - Get recommendations based on the previous User's watched list.

## Note
- Make sure to have the necessary CSV files ('main dataset\\main.csv' and 'main dataset\\user_profiles.csv') in the specified directory for data retrieval.

This README provides an overview of the Anime Recommendation System. For more details on the code and functionality, please refer to the code comments and documentation within the script.
