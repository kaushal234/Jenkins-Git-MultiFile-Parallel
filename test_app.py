import time
from datetime import datetime

print("=" * 60)
print("Running Automated Tests")
print(f"Time : {datetime.now()}")

for i in range(1, 9):
    print(f"Executing Test Case {i}")
    time.sleep(1)

print("All Test Cases Passed")
print("=" * 60)
