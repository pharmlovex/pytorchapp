FROM pytorch/pytorch:2.5.1-cuda12.1-cudnn9-runtime


WORKDIR /app

COPY . /app

CMD ["python", "main.py", "--size", "1000", "--device", "cuda"]