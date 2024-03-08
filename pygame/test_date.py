import datetime


def save_current_time(filepath):
    current_time = datetime.datetime.now()
    with open(filepath, "w") as file:
        file.write(str(current_time))


def read_datetime_from_file(filepath):
    with open(filepath, "r") as file:
        datetime_str = file.read()
        return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")


if __name__ == "__main__":
    save_current_time("test_date.txt")
    print(read_datetime_from_file("test_date.txt"))
