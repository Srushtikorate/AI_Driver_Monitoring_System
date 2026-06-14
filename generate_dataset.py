import pandas as pd
import random

data = []

# Alert = 0
for _ in range(200):
    data.append([
        random.randint(15, 25),      # Eye Opening
        random.randint(1, 10),       # Blink Count
        round(random.uniform(0.0, 0.5), 2),  # Closed Time
        0,                           # Forward
        0                            # Alert
    ])

# Drowsy = 1
for _ in range(200):
    data.append([
        random.randint(3, 10),       # Eye Opening
        random.randint(5, 20),       # Blink Count
        round(random.uniform(1.5, 5.0), 2),  # Closed Time
        0,                           # Forward
        1                            # Drowsy
    ])

# Distracted = 2
for _ in range(200):
    data.append([
        random.randint(15, 25),      # Eye Opening
        random.randint(1, 10),       # Blink Count
        round(random.uniform(0.0, 0.5), 2),  # Closed Time
        random.choice([1, 2]),       # Left or Right
        2                            # Distracted
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Eye_Opening",
        "Blink_Count",
        "Closed_Time",
        "Head_Direction",
        "Driver_State"
    ]
)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("driver_dataset.csv", index=False)

print("Dataset Created Successfully!")
print("Total Records:", len(df))