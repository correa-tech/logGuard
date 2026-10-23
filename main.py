import csv

def read_csv(file_path):

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        print(reader.fieldnames)
        print(data[0])

    return data 


def readLogsError(data):

    ipFailed = {}

    count = 0

    for w in data:

        if w['status'] == 'FAILED':

            ip = w['ip']

            if ip in ipFailed:
                ipFailed[ip] += 1
            else:
                ipFailed[ip] = 1

            count += 1
    
    print(f"Total error logs: {count}")
    print(f"IPs with errors: {ipFailed}")
    return count

print("Reading CSV file...\n")



readLogsError(read_csv('logs.csv'))