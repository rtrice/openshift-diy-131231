#!/usr/bin/env python
# coding:utf-8

from app import application

if __name__ == '__main__':
    import os, logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', datefmt='[%b %d %H:%M:%S]')
    host = os.environ.get('OPENSHIFT_DIY_IP', '127.0.0.1')
    port = os.environ.get('OPENSHIFT_DIY_PORT', '8080')
    logging.info('local python application serving at %s:%s', host, port)
    from gunicorn.app.wsgiapp import WSGIApplication
    class GunicornApplication(WSGIApplication):
        def init(self, parser, opts, args):
            return {'bind': '%s:%d' % (host, int(port)),
                    'workers': 2,
                    'worker_class': 'gevent'}
        def load(self):
            return application
    GunicornApplication().run()

