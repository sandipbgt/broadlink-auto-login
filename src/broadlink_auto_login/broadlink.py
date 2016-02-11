"""Broadlink hotspot auto login script"""

import requests
from bs4 import BeautifulSoup
import json
import sys
import argparse
import os
from collections import OrderedDict

login_url = 'http://hotspot.broadlink.com.np/login'
status_url = 'http://hotspot.broadlink.com.np/status'
logout_url = 'http://hotspot.broadlink.com.np/logout?'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
    'Referer': 'http://hotspot.broadlink.com.np/login',
    'Host': 'hotspot.broadlink.com.np'
}

def get_file_path():
    path = os.path.join(os.path.expanduser('~'), 'broadlink_accounts.json')
    return path

def login(username, password):
    data = {
        'dst': status_url,
        'username': username,
        'password': password
    }

    response = requests.post(login_url, data, headers=headers)
    page = BeautifulSoup(response.content, "html.parser")
    try:
        message = page.find_all(class_='link3')[2].find_next('div').string
        if message is not None:
            return message.strip()
        return None
    except IndexError:
        return None

def logout():
    requests.get(logout_url)

def get_status():
    response = requests.get(status_url)
    page = BeautifulSoup(response.content, "html.parser")
    try:
        message = page.find_all(class_='link3')[0].string
        if message is not None:
            return message.strip()
        return None
    except IndexError:
        return None

def add_account(username, password):
    f = open(get_file_path(), 'r')
    accounts = json.loads(f.read())
    account = OrderedDict([('username', username), ('password', password)])
    accounts.append(account)
    f.close()

    accounts_json = json.dumps(accounts, indent=4)
    f = open(get_file_path(), 'w')
    f.write(accounts_json)
    f.close()
    print('Account added successfully.')

def setup():
    f = open(get_file_path(), 'w')
    f.write(json.dumps([], indent=4))
    f.close()
    username = input("Enter account username: ").strip()
    password = input("Enter account password: ").strip()
    add_account(username, password)

def start_login():
    # Check if user is already logged in
    message = get_status()
    if message is not None:
        print(message + "\n")
        sys.exit(0)

    # User is not logged in.
    try:
        accounts_file = open(get_file_path(), 'r')
    except FileNotFoundError:
        print('broadlink_accounts.json file not found.')
        print('Creating file...')
        setup()
        accounts_file = open(get_file_path(), 'r')

    accounts = json.load(accounts_file)
    for account in accounts:
        username = account['username']
        password = account['password']

        print("Logging in:\nusername: %s\npassword: %s" % (username, password))
        message = login(username, password)

        if message is None:
            message = get_status()
            print(message + "\n")
            break
        else:
            print(message + "\n")

def main():
    parser = argparse.ArgumentParser(description='Broadlink hotspot auto login command line tool.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-sp', '--setup', help='Initial setup', action='store_true')
    group.add_argument('-a', '--add', help='Add account', action='store_true')
    group.add_argument('-s', '--status', help='Show log in status', action='store_true')
    group.add_argument('-lt', '--logout', help='Logout user', action='store_true')

    parser.add_argument('-u', '--username', help='Login using custom username', default=None, action='store')
    parser.add_argument('-p', '--password', help='Login using custom password', default=None, action='store')

    args = parser.parse_args()

    if args.setup:
        print("Initial setup...")
        setup()
    elif args.add:
        print('Adding account.\n')
        username = input("Enter account username: ").strip()
        password = input("Enter account password: ").strip()
        add_account(username, password)
    elif args.status:
        message = get_status()
        if message is None:
            print('Not logged in...')
        else:
            print(message + "\n")
    elif args.logout:
        print('Logging out...')
        logout()
    elif args.username is not None and args.password is not None:
        message = login(args.username, args.password)
        print(message)
    else:
        start_login()

if __name__ == '__main__':
    main()
