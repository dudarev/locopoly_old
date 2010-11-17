# -*- coding: utf-8 -*-
from tipfy import RequestHandler, cached_property, redirect
from tipfy.ext.jinja2 import render_response
from models import Post

from tipfy.ext.wtforms import Form, fields, validators
from tipfy.ext.auth import MultiAuthMixin, login_required, user_required
from tipfy.ext.session import AllSessionMixins, SessionMiddleware
from tipfy.ext.jinja2 import Jinja2Mixin


class IndexHandler(RequestHandler, MultiAuthMixin, Jinja2Mixin,
        AllSessionMixins):
    middleware = [SessionMiddleware]

    def render_response(self, filename, **kwargs):
        auth_session = None
        if 'id' in self.auth_session:
            auth_session = self.auth_session

        ctx = self.request.context
        locale = ctx.get('locale', None)
        if not locale:
            locale = 'en'

        self.request.context.update({
            'auth_session': auth_session,
            'current_user': self.auth_current_user,
            'login_url':    self.auth_login_url(),
            'logout_url':   self.auth_logout_url(),
            'current_url':  self.request.url,
            'locale': locale,
        })

        return super(IndexHandler, self).render_response(filename, **kwargs)

    def get(self):
        return self.render_response('locopoly/index.html')
