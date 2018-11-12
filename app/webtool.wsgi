import sys
sys.path.insert(0, '/var/www/demo-app')
from app.demo_app import app as application

if __name__ == "__main__":
    application.run()
