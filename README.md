# Anime/Manga Recommendation System with IR Algorithm
This Flask-based Anime/Manga recommendation system utilizes an IR similarity algorithm to provide personalized suggestions based on user preferences, including descriptions, ratings, interactions, and viewing history. Built with Flask, it features document search, ranking, spell correction, and user feedback, offering Anime/Manga enthusiasts a comprehensive platform for seamless content discovery.


## Table of Contents
- [Description](##Description)
- [Installation](##Installation)
- [Usage](##Usage)
- [Run the Application](##RunthApplication)
- [Features](##Features)
- [Contributing](##Contributing)
- [License](##License)
- [Note](##Note)

## Description
This web application serves as an information retrieval system for Anime/Manga recommendations, integrating features that enable users to input their preferences and receive personalized suggestions. The system leverages an Information Retrieval (IR) similarity algorithm to match user preferences with Anime/Manga in the dataset. Recommendations are generated based on various factors, including anime/manga descriptions, ratings, user interactions, and the user's viewing history.

Built with Flask, the application also incorporates functionalities such as document search and ranking, spell correction for user queries, and a user feedback system. Users can explore and interact with the system through a web-based interface.

This integration offers a comprehensive platform for Anime/Manga enthusiasts, providing a seamless experience for discovering new content tailored to their tastes. Whether users are seeking recommendations based on descriptions, ratings, or personal viewing history, the system aims to enhance the overall Anime/Manga discovery process.

## Installation
  1. **Clone the repository :**
       ```bash
      git clone https://github.com/ReyKan-KP/Anime-Manga-Recommendation-System-Using-IR.git
  2. **Install dependencies :**
      ```bash
      pip install -r requirements.txt
## Run the Application
1. **Run main.py :**
    ```bash
    python main.py
    ```
2. **Open index.html:**
  `Open index.html preferably with live sever or vite server`

## Usage
- Run the script, and the system will prompt you to indicate whether you are an existing user or not.
- If you are an existing user, you will be asked to enter your User ID.
- Else you are a guest with User ID = 1
- Based on your input, you can either:
  - Enter the description of the Anime/Manga you'd like to read.
  - Get recommendations based on the previous User's watched list.

## Features
  1. **Spell correction for user queries.**
  2. **Document search and ranking.**
  3. **User feedback handling.**
  4. **Web-based interface using Flask.**

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, here's how:

### Kanishaka Pranjal:

- **Features or Improvements:**
  - Describe the features or improvements you added.
  - Mention any challenges you faced and how you overcame them.
  - Provide a brief summary of your contribution.

### Swastik Mukati:

- **Features or Improvements:**
  - Describe the features or improvements you added.
  - Mention any challenges you faced and how you overcame them.
  - Provide a brief summary of your contribution.

### To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License
  This project is licensed under the [MIT License](LICENSE).
## Note
- Make sure to have the necessary CSV files ('main dataset\\main.csv' and 'main dataset\\user_profiles.csv') in the specified directory for data retrieval.

This README provides an overview of the Anime Recommendation System. For more details on the code and functionality, please refer to the code comments and documentation within the script.
