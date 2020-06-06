from hyper_internal_service import web

__all__ = ['Server']


class Server(object):

    def __init__(self, port=5601):
        self.port = port
        self.web_application = web.Application()
        self.web_application.add_routes(
            [web.get('/', self.predict)]
        )

    async def predict(self, request):
        data = {'some': 'data'}
        return web.json_response(data)

    def start(self):
        web.run_app(app=self.web_application, port=self.port)
        return True

    def stop(self):
        self.web_application.shutdown()
        self.web_application.cleanup()
        return True