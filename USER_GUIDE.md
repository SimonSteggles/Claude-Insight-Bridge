# Claude to GitHub Automation - User Guide

## Overview

This automation system automatically saves all your Claude conversations and generated code to your GitHub repository (**Claude-Insight-Bridge**). Every response from Claude and any code it generates can be captured and version-controlled in GitHub, creating a permanent record of your AI-assisted work.

## What This System Does

The Claude to GitHub automation provides a seamless way to:

- **Archive Conversations**: Save complete Claude conversation threads as markdown files
- **Store Generated Code**: Automatically save code snippets and files with proper formatting
- **Version Control**: Track changes and maintain history of all your Claude interactions
- **Organize Content**: Separate conversations and code into dedicated folders
- **Auto-Commit**: Automatically commit and push changes to GitHub with timestamps

## Repository Structure

Your **Claude-Insight-Bridge** repository is organized as follows:

```
Claude-Insight-Bridge/
├── conversations/          # All Claude conversation logs
│   └── YYYY-MM-DD_HH-MM-SS_conversation.md
├── code/                   # All generated code files
│   └── YYYY-MM-DD_HH-MM-SS_filename.ext
├── claude_to_github.py    # Main automation script
└── README.md              # Repository description
```

## How to Use the Automation

### Method 1: Save a Conversation

To save a conversation you've had with Claude:

1. Copy the conversation text from Claude
2. Save it to a file (e.g., `my_conversation.txt`)
3. Run the command:

```bash
python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py conversation my_conversation.txt
```

Or pipe the content directly:

```bash
echo "Your conversation text here" | python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py conversation
```

### Method 2: Save Generated Code

To save code that Claude generated:

```bash
echo "your code here" | python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py code filename language
```

**Example - Save Python code:**
```bash
cat > /tmp/my_script.py << 'EOF'
def hello_world():
    print("Hello from Claude!")
EOF

cat /tmp/my_script.py | python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py code my_script python
```

**Supported Languages:**
- python
- javascript
- typescript
- html
- css
- bash
- sql
- json
- yaml
- markdown

### Method 3: Run a Test

To test that everything is working:

```bash
python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py test
```

This will create a test conversation and push it to GitHub.

## Advanced Usage

### Using the Python API

You can also use the automation programmatically in your own Python scripts:

```python
from claude_to_github import ClaudeGitHubSync
import datetime

# Initialize
repo_path = "/home/ubuntu/Claude-Insight-Bridge"
token_file = "/home/ubuntu/.github_token"

with open(token_file, 'r') as f:
    github_token = f.read().strip()

sync = ClaudeGitHubSync(repo_path, github_token)

# Save a conversation
conversation_text = """
# My Claude Conversation

**User:** How do I automate GitHub?

**Claude:** Here's how you can automate GitHub...
"""

sync.sync_all(
    conversation_content=conversation_text,
    commit_message="Saved conversation about GitHub automation"
)

# Save code files
code_files = [
    {
        'content': 'print("Hello World")',
        'filename': 'hello',
        'language': 'python'
    }
]

sync.sync_all(
    code_files=code_files,
    commit_message="Added hello world script"
)
```

### Custom Commit Messages

You can provide custom commit messages:

```bash
python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py conversation my_file.txt
# This will use a default message with timestamp

# For custom messages, modify the script or use the Python API
```

## File Naming Convention

All files are automatically timestamped to prevent conflicts:

- **Conversations**: `YYYY-MM-DD_HH-MM-SS_conversation.md`
- **Code Files**: `YYYY-MM-DD_HH-MM-SS_filename.extension`

Example: `2025-10-31_08-48-34_conversation.md`

## Viewing Your Saved Content

### On GitHub

1. Visit: https://github.com/SimonSteggles/Claude-Insight-Bridge
2. Click on the **conversations** folder to see all saved conversations
3. Click on the **code** folder to see all saved code files
4. Each file can be viewed, downloaded, or shared directly from GitHub

### Locally

All files are also stored locally in:
- `/home/ubuntu/Claude-Insight-Bridge/conversations/`
- `/home/ubuntu/Claude-Insight-Bridge/code/`

## Authentication Details

The system uses a GitHub Personal Access Token for authentication:

- **Token Location**: `/home/ubuntu/.github_token`
- **Token Permissions**: repo, workflow, gist
- **Expiration**: November 30, 2025
- **Security**: Token is stored securely with restricted file permissions (600)

### Renewing the Token

When your token expires on November 30, 2025:

1. Go to https://github.com/settings/tokens
2. Click on "Claude Automation"
3. Click "Regenerate token"
4. Copy the new token
5. Update the token file:
   ```bash
   echo "your_new_token_here" > /home/ubuntu/.github_token
   chmod 600 /home/ubuntu/.github_token
   ```

## Troubleshooting

### Authentication Failed

If you see "Authentication failed" errors:

1. Check that the token file exists:
   ```bash
   cat /home/ubuntu/.github_token
   ```

2. Verify the token is valid:
   ```bash
   curl -H "Authorization: token $(cat /home/ubuntu/.github_token)" https://api.github.com/user
   ```

3. If invalid, regenerate the token on GitHub and update the file

### No Changes to Commit

If you see "No changes to commit":
- This means the files were already saved previously
- The system only commits when there are new or modified files

### Push Failed

If push fails:
1. Check your internet connection
2. Verify the repository exists: https://github.com/SimonSteggles/Claude-Insight-Bridge
3. Ensure the token has not expired

## Best Practices

### Organizing Conversations

- Save conversations with descriptive titles when possible
- Group related conversations by topic
- Review and clean up old conversations periodically

### Code Management

- Always specify the correct language for proper file extensions
- Use meaningful filenames for generated code
- Test code before saving to ensure it's working

### Security

- **Never share your GitHub token** with anyone
- Keep the token file secure (already set to 600 permissions)
- Regenerate the token if you suspect it has been compromised

## Integration Ideas

### Automated Workflow

Create a bash script to automatically save conversations:

```bash
#!/bin/bash
# save_claude_conversation.sh

CONVERSATION_FILE="$1"
SCRIPT_PATH="/home/ubuntu/Claude-Insight-Bridge/claude_to_github.py"

if [ -z "$CONVERSATION_FILE" ]; then
    echo "Usage: $0 <conversation_file>"
    exit 1
fi

python3 "$SCRIPT_PATH" conversation "$CONVERSATION_FILE"
echo "Conversation saved and pushed to GitHub!"
```

### Scheduled Backups

You could set up a cron job to automatically backup conversations at regular intervals:

```bash
# Add to crontab (crontab -e)
0 */6 * * * /path/to/backup_script.sh
```

## Support and Updates

### Repository Information

- **Repository**: https://github.com/SimonSteggles/Claude-Insight-Bridge
- **Owner**: SimonSteggles
- **Description**: AMS to IG version of Insight Bridge

### Getting Help

If you encounter issues:

1. Check this user guide first
2. Review the troubleshooting section
3. Check the GitHub repository for any updates
4. Verify your token is still valid

## Summary

This automation system provides a robust way to archive and version-control all your Claude interactions. By automatically saving conversations and code to GitHub, you create a searchable, shareable, and permanent record of your AI-assisted work.

**Key Benefits:**
- ✅ Automatic timestamping and organization
- ✅ Full version control with Git
- ✅ Accessible from anywhere via GitHub
- ✅ Supports multiple programming languages
- ✅ Simple command-line interface
- ✅ Programmatic API for custom integrations

---

**Last Updated**: October 31, 2025  
**Version**: 1.0  
**Author**: Automated setup by Claude
