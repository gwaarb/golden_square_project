from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_generate_cat_fact_request_and_response():
    requester_mock = Mock()
    response_mock = Mock()
    
    requester_mock.get.return_value = response_mock
    
    response_mock.json.return_value = {
        "fact": "cats have tails"
    }
    
    cat_fact = CatFacts(requester_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: cats have tails"