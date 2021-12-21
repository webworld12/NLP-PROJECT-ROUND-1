from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk import FreqDist
from matplotlib import pylab as plt
from nltk.tag import pos_tag
from nltk.corpus import brown
from wordcloud import WordCloud, STOPWORDS
import re
import string


#Function for creating a set of 
#(contracted_form,expanded_form) list
def contractions_set():
	contractions_dict = {
		'can\'t': 'cannot',
	'could\'ve': 'could have',
	'couldn\'t': 'could not',
	'didn\'t': 'did not',
	'doesn\'t': 'does not',
	'don\'t': 'do not',
	'hadn\'t': 'had not',
	'hasn\'t': 'has not',
	'haven\'t': 'have not',
	'how\'d': 'how did',
	'how\'ll': 'how will',
	'I\'m': 'I am',
	'I\'ve': 'I have',
	'isn\'t': 'is not',
	'let\'s': 'let us',
	'ma\'am': 'madam',
	'mayn\'t': 'may not',
	'might\'ve': 'might have',
	'mightn\'t': 'might not',
	'must\'ve': 'must have',
	'mustn\'t': 'must not',
	'needn\'t': 'need not',
	'o\'clock': 'of the clock',
	'oughtn\'t': 'ought not',
	'shan\'t': 'shall not',
	'so\'ve': 'so have',
	'they\'re': 'they are',
	'they\'ve': 'they have',
	'to\'ve': 'to have',
	'wasn\'t': 'was not',
	'we\'ll': 'we will',
	'we\'re': 'we are',
	'we\'ve': 'we have',
	'weren\'t': 'were not',
	'what\'re': 'what are',
	'what\'ve': 'what have',
	'when\'ve': 'when have',
	'where\'d': 'where did',
	'where\'ve': 'where have',
	'who\'ve': 'who have',
	'why\'ve': 'why have',
	'will\'ve': 'will have',
	'won\'t': 'will not',
	'would\'ve': 'would have',
	'wouldn\'t': 'would not',
	'y\'all': 'you all',
	'you\'re': 'you are',
	'you\'ve': 'you have'
	}
	return contractions_dict
	
	

#PreprossingFunction
#Expands the contractions
#present in the text
def expand_contractions(text):
	contractions_dict = contractions_set()
	contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))
	def replace(match):
	    return contractions_dict[match.group(0)]
	return contractions_re.sub(replace, text)


#Preprocessing Function
#removes punctuations
#from the text
def remove_punctuation(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 



#Preprocessing Function
#convertes all the 
#uppercases to lowercases    
def text_lowercase(text): 
    return text.lower() 



#Preprocessing Function
#removes whitespaces
#from the text    
def remove_whitespaces(text): 
    return  " ".join(text.split()) 
	


#Preprocessing Function
#Removes the "Chapter (chapter number)" 
#from the text
def remove_chap(text): 
    result = re.sub(r'CHAPTER \d+', '', text) 
    return result 	



#Preprocessing Function
#Preprocesses the Book1
def preprocessing_book1(text):
	
	#Removing the title and author name from the text
	text = text.replace( "[Sense and Sensibility by Jane Austen 1811]" , ' ' )
	
	#Removing the end form the text
	text = text.replace("THE END" , ' ' )
	
	#Calling all the prepocessing functions
	#for the book1 text
	text = remove_chap(text)
	text = expand_contractions(text)
	text = remove_punctuation(text)
	text = remove_whitespaces(text)
	text = text_lowercase(text)
	
	#returning the preprocessed text
	return text



#Preprocessing Function
#Preprocesses the Book2
def preprocessing_book2(text):

	#Removing the title and author name from the text
	text = text.replace( "[Persuasion by Jane Austen 1818]" , ' ' )
	
	#Removing the end form the text
	text = text.replace("Finis" , ' ' )
	
	#Calling all the prepocessing functions
	#for the book2 text
	text = remove_chap(text)
	text = expand_contractions(text)
	text = remove_punctuation(text)
	text = remove_whitespaces(text)
	text = text_lowercase(text)
	
	#returning the preprocessed text
	return text
	



#Creating a frequency distribution
#of a given list of tokens	
def freq_dist(token):

	fd = FreqDist(token)
	
	#displaying the samples and outcomes
	print(fd)
	
	#displaying the 20 most common words
	print(fd.most_common(20))
	print('\n\n\n\n')
	
	#ploting a line graph of 20 most common words
	fd.plot(20)
	



#Creating a wordcloud 
#firstly with stopwords 
#then without stopwords
def word_cloud(text):

	stopwords = set(STOPWORDS)
	#clearling the stopwords set so 
	#the word can be made with stopwords
	stopwords.clear()
	
	#creating wordcloud with stopwords
	wordcloud = WordCloud(width = 800, 
							height = 800, 
							background_color ='black', 
							stopwords = stopwords, 
							min_font_size = 10).generate(text) 
	
	#displaying the wordcloud made                  
	plt.figure(figsize = (8, 8), facecolor = None) 
	plt.imshow(wordcloud) 
	plt.axis("off") 
	plt.tight_layout(pad = 0) 
	 
	plt.show() 
	
	#creating the stopwrods set so the 
	#wordcloud is made without them
	stopwords = set(STOPWORDS)
	
	#Creating wordcloud without stopwords
	wordcloud = WordCloud(width = 800, 
							height = 800, 
							background_color ='white', 
							stopwords = stopwords, 
							min_font_size = 10).generate(text) 
	
	#displaying wordcloud                  
	plt.figure(figsize = (8, 8), facecolor = None) 
	plt.imshow(wordcloud) 
	plt.axis("off") 
	plt.tight_layout(pad = 0) 
	 
	plt.show() 



	
#Function for plotting 
#a bar graph	
def plot(X,Y,xlabel,ylabel,title):
	plt.bar(X, Y, tick_label = X, width = 0.8, color = ['red', 'green'])
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()



#Function to show the 
#relationship between the 
#length of words and their frequency	
def plotRelationShip(fd):

	#fd is the frequency distribution of each of word
	
	#word length is a list that will 
	#store the length of a word and the
	#frequency of the words of that length
	word_lengths = {}
	
	
	for i in fd.keys():
		if len(i) not in word_lengths.keys():
			word_lengths[len(i)] = fd[i]	#adding a new word length and its frequency
		else:
			word_lengths[len(i)] += fd[i]	#adding the frequency of already existing word length
	
	#X will contain all lengths of the word
	#Y will contain the corresponding frequency		
	X = []
	Y = []
	
	for i in word_lengths.keys():
		X.append(i)
		
	X.sort()
	
	for i in X:
		Y.append(word_lengths[i])
		
	#Plotting a bar graph for recorded data
	xlabel = 'word length'
	ylabel = 'frequency'
	title = 'Relationship between word length and frequency'
	plot(X,Y,xlabel,ylabel,title)

	

#Function for PoS_Tagging
def PoS_Tagging(token):
	
	#PoS tagging done using pos_tag function
	tagged_tuple = pos_tag(token)
	
	#tagged_tuple contains list of (w,t) tuples 
	#where w is the word and 
	#t is the tag for the word
	
	
	#collecting all the tags used 
	tags = [ t for (w,t) in tagged_tuple ]
	
	
	#Analysing frequency distribution of the tags
	freq_dist(tags)
	
	
	
#t1 contains the book1
t1 = open("book1.txt","r")
t1 = t1.read()

#t2 contains the book2
t2 = open("book2.txt","r")
t2 = t2.read()

#Preprocessing Book1
t1 = preprocessing_book1(t1)

#Preprocessing Book2
t2 = preprocessing_book2(t2)

#Tokenizing Book1
token_t1 = word_tokenize(t1)

#Tokenizing Book2
token_t2 = word_tokenize(t2)

#Analyzing Frequency Distribution 
#of tokens in Book1
freq_dist(token_t1)

#Analyzing Frequency Distribution 
#of tokens in Book2
freq_dist(token_t2)

#Generating WordCloud for Book1
word_cloud(t1)

#Generating WordCloud for Book2
word_cloud(t2)

#Plotting the relationship between 
#word length and word frequency
plotRelationShip(FreqDist(token_t1))

#Plotting the relationship between 
#word length and word frequency
plotRelationShip(FreqDist(token_t2))

#Pos_Tagging for Book1
PoS_Tagging(token_t1)

#PoS_Tagging for Book2
PoS_Tagging(token_t2)

#Mayank Roy Gautam Agrawal Sansakr Garg







