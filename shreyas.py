import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Hello from Shreyas' CI/CD pipeline!")
    print(f"Current time inside the container is: {now}")

if __name__ == "__main__":
    main()