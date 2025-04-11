from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from email_validator import validate_email, EmailNotValidError
from flask_wtf import FlaskForm
from app import mail, db, csrf

main = Blueprint('main', __name__)
limiter = Limiter(key_func=get_remote_address)

class ContactForm(FlaskForm):
    pass

@main.route('/')
def index():
    form = ContactForm()
    return render_template('index.html', form=form)

@main.route('/contact', methods=['POST'])
@limiter.limit("5 per hour")  # Limit to 5 submissions per hour per IP
def contact():
    form = ContactForm()
    if not form.validate_on_submit():
        flash('Invalid form submission.', 'error')
        return redirect(url_for('main.index'))

    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()
    
    # Input validation
    if not all([name, email, message]):
        flash('All fields are required.', 'error')
        return redirect(url_for('main.index'))
    
    # Email validation
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError:
        flash('Please enter a valid email address.', 'error')
        return redirect(url_for('main.index'))
    
    # Message length validation
    if len(message) < 10:
        flash('Message must be at least 10 characters long.', 'error')
        return redirect(url_for('main.index'))
    
    try:
        msg = Message('New Contact Form Submission',
                    sender=('Portfolio Contact Form', email),
                    reply_to=email,
                    recipients=['ankith3690@gmail.com'])
        msg.body = f"""
        New message from your portfolio website:
        
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        mail.send(msg)
        flash('Your message has been sent successfully! I will get back to you soon.', 'success')
    except Exception as e:
        flash('An error occurred while sending your message. Please try again later.', 'error')
    
    return redirect(url_for('main.index')) 