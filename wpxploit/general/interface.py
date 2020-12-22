# XMLRPC Exploit
#
# Author : Relarizky
# Github : @relarizky (https://github.com/relarizky)
# File   : interface.py
# Last Modified : 11/27/20, 16:02 PM
#
# Copyright (c) 2020 Relarizky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from sys import exit, argv
from requests import get
from datetime import datetime
from functools import wraps


def current_time():
    time = datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second

    return f"[{hour}:{minute}:{second}]"


def banner(func):
    @wraps(func)
    def banner(*args):
        print("__          _________   __      _       _ _")
        print("\\ \\        / /  __ \\ \\ / /     | |     (_) |")
        print(" \\ \\  /\\  / /| |__) \\ V / _ __ | | ___  _| |_")
        print("  \\ \\/  \\/ / |  ___/ > < | '_ \\| |/ _ \\| | __|")
        print("   \\  /\\  /  | |    / . \\| |_) | | (_) | | |_")
        print("    \\/  \\/   |_|   /_/ \\_\\ .__/|_|\\___/|_|\\__|")
        print("                         | |   [Version 1.0.0]")
        print("                         |_|\n")
        return func(*args)
    return banner


def url_check(func):
    @wraps(func)
    def check(*args):
        url = args[0]
        if not (url.startswith("https://") or url.startswith("http://")):
            print(current_time(), "your url seems to be invalid.")
            exit(1)
        print(current_time(), "URL is valid!")
        return func(*args)
    return check


def connection_check(func):
    @wraps(func)
    def check(*args):
        try:
            url = args[0]
            con = get(url, timeout=5, headers={"user-agent": "mozilla"})
            con.close()
        except Exception:
            print(current_time(), "unable to connect to the target website.")
        else:
            print(current_time(), "connection is successfully establised!")
            return func(*args)
    return check


@banner
def help():
    print("[+] Usage\t: {} <url> <thread> <timeout>".format(argv[0]))
    print("[+] Examlple\t: {} http://target.com/ 5 15".format(argv[0]))
    exit(0)


def get_user_name():
    try:
        print(current_time(), "please provide the username : ", end="")
        user = input()
    except KeyboardInterrupt:
        exit(1)

    return user
