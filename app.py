from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

from youtube_search import YoutubeSearch

import subprocess
import hashlib 
import uuid

app = Flask(__name__, template_folder='templates', static_url_path='')

@app.route('/audio/<path:path>')
def send_js(path):
    return send_from_directory('audio/', path)


@app.route('/play', methods = ['POST'])
def play():
    suffix = request.json.get('suffix')
    url = "https://youtube.com/{}".format(suffix)
    filename = str(uuid.uuid1())
    filename = "audio/{}.mp3".format(filename)
    params = ['youtube-dl',
            '-x',
            '--audio-format',
            'mp3',
            url,
            "--output",
            filename]
    process = subprocess.Popen(params,
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        return "error"
    return filename


@app.route('/', methods = ['GET', 'POST'])
def main():
    videos = False
    search = False
    if request.method == 'GET':
        search = request.args.get('search', default="", type=str)
        print(search)
        if search:
            videos = YoutubeSearch(search, max_results=30).to_dict()
    return render_template('base.html', results=videos, search=search)


if __name__ == '__main__':
    app.run()
