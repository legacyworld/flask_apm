from flask import Flask, jsonify, request, make_response,send_from_directory
from elasticapm.contrib.flask import ElasticAPM
app = Flask('test')
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'flask',

# Use if APM Server requires a secret token
'SECRET_TOKEN': '',

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': 'http://10.174.0.25:8200',

# Set the service environment
'ENVIRONMENT': 'production',
}
apm = ElasticAPM(app)
@app.route('/api/v1/test/',methods=['GET'])
def test():
    return "Flask OK",200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
