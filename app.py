import time
from datetime import datetime

print("=" * 60)
print("Application Execution Started")
print(f"Time : {datetime.now()}")

for i in range(1, 6):
    print(f"Processing Task {i}")
    time.sleep(1)

print("Application Completed Successfully")
print("=" * 60)
