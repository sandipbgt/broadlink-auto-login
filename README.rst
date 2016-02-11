broadlink-auto-login
====================

A Python module to login to broadlink hotspot automatically.
If you have ever found it boring to enter the username and password for broadlink hotspot login page then **broadlink-auto-login** app can help
you. Just specify your username and password in a config file and type `broadlink` anywhere from your terminal to login to the broadlink hotspot page
automatically. This app also supports multiple username and password. If you use multiple accounts to login to broadlink hotspot page, then you can
specify all of those usernames and passwords in a single file and this script will try to login each account from top, once the login is successfull,
it stops automatically and you can browse internet. 

Installation
------------

- `broadlink-auto-login` can be installed using pip
- You will need `python3` and `pip3`.

::

    $ sudo pip3 install broadlink_auto_login

Usage
-----

- To start initial setup
::

	$ broadlink --setup

- To add your account username and passsword to config file. The username and passwords are stored in `broadlink_accounts.json` file in your home folder.
::

	$ broadlink --add

- To get your current login status.
::

	$ broadlink --status

- To logout.
::

	$ broadlink --logout

- To supply custom username and password from commandline without storing it in config file. 
::

	$ broadlink --username YOUR_USERNAME --password YOUR_PASSWORD

	
Advanced Usage
-------------

usage: broadlink [-h] [-sp | -a | -s | -lt] [-u USERNAME] [-p PASSWORD]

Broadlink hotspot auto login command line tool.

optional arguments:
  -h, --help            show this help message and exit
  -sp, --setup          Initial setup
  -a, --add             Add account
  -s, --status          Show log in status
  -lt, --logout         Logout user
  -u USERNAME, --username USERNAME
                        Login using custom username
  -p PASSWORD, --password PASSWORD
                        Login using custom password


Contribution
------------

Feel free to create a Github issue. Also, you are more than welcome to submit
a pull request for a bug fix or additional feature.