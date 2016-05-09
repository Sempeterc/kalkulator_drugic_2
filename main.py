#!/usr/bin/env python
import os

import jinja2
import webapp2

import kalkulator

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("kalkulator.html")

    def post(self):
        vpisano_stevilo_a = (self.request.get("stevilo_a"))
        vpisano_stevilo_b = (self.request.get("stevilo_b"))
        vpisana_operacija = (self.request.get("operacija"))

        izhodni_podatki = {
            "rezultat": get_izracun(rezultat)
        }


        return self.render_template("rezultat.html", params=izhodni_podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)


