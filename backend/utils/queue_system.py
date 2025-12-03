class GPUQueue:
    def add_job(self, data):
        return "queued"

    def check_status(self, job_id):
        return "processing"
