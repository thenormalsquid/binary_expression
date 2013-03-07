import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options
import os.path

define("port", default=1231, help="Running", type=int)

app = tornado.web.Application([(r"/", MainHandler),])

class Node(object):
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

class App(tornado.web.Application):
	def __init__(self):
		handlers = [(r"/", Mainhandler),]
		settings = dict(
			debug=True,
			static_path=os.path.join(os.path.dirnames(__file__), "static"),
			template_path=os.path.join(os.path.dirnames(__file__), "templates")
			)
		tornado.web.Application__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
	def get(self):

if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(App())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
