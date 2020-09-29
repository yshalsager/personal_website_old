from personal_website import create_app

import cherrypy

app = create_app()

cherrypy.tree.graft(app, '/')
cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 5000,
                        'engine.autoreload.on': True})

if __name__ == '__main__':
    cherrypy.engine.start()
