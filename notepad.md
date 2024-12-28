## Here are 5 steps required to leverage NVIDIA gpu from a docker container
1. Make sure your machine has nvidia gpu
```
nvidia-smi
```
2. Check if you machine has a docker engine
`docker --version`
3. Install nvidia-container-toolkit
This is based on your type of machine
- Get the production repo
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```


- Get apt-update 
```
sudo apt-get update
```
- Install the nvidia-container-toolkit
```
sudo apt-get install -y nvidia-container-toolkit
```
- Confirm installation 
```
nvidia-ctk -version
```
4. Configure docker to use nvidia-container runtime
```
sudo nvidia-ctk runtime configure --runtime=docker
```
- restart docker 
```
sudo systemctl restart docker
```
5. Run docker container with additional flags as shown below 
`docker run --rm --runtime=nvidia --gpus all <image>`
