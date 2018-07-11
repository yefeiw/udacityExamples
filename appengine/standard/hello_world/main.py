# Copyright 2016 Google Inc.
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

import webapp2

form = """
<form method="POST">
    What is your birthday?
    <br>
    <label> Month
    <input type="text" name="month">
    </label>
    <label> Day
    <input type="text" name="day">
    </label>
    <label> Year
    <input type="text" name="year">
    </label>
    <br>
    <br>
    <input type="submit">
</form>
"""
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):

    month_abbvs = dict((m.lower(), m) for m in months)
    if month_abbvs.has_key(month.lower()):
        return months[month_abbvs.get(month.lower())]
    else:
        return None


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

    def post(self):
        self.response.out.write("Thanks! That is a totally valid day")


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
