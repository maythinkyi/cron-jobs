import datetime
import os

try:
    print("Job started")

    output_path = "/home/may-thin-kyi/cron-job/timestamp.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    is_file_exists = os.path.exists(output_path)
    with open(output_path, "a" if is_file_exists else "w") as f:
        f.write(now)

    print("Job finished successfully")

except Exception as e:
    print(f"Error occurred: {e}")