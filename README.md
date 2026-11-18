# Old World sim archive

Game logs of simulation batches, kept outside the main repository and outside the shared project folder.

## The rules (Morten 2026-11-18)

1. **One branch per batch.** A batch owner pushes its batch as ONE commit on its own branch (the thread's
   `claude/project-thread-...` branch, cut from `main`), holding `batches/<batch>/`: one packed file per part
   (`<part>.tar.gz`), `SHA256SUMS`, `FILECOUNTS.txt`, the pair lists and the report.
2. **Batch branches are never merged into `main`.** `main` got the first 20 batches (2026-11-06 to 11-16) and stays as it is;
   a merged batch can never be let go of again.
3. **Logs are kept 14 days.** A batch branch is deleted 14 days after its commit. The report, the game tables and the
   comparison stay in the shared project folder and, for batches that reached the replay page, in the main repository
   (`deploy/sim-replays/<batch>/findings.tsv`, `games.csv`).
4. **A thread that needs one batch fetches that branch only**: `git fetch --depth 1 origin <branch>` and reads
   `batches/<batch>/`. Nobody needs a full copy of this repository.
5. **Before deleting a batch from the shared project folder**: check `SHA256SUMS` here, check every file there against the
   packed files (path and size), delete only what matches, keep every report (`.md`, `.docx`).

`scripts/batch-branches.sh` lists every batch branch with its batch, date and whether its 14 days are over.
`INDEX.md` lists the 20 batches on `main`.
