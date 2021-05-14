"""
Data Generation server

Usage: {filename} [options] [--verbose|--silent]

    --help               Show this
    --host=HOST          Host location [default: localhost]
    --port=PORT          Port [default: 5000]

"""

import asyncio
import os
import sys
import shlex
from docopt import docopt
from flask import Flask
from flask_socketio import SocketIO, emit
import eventlet

from util import logging
from util.dont_import import DontImport

# monkey patch flask_socketio
eventlet.monkey_patch()

#  Replace current filename in docopt
__doc__ = __doc__.format(filename=os.path.basename(__file__))
args = docopt(__doc__)

app = Flask(__name__)
socketio = SocketIO(app, async_mode="eventlet", logger=args["--verbose"], engineio_logger=args["--verbose"])


@socketio.event
def powersof4():
    for i in range(1, 100000):
        if (i-1) & i == 0 and i & 1431655764 != 0:
            emit("powersof4", {"data": i})


async def list_top_n_ps(n: int) -> None:
    command = "watch \"ps aux | sort -nrk 3,3 | head -n {n}\"".format(
        n=n
    )
    print(command)
    process = await asyncio.create_subprocess_exec(
        *shlex.split(command),
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.PIPE,
        stderr=None,
        cwd=os.environ["BUILD_WORKSPACE_DIRECTORY"],
    )

    assert process.stdout is not None

    while not process.stdout.at_eof():
        data = await process.stdout.readline()
        if data is None or len(data) == 0:  # EOF
            break
        ps = data.decode().rstrip()
        print(ps)
        emit("stream", {"data": ps})

    if await process.wait() != 0:
        app.logger.error("command failed")
        raise Exception("command failed")


@socketio.event
async def stream():
    print("Stream")
    await list_top_n_ps(5)


@socketio.event
def hello(message):
    print(message)
    emit("response", {"data": "hi"})
    

@socketio.event
def connect():
    emit("response", {"data": "Connected"})


@socketio.event
def disconnect():
    print("Client disconnected")


async def main() -> int:
    logging.set_log_level(args, app.logger)
    app.logger.debug("Args: %s", args)
    DontImport().print()
    socketio.run(app, host=args["--host"], port=int(args["--port"]), debug=args["--verbose"])
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
