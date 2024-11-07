#Experimenting emojis

import demoji
class testing_Emoji:
     def __int__(self):
        pass
     def print_emoji(self):

        print("trying differenct emojees")
       # thumbsup="\U0001F600"
        print("\U0001F600")
        text ="i feel 😀😀😃😄😁"
        emotions=demoji.findall(text)
        print(emotions)
        #print(emoji.emojize('this is :thumbs up:',language='alias'))
        #print(emoji.emojize("red_heart"))
obj1= testing_Emoji()
obj1.print_emoji()
