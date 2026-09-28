from app import app

def test_home():
    assert app.test_client().get("/").status_code == 200

def test_submit():
    r = app.test_client().post("/", data={"name": "Ravi", "course": "DevOps", "feedback": "Great"})
    assert b"Ravi" in r.data