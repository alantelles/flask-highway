from app import app
import os

debug = bool(os.environ.get('DEBUG', True))
port = int(os.environ.get('PORT', 5000))
host = os.environ.get('HOST', '127.0.0.1')
use_reloader = os.environ.get('USE_RELOADER', True)



if __name__ == '__main__':
    app.run(debug=debug, port=port, host=host, use_reloader=use_reloader)