import sys
import logging
import json
from datetime import timedelta
from flask import Flask, request, jsonify, render_template

logging.getLogger().setLevel(logging.INFO)
app = Flask(__name__, static_folder='static')
app.send_file_max_age_default = timedelta(seconds=5)


@app.route('/', methods=['GET'])  # 添加路由
def index():
    return jsonify({"hello": "hello world_liwei111"})


@app.route('/postTest', methods=['POST'])  # 添加路由
def post_test():
    data_raw = request.get_data()
    try:
        data = json.loads(data_raw)
    except json.decoder.JSONDecodeError as e:
        return jsonify({"code": 403, "data": None, "msg": "格式错误"})
    return jsonify({"received_data": data})


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # logging.error("usage: %s port" % (sys.argv[0]))
        # sys.exit(-1)
        p = 8080
    else:
        p = int(sys.argv[1])
    logging.info("start at port %s" % p)
    if sys.platform == "linux":
        app.run(host='::', port=p, debug=True, threaded=True)
    else:
        app.run(host='0.0.0.0', port=p, debug=True, threaded=True)