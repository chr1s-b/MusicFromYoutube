# MusicFromYoutube

## Setup
### Download and Virtual Environment
The following steps will help you set up a Python virtual environment from which this script can run within:
1. Clone this repo with: ```git clone https://github.com/chr1s-b/MusicFromYoutube.git```

2. Enter directory: ```cd MusicFromYoutube```

3. Create virtual environment: ```python -m venv venv```

4. Activate virtual environment. On Windows this is: ```.\venv\Scripts\activate.bat```
   Google it if you are on another platform...
5. A prefix should be added to your command prompt, showing that you are in a virtual environment.
6. Install the required library: ```pip install youtube-dl```
7. Wait to install and then you can run the program from the prompt in the virtual environment:
```python main.py```
### Codec Binaries
The following binaries are required and can be found easily after searching for ```ffmpeg binaries```:
   * ffmpeg.exe
   * ffplay.exe
   * ffprobe.exe

**Note:** The program will not function without these binaries in the same directory as ```main.py```
## Program Use
You can run this script from the command line within a virtual environment, or if the required library is installed globally it can also be double-clicked. If the script is run without arguments, then it will prompt for a video ID. Alternatively, you can provide a video ID as an argument when running the program from the command line. E.g.
```python main.py mYVIdEoiDxx```
