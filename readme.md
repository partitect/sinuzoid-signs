# Flask Signal Generator

This is a Flask web application that generates and displays sinusoidal signals based on user input.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (version 3.x) installed on your system.
- pip (Python package manager) installed.

### Installation

1. Clone the repository or download the project files to your local machine.

2. Create a virtual environment to isolate the project's dependencies. You can create a virtual environment using the following command:

   ```shell
   python -m venv venv


Activate the virtual environment:

On Windows:


venv\Scripts\activate
On macOS and Linux:


source venv/bin/activate
Install the required libraries listed in the requirements.txt file using the following command:


pip install -r requirements.txt
Project Structure
Organize your project files and directories as follows:

arduino
Copy code
your_project/
├── app.py
├── static/
│   ├── sinuzoid-frequency.png
│   └── sinuzoid-arrange.png
├── templates/
│   ├── index.html
│   ├── frekans.html
│   ├── arrange.html
│   ├── resultfreqency.html
│   └── resultarrange.html
└── requirements.txt
Running the Application
In your project directory, run the Flask application using the following command:

flask run
The Flask development server will start, and you'll see output indicating the server is running. Access the app in your web browser at the provided URL, typically something like http://127.0.0.1:5000/.

Using the Application
Navigate to the different routes (/, /frekans, /arrange) to interact with the web application and see the results.
Stopping the Application
To stop the Flask development server, press Ctrl+C in your terminal.
Authors
Telat Kaya
License
This project is licensed under the MIT - see the LICENSE.md file for details.
