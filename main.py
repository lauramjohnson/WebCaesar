#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

def escape_html(text):
    return cgi.escape(text, quote = True)

def page(text_content, rot_content):
    header = "<header><h1>Encrypt this!</hi></header>"

    label_text = "<label>Type a message:  </label><br>"
    textarea = "<textarea name='message'>" + str(text_content) + "</textarea>"

    label_rot = "<label>Rotate by:  </label><br>"
    input_rot = "<input name='rot' value ='" + str(rot_content) + "'/>"

    submit_button = "<input type='submit'/>"

    form = "<form method='post'>" + label_text + textarea + "<br><br>" + label_rot + input_rot + "<br><br>" + submit_button + "</form>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(page("",""))


    def post(self):
        message = self.request.get("message")
        rot = int(self.request.get("rot"))
        encrypted_message = caesar.encrypt(message, rot)
        escaped_encmessage = escape_html(encrypted_message)
        self.response.write(page(escaped_encmessage, str(rot)))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
