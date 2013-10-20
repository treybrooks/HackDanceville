from tg import expose, app_globals as g
from danceserver.lib.base import BasePluginController
from hackdanceville.move import Move


class BombermanController(BasePluginController):

    def __init__(self, api):
        super(BombermanController, self).__init__(api)
        self.key_conversions = {
            37: 260,
            38: 259,
            39: 261,
            40: 258,
            67: 99,
            81: 113
        }
        self.bomber = Move()

    @expose('danceserver.plugins.bomberman.templates.index')
    def index(self):
        g.kill_loops_not_in('bomberman')
        self.bomber.initialize_loop()
        g.add_loop('bomberman', self.bomber.loop)
        return {}

    @expose()
    def keypress(self, key):
        key = int(key)
        key = self.key_conversions.get(key, key)
        self.bomber.put(key)
        if not self.bomber.go:
            return 'gameover'