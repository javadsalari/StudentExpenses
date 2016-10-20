import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from urls import urlList

define("port", default=8092, help="run on the given port", type=int)


class EducationPortal(tornado.web.Application):
    def __init__(self):
        handlers = urlList
        settings = dict(
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(EducationPortal())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
