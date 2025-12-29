import smtplib

sender = "RiivoMaadla@hotmail.com"
receiver = "RiivoMaadla@gmail.com"
password = "parool emaililt"    # selle jaoks et seda kasutada peab g maili  security -> less secure log in
subject = "Python e mail test"  #                                            less secure app accsess
body = "I wrote an email :D from my py file"


# this is our header
message = f"""From: {sender}
To: Riivo Maadla {receiver}
Subject:{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:
    server.login(sender, password)
    print("Logged in ...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")

except smtplib.SMTPAuthenticationError:
    print("Unable to log in")







