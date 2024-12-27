import torch
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--size", type=int, default=1000, help="Matrix size")
parser.add_argument("--device", type=str, default="cpu", help="Device to use (cpu or cuda)")
args = parser.parse_args()


def matrix_multiply(size, device="cpu"):
    """
    Perform matrix multiplication on specified device (CPU or GPU)
    """
    # Create random matrices
    matrix1 = torch.randn(size, size, device=device)
    matrix2 = torch.randn(size, size, device=device)
    
    # Record start time
    start_time = time.time()
    
    # Perform matrix multiplication operation
    torch.mm(matrix1, matrix2)
    
    # Record end time
    end_time = time.time()
    
    return end_time - start_time

def main():
    # Matrix size
    size = args.size
    
    # Check if GPU is available
    device = torch.device(args.device)
    print(f"Using device: {device}")
    
    # CPU computation
    cpu_time = matrix_multiply(size, device="cpu")
    print(f"CPU computation time: {cpu_time:.4f} seconds")
    
    # GPU computation (if available)
    if torch.cuda.is_available():
        gpu_time = matrix_multiply(size, device="cuda")
        print(f"GPU computation time: {gpu_time:.4f} seconds")
        print(f"GPU speedup: {cpu_time/gpu_time:.2f}x")

if __name__ == "__main__":
    main()