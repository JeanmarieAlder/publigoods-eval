# User Evaluation Web Application

This web application is designed for user evaluation, allowing users to test two different ways of selecting an appointment time. The project is part of the Master course in User-Centered Design at the University of Fribourg.


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

4. Use Jupyter notebooks.

- Step 2 (install dependencies) should be done.
- Make sure to install jupyter notebook **inside virtual env**: ```pip install notebook```
- Set the virtual environment as a Jupyter Kernel: ```python -m ipykernel install --user --name=venv``` (adapt name according to you virtual env name)
- Start notebook using ```jupyter notebook```
- When selecting a notebook, make sure to select the venv kernel.

5. Open your web browser and navigate to `http://localhost:5000/` to access the application.

## Additional Information

- **Session Handling:**
  - Session data is stored, and the `pop` or `del` method can be used to remove items from the session.

- **Styling:**
  - Styling is defined in the `styles.css` file in the `static/styles` directory.

## License

This project is licensed under the [MIT License](LICENSE).
