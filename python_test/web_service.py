import os
from http import HTTPStatus
from flask import Flask, request, abort
import main, test1
import json
import logger
import logging
from logging.handlers import SMTPHandler
from flask.logging import default_handler
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/search", methods=["POST"])
def post():
    try:
    # if "/" in filename:
    #     abort(400, "no subdirectories directories allowed")
        searcher = test1.searcher()
        return_state, result = searcher.main(request.data)
        res = {'statusCode':return_state,'data':result}
    #    jsonResult = json.loads(res)
        status = 200
        if return_state == HTTPStatus.OK:
            status = 200
        else:
            if return_state == 1000 or return_state == 1003 :
                status = 400
            elif return_state == 1001:
                status = 511
            elif return_state == 1002 or return_state == 1004:
                status = 503
            elif return_state == 1005:
                status = 500
            elif return_state == 1006:
                status = 404
            print('shit')
            lgr = logger.logger()
            lgr.mailLogger(res, status, "Search API")
            print('Activity Logged To The SMTP Server')
        return res, status
    except Exception as e:

        lgr = logger.logger()
        lgr.mailLogger(str(e), 500, "Search API")
        print('Activity Logged To The SMTP Server')
        return str(e), 500
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=False, threaded=True)
