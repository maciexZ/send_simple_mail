# send_simple_mail
very simple python package and script for sending emails from cli and scripts via own email.
Requires python >3.6.

### manual installation (linux)
Sender credentials must be in ``~/.config/send_simple_mail/config``. Create directory ``~/.config/send_simple_mail`` and put there config file (ini format) with your settings. 

Install package (inside dir with ``send_simple_mail`` and ``setup.py``):

```pip install .``` or ```pip3 install .```

Make ``send_mail.py`` executable and put it in ``/usr/local/bin/`` or ``~/bin/`` or in other dir from ``PATH``. Optionaly change name to ``send_mail``.

And you are good to go.

## Examples
Sending email from a default addres with binary attachment and text file
```
send_mail -a ijon_tichy@startraveler.com -s "Ijon come back" -t "Dear, Ijon we are missing you!" -fb home.jpeg -f letter_to_ijon.txt
```
Sending email from an another address defined in config file (not DEFAULT)
```
send_mail -es ADMIN -a ijon_tichy@startraveler.com -s "Ijon come back" -t "Dear, Ijon we are missing you!" -fb home.jpeg -f letter_to_ijon.txt
```
Sending email to many recipients with a log message. One email to scare them all
```
#!/bash/bin
...
send_mail -a maciex@solaris.com agatex@solaris.com admin@solaris.com -s WARNING -t "there seems to be a critical problem" -f logfile
```


#### IMPORTANT: be aware that your email password is stored in textfile. Use with caution.
