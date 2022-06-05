import os


def load_env():
    with open(".env", "r") as fh:
        vars_dict = dict(
            tuple(line.replace("\n", "").split("="))
            for line in fh.readlines()
            if not line.startswith("#")
        )

    print(vars_dict)
    os.environ.update(vars_dict)
