from flask import Flask, request, json, Response, abort

app = Flask(__name__)

@app.route('/v1')
def index():
	return 'Hello World!'


@app.route('/v1/sort', methods=['POST'])
def sort():
	if request.method == 'POST':
		if not request.json:
			return abort(400, 'Content type must be in JSON format')
		else:
			print(request.is_json)
			data = request.get_json()
			print(data['data'])

			# Sorting
			l = len(data['data'])

			for i in range(l):
				for j in range(l-1):
					if data['data'][i] < data['data'][j]:
						data['data'][i], data['data'][j] = data['data'][j], data['data'][i]

			return Response(json.dumps(data), status=200, mimetype="application/json")
		
	else:
		return abort(405)


if __name__ == '__main__':
	app.run(debug=True)