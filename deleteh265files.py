import glob
import subprocess
import json
from pathlib import Path
from pprint import pprint

files = glob.glob('E:/Videos' + '/**/*.mkv', recursive=True)
for file in files:
    try:
        info = subprocess.check_output(['ffprobe', '-show_format', '-show_streams', '-loglevel', 'quiet', '-print_format', 'json', file])
        video = json.loads(info)
        if video["streams"][0]["codec_name"] == 'hevc':
            #print(video["streams"][0]["codec_name"])
            print("deleting: ",file)
            hevc_file = Path(file).unlink()
    except:
        pass
