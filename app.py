from flask import Flask, request, render_template_string

app = Flask(__name__)
feedbacks = []

HTML = """
<h2>Student Feedback</h2>
<form method="post">
  <input name="name" placeholder="Name" required><br>
  <input type="email" name="email" placeholder="Email (@niet.co.in)"
         pattern=".+@niet\\.co\\.in" title="Use your @niet.co.in email" required><br>
  <input name="course" placeholder="Course" required><br>
  <textarea name="feedback" placeholder="Feedback" required></textarea><br>
  <button>Submit</button>
</form>
{% if error %}<p style="color:red">{{error}}</p>{% endif %}
<h3>Submitted Feedback</h3>
{% for f in feedbacks %}
  <p><b>{{f.name}}</b> ({{f.email}}, {{f.course}}): {{f.feedback}}</p>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        data = request.form.to_dict()
        if data.get("email", "").lower().endswith("@niet.co.in"):
            feedbacks.append(data)
        else:
            error = "Only @niet.co.in email addresses are allowed."
    return render_template_string(HTML, feedbacks=feedbacks, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)