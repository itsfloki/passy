import sys
from config import Config


def run(conf: Config):
    print(conf.option())
    print(conf.label())


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
