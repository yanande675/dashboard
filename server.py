import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "/dashboard-yannis"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    # Check if files exist
    if not os.path.exists(os.path.join(DIRECTORY, "index.html")):
        print(f"Error: index.html not found in {DIRECTORY}!")
        return

    # Serve the files
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving Dashboard Yannis at http://localhost:{PORT}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    run_server()
