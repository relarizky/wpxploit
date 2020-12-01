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


class WordList:
    """ wordlist reader class"""

    def __init__(self, file_name: str, thread_size: int):
        self.name = file_name
        self.size = thread_size

    def __exit__(self, type, value, traceback):
        if type is not None:
            if type is FileNotFoundError:
                print(current_time(), "please input only existing file!")

        self.file_object.close()

        return True

    def __enter__(self):
        self.file_object = open(self.name, "r", encoding="latin1")

        return self

    def create_chunk(self):
        words = self.file_object
        chunk = []
        chunk_size = words.readlines().__len__() // self.size

        # change stream position to the beginning of the file
        words.seek(0)

        while True:
            word = []
            stop = False

            for size in range(chunk_size):
                try:
                    word.append(words.__next__().strip())
                except StopIteration:
                    stop = True
                    break

            chunk.append(word)
            if stop is True:
                break

        return chunk.__iter__()


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
