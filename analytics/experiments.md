# Experiments log

The human-readable twin of the `experiments` table (`python3 analytics/tracker.py columns experiments`). Copy the template block for each experiment, fill it **before** the first post of the experiment, and import the same facts with `tracker.py import experiments FILE.csv` so the dashboard and weekly report can see it. `weekly_report.py` prints a suggested block and a paste-ready CSV row.

**Rules (strategy/portfolio.md 6.3 and 4.2):**

1. **One variable at a time**, and one experiment at a time per persona. Change nothing else on that persona while it runs (no new pillar, format or cadence).
2. A **Fix experiment** (the tree said Fix) runs **4 weeks** and changes ONE of format, hook or platform. Tick `is_fix`: its dates become the re-test window, and after it ER 0.6% or more with effort within Keep means Keep, otherwise retire-review.
3. A **redesign** (kind `redesign`) changes the workflow, not the content (for example how drafts reach the wife). It is the "one redesign" that 6.3 step 3 requires before an effort or rejection retire-review.
4. **Write the decision rule before the data.** A difference counts as clear only at 1.5x or more, with at least 4 posts in each arm. There is no significance test at these sample sizes, so a pass is a hypothesis for the next experiment, not proof.
5. **Alternate the arms** (control, treatment, control, ...) on the same pillar and posting slot where possible, so week and topic effects do not line up with one arm.
6. Posts for the experiment are ordinary posts: same approvals, labels and disclosure. An account with an open standing gate (6.2) does not run experiments.
7. **Stop early only** for a Ground-rule or account-standing problem, and write that down as the result.
8. Sponsored posts are excluded from the comparison, as everywhere.

Status values: `planned`, `running`, `done`, `abandoned`. Decision values to use in the log: **adopt** (treatment becomes the default), **keep control**, **extend** (not enough posts: run 2 more weeks, once), **abandon** (and why).

## Template (copy this block)

```
### E000: <short name>                                   status: planned | running | done | abandoned

Persona / platform:      <slug> / <platform or "all">
Linked hypothesis:       <H1 to H9 from portfolio.md 4.2, or none>
Kind:                    hook | format | platform | cadence | redesign | other        Fix experiment (is_fix):  yes | no
Why now:                 <the status and numbers that triggered it, with sample sizes: "median ER 0.43%, n=11, weeks 3 to 6">

Hypothesis:              <one sentence: "X earns a higher median ER than Y on this account">
Variable changed:        <exactly one>
Control:                 <what stays as it is>
Treatment:               <the one change>
Everything held fixed:   <pillar, posting slot, length, label wording, ...>

Start / end:             YYYY-MM-DD / YYYY-MM-DD            (4 weeks for a Fix)
Planned posts:           <at least 4 per arm; 12 in total for a 3-a-week account>
Primary metric:          median ER (reach | views), organic posts only
Baseline:                <number and n>

DECISION RULE (written before the data):
  Treatment median ER at least 1.5x the control's, with at least 4 posts per arm, then <adopt>.
  Anything less: "no clear difference", <keep control>.
  Stop early only for: <Ground-rule / standing gate>.

--- fill in at the end ---
Result:                  control <median, n> | treatment <median, n> | ratio <x>
Spread (min to max):     control <..> | treatment <..>
Decision:                adopt | keep control | extend | abandon
What we do not know:     <confounds, small n, anything that changed during the run>
Next:                    <the next single variable, or "none">
Logged in tracker:       exp_id <E000>  (import experiments)
```

## Log

No real experiment has been run. The block below is an **EXAMPLE with invented numbers**, to show the level of detail. It is not a result and is not in any database.

```
### E000 (EXAMPLE, invented): Hook type: number-first vs question-first            status: done

Persona / platform:      sehuan / instagram
Linked hypothesis:       none
Kind:                    hook          Fix experiment (is_fix):  yes
Why now:                 EXAMPLE: status Fix, median ER 0.43%, n=11, weeks 3 to 6

Hypothesis:              EXAMPLE: carousels whose first line leads with a number earn a higher median ER than ones that lead with a question
Variable changed:        hook type (first line)
Control:                 question-first
Treatment:               number-first
Everything held fixed:   pillar rotation, Monday / Wednesday / Friday slots, carousel format, label wording

Start / end:             2027-01-04 / 2027-01-31
Planned posts:           12 (6 per arm)
Primary metric:          median ER (reach), organic posts only
Baseline:                0.43% (n=11)

DECISION RULE (written before the data):
  Treatment median ER at least 1.5x the control's, with at least 4 posts per arm: adopt number-first.
  Anything less: "no clear difference", keep question-first.

--- fill in at the end ---
Result:                  EXAMPLE: control 0.40% (n=6) | treatment 0.52% (n=6) | ratio 1.3x
Decision:                keep control
What we do not know:     EXAMPLE: one post in the treatment arm was shared by a larger account; 6 posts per arm cannot tell 1.3x from noise
Next:                    EXAMPLE: test format (carousel vs reel) for 4 weeks
```
