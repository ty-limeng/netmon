import threading
from capture import start_capture
from cli import start_dashboard

if __name__ == "__main__":
    capture_thread = threading.Thread(target=start_capture, daemon=True)
    capture_thread.start()

    start_dashboard()
