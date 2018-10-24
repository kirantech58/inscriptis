#!/usr/bin/env python3
# coding:utf-8
'''
Inscriptis Web Service
'''

from flask import request, Response, Flask
from inscriptis import get_text

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/get_text", methods=['POST'])
def get_text_call():
    content_type = request.headers['Content-type']
    if '; encoding=' in content_type:
        encoding = content_type.split('; encoding=')[1]
    else:
        encoding = 'UTF-8'
    html_content = request.data.decode(encoding, errors='ignore')
    text = get_text(html_content,
                    display_images=True,
                    deduplicate_captions=True,
                    display_links=False)
    return Response(text, mimetype='text/plain')

@app.route("/get_content", methods=['POST'])
def get_content_call():
    content_type = request.headers['Content-type']
    if '; encoding=' in content_type:
        encoding = content_type.split('; encoding=')[1]
    else:
        encoding = 'UTF-8'
    html_content = request.data.decode(encoding, errors='ignore')
    url = 'test-url'
    text = get_text(html_content,
                    url)
    return Response(text, mimetype='text/plain')


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
