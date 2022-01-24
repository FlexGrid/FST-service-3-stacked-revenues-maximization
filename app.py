#!/usr/bin/env python3

import connexion

from swagger_server.encoder import JSONEncoder

app = connexion.App(__name__, specification_dir='./swagger_server/swagger/')

app.app.json_encoder = JSONEncoder
 #   app.add_api('swagger.yaml', arguments={'title': 'Flexgrid ATP API'}, pythonic_params=True)
app.add_api('swagger.yaml', arguments={'title': 'Flexgrid Ppicing API'}, pythonic_params=True,strict_validation=True, validate_responses=True)

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080)
