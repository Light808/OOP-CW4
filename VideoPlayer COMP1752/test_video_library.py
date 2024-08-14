import pytest
import video_library as lib

def test_get_name():
    assert lib.get_name("01") == "Tom and Jerry"
    assert lib.get_name("02") == "Breakfast at Tiffany's"
    assert lib.get_name("99") is None  # Test for a non-existing video ID

def test_get_director():
    assert lib.get_director("01") == "Fred Quimby"
    assert lib.get_director("02") == "Blake Edwards"
    assert lib.get_director("99") is None  

def test_get_rating():
    assert lib.get_rating("01") == 4
    assert lib.get_rating("02") == 5
    assert lib.get_rating("99") is None 

def test_get_play_count():
    assert lib.get_play_count("01") == 0  
    lib.increment_play_count("01")
    assert lib.get_play_count("01") == 1  
    assert lib.get_play_count("99") is None  

def test_list_all():
    result = lib.list_all()
    assert "01: Tom and Jerry" in result
    assert "02: Breakfast at Tiffany's" in result
    assert "03: Casablanca" in result

def test_add_video():
    success = lib.add_video("06", "Inception", "Christopher Nolan", 5)
    assert success
    assert lib.get_name("06") == "Inception"
    assert lib.get_director("06") == "Christopher Nolan"
    assert lib.get_rating("06") == 5
    success = lib.add_video("06", "Duplicate Video", "Some Director", 1)
    assert not success  

def test_increment_play_count():
    lib.increment_play_count("02")
    assert lib.get_play_count("02") == 1  
    lib.increment_play_count("02")
    assert lib.get_play_count("02") == 2  

def test_update_rating():
    success = lib.update_rating("03", 4)
    assert success
    assert lib.get_rating("03") == 4
    success = lib.update_rating("99", 5)
    assert not success 

def test_get_random_video_id():
    video_id = lib.get_random_video_id()
    assert video_id in lib.library 


if __name__ == "__main__":
    pytest.main()
