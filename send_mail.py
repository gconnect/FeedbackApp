import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port=2525
    smtp_server = 'smtp.mailtrap.io'
    username = 'e18b0a5be4374c'
    password = '8b9e56dd0b2d45'
    message = f"<h3> New Feedback Submission</h3> <ul><li>Customer: {customer} </li> <li>Dealer: {dealer} </li><li>Rating: {rating} </li><li>Comments: {comments}</li></ul>"
    sender_email = 'email1@example.com'
    receiver_email = '116b94e2c3-0ffc83@inbox.mailtrap.io'
    msg = MIMEText(message, 'html')
    msg['subject'] = 'Payowners Feedback Form'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
