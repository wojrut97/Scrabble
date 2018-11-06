SCRABBLES_SCORES = [(1, "E A O I N R T L S U"),
                    (2, "D G"),
                    (3, "B C M P"),
                    (4, "F H V W Y"),
                    (5, "K"),
                    (8, "J X"),
                    (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES for letter in letters.split()}

# C:\Users\19woj\AppData\Local\Programs\Python\Python37-32


def test():
    print(LETTER_SCORES['H'])
    pass
