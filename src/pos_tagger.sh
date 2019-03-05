cd twitie-tagger
java -jar twitie_tag.jar models/gate-EN-twitter-fast.model $1 > $2
mv $2 ..x
cd ..
python3 tweetgen.py