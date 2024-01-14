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
        
def get_file_extensions(files: list[str]) -> list[str]:
    """Get file extension as list without duplication"""
    
    types = map(lambda x: x.split('.')[1], files)
    types_deduplicate = set(types)
    return list(types_deduplicate)

def create_directories(file_extensions: list[str]) -> None:
    """Create directories in the desktop according to specified extension names"""
    
    for file_extension in file_extensions:
        path = os.path.join(desktop_path, file_extension.upper())
        
        # check whether the path is exist or not
        if not os.path.exists(path):
            os.mkdir(path)

desktop_path = get_desktop_path()        
onlyfiles = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
file_extensions = get_file_extensions(onlyfiles)

create_directories(file_extensions)