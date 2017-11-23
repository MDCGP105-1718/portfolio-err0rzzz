## song lyric analyser ##

# step 1: strip punctuation and make each word an item in a list

# step 2:

lyrics = """
I get up, and nothing gets me down.
You got it tough. I've seen the toughest all around.
And I know, baby, just how you feel.
You've got to roll with the punches to get to what's real
Oh can't you see me standing here,
I've got my back against the record machine
I ain't the worst that you've seen.
Oh can't you see what I mean?
Might as well jump. Jump!
Might as well jump.
Go ahead, jump. Jump!
Go ahead, jump.
Aaa-ohh Hey you! Who said that?
Baby how you been?
You say you don't know, you won't know until you begin.
Well can't you see me standing here,
I've got my back against the record machine
I ain't the worst that you've seen.
Oh can't you see what I mean?
Might as well jump. Jump!
Go ahead, jump.
Might as well jump. Jump!
Go ahead, jump.

[Guitar solo]

[Keyboard solo]

Might as well jump. Jump!
Go ahead, jump.
Get it and jump. Jump!
Go ahead, jump. """



def toChars(raw_string):
    '''
    input: raw_string data
    output: string data in lowercase with all non alphabet removed
    and spaces retained. converts line breaks to spaces.
    '''
    raw_string = raw_string.lower()
    raw_string = raw_string.replace('\n', ' ') #converts all line breaks into spaces

    res = ''
    for char in raw_string:
        if char in 'abcdefghijklmnopqrstuvwxyz ':
            res = res + char
    return res


##main program
lyrics = toChars(lyrics) #remove all unwanted symbols from string
lyric_list = lyrics.split()
search_freq = int(input ('minimum threshold for word occurances?: '))

words_freq = {}
output_words = []

### for each word in the list it checks if its already in the dictionary
for word in lyric_list:
    if word not in words_freq: ## if its not the key is created and value set to one
        words_freq[word] = 1
    else:
        words_freq[word] += 1 ## if it is the value for that key is increased by 1


for word, freq in words_freq.items():
    if freq >= search_freq:
        output_words.append((freq,word))
output_words.sort()
output_words.reverse()

for freq, word in output_words:
     print(word,freq)
