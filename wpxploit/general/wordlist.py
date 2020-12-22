# XMLRPC Exploit
#
# Author : Relarizky
# Github : @relarizky (https://github.com/relarizky)
# File   : wordlist.py
# Last Modified : 12/1/20, 01:33 AM
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


import os
from wpxploit.general.interface import current_time


def show_word_list():

    DIR = "wordlist/"  # default dir of wordlist

    def filter_dir(element):
        """ eliminate directory in file list """

        return os.path.isfile(DIR + element)

    list_file = os.listdir(DIR)
    list_file = list(filter(filter_dir, list_file))
    list_file = list(map(lambda file: DIR + file, list_file))

    try:
        for count in range(len(list_file)):
            content = list_file[count]
            print(current_time(), "{}. {}".format(str(count), content))
        else:
            print(current_time(), "select your file number : ", end="")
            user_input = int(input())
    except (KeyboardInterrupt, ValueError):
        os._exit(1)

    return list_file[user_input]


def read_word_list(file_name: str, size: str) -> list:
    """
    generator for creating wordlist chunk
    """

    with open(file_name) as file:
        word_char = file.readlines().__iter__()
        word_size = word_char.__length_hint__() // size

        # put the stream point in the beginning of the file
        file.seek(0)

        while word_char.__length_hint__() != 0:
            chunk = []
            stops = False
            for word in range(word_size):
                try:
                    chunk.append(word_char.__next__().strip())
                except StopIteration:
                    stops = True
                    break

            yield chunk
