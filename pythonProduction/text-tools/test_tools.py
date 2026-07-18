from main import word_count , shout 

def test_word_count():
    assert(word_count("this is my sentence")) == 4 

def test_shout():
    assert(shout("word")) == "WORD"