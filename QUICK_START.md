# Claude to GitHub - Quick Start Guide

## 🚀 Quick Commands

### Save a Conversation
```bash
python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py conversation your_file.txt
```

### Save Code
```bash
echo "your code" | python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py code filename language
```

### Run Test
```bash
python3 /home/ubuntu/Claude-Insight-Bridge/claude_to_github.py test
```

## 📁 Where Files Are Saved

- **Conversations**: `/home/ubuntu/Claude-Insight-Bridge/conversations/`
- **Code**: `/home/ubuntu/Claude-Insight-Bridge/code/`
- **GitHub**: https://github.com/SimonSteggles/Claude-Insight-Bridge

## 🔑 Authentication

- **Token File**: `/home/ubuntu/.github_token`
- **Expires**: November 30, 2025
- **Renew at**: https://github.com/settings/tokens

## 📖 Full Documentation

See [USER_GUIDE.md](USER_GUIDE.md) for complete documentation.

## ✅ System Status

- ✅ GitHub Authentication: Configured
- ✅ Repository: Claude-Insight-Bridge
- ✅ Automation Script: Installed
- ✅ Test: Passed

## 🆘 Troubleshooting

**Authentication Error?**
```bash
# Check token
cat /home/ubuntu/.github_token

# Test token
curl -H "Authorization: token $(cat /home/ubuntu/.github_token)" https://api.github.com/user
```

**Need to update token?**
```bash
echo "your_new_token" > /home/ubuntu/.github_token
chmod 600 /home/ubuntu/.github_token
```

---

**Setup Date**: October 31, 2025  
**Repository**: https://github.com/SimonSteggles/Claude-Insight-Bridge
