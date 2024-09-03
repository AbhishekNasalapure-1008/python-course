import smtplib


my_email='tejasrnaik2005@gmail.com'
password='zklt cpnp xipb ltax'

with smtplib.SMTP('smtp.gmail.com',587) as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=password
    )
    connection.sendmail(
        from_addr=my_email,
        to_addrs='pchitale6@gmail.com',
        msg=f'Subject: My first mail from python \n\n Hi from python code'

    )
    print('sent')
