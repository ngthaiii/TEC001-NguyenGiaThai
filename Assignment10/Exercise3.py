from flask import Flask, jsonify
app = Flask(__name__)
def check_num(i):
    if i <= 1:
        return False
    if i <= 3:
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    n = 5
    while n * n <= i: #check the square root
        if i % n == 0 or i % (n + 2) == 0:
            return False
        n += 6
    return True
@app.route("/prime_number/<num>")
def prime_num(num):
    result = check_num(int(num))
    data = {"Number":num, "isPrime": result}
    return jsonify(data)
if __name__ == "__main__":
    print("http://127.0.0.1:5000/prime_number/31")
    print("http://127.0.0.1:5000/prime_number/1")
    app.run(debug=True)