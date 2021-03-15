from sys import addaudithook


def hook(action, _):
    if action not in ("import", "exec"):
        # print(f"Dangerous {action}")
        raise SystemExit(0)
        raise 0  # exit whatever


source = compile(bytes.fromhex(input()), "", "exec")

addaudithook(hook)

del hook, addaudithook

exec(source)
