# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado
import tornado.web


# 定义一个阶乘服务对象
class FactorialService(object):
  def __init__(self):
    self.cache ={}  # 用字典记录已经计算过的阶乘

  def calc(self,n):
    if n in self.cache: # 如果有直接返回
      return self.cache[n]
    s = 1
    for i in range(1,n):
      s *= i
    self.cache[n] = s # 缓存起来
    return s


class FactorialHandler(tornado.web.RequestHandler):
  #new出阶乘服务对象
  service = FactorialService()

  def get(self):
    # 获取url的参数值,此处用?参数传参
    n = int(self.get_argument("n"))
    # 使用阶乘服务
    self.write(str(self.service.calc(n)))

def make_app():
  return tornado.web.Application([
    (r"/fact",FactorialHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(8000)
  tornado.ioloop.IOLoop.current().start()
