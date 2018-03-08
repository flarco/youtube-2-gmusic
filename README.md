# youtube-2-gmusic
Rip YouTube Audio straight to your Google Music Library.

## Installation
* youtube-dl: `pip install youtube-dl`
* Google Music API:  `pip install gmusicapi`
* ffmpeg: `brew install ffmpeg`
* This repo: `git clone https://github.com/flarco/youtube-2-gmusic.git`

## Usage

* During first run the Google Music API asks you to authenticate yourself via OAuth, for subsequent runs it's not required.

```
python youtube-2-gmusic.py <YouTube Link>
```
