from flask import Flask, request, render_template_string

app = Flask(__name__)
feedbacks = []

HTML = """
<h2>Student Feedback</h2>
<form method="post">
  <input name="name" placeholder="Name" required><br>
  <input name="course" placeholder="Course" required><br>
  <textarea name="feedback" placeholder="Feedback" required></textarea><br>
  <button>Submit</button>
</form>
<h3>Submitted Feedback</h3>
{% for f in feedbacks %}
  <p><b>{{f.name}}</b> ({{f.course}}): {{f.feedback}}</p>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        feedbacks.append(request.form.to_dict())
    return render_template_string(HTML, feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)