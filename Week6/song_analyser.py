## song lyric analyser ##

# step 1: strip punctuation and make each word an item in a list

# step 2:

lyrics = """
Just somethin' about you
Way I'm lookin at you whatever
keep lookin at me
Gettin' scared now, right?
Don't fear me baby, it's just Justin
It feel good right?
Listen

I kind of noticed something wasn't right
In your colorful face
It's kind of weird to me
Since you're so fine
If it's up to me your face'll change......

If you smilin', that should set the tone
Just be limber
And If you let go, the music should groove your bones
Just remember
Sing this song with me

Ain't nobody love you like I love you
You're a good girl and that's what makes me trust ya
Late at night, I talk to you
You will know the difference when I touch you

People are so phony
Nosy cause they're lonely
Aren't you sick of the same thing?
They say so and so was dating
Love you or they're hating
When it doesn't matter anyway
Cause we're here tonight

If you smiling, that should set the tone
Just be limber baby
And If you let go, the music should groove your bones
Baby just remember
Sing this song with me

Ain't nobody love you like I love you
You're a good girl and that's what makes me trust ya
Late at night, I talk to you
You will know the difference when I touch you

Yeah, you know I can make ya happy
I could change your life
If you give me that chance
To be your man
I won't let you down baby
If you give me that chance
To be your man
Here baby, put on my jacket
And then ...

Maybe we'll fly the night away (I just wanna love you baby)
Yeah, yeah, yeah
Girl
Maybe we'll fly the night away(I just wanna love you baby)
Girl ...

Ma, what you wanna do?
I'm in front of you
Grab a friend, see I can have fun with two
Or me and you put on a stage show
And the mall kids, that's how to change low
From them you heard "wow, it's the same glow"
Look at me, I say "yeah, it's the same dough"
We the same type, you my air of life
You have me sleeping in the same bed, every night

Go rock with me, you deserve the best
Take a few shots
Let it burn in your chest
We could ride down
Pumping N.E.R.D. in the deck
Funny how a few words turn into sex
Play this free, joint called "brain"
(I just love your, Brain)
Ma, take a hint
Make me suerve in the lane
The name Malicious
And I burn every track
Clipse and J. Timberlake
Now how heavy is that?

Maybe we'll fly the night away (I just wanna love you baby)
Yeah, yeah, yeah
Girl
Maybe we'll fly the night away(I just wanna love you baby)
Girl ...

Ain't nobody love you like I love you
(Can't love you like I do)
You're a good girl and that's what makes me trust ya
(Trust ya like I do)
Late at night, I talk to you
(Hey)
You will know the difference when I

Break this down

You know, I used to dream about this when I was a
little boy
I never thought it would end up this way, Drums
(Hey)
It's kind of special right? yeah
You know, you think about it
Sometimes people just destined
Destined to do what they do
And that's what it is
Now everybody dance."""


def toChars(s):
    s = s.lower()
    res = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz ':
            res = res + c
    return res


# def isOverThresh(j): #takes a dictonary assigns the temp name j to it
#     for i in j:      # for each item in k
#         if occurances =< x.values():   #checks if its value is =< than the occurance number we asked for
#             result = result + x     #if it is then we add that to the output_words
#     return result

lyrics = lyrics.replace('\n', ' ') #converts all line breaks into spaces
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
