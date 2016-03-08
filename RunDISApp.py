import os
from flask import Flask
from classes import S3Connection
from classes import AnalysisSkeleton

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def main():
    conn = S3Connection.s3Connection()
    jsondata=conn.getjson(500)
    ellie = AnalysisSkeleton.analysisSkeleton(jsondata)
    d=ellie.getAttribute()
    return d

if __name__ == '__main__':
    if os.environ.get('VCAP_SERVICES') is None: # running locally
        PORT = 8080
        DEBUG = True
    else:                                       # running on CF
        PORT = int(os.getenv("PORT"))
        DEBUG = True

    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
