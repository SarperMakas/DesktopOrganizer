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
        
def get_file_type(files: list[str]) -> list[str]:
    types = map(lambda x: x.split('.')[1], files)
    types_deduplicate = set(types)
    return list(types_deduplicate)

desktop_path = get_desktop_path()        
onlyfiles = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
types = get_file_type(onlyfiles)

print(types)