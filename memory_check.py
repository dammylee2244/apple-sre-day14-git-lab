import psutil

def check_memory():

    memory = psutil.virtual_memory()

    print("===== MEMORY HEALTH REPORT =====")
    print(f"Total: {memory.total / (1024 ** 3):.2f} GB")
    print(f"Available: {memory.available / (1024 ** 3):.2f} GB")
    print(f"Used: {memory.percent}%")

if __name__ == "__main__":
    check_memory()
