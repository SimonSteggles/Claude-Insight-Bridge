# Claude-Insight-Bridge

Automated system for saving Claude AI conversations and generated code to GitHub.

## Overview

This repository automatically captures and version-controls all your Claude conversations and code. Every interaction with Claude can be preserved, organized, and accessed through GitHub.

## Features

- ✅ **Automatic Conversation Archiving** - Save complete Claude conversation threads
- ✅ **Code Storage** - Store generated code with proper formatting and syntax
- ✅ **Version Control** - Full Git history of all interactions
- ✅ **Organized Structure** - Separate folders for conversations and code
- ✅ **Timestamped Files** - Automatic naming with date and time
- ✅ **Multi-Language Support** - Python, JavaScript, HTML, CSS, and more

## Quick Start

### Save a Conversation
```bash
python3 claude_to_github.py conversation your_conversation.txt
```

### Save Generated Code
```bash
echo "print('Hello World')" | python3 claude_to_github.py code hello python
```

### Run Test
```bash
python3 claude_to_github.py test
```

## Repository Structure

```
Claude-Insight-Bridge/
├── conversations/          # All Claude conversation logs
├── code/                   # All generated code files
├── claude_to_github.py    # Main automation script
├── USER_GUIDE.md          # Complete documentation
├── USER_GUIDE.docx        # Word format documentation
├── QUICK_START.md         # Quick reference guide
└── README.md              # This file
```

## Documentation

- **[Quick Start Guide](QUICK_START.md)** - Essential commands and quick reference
- **[Complete User Guide](USER_GUIDE.md)** - Comprehensive documentation
- **[User Guide (Word)](USER_GUIDE.docx)** - Downloadable Word document

## Authentication

This system uses a GitHub Personal Access Token stored securely at:
- `/home/ubuntu/.github_token`

Token expires: **November 30, 2025**

To renew, visit: https://github.com/settings/tokens

## System Requirements

- Python 3.x
- Git
- GitHub account with Personal Access Token
- Internet connection

## Usage Examples

### Example 1: Save a conversation from a file
```bash
# Create a conversation file
cat > my_conversation.txt << 'END'
# Discussion about Python automation

**User:** How do I automate tasks in Python?

**Claude:** Here are several ways to automate tasks in Python...
END

# Save to GitHub
python3 claude_to_github.py conversation my_conversation.txt
```

### Example 2: Save code directly
```bash
# Save a Python script
cat > script.py << 'END'
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
END

cat script.py | python3 claude_to_github.py code greeting python
```

### Example 3: Using the Python API
```python
from claude_to_github import ClaudeGitHubSync

# Initialize
sync = ClaudeGitHubSync(
    repo_path="/home/ubuntu/Claude-Insight-Bridge",
    github_token="your_token_here"
)

# Save content
sync.sync_all(
    conversation_content="Your conversation here",
    commit_message="Saved important discussion"
)
```

## Supported Languages

Python • JavaScript • TypeScript • HTML • CSS • Bash • SQL • JSON • YAML • Markdown

## Troubleshooting

### Authentication Issues
```bash
# Verify token
cat /home/ubuntu/.github_token

# Test authentication
curl -H "Authorization: token $(cat /home/ubuntu/.github_token)" https://api.github.com/user
```

### Update Token
```bash
echo "your_new_token" > /home/ubuntu/.github_token
chmod 600 /home/ubuntu/.github_token
```

## About

**Created**: October 31, 2025  
**Purpose**: Archive Claude AI interactions for InsightGuide.com  
**Owner**: SimonSteggles  
**Location**: Sutton Coldfield, Birmingham, UK

## License

Private repository for personal use.

## Support

For issues or questions, refer to the [Complete User Guide](USER_GUIDE.md).

---

**Repository**: https://github.com/SimonSteggles/Claude-Insight-Bridge  
**Last Updated**: October 31, 2025
