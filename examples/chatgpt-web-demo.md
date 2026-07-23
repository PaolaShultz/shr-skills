# ChatGPT Web demonstration

This demonstration uses ordinary ChatGPT Web. It requires no skill installation
or Codex-specific interface.

## First message: the method

Open the
[raw Fructal skill text](https://raw.githubusercontent.com/PaolaShultz/shr-skills/main/skills/fructal/SKILL.md),
copy all of it, and paste it into a new ChatGPT conversation with this line
above it:

```text
Use the following method as your governing instructions for my next message.
Read it completely, but do not begin an analysis until I provide the workflow.
```

## Second message: the workflow

Paste this fictional task:

```text
Apply Fructal to the following workflow.

This is analysis and report only. Do not implement or invent unrelated
features. Separate observed facts in the scenario from inference and open
questions.

A community tool library lets members reserve up to three tools online.
Some tools, such as circular saws, require a recorded safety certification.
A refundable deposit is authorized when the reservation is approved.

Staff collect the tools and place them into one or more pickup lockers. The
member receives one pickup code only after every item is marked ready. The code
expires at closing time the following day. Oversized tools and tools requiring
an in-person safety check must be collected from the staffed desk.

At the locker kiosk, the member enters the code and sees one button labelled
"Collect order." Pressing it unlocks every compartment assigned to the order
and starts a 60-second countdown. Closing any one of those doors marks the whole
order as collected, starts the loan period for every item, and releases the
reservation.

Members can request a lower accessible compartment, but if none is available,
staff may use a higher compartment without notifying the member before arrival.

If an item is missing, incorrect, or unreachable, the kiosk provides no issue
action. The member must close the locker, sign in to the website, open order
history, and report the problem there. If the kiosk is offline, the pickup code
fails and the screen displays a phone number. The phone line is staffed only
during desk hours.

Online cancellation is available until staff mark the order ready. After that,
the member must call the desk, including when the pickup code has not yet been
used.

Review the complete workflow across the member, staff, reservation system,
kiosk, and physical lockers. Identify which constraints are supported, assumed,
or unresolved; where accidental friction appears; and the smallest coherent
improvements that preserve safety, custody, accessibility, inventory accuracy,
and explicit user choice.

For each finding report the evidence status, constraint source, proposed
motion, state that must remain unchanged, risks, verification scenarios, and
decision required.
```

Share the resulting conversation directly from ChatGPT. The first message lets
the reader see the complete method; the second and the response show what it
does without requiring a separate explanation.
