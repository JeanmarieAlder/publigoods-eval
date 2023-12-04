# User Evaluation Web Application

This web application is designed for user evaluation, allowing users to test two different ways of selecting an appointment time. The project is part of the Master course in User-Centered Design at the University of Fribourg.

## Features

- **Index Page:**
  - Title: "Publigoods - User Evaluation"
  - Introduction paragraph explaining the purpose of the evaluation.
  - Optional name field for users.
  - Button to start the quiz and redirect to `/instructions`.

- **Instructions Page (`/instructions`):**
  - Explanation of using Publigoods for lending and borrowing tools.
  - User is asked to select the time 16:20 using the time picker.
  - Button to start the time picker at `/timepicker/0`.

- **Time Picker Page (`/timepicker/0`):**
  - HTML table with two columns displaying hours and corresponding quarters.
  - Buttons in the second column are initially invisible and disabled.
  - Buttons become visible and enabled when a plain hour is clicked.
  - Ability to select a quarter by clicking the corresponding button.
  - Selected button is colored green, and green color is removed from other buttons if any was selected before.

- **Thank You Page (`/thank_you`):**
  - Displays a thank you message.
  - Background image set to `thank_you.jpeg`.
  - Text styled with black color, white border, and improved visual appearance.

- **Quizz Page (`/quizz`):**
  - A set of three placeholder questions with labels and input fields.
  - Submit button that redirects to `/thank_you`.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/user-evaluation-app.git
    ```

2. Install dependencies (+ venv):

    ```bash
    cd user-evaluation-app
    python -m venv venv
    (Enter virtual env, different on all systems.)
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your web browser and navigate to `http://localhost:5000/` to access the application.

## Additional Information

- **Session Handling:**
  - Session data is stored, and the `pop` or `del` method can be used to remove items from the session.

- **Styling:**
  - Styling is defined in the `styles.css` file in the `static/styles` directory.

## License

This project is licensed under the [MIT License](LICENSE).
