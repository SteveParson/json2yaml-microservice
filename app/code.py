import web
import sys
import json
import yaml

urls = (
        '/', 'index'
)

class index:
    def POST(self):
        i = web.data()
        j = json.loads(i)
        return yaml.safe_dump(j)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

