import torch

def main()->None:
    """
    Check to know if container leverage NVIDIA GPU accelerator
    """
    if torch.cuda.is_available():
        print("GPU accelerator is now configured")
        print("----------------------")
        print(f"You have got {torch.cuda.device_count()} available gpu")
        print(f"Cuda version: {torch.version.cuda}")
        print("Your application can now leverage NVIDIA GPU")
    else:
        print(f"Using CPU with no accelerator")
        print("----------------------------")
        print(f"You have got {torch.cpu.device_count()} cpu")
        print("Please set up docker engine to use NVIDIA GPU-accelerator")

if __name__ == "__main__":
    main()
