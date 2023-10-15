import sys
from config import Config


def run(conf: Config):
    print(conf.option())
    print(conf.label())


def main():
    conf = Config(sys.argv[1:])
    run(conf)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.stderr.write(f"Unexpected: {e}")
        sys.exit(1)
