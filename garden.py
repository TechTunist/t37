import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = [
    "We painted the wall with cracks",
    "The man who whistles tunes pianos",
    "The cotton clothing is made of grows in Mississippi",
    "Have the students who failed the exam take the resit",
    "I know the words to that song about the queen don’t rhyme",
    "The complex houses married and single soldiers and their families"
    ]

for i in gardenpathSentences:
    doc = nlp(i)

    # tokenisation
    tokenised = ([token.orth_ for token in doc])

    # entity recognition
    print([(i, i.label_, i.label) for i in doc.ents])


# spacy only gave one sentence any value for entity recognition...

output = """
[]
[]
[(Mississippi, 'GPE', 384)]
[]
[]
[]
"""
#GPE stands for Geopolitical Entity (country, state etc)