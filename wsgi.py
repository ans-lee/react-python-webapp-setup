import sys

from api import create_app, ENVS

if len(sys.argv) == 2:
    if sys.argv[1] in ENVS:
        app = create_app(sys.argv[1])
    else:
        print('Error: No such environment found.')
        exit(1)
else:
    app = create_app('dev')


if __name__ == "__main__":
    app.run()
