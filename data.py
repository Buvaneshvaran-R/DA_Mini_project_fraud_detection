import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def create_dummy_data(filename="transactions.csv", num_records=500):

    users = ['A101', 'B205', 'C309', 'D401', 'E502']
    types = ['Transfer', 'Payment']

    start_date = datetime(2024, 1, 1)

    data = []

    for _ in range(num_records):
        sender = random.choice(users)
        receiver = random.choice([u for u in users if u != sender])

        amount = random.randint(100, 100000)

        random_days = random.randint(0, 30)
        date = start_date + timedelta(days=random_days)

        time_str = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"

        t_type = random.choice(types)

        # Fraud logic
        if amount > 50000:
            fraud = random.choices(["Yes", "No"], weights=[70, 30])[0]
        else:
            fraud = random.choices(["Yes", "No"], weights=[10, 90])[0]

        data.append({
            "Sender": sender,
            "Receiver": receiver,
            "Amount": amount,
            "Date": date.strftime('%Y-%m-%d'),
            "Time": time_str,
            "Type": t_type,
            "Fraud": fraud
        })

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

    print(f"✅ Generated {num_records} records in '{filename}'")

if __name__ == "__main__":
    create_dummy_data()
