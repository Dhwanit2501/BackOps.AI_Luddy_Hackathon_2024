from datetime import datetime, timedelta, timezone
import re

TIMESTAMP_STR = "%m/%d/%Y %H:%M:%S"

def get_current_time_in_str(format=TIMESTAMP_STR):
    return datetime.now().strftime(format)

def get_today_date_attr():
    datetime_obj = datetime.now()
    return datetime_obj.year, datetime_obj.month, datetime_obj.day

def today_stats():
    year, month, day = get_today_date_attr()

    return get_stats(year, month, day)

def get_stats(year: int, month: int, day: int):
    stats = {
        'Inserted': 0,
        'Updated': 0,
        'Deleted': 0
    }
    with open('myapp.log') as f:
        for log in f:
            log = log.strip()

            # Extract year (0 - 3)
            logYear = int(log[0: 4])

            # Extract month (5 - 6)
            logMonth = int(log[5: 7])

            # Extract day (8 - 10)
            logDay = int(log[8: 11])

            # Message of the log
            splitStrList = log.split("-")[-1].lstrip()

            if log.split("-")[4] == 'ERROR':
                continue

            op = splitStrList.split(" ")[0]

            # Process log if it only matches given query criteria
            if year == logYear and month == logMonth and day == logDay:
                stats[op] += 1

    return stats

def visualization_of_lifecycle_of_key_for_today():
    data = {
        "Insert": [],
        "Update": [],
        "Delete": [],
    }

    today = datetime.now()
    day = today.day
    month = today.month
    year = today.year

    insert_pattern = r'Inserted key:(\S+)\s+with value:\s*(\S+)'
    update_pattern = r'Updated existing key:\s*(\S+)\s+with new value:\s*(\S+)'
    delete_pattern = r'Deleted given key:\s*(\S+)'

    with open('myapp.log') as f:
        for log in f:
            log = log.strip()

            # Extract year (0 - 3)
            logYear = int(log[0: 4])

            # Extract month (5 - 6)
            logMonth = int(log[5: 7])

            # Extract day (8 - 10)
            logDay = int(log[8: 11])

            # Message of the log
            log_timestamp = log[0: 19]
            splitStrList = log.split("-")[-1].lstrip()

            op = splitStrList.split(" ")[0]

            # Process log if it only matches given query criteria
            if year == logYear and month == logMonth and day == logDay:
                insert_match = re.search(insert_pattern, log)

                if insert_match:
                    data["Insert"].append({"key": insert_match.group(1), "value": insert_match.group(2), "created_time": log_timestamp})

                update_match = re.search(update_pattern, log)
                if update_match:
                    data["Update"].append({"key": update_match.group(1), "value": update_match.group(2), "updated_time": log_timestamp})
                
                delete_match = re.search(delete_pattern, log)
                if delete_match:
                    data["Delete"].append({"key": delete_match.group(1), "value": "", "delete_time": log_timestamp})

    return data



            

