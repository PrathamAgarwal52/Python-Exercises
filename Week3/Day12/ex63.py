from datetime import datetime, timedelta

def get_time_difference(time1, time2):
    format_str = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the timestamps
    time1 = datetime.strptime(time1, format_str)
    time2 = datetime.strptime(time2, format_str)
    
    # Calculate the time difference
    time_diff = abs(time1 - time2).total_seconds()
    
    return int(time_diff)

if __name__ == '__main__':
    n = int(input().strip())
    
    for _ in range(n):
        time1 = input().strip()
        time2 = input().strip()
        
        time_diff = get_time_difference(time1, time2)
        
        print(time_diff)
