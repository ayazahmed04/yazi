import random 
from config.settings import USER_AGENTS

class Middleware:
    def get_user_agent(self):
        """Return a random user agent from the list"""
        return random.choice(USER_AGENTS)

    def apply(self, headers):
        """Modify Request Header e.g.< rotating user agents"""
        headers['User-Agent'] = self.get_user_agent()
        return headers
