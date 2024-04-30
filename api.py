from flask import Flask, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    num_rows = int(request.args.get('num_rows', 10000))  # Get the number of rows from query parameter, default is 10000 if not specified

    data_set = []
    for _ in range(num_rows):
        entry = {
            "Timestamp": datetime.now() - timedelta(days=random.randint(0, 3650)),
            "IP Address": f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
            "Request Type": random.choice(["GET", "POST", "PUT", "DELETE"]),
            "Page Category": random.choice(["Sports", "News", "Olympic Events", "Highlights and Recaps", "Fan zone and community"]),
            "Requested page": f"/{random.choice(['home', 'about', 'contact', 'services'])}",
            "Response Code": random.randint(200, 500),
            "User Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(50, 90)}.0.4430.{random.randint(100, 999)} Safari/537.36",
            "Sports Start Time": f"{random.randint(0,23)}:{random.randint(0,59)}:{random.randint(0,59)}",
            "Sports End Time": f"{random.randint(0,23)}:{random.randint(0,59)}:{random.randint(0,59)}",
            "Country of Visitors": random.choice(["USA", "UK", "Canada", "Australia", "Germany"]),
            "Advancement Status": random.choice(["Qualified", "Disqualified", "Pending"]),
            "Live on Demand": random.choice(["Live", "On Demand"]),
            "Sport Date": datetime.now() - timedelta(days=random.randint(0, 365)),
            "Viewership": random.randint(100, 10000),
            "Medal": random.choice(["Gold", "Silver", "Bronze"]),
            "Country of participants": random.choice(["USA", "UK", "Canada", "Australia", "Germany"]),
            "Names of participants": f"{random.choice(['John', 'Jane', 'Michael', 'Emily', 'David'])} {random.choice(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown'])}",
            "Sports type": random.choice(["Swimming", "Athletics", "Gymnastics", "Cycling", "Football", "Basketball", "Judo", "Hockey", "Taekwondo", "Badminton"]),
            "Gender of visitors": random.choice(["Male", "Female"])
        }
        data_set.append(entry)

    return jsonify(data_set)

if __name__ == '__main__':
    app.run(debug=True)
