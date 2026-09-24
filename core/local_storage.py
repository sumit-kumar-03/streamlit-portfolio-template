"""
Simple local file storage for contact form submissions.
"""
from datetime import datetime
import os


def save_contact_to_file(name, email, subject, message, filepath="contact_submissions.txt"):
    """
    Save contact form submission to a local text file.
    
    Args:
        name: Contact's name
        email: Contact's email
        subject: Message subject
        message: Message content
        filepath: Path to the submissions file
    
    Returns:
        tuple: (success: bool, message: str)
    """
    try:
        # Ensure the submissions directory exists
        submissions_dir = os.path.join(os.path.dirname(__file__), '../submissions')
        os.makedirs(submissions_dir, exist_ok=True)
        
        # Full path to the file
        full_path = os.path.join(submissions_dir, filepath)
        
        # Prepare the submission text
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        submission = f"""
{'='*80}
TIMESTAMP: {timestamp}
NAME: {name}
EMAIL: {email}
SUBJECT: {subject or 'No subject'}
MESSAGE:
{message}
{'='*80}

"""
        
        # Append to file (creates if doesn't exist)
        with open(full_path, 'a', encoding='utf-8') as f:
            f.write(submission)
        
        return True, f"Message saved successfully! Submission #{get_submission_count(full_path)}"
        
    except Exception as e:
        return False, f"Error saving message: {str(e)}"


def get_submission_count(filepath):
    """
    Count the number of submissions in the file.
    
    Args:
        filepath: Path to the submissions file
    
    Returns:
        int: Number of submissions
    """
    try:
        if not os.path.exists(filepath):
            return 0
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Count the separator lines
            return content.count('='*80) // 2
    except:
        return 0
