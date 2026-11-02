# build-your-own-database
A step-by-step tutorial for building a small key-value database in Python.
Around 40 lines of code, no dependencies.

## The idea
Real databases like Redis and Bitcask start from one simple idea: an
append-only log. Every change is written to the end of a file. To get
the current state back, you read the file from top to bottom.

## Step 1: Store data in memory
A Python dictionary holds the current state: key to value.

## Step 2: Write every change to a log
Each set or delete becomes one line of JSON appended to a file:

    {"op": "set", "key": "name", "value": "Ada"}
    {"op": "delete", "key": "language"}

Appending is fast and safe, because old data is never overwritten.

## Step 3: Rebuild state on startup
When MiniDB starts, it replays the log line by line. A set adds the
key, a delete removes it. After the replay, the dictionary matches
what it was before the program stopped.

## Step 4: Try it
Open demo.py to see it in action. The data survives restarts because
it lives in the log file, not only in memory.

## Ideas to extend it
- Compact the log so it does not grow forever
- Add expiry times for keys
- Add a simple command-line interface
- Add tests

## Files
- minidb.py: the database
- demo.py: a short example