# How to contribute to the project
(eMobilis class (GO 2:00pm) assignment)

Prerequisites

    Python 3.8+
    Git
    Bootstrap: The project uses Bootstrap locally, so make sure you have it downloaded in the appropriate directory. (More info below.)

Getting Started
1. Clone the Repository

    Clone the  repository to your local machine.

# For Linux and macOS
```
git clone https://github.com/jeffx-3/Project1.git

```

# For Windows (Git Bash)
```
git clone https://github.com/jeffx-3/Project1.git
```

Navigate into the project directory:

    cd Project1

2. Set Up a Virtual Environment

We  set up a virtual environment to manage dependencies.

# Linux and macOS
```
python3 -m venv venv
source venv/bin/activate
```

# Windows (Command Prompt)
```
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies

Once your virtual environment is activated, install the project dependencies:

# Linux, macOS, and Windows
```
pip install -r requirements.txt
```


4. Add Bootstrap Locally

Download Bootstrap and save it in the project’s static directory (or as specified in your settings.py file).

    Download the Bootstrap CSS and JavaScript files.

    Place the files in the following structure (example):

project_root/
└── static/
    └── bootstrap/
        ├── css/
        │   └── bootstrap.min.css
        └── js/
            └── bootstrap.bundle.min.js

Update your HTML templates to include Bootstrap:

    <!-- Example in your base template -->
  
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    <script src="{% static 'bootstrap/js/bootstrap.bundle.min.js' %}"></script>

5. Configure the Database

Run the migrations to set up the database:

# Linux, macOS, and Windows
```
python manage.py migrate
```

6. Run the Development Server

Now that everything is set up, you can run the development server to verify your installation:

# Linux, macOS, and Windows
```
python manage.py runserver
```

Open http://localhost:8000 in your browser to view the project.

# Contribution Guidelines

    Create a Branch:
        Create a new branch for each feature or bug fix.
```git
git checkout -b your-branch-name
```

Make Your Changes:

    Ensure your code follows PEP 8 guidelines.
    Run tests and linting checks to verify your changes.

Commit Your Changes:

    Write clear, concise commit messages.
```git
git add .
git commit -m "Your detailed commit message here"
```

Push Your Changes:

    Push to the repository.
```git
    git push origin your-branch-name
```

    Submit a Pull Request:
        Create a pull request to the main repository.
        Include a detailed description of the changes you've made.

Running Tests

To run tests, use the following command:

# Linux, macOS, and Windows
```
python manage.py test

