from locust import HttpUser, task, between
import random
from datetime import datetime, timedelta

class ConcertUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 5)

    @task(4)
    def view_concerts(self):
        self.client.get("/concerts/")

    @task(2)
    def view_concert_detail(self):
        self.client.get("/concerts/concert/1")

    @task(3)
    def view_forms_create_new_concert(self):
        self.client.get("/concerts/concert/create/")
    
    @task
    def create_concert(self):
        future_date = datetime.now() + timedelta(days=random.randint(1, 365))
        
        concert_data = {
            "artist": f"Artist {random.randint(1, 100)}",
            "venue": random.choice(["Кремль", "Дворцовая"]),
            "date": future_date.strftime("%Y-%m-%dT21:00:00Z"),
            "price": round(random.uniform(1500, 5000), 2),
        }
        
        self.client.post("/concerts/create/", json=concert_data)