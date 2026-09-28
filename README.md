# wordcount

Counts word frequencies in text files.

```sh
python -m wordcount [--top N] FILE [FILE ...]   # '-' reads stdin
```

Prints `<count> <word>` per line, most frequent first.

Development: `python -m pytest`.
