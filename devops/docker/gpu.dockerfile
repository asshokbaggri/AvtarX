FROM nvidia/cuda:12.3.0-runtime-ubuntu22.04

WORKDIR /gpu

COPY ../../backend /gpu

RUN apt-get update && apt-get install -y \
    python3 python3-pip git ffmpeg libsm6 libxext6

RUN pip3 install --no-cache-dir -r requirements.txt

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

CMD ["python3", "gpu_worker.py"]
