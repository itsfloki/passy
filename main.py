import os
import sys
import json
from config import Config
from manager import Manager

# Constants
INVENTORY_DIR = os.getenv("HOME") + "/.config/passy"
INVENTORY_FILE = os.path.join(INVENTORY_DIR, "data.json")


def configure():
    """Configure environment"""
    os.makedirs(INVENTORY_DIR, exist_ok=True)

    with open(INVENTORY_FILE, 'w') as fp:
        json.dump([], fp, sort_keys=True, indent=4)
    print("Inventory added.")


def generate(label: str, length: int) -> str:
    pass_manager = Manager(label)
    password = pass_manager.create(length)
    pass_obj = {"label": label, "password": password}
    data = []

    with open(INVENTORY_FILE, 'r') as fp:
        data = json.load(fp)

    with open(INVENTORY_FILE, 'w') as fp:
        data.append(pass_obj)
        json.dump(data, fp, sort_keys=True, indent=4)
    return password


def run(conf: Config):
    match conf.option():
        case "configure":
            configure()
        case "generate":
            password = generate(conf.value(), conf.length())
            print(password)
        case _:
            raise ValueError("Invalid option.")


def main():
    try:
        conf = Config(sys.argv[1:])
        run(conf)
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
