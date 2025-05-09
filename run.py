
import logging

# Configure root logger: INFO level, with timestamp
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
