#!/usr/bin/env python3
"""
Claude to GitHub Automation Script
This script captures Claude conversations and code, then automatically commits and pushes to GitHub.
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

class ClaudeGitHubSync:
    def __init__(self, repo_path, github_token):
        self.repo_path = Path(repo_path)
        self.github_token = github_token
        self.conversations_dir = self.repo_path / "conversations"
        self.code_dir = self.repo_path / "code"
        
        # Create directories if they don't exist
        self.conversations_dir.mkdir(exist_ok=True)
        self.code_dir.mkdir(exist_ok=True)
    
    def save_conversation(self, content, title=None):
        """Save a conversation to a markdown file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        if title:
            filename = f"{timestamp}_{title}.md"
        else:
            filename = f"{timestamp}_conversation.md"
        
        filepath = self.conversations_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Claude Conversation - {timestamp}\n\n")
            f.write(content)
        
        print(f"✓ Conversation saved: {filename}")
        return filepath
    
    def save_code(self, code_content, filename, language="python"):
        """Save code to a file"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Determine file extension based on language
        extensions = {
            "python": ".py",
            "javascript": ".js",
            "typescript": ".ts",
            "html": ".html",
            "css": ".css",
            "bash": ".sh",
            "sql": ".sql",
            "json": ".json",
            "yaml": ".yaml",
            "markdown": ".md"
        }
        
        ext = extensions.get(language.lower(), ".txt")
        
        if not filename.endswith(ext):
            filename = f"{timestamp}_{filename}{ext}"
        else:
            filename = f"{timestamp}_{filename}"
        
        filepath = self.code_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code_content)
        
        print(f"✓ Code saved: {filename}")
        return filepath
    
    def git_commit_and_push(self, message=None):
        """Commit and push changes to GitHub"""
        if not message:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"Claude update - {timestamp}"
        
        try:
            # Change to repo directory
            os.chdir(self.repo_path)
            
            # Configure git to use token
            subprocess.run([
                "git", "config", "credential.helper", 
                f"!f() {{ echo username=x-access-token; echo password={self.github_token}; }}; f"
            ], check=True, capture_output=True)
            
            # Add all changes
            subprocess.run(["git", "add", "."], check=True, capture_output=True)
            
            # Check if there are changes to commit
            result = subprocess.run(
                ["git", "status", "--porcelain"], 
                check=True, 
                capture_output=True, 
                text=True
            )
            
            if not result.stdout.strip():
                print("✓ No changes to commit")
                return True
            
            # Commit changes
            subprocess.run(
                ["git", "commit", "-m", message], 
                check=True, 
                capture_output=True
            )
            
            # Push to GitHub
            subprocess.run(
                ["git", "push", "origin", "main"], 
                check=True, 
                capture_output=True
            )
            
            print(f"✓ Successfully pushed to GitHub: {message}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Git operation failed: {e}")
            print(f"  Error output: {e.stderr.decode() if e.stderr else 'N/A'}")
            return False
    
    def sync_all(self, conversation_content=None, code_files=None, commit_message=None):
        """Save conversation and code, then sync to GitHub"""
        saved_files = []
        
        if conversation_content:
            filepath = self.save_conversation(conversation_content)
            saved_files.append(filepath)
        
        if code_files:
            for code_info in code_files:
                filepath = self.save_code(
                    code_info['content'],
                    code_info['filename'],
                    code_info.get('language', 'python')
                )
                saved_files.append(filepath)
        
        # Commit and push
        if saved_files:
            success = self.git_commit_and_push(commit_message)
            if success:
                print(f"\n✓ Successfully synced {len(saved_files)} file(s) to GitHub")
            return success
        else:
            print("✗ No content to sync")
            return False


def main():
    """Main function for command-line usage"""
    repo_path = "/home/ubuntu/Claude-Insight-Bridge"
    token_file = "/home/ubuntu/.github_token"
    
    # Read GitHub token
    with open(token_file, 'r') as f:
        github_token = f.read().strip()
    
    # Initialize sync
    sync = ClaudeGitHubSync(repo_path, github_token)
    
    # Example usage
    if len(sys.argv) > 1:
        if sys.argv[1] == "conversation":
            # Save conversation from stdin or file
            if len(sys.argv) > 2:
                with open(sys.argv[2], 'r') as f:
                    content = f.read()
            else:
                content = sys.stdin.read()
            
            sync.sync_all(conversation_content=content)
        
        elif sys.argv[1] == "code":
            # Save code file
            if len(sys.argv) < 4:
                print("Usage: claude_to_github.py code <filename> <language>")
                sys.exit(1)
            
            filename = sys.argv[2]
            language = sys.argv[3]
            content = sys.stdin.read()
            
            sync.sync_all(code_files=[{
                'content': content,
                'filename': filename,
                'language': language
            }])
        
        elif sys.argv[1] == "test":
            # Test the setup
            test_content = f"""
# Test Conversation

This is a test conversation saved at {datetime.datetime.now()}.

## Claude Response

This is a test of the Claude to GitHub automation system.

## Code Example

```python
def hello_world():
    print("Hello from Claude!")
```
"""
            sync.sync_all(
                conversation_content=test_content,
                commit_message="Test: Claude to GitHub automation"
            )
    else:
        print("Claude to GitHub Sync Tool")
        print("\nUsage:")
        print("  python3 claude_to_github.py conversation [file]")
        print("  python3 claude_to_github.py code <filename> <language>")
        print("  python3 claude_to_github.py test")


if __name__ == "__main__":
    main()
