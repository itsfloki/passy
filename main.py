import os
import sys
from config import Config
from manager import Manager


def configure():
    """Configure environment"""
    config_path = os.getenv("HOME") + "/.config/passy"
    os.makedirs(config_path, exist_ok=True)

    config_file_path = os.path.join(config_path, "data.json")

    with open(config_file_path, 'w') as cf:
        cf.write('')
    print("Configuration added.")


def generate(label: str, length: int) -> str:
    pass_manager = Manager(label)
    return pass_manager.create(length)


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
