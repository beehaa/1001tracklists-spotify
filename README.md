# 1001tracklists-spotify

This program is a web scraping bot that takes in a URL from 1001tracklists.com and creates a Spotify playlist on your account using the Spotify songs linked to each song in the tracklist. 

# Motivation

I am a huge fan of EDM music and listen to various DJ sets regularly. However, these DJ sets are usually on youtube or soundcloud and need to be downloaded to listen offline. My main music app is Spotify so I wanted to make a playlist with all of the hottest EDM songs from a given DJ set each time it drops and and is IDed on tracklist.

One caveat is that the playlist on Spotify will have the original verison of the songs (if ID'ed) in the order of DJ set, but will obviously not have the mixing as the tracklist link. I have crossfade on so it is a bit more bearable. 

# Setup 

Clone this project locally:
```
git clone https://github.com/beehaa/1001tracklists-spotify.git
```

Get your Spotify developer API key and put it in a config.py file. Then simply run in the terminal and follow the prompts. It will ask you for the URL and then a confirmation. 

```
python main.py
``` 

Example shell output: 


```
/usr/local/bin/python3 /Users/brianha/Desktop/1001tracklists-spotify/main.py
Please enter the 1001tracklists.com URL to create the Spotify playlist: https://www.1001tracklists.com/tracklist/1zr0b981/tiesto-club-life-821-musical-freedom-yearmix-2022-12-24.html
[WDM] - 

[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 108.0.5359
[WDM] - Get LATEST driver version for 108.0.5359
[WDM] - Driver [/Users/brianha/.wdm/drivers/chromedriver/mac64/108.0.5359.71/chromedriver] found in cache
You are about to create a new Spotify playlist, Tiësto - Club Life 821 (Musical Freedom Yearmix) 2022-12-24, with 21 tracks on account: brianhha.

0 Öwnboss & FAST BOY - Left & Right
1 BYOR - Flavour
2 Billen Ted & Shift K3Y - Step Correct
3 Fancy Inc ft. Jack Dawson - Circles
4 MORTEN - No Good
5 Sevek & Jake Tarry - Bang Bang
6 TELYKast ft. PHIA - Body To Body
7 PAJANE - Back Once More
8 JAUZ & Habstrakt - Like Before
9 Mike Williams & Magnificence - Here For You
10 Morgan Page & VINNE - On & On
11 KREAM & Jake Tarry - Once Again
12 Jonas Blue & Sevenn - Angles
13 TUJAMO ft. DRUMMAKID - Click
14 KREAM - Pressure
15 Michael Calfan & Leo Stannard - Better
16 Imanbek & BYOR - Belly Dancer
17 Will Sparks & New World Sound - LSD
18 Steff Da Campo - Hot In Here
19 David Guetta & MORTEN - Permanence
20 Öwnboss & Sevek - Move Your Body

Are you sure? (y/n)y
Myw3NDQ0YWM0NDgzZmM3NGMyMzI3OGQ1OGMyZGEwMDY5NGVkZGQ0ZDUx
```

## Future Improvements

* Captcha: Sometimes, you might get caught by captcha and will need to solve it. One upgrade is to capture this through my code and maybe have it enter a debugger, pause, and continue after it's solved.  
* I tried to do this through requests, but it got stuck in captcha right away therefore I resorted to using selenium.   
* Making this into some sort of web application for easy navigation and redirecting to your own login page to avoid cloning and running locally. 