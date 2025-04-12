# Portfolio Website

A modern, responsive portfolio website built with Flask and HTML5 UP template, showcasing my projects, skills, and accomplishments.

## Features

- 🎨 Modern, responsive design
- 💼 Project showcase
- 📝 Dynamic contact form with email integration
- 🚀 Skills and accomplishments section
- 📱 Mobile-friendly interface

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Email**: Flask-Mail
- **Template**: HTML5 UP

## Setup and Installation

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following:
   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-specific-password
   SECRET_KEY=your-secret-key
   ```

4. Run the application:
   ```bash
   python run.py
   ```

The website will be available at `http://localhost:5000`

## Project Structure

```
portfolio/
├── app/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   └── routes.py
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

## License

This project is open source and available under the MIT License. 