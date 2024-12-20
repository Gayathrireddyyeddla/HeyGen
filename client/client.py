import requests
import time

class VideoTranslationClient:
    def __init__(self, server_url, timeout=30, poll_interval=2):
        self.server_url = server_url
        self.timeout = timeout
        self.poll_interval = poll_interval

    def get_status(self, job_id):
        url = f"{self.server_url}/status/{job_id}"
        start_time = time.time()

        while time.time() - start_time < self.timeout:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                result = response.json()["result"]

                if result == "completed":
                    return "Job completed"
                elif result == "error":
                    return "Job failed with error"
                
                print(f"Job status: {result}, retrying...")
                time.sleep(self.poll_interval)
            except requests.exceptions.RequestException as e:
                print(f"Error contacting server: {e}")
                time.sleep(self.poll_interval)

        return "Timeout: Job status could not be determined"

