from app import app

def test_home():
    assert app.test_client().get("/").status_code == 200

def test_valid_email():
    r = app.test_client().post("/", data={"name": "Ravi", "email": "ravi@niet.co.in", "course": "DevOps", "feedback": "Great"})
    assert b"Ravi" in r.data

def test_invalid_email():
    r = app.test_client().post("/", data={"name": "Amit", "email": "amit@gmail.com", "course": "DevOps", "feedback": "Bad"})
    assert b"Only @niet.co.in" in r.data
    assert b"Amit" not in r.data