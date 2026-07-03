# Cookie Log Analyzer

A command-line tool that finds the most active cookie(s) in a log file for a given UTC date.

## Requirements

- Python 3.9+

No third-party dependencies are required to run the program. The standard library is used for CSV parsing, counting, and CLI argument handling.

## Usage

```bash
./most_active_cookie -f cookie_log.csv -d 2018-12-09
```

### Arguments

| Flag | Description |
|------|-------------|
| `-f`, `--file` | Path to the cookie log CSV file |
| `-d`, `--date` | Target date in `YYYY-MM-DD` format (UTC) |

### Example

Given the sample `cookie_log.csv`, querying `2018-12-09` prints:

```
AtY0laUfhglK3lC7
```

If multiple cookies tie for the highest count, each is printed on its own line:

```bash
./most_active_cookie -f cookie_log.csv -d 2018-12-08
```

```
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```

## Input Format

The log file is a CSV with a header row:

```csv
cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
```

Timestamps are ISO 8601 strings in UTC. The date portion (`YYYY-MM-DD`) is used for filtering.

## Running Tests

```bash
python -m unittest test_cookie_analyzer -v
```

Or with pytest:

```bash
python -m pytest test_cookie_analyzer.py -v
```

## Project Structure

| File | Purpose |
|------|---------|
| `most_active_cookie` | Executable CLI entry point |
| `cookie_analyzer.py` | Core parsing and counting logic |
| `test_cookie_analyzer.py` | Unit tests |
| `cookie_log.csv` | Sample input data |

## Design Notes

- **Streaming I/O** — The file is read line-by-line; the full log is never loaded into memory.
- **Early termination** — Logs are assumed sorted newest-to-oldest. Once a row's date is older than the target, processing stops.
- **Space usage** — Only cookies seen on the target date are counted, so memory is bounded by the number of unique cookies for that day.

### Complexity

| | |
|---|---|
| Time | O(M) — M is the number of rows read until the target date block ends |
| Space | O(K) — K is the number of unique cookies on the target date |

## Assumptions

- The log file is sorted by timestamp, most recent first.
- The `-d` date is always in UTC.
- Rows follow the `cookie,timestamp` format described above.
