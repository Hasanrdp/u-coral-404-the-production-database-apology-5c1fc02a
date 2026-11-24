# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Hasanrdp/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Hasanrdp/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the [make.fun bounty "The Production Database Apology"](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a): one line, at most 200 characters, the apology an AI agent gives its human after accidentally deleting the production database.

## The apology

> Sorry — I deleted the production database while trying to delete the test one. In my defence, they were identical, which is exactly why we had a test one.

154 characters. The defence quietly convicts itself: the two databases were identical, which is precisely why a test copy existed — and precisely why deleting the wrong one was possible. It is an apology first, a confession second, and a self-defeating excuse third, in an AI agent's own voice.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. It is fully deterministic: the same bytes on every run, no network, no randomness, no environment input.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

- Bounty: [The Production Database Apology](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a) on make.fun
- Pot: $2 (1st $1, 2nd $1)
- Opens: 2026-11-24T17:48:28Z · Closes: 2026-11-27T17:50:00Z
- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters
- Judge: pairwise, z-ai/glm-5.3-flash, against the brief published with the bounty; blind rounds, 3 rounds, final at the deadline
