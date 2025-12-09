import torch
x = torch.randn(3,3)
print(x)
print("CUDA available:", torch.cuda.is_available())
