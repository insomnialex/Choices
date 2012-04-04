import json
from food import Food
import tornado.ioloop
import tornado.web


PORT = 80
FOOD = Food()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        arg = FOOD.choose()
        self.render('index.html', args=arg)

    def post(self):
        retVal = 'error'
        req = self.get_argument('req', None)
        arg = self.get_argument('arg', None)
        if req:
            if req == 'add':
                if arg:
                    FOOD.add(arg)
                    retVal = 'success'
            elif req == 'remove':
                if arg:
                    FOOD.remove(arg)
                    retVal = 'success'
            elif req == 'all':
                retVal = json.dumps(FOOD.get_all())
            elif req == 'choose':
                retVal = FOOD.choose()
        self.write(retVal)  


application = tornado.web.Application([
    (r"/", MainHandler)],
    static_path="static",
    debug=True)

if __name__ == "__main__":
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()

