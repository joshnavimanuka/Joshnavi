import os
from pathlib import Path
 
file_types = {
 
    'IMAGES':['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.svg', '.heif', '.psd'],
    'AUDIO':['.aac', '.aa', '.dvf', '.m4a', '.m4b', '.m4p', '.mp3', '.msv', '.raw', '.wav', '.wma'],
    'VIDEOS':['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg','.mpeg', '.3gp'],
    'DOCOUMENTS':['.oxps','.epub', '.pages', '.docx', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx']
}
 
dct = dict()
for directory, file_formats in file_types.items():
    for file_format in file_formats:
        dct[file_format] = directory
 
 
def file_organizer():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
 
        if file_format in dct:
            directory_path = Path(dct[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
 
        else:
            others = Path('OTHERS')
            others.mkdir(exist_ok=True)
            file_path.rename(others.joinpath(file_path))
 
 
if __name__ == '__main__':
    file_organizer()