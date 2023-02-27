from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Austin, TX, USA',
  'salary': '$75,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Dallas, TX, USA',
  'salary': '$95,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, CA, USA',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company="CompSci")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
