# Youtube-Downloader

## Setup
The following steps should help you source the required codec binaries and also set up a Python virtual environment from which this script can run within:
1. Clone this repo with: ```git clone [url]```

2. Enter directory: ```cd [repo name]```

3. Create virtual environment: ```python -m venv venv```

4. Activate virtual environment. On Windows this is: ```.\venv\Scripts\activate.bat```
   Google it if you are on another platform...
5. A prefix should be added to your command prompt, showing that you are in a virtual environment.
6. Install the required library: ```pip install youtube-dl```
7. Wait to install and then you can run the program from the prompt in the virtual environment:
```python main.py```

## Use
You can run this script from the command line within a virtual environment, or if the required library is installed globally it can also be double-clicked. If the script is run without arguments, then it will prompt for a video ID. Alternatively, you can provide a video ID as an argument when running the program from the command line. E.g.
```python main.py mYVIdEoiDxx```
