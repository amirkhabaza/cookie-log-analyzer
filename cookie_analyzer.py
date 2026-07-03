import csv
from collections import Counter
from typing import List


def get_most_active_cookies(file_path: str, target_date: str) -> List[str]:
    """Parses the cookie log and returns a list of the most active cookies

    for the specified UTC date.
    """
    cookie_counts = Counter()

    with open(file_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        # Skip the header row (cookie,timestamp)
        try:
            next(reader)
        except StopIteration:
            return []

        for row in reader:
            if not row:
                continue
            cookie, timestamp = row[0], row[1]

            # Extract the date portion (YYYY-MM-DD) from the ISO timestamp
            date_part = timestamp.split("T")[0]

            if date_part == target_date:
                cookie_counts[cookie] += 1
            elif date_part < target_date:
                # Optimization: Since the file is sorted from newest to oldest,
                # once we see a date older than our target, we can stop reading.
                break

    if not cookie_counts:
        return []

    # Find the maximum frequency
    max_count = max(cookie_counts.values())

    # Get all cookies that match the maximum frequency
    return [
        cookie
        for cookie, count in cookie_counts.items()
        if count == max_count
    ]