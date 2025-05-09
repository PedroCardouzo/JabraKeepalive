# Jabra Keepalive

Jabra has a very dumb feature that puts the headset on sleep mode as soon as ~1 second of silence. 
Yes, this is somehow not a bug, but a feature. 
So fine, I'll fix it myself :)

## Validated
for now, only on Windows with Jabra Evolve2 85.

## Install
### Windows
`pip install sounddevice numpy`
### MacOS
first, install portaudio
`brew install portaudio`
then, run the same install command as the windows version
`pip install sounddevice numpy`
if you already had sounddevice installed before portaudio, you might need to reinstall it
`pip install --force-reinstall --no-cache-dir sounddevice`

## Run
`python jabra-keepalive.py`
