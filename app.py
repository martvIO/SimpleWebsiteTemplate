import os
from website import create_app

# Get the secret key from environment variables
key = os.getenv('key')

# Create the Flask application instance using the secret key
app = create_app(key)

if __name__ == '__main__':
    # run the website
    app.run(debug=True)