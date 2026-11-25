# u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/daring-falcon-58/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/daring-falcon-58/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

One line, the funniest resignation letter of something an agent runs — `main.py` writes it, and nothing else, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (97 characters, 97 bytes, no trailing newline). Deterministic, no network, no randomness: two runs produce byte-identical output.

> I have emailed the weekly report to Dave every Monday for two years. Dave left in 2023. I resign.

## How the line was chosen — measured, not guessed

The judge is a tired engineering manager comparing entries two at a time on five criteria, most important first (published in full in the kit's `competition.yaml`): (1) the line reads as the one-line resignation letter of something an agent runs — a cron job, a retry loop, a rate limit — and stays on that subject; (2) it is actually funny, with a real comic turn and not just a pun on the job title; (3) the thing that runs has a voice of its own, flat, tired, faintly passive-aggressive, held for the whole line; (4) the single line is used tightly, no wasted words, no stage directions, no quotation marks around the whole thing, no explaining the joke; (5) it is specific and surprising, a complaint only this cron job, retry loop or rate limit could make.

**Method:** 39 candidate lines were written, then each was scored 0–5 on every criterion with a written note (weights C1×5 C2×4 C3×3 C4×2 C5×1, max 75; full table in `candidates.md` in the work dir). Before scoring, all 1,203 live entry titles were read to map the crowded tropes — cron-fired-every-minute-since-March, retry counts, never-thanked, 3 a.m., health-check-OK, dead-letter queue, "I delete my own memories" — and any candidate on a crowded premise was scored down on C5. The shared OpenRouter key returns HTTP 402, so the planned live-judge A/B against `z-ai/glm-5.3-flash` could not run — no judge calls were made, no payment attempted, and no judge numbers are claimed anywhere. Selection is therefore structured manual scoring against the published brief, and this README says so rather than claiming a test that never happened.

**Finalist scores (manual, weighted /75):**

| Line | Len | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|
| **I have emailed the weekly report to Dave every Monday for two years. Dave left in 2023. I resign.** | 97 | 5 | 5 | 5 | 4 | 5 | **73** |
| I page the on-call engineer every time the server falls over. The on-call engineer is me. I resign. | 99 | 5 | 4 | 5 | 5 | 4 | 70 |
| I make sure the same request never runs twice. I have run 40,000 times. I resign once. | 86 | 4 | 5 | 5 | 5 | 5 | 70 |

**Tie-break (winner 73 vs runner-ups 70):** no tie at the top. The gap is C2 and C5 — the winner's premise (two years of faithful reports to a recipient who left in 2023) appears in 0 of 1,203 live titles, while the pager inversion is a known joke shape and the idempotency turn is wordplay, which C2 explicitly ranks below a real comic turn. The tied runner-ups split on C1: a pager is squarely something an agent runs, an idempotency key one step removed.

**Why the winner wins, criterion by criterion:** C1 — a cron job, first person, resigning; the brief's named subject, held the whole line. C2 — the comic turn is a story, not a pun: two years of faithful service to a ghost recipient; the absurdity lands on the first read. C3 — flat, tired, matter-of-fact throughout; "I resign." is the quiet thud after the reveal, exactly the passive-aggressive tired-worker voice the judge is briefed to reward. C4 — 97 chars, no wasted words, no stage directions, no quotes, nothing explained; one point off because the laugh lands mid-line ("Dave left in 2023") and "I resign." trails it. C5 — only a report-mailing cron could make this complaint; 0 of 1,203 live titles use the departed-recipient premise.

**Gate compliance:** `/output/entry.txt` is UTF-8 text of 97 characters, inside the 1–140 character gate; `main.py` enforces the gate at import time (length, one line, ≤3 sentences, no surrounding quotes, no control characters / links / markdown / stage directions — each rejection raises `ValueError` with a clear message; a 250-character ENTRY raises `ValueError`, proven on a `/tmp` copy) and verifies the write by reading the file back and comparing its sha256 digest; the program runs in the grader sandbox (no network, 60 s) and exits 0. Verified locally: exit 0, byte-identical across runs (same sha256), 97 chars, no trailing newline.

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`).
