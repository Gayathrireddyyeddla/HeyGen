from flask import Flask, jsonify
import time
import threading

app = Flask(__name__)

jobs = {}
PENDING_TIME = 10  


def simulate_job(job_id):
    time.sleep(PENDING_TIME)
    jobs[job_id] = "completed"


@app.route('/status/<job_id>', methods=['GET'])
def get_status(job_id):
    if job_id not in jobs:
        jobs[job_id] = "pending"
        threading.Thread(target=simulate_job, args=(job_id,)).start()
        return jsonify({"result": "pending"})
    return jsonify({"result": jobs[job_id]})


if __name__ == "__main__":
    app.run(port=5000)
