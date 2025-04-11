# Ankith R's Portfolio Website

A modern, responsive portfolio website built with Flask and HTML5 UP template, showcasing my projects, skills, and accomplishments.

## Features

- 🎨 Modern, responsive design
- 💼 Project showcase with GitHub integration
- 📝 Dynamic contact form with email integration
- 🚀 Skills and accomplishments section
- 📱 Mobile-friendly interface

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
- **Email**: Flask-Mail
- **Template**: HTML5 UP
- **Deployment**: Ready for deployment on any Python-compatible hosting

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/XelpiCode/portfolio.git
   cd portfolio
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following:
   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-specific-password
   SECRET_KEY=your-secret-key
   ```

5. Run the application:
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
├── README.md
└── run.py
```

## Contact

- Email: ankith3690@gmail.com
- GitHub: [@XelpiCode](https://github.com/XelpiCode)
- Location: Cherthala, Kerala, India

## License

This project is open source and available under the [MIT License](LICENSE). 