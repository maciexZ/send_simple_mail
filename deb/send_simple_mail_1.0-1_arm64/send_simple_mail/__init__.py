import smtplib
from email.message import EmailMessage


class Mail:

    # creating connection to smtp server
    def __init__(self, address, passwd, smtp, port):
        self.connection = smtplib.SMTP(smtp, port)
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(address, passwd)
        self.address = address

    # creating new message
    def new_message(self, subject, recipient):
        self.msg = EmailMessage()
        self.msg["From"] = self.address
        self.msg["Subject"] = subject
        self.msg["To"] = recipient

    # adding text of email
    def add_content(self, text):
        self.msg.set_content(text)
        ##TODO html formatting

    # adding binary attachment
    # default mime should be overwritten
    def add_attachment_binary(self, path, mimetype="application/octet-stream"):
        with open(path, "rb") as file:
            file_data = file.read()
        self.msg.add_attachment(
            file_data,
            maintype=mimetype[: mimetype.index("/")],
            subtype=mimetype[mimetype.index("/") + 1 :],
            filename=path if "/" not in path else path[path.rindex("/") + 1 :],
        )
        # for x in self.msg.walk():
        #     print(x.is_attachment())
        #     print(x.get_content_type())
        #     print(x.get_filename())
        #     # print(x.as_string())

    # adding simple text attachment
    def add_atachments_plain(self, path):
        with open(path, "r") as file:
            file_data = file.read()
        self.msg.add_attachment(
            file_data,
            filename=path if "/" not in path else path[path.rindex("/") + 1 :],
        )
        # for x in self.msg.walk():
        #     print(x.is_attachment())
        #     print(x.get_content_type())
        #     print(x.get_filename())
        #     print(x.as_string())

    def send_mail(self):
        self.connection.send_message(self.msg)

    def __str__(self):
        attachments = []
        for attachment in self.msg.walk():
            if attachment.is_attachment():
                attachments += (
                    attachment.get_filename(),
                    attachment.get_content_type(),
                )
        return (
            f"MESSAGE\n---------\nFrom: {self.msg['From']}\nto: {self.msg['To']}\n{self.msg.get_body()}\nwith attachments"
            f"{attachments} is ready to be send."
        )

    def __repr__(self):
        return self.msg.as_string()
