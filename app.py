from pathlib import Path
import os


def load_env_file(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main():
    load_env_file()
    api_key = os.getenv("API_KEY")
    print("API key loaded:", bool(api_key))


if __name__ == "__main__":
    main()
