python3 -m pip install playsound
python3 -m pip install tk
python3 -m pip install pyobjc
python3 -m pip install pyaudio
python3 -m pip install tk

mkdir /Users/$(USERS)/alarm42
cp main.py sound.mp3 /Users/$(USERS)/alarm42

echo 'alias alarm="python3 ~/alarm42/main.py &"' >> /Users/$(USERS)/.zshrc
echo 'alias alarm_stop="pkill -f main.py"' >> /Users/$(USERS)/.zshrc
echo 'alias alarm_config="open /Users/$(USERS)/alarm42"' >> /Users/$(USERS)/.zshrc