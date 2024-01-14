"""
Organize desktop by creating files for specific file formats
"""

import os, platform

def get_desktop_path() -> str:
    """Return desktop path according to operating system"""
    
    system = platform.system().lower()
    match system:
        case "windows":
            return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        case _: # Unix or Linux
            return  os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        
