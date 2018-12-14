import sys
from app import App

app = App()

host = sys.argv[1] if len(sys.argv) > 1 else None
port = int(sys.argv[2]) if len(sys.argv) > 2 else None


if __name__ == '__main__':
    app.run(
        host=host,
        port=port,
    )
