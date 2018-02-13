import json
import os
from flask import Flask, render_template, abort

app = Flask(__name__)
class Files():
    directory = '/home/shiyanlou/files'
    def __init__(self):
        self._result = self._read_files()

    def _read_files(self):
        result={}
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            #get the full path of all files in the directory
            with open(filepath) as f:
                filedata = json.load(f)
                result[filename[:-5]]= filedata
                #-5:remove the last 5 letters in filename, eg for helloworld.json, remove the .json part of the filename
        return result

    def get_title_list(self):
        return [item['title'] for item in self._result.values()]

    def get_file(self, filename):
        return self._result[filename]

files = Files()


@app.route('/')
def index():
    title_list = files.get_title_list()
    return render_template('index.html', title_list = title_list)

@app.route('/files/<filename>')
def file(filename):
    file_item = files.get_file(filename)
    if not file_item:
    #if file_item does not exist
        abort(404)
    return render_template('file.html', file_item=file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__== '__main__':
    app.run()
