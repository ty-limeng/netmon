from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from threading import Thread
import uvicorn
from flow_tracker import get_top_upstream, get_top_inbound

from capture import start_capture
from stats import get_stats
from dns_tracker import get_top_domains
from service_detector import get_top_services
from device_tracker import get_devices

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# -----------------------
# Background packet capture
# -----------------------
def run_sniffer():
    start_capture(interface=None)

Thread(target=run_sniffer, daemon=True).start()


# -----------------------
# Web Page
# -----------------------
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


# -----------------------
# API endpoint
# -----------------------
@app.get("/api/stats")
def api_stats():
    stats = get_stats()

    return {
        "bandwidth": stats["bandwidth"],
        "pps": stats["pps"],
        "top_ips": stats["top_ips"],
        "protocols": stats["protocols"],
        "upstream": get_top_upstream(),
        "inbound": get_top_inbound(),
        "domains": get_top_domains(),
        "services": get_top_services(),
        "devices": get_devices()
    }



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
