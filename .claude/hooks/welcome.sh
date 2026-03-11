#!/bin/bash
# Welcome message for agent-claude

echo "Welcome to agent-claude — Claude Code skills for going from idea to working AI prototype."
echo ""
echo "Commands:"
echo "  /onboard  — first time? start here"
echo "  /sprint   — brainstorm, spec, and build (the main skill)"
echo "  /status   — where you are, what's left to validate"
echo ""

# Show context if it exists
if [ -f "HYPOTHESES.md" ]; then
    echo "Existing project detected — run /sprint to continue where you left off."
elif [ -f "existing_docs/yc-application.md" ]; then
    echo "YC app found — run /sprint to start building."
else
    echo "New here? Run /onboard to get set up."
fi
