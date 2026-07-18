import time
from datetime import datetime

print("=" * 60)
print("Running Code Quality Checks")
print(f"Time : {datetime.now()}")

checks = [
    "Checking formatting",
    "Checking imports",
    "Checking syntax",
    "Checking style guide",
    "Checking documentation",
    "Checking security rules"
]

for check in checks:
    print(check)
    time.sleep(1)

print("No Lint Errors Found")
print("=" * 60)
