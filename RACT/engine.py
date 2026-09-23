from pathlib import Path

FRAMEWORK = Path(__file__).with_name("framework-v1")

def main():
    if not FRAMEWORK.exists():
        raise FileNotFoundError("RACT framework-v1 not found")

    content = FRAMEWORK.read_text(encoding="utf-8")

    print("RACT ENGINE: PASS")
    print(f"Framework loaded: {FRAMEWORK.name}")
    print(f"Framework size: {len(content)} characters")

if __name__ == "__main__":
    main()
