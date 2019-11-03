from datetime import datetime

now = datetime.now()
two = now.replace(hour=2)
two = two.replace(minute=30)


if __name__ == "__main__":
    print(now)
    print(two)
