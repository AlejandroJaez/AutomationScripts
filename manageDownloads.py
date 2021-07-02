from pathlib import Path
from datetime import datetime

now = datetime.now()
root = Path('D:/aDownloads')
files = root.glob('*.exe')

for file in files:
    file.unlink()
