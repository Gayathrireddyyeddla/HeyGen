from client import VideoTranslationClient

client = VideoTranslationClient("http://127.0.0.1:5000", timeout=30, poll_interval=5)
print(client.get_status("my_job_id"))
