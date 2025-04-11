from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from app import mail, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            msg = Message('New Contact Form Submission',
                        sender=email,
                        recipients=['ankith3690@gmail.com'])
            msg.body = f"""
            From: {name}
            Email: {email}
            Message: {message}
            """
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('An error occurred while sending your message. Please try again.', 'error')
        
    return redirect(url_for('main.index')) 