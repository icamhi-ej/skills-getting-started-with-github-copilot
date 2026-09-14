from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "student@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == f"Removed {email} from {activity_name}"

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    assert email not in activities_response.json()[activity_name]["participants"]
