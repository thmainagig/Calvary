from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from flask import current_app
from datetime import datetime

year=datetime.now().year

main_bp=Blueprint('main', __name__)
mail = Mail()

@main_bp.route("/")
def home():
    return render_template('index.html', title='Home', year=year)

@main_bp.route("/about")
def about():
    return render_template('about.html', title='About Us', year=year)

@main_bp.route("/programs")
def programs():
    return render_template('programs.html', title='Programs', year=year)


@main_bp.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if not (name and email and message):
        flash('All fields are required.', 'error')
        return redirect(request.referrer)
    try:
        msg = Message(
            subject=f"Contact Form Submission from {name}",
            sender=email,
            recipients=[current_app.config.get('MAIL_DEFAULT_SENDER')],
            body=f"From: {name} <{email}>\n\n{message}"
        )
        mail.init_app(current_app)
        mail.send(msg)
        flash('Message sent successfully!', 'success')
    except Exception as e:
        flash('Failed to send message. Please try again later.', 'error')
    return redirect(request.referrer)