from quart import Quart, render_template
from nextcord.ext import ipc

app = Quart(__name__, template_folder="./templates")
ipc_client = ipc.Client(secret_key="werkzeug", multicast_port=None, host="0.0.0.0", port=80)

@app.route("/")
async def index():
    return await render_template('index.html')
