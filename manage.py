import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask.ext.script import Manager, Server
from tay_flask import app
manager = Manager(app)
manager.add_command("runserver", Server(
	use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 5000)))
)
from tay_flask import views
if __name__ == "__main__":
    manager.run()
