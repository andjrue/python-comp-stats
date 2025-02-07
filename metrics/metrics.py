import psutil

def get_metrics():
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=.1)
    
    # MEM
    mem = psutil.virtual_memory()
    mem_percent = mem.percent

    # NETWORK I/O
    network = psutil.net_io_counters()
    bytes_sent = round(network.bytes_sent / (1024 ** 2),0) # bytes -> MB
    bytes_rec = round(network.bytes_recv / (1024 ** 2),0)

    # Return a map here, use it for the UI
    return {
        "cpu_percent": cpu_percent,
        "mem_percent": mem_percent,
        "bytes_sent": bytes_sent,
        "bytes_rec": bytes_rec
    }

    
    

