## NightCycle

Changes a user's Sublime Text 2 colour scheme and UI theme automatically according to what time of day it is.

## Usage

Install in your preferred fashion, then restart Sublime Text.

If desired, configure your time periods and desired colour schemes by editing the config file, which can be accessed through these steps:

Preferences menu -> Package Settings -> NightCycle -> Settings - User

This file will initially be blank, look at the contents of "Settings - Default" to get the configuration structure (it's easiest to copy the default configuration over and then edit from that base).

The default time periods are 'day' and 'night', switching between Solarized Light and Solarized Dark at 0700 hours and 1700 hours respectively.

Time periods should not overlap, as this could result in rapid switching between the overlapping colour schemes.

If no configured time period is found for a given time, the current colour scheme will continue to be used.

Start and end times must use 24 hour time in the format Hour:Minute in order to be recognised, use the default config as a guide if unsure.

## Acknowledgements

[urbushey](http://www.reddit.com/user/urbushey) for the original idea

[p4ul](https://github.com/p4ul) for contributing code on user settings

[Scott Bai](https://github.com/sbai) for adding in UI theme support
