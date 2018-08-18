# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado
import tornado.web


class FactorialService(object):
  def __init__(self):
    self.cache ={}

  def calc(self,n):
    if n in self.cache:
      return self.cache[n]
    s = 1
    for i in range(1,n):
      s *= i
    self.cache[n] = s
    return s


class FactorialHandler(tornado.web.RequestHandler):

  service = FactorialService()

  def get(self):
    n = int(self.get_argument("n"))
    self.write(str(self.service.calc(n)))

def make_app():
  return tornado.web.Application([
    (r"/fact",FactorialHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.ioloop.IOLoop.current().start()
