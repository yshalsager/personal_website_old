from cheroot.wsgi import Server

from personal_website import create_app

import cherrypy

app = create_app()

cherrypy.tree.graft(app, '/')
cherrypy.config.update({'engine.autoreload.on': True})
server = Server(('127.0.0.1', 5000), cherrypy.tree, server_name='XFU/1.1.0')

if __name__ == '__main__':
    server.start()
