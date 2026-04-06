from flask import Flask, jsonify
import json
app = Flask(__name__)
file = open("airports-1.json", "r")
data_airports = json.load(file)
@app.route("/airport/<icao_id>")
def information(icao_id):
    icao_id = icao_id.upper()
    if icao_id in data_airports:
        airport = data_airports[icao_id]
        result = {"ICAO": icao_id,
                  "NAME": airport.get("name","Not found the airport"),
                  "CITY": airport.get("city","Not found the city"),
                  "COUNTRY": airport.get("country", "Not found the country")}
        return jsonify(result)
    else:
        error_notice = {"ERROR": "Airport not found.",
                        "MESSAGE": f"The flight code {icao_id} not found."}
        return jsonify(error_notice),404
if __name__ == "__main__":
    print("http://127.0.0.1:5000/airport/LFLL")
    print("http://127.0.0.1:5000/airport/00AK")
    app.run(debug=True)
