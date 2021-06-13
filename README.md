# send_simple_mail
Very simple python package and script for sending emails via own email address from cli and scripts.

Sender credentials must be in ``~/.config/send_simple_mail/config`` 

Install package (dir with ``send_simple_mail`` and ``setup.py``)

```pip install .``` or ```pip3 install .```

Make ``send_mail`` executable and put it in ``/usr/local/bin/`` or ``~/bin/``.

## Examples
Sending email from a default addres with binary attachment and text file
```
send_mail -a ijon_tichy@startraveler.com -s "Ijon come back" -t "Dear, Ijon we are missing you!" -fb home.jpeg -f letter_to_ijon.txt
```
Sending email from an another address defined in config file
```
send_mail -es ADMIN -a ijon_tichy@startraveler.com -s "Ijon come back" -t "Dear, Ijon we are missing you!" -fb home.jpeg -f letter_to_ijon.txt
```
Sending email to many recipients with a log message to scare them all
```
#!/bash/bin
...
send_mail -a maciex@solaris.com agatex@solaris.com admin@solaris.com -s WARNING -t "there seems to be a critical problem -f logfile
```


#### IMPORTANT: be aware that your email password is stored in textfile. Use with caution.
