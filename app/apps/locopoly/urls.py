from tipfy import Rule

def get_rules(app):
    rules = [
        Rule('/', endpoint='main', handler='apps.locopoly.handlers.IndexHandler'),
    ]

    return rules
