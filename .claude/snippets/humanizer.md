# Humanizer pass (shared)

Single source of truth for how every Libby agent runs the humanizer. Agents
reference this file instead of repeating the skill path and fallback (which had
already drifted between agents).

## The skill
Apply the humanizer skill at `.claude/skills/humanizer/SKILL.md` — vendored into
this repo, MIT-licensed. If the project-level copy is missing, fall back to
`~/.claude/skills/humanizer/SKILL.md`.

## The protocol
Read the skill once at the start of the run. Run its 29-pattern check plus the
final "obviously AI generated" audit over the prose before writing. For a
one-to-three-sentence cell the full 29-pattern sweep is overkill, but the
principles still bite: no marketing language, no formulaic openers, no
copula-evasion verbs ("represents" / "constitutes" / "serves as" / "stands as" /
"demonstrates" / "highlights"), no rule-of-three padding, no slogan closers.

Each agent states its own *when* (before which artifact) and *scope* (which
fields) where it invokes this pass.
