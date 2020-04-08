import datetime

now = datetime.datetime.now()
two = now.replace(hour=14, minute=30)

if __name__ == "__main__":
    print(f"Now: {now} | Replaced: {two}")