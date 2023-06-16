# Machine Learning FastAPI⚡ - README.md

This repository contains a Machine Learning FastAPI project that implements sentiment analysis and rating prediction based on user input. The project provides an API with two endpoints: `/predict_review` for sentiment analysis and `/new_ratings` for predicting new ratings based on sentiment analysis results.

## Prerequisites📝

Before running the project, make sure you have the following:

- Python 3.x installed 🐍
- Required dependencies installed. You can install them by running the following command:
  ```
  pip install -r requirements.txt
  ```
- `nlp_model.h5` file or download via [this link](https://drive.google.com/drive/folders/1uMxvLDZasS30YuTvc7Ng2sGkp7mbeO3O?usp=sharing)

## Usage ⚙️

To start the server and use the API, follow these steps:

1. Ensure all the prerequisites are met.✅
2. Open a terminal or command prompt in the project directory.
3. Run the following command to start the server:
   ```
   python main.py
   ```
   The server will start running at `http://localhost:8080`.

## API Endpoints 🔗

### Health Check Endpoint 🚑

- **Endpoint:** `/`
- **Method:** GET
- **Description:** A test endpoint to check if the server is running.
- **Response:** Returns a simple "Hello world from ML endpoint!" message.

### Sentiment Analysis Endpoint 🔮

- **Endpoint:** `/predict_review`
- **Method:** POST
- **Description:** Predicts sentiment analysis based on the given text.
- **Request Body:**
  - `text` (str): The text to analyze.
- **Response:** Returns the predicted sentiment as a string. Possible values are "Positive", "Neutral", or "Negative". If an error occurs during prediction, it returns an "Internal Server Error" message.

### Rating Prediction Endpoint ✨

- **Endpoint:** `/new_ratings`
- **Method:** POST
- **Description:** Predicts new ratings for a user based on a list of user ratings and a sentiment analysis result.
- **Request Body:**
  - `predicted` (str): The sentiment analysis result (e.g., "Positive", "Neutral", "Negative").
  - `user_rating` (list): A list of user ratings.
- **Response:**
  - `total_rating` (float): The updated overall rating.
  - `new_ratings` (list): The list of user ratings with the new rating appended.
- **Response Model:** `ResponseRating`
- **Response Model Fields:**
  - `total_rating` (float): The updated overall rating.
  - `new_ratings` (list): The list of user ratings with the new rating appended.

## Additional Notes 📜

- If this is your first time running the project, make sure to install the required dependencies by running `pip install -r requirements.txt`.
- You can access the API documentation easily by visiting `http://localhost:8080/docs` in your browser after starting the server.
- The model used for sentiment analysis can be either an h5 model (`nlp_model.h5`) or a saved model (`my_model_folder`). Make sure to uncomment the appropriate line in `main.py` based on the model type you are using.

## Contributing ✍️

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author 👤

- [Alif](https://github.com/muhammadalifalfarizi)
- [Dafa](https://github.com/daptheHuman)
- [Anin](https://github.com/peachaen)
