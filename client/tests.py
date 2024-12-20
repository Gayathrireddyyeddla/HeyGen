import subprocess
import time
from client import VideoTranslationClient

def test_client_library():
    server_process = subprocess.Popen(["python3", "server.py"])
    time.sleep(2) 

    client = VideoTranslationClient("http://127.0.0.1:5000", timeout=15, poll_interval=3)
    job_id = "test_job"

    print(client.get_status(job_id))

    server_process.terminate()

if __name__ == "__main__":
    test_client_library()
