# 🏗️ **Flask Application Runner**

Welcome to the **Flask Application Runner**! This script initializes and runs your Flask application, making it easy to get your web service up and running.

---

## 📝 **Features**

- **Application Initialization**: Creates an instance of your Flask application using a secret key.
- **Environment-Based Configuration**: Retrieves the secret key from environment variables for secure application setup.
- **Debug Mode**: Runs the application in debug mode for easier development and debugging.

---

## 🛠️ **Setup**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-repo/flask-app-runner.git
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then install Flask:

   ```bash
   pip install Flask
   ```

3. **Create Environment Files**:
   - **.env**: Create a `.env` file in the root directory of your project to store environment variables. Add your secret key like this:
     ```ini
     key=your-secret-key
     ```
   - **.gitignore**: Ensure that your `.env` file is included in the `.gitignore` to avoid committing sensitive information to your version control. Add the following line to your `.gitignore` file:
     ```gitignore
     .env
     ```

---

## 🚀 **Usage**

### **Run the Application**

1. **Set Up Environment Variables**:
   Make sure your environment variables are correctly set up in the `.env` file.

2. **Run the Application**:
   Execute the `app.py` script to start the Flask application in debug mode.
   ```bash
   python app.py
   ```

---

## 🧠 **How It Works**

1. **Retrieving the Secret Key**:

   - The script uses the `os.getenv` function to retrieve the secret key from environment variables. This key is essential for securing session data.

   ```python
   key = os.getenv('key')
   ```

2. **Creating the Flask Application**:

   - The `create_app` function from the `website` module is used to initialize the Flask application instance with the secret key.

   ```python
   app = create_app(key)
   ```

3. **Running the Application**:

   - The `app.run(debug=True)` command starts the Flask development server in debug mode, which provides detailed error logs and auto-reloading.

   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

---

## 📚 **Additional Files**

### **.gitignore**

The `.gitignore` file tells Git which files and directories to ignore. It's essential for keeping sensitive information and unnecessary files out of your version control system. For example, you should include the `.env` file in `.gitignore` to prevent it from being committed:

```gitignore
.env
```

### **.env**

The `.env` file is used to store environment variables that should not be hardcoded into your source code. It helps manage configurations securely and makes it easier to handle different environments (development, testing, production). In your case, it stores the secret key used for your Flask application:

```ini
key=your-secret-key
```

---

## 📝 **License**

This project is licensed under the MIT License.

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to submit a pull request with improvements or fixes.

---

Happy coding with Flask! 🚀

---
