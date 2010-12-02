# -*- coding: utf-8 -*-

# based on 
# http://www.tipfy.org/wiki/extensions/auth/twitter/

from tipfy import RequestHandler, Response
from tipfy.ext.auth.twitter import TwitterMixin
from tipfy.ext.auth import MultiAuthMixin
from tipfy.ext.session import AllSessionMixins, SessionMiddleware

class UpdateHandler(RequestHandler, MultiAuthMixin, AllSessionMixins,
        TwitterMixin):
    middleware = [SessionMiddleware]
    
    def post(self):
        # access_token is stored in the auth_session and has keys
        # {'secret': '...', 'user_id': '...', 'screen_name': '...', 'key': '...'}
        access_token = self.auth_session.get('access_token')

        message = self.request.form.get('message').encode('utf8')
        
        try:
            return self.twitter_request(
                '/statuses/update',
                post_args={'status': message},
                access_token=access_token,
                callback=self._on_post)
        except:
            return Response('Error in post(self) tweeting: %s' % self.request.form.get('message') )

    def _on_post(self, new_entry):
        if not new_entry:
            # Call failed. Perhaps missing permission?
            return Response('Error in _on_post tweeting: %s' % self.request.form.get('message') )
        return Response('Success')
