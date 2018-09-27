#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
#Variables that contains the user credentials to access Twitter API 
access_token = "590093056-3urrwBCTS9IfciDLlJsQi2RBni2A5g6w9hdmq18e"
access_token_secret = "3ixOi6KMy2ktOYIVwk4FNJHvQGusllUT6bbvnj4sKJnC9"
consumer_key = "JjozT4EM7F8AMAtObaWAmyKZp"
consumer_secret = "UMYaUyeaykbKGb10rYK0rX9Uf8nWuGo1hx8e4pfSxEiwBlQTYz"

class StdOutListener(StreamListener):

    def on_data(self, data):
        d = json.loads(data)
        #print(data)
        #print("=====================INICIO========================================")
        print(d['text'])
        #print("=====================FIN========================================")
        with open('se.json','a') as outfile:
            #json.dump(data, outfile)
            outfile.write(data)
        return True

        def on_error(self, status):
            print(status)


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['uber','easytaxi','cabify','beat'],languages=['es'])