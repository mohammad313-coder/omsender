# -*- coding: utf-8 -*-
# Copyright (c) 2017-2018, Aydin Uzmez
#
# This module is part of quickConvert and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
#   File
#    - Author: Aydin Uzmez
#    - File : fusion
#    - Date: Sep 2017


import json
import urllib2
import os

IP = "http://192.168.0.3:14125/api/"
API_KEY = "3DHS33113425CEEX0HXS7FQ3X77S3457"
#ROOM = os.environ["COMPUTERNAME"]+"1231"
USER = os.environ["USERNAME"]
MESSAGECOLOR = "#F7CA18"
TRANSFER = "SERKANA"
#TRANSFER = "BURAKK"


class Message(object):
    def __init__(self,write):
        self.__to_transfer = {
            "from":USER,
            "to":TRANSFER,
            "notify":1,
            "message": "",
        }
        self.__to_user = {
            "from":TRANSFER,
            "to":USER,
            "color": MESSAGECOLOR,
            "notify":1,
            "message": "",
        }
            #"ROOM": ROOM,

        self.url_chat = IP+r"/notify"
        self.write = write

    def to_user(self):
        try:
            self.__to_user["message"] = self.write
            req = urllib2.Request(url=self.url_chat)
            req.add_header('Accept', "application/json, text/javascript, */*")
            req.add_header("API-KEY", API_KEY)
            response = urllib2.urlopen(req, data=json.dumps(self.__to_user))
            json_response = json.load(response)
            print "User {0} sent message, Result: ".format(USER) + str(json_response["success"])
        except urllib2.HTTPError, e:
            print (e.code, e.msg)

    def to_transfer(self):
        try:
            self.__to_transfer["message"] = self.write
            req = urllib2.Request(url=self.url_chat)
            req.add_header('Accept', "application/json, text/javascript, */*")
            req.add_header("API-KEY", API_KEY)
            response = urllib2.urlopen(req, data=json.dumps(self.__to_transfer))
            json_response = json.load(response)
            print "Transfer {0} sent message, Result: ".format(TRANSFER) + str(json_response["success"])
        except urllib2.HTTPError, e:
            print (e.code, e.msg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True
