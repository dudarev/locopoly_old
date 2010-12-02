from tipfy import Rule

def get_rules(app):
    rules = [
        Rule('/', endpoint='main', handler='apps.locopoly.handlers.IndexHandler'),
        Rule('/about', endpoint='about', handler='apps.locopoly.handlers.AboutHandler'),
        Rule('/twitter/statuses/update', handler='apps.locopoly.handlers_twitter.UpdateHandler'),
    ]

    return rules
