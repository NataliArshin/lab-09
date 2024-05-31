from pages.var_16.main import *

def test_survivors_female_in_all_classes():
    test_data = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,0,female,0,0,0,0,71.23,0,0',
        '2,1,2,0,0,male,0,0,0,0,8.13,0,0',
        '3,1,2,0,0,female,0,0,0,0,24.1000,0,0',
        '4,1,1,0,0,male,0,0,0,0,40.0500,0,0',
        '5,1,3,0,0,female,0,0,0,0,14.9250,0,0',
        '6,1,2,0,0,male,0,0,0,0,53.35,0,0',
        '7,1,2,0,0,female,0,0,0,0,53.10,0,0',
        '8,1,2,0,0,male,0,0,0,0,15.412224,0,0',
        '9,1,1,0,0,male,0,0,0,0,33.924250,0,0',
        '10,1,2,0,0,female,0,0,0,0,52.142,0,0',
    ]
    price = (0, 100)
    assert count_survivors(test_data, price) == [1, 3, 1]


def test_survivors_female_expensive_tickets_only():
    test_data = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,0,female,0,0,0,0,421.23,0,0',
        '2,1,2,0,0,male,0,0,0,0,8.13,0,0',
        '3,1,2,0,0,female,0,0,0,0,24.1000,0,0',
        '4,1,1,0,0,female,0,0,0,0,412.0500,0,0',
        '5,1,3,0,0,female,0,0,0,0,14.9250,0,0',
        '6,1,2,0,0,male,0,0,0,0,53.35,0,0',
        '7,1,2,0,0,female,0,0,0,0,122.10,0,0',
        '8,1,2,0,0,male,0,0,0,0,105.424,0,0',
        '9,1,1,0,0,male,0,0,0,0,33.924250,0,0',
        '10,1,2,0,0,female,0,0,0,0,52.142,0,0',
    ]
    price = (100, 1000)
    assert count_survivors(test_data, price) == [2, 1, 0]


def test_not_survived_female():
    test_data = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,0,1,0,0,female,0,0,0,0,421.23,0,0',
        '2,1,2,0,0,male,0,0,0,0,8.13,0,0',
        '3,1,2,0,0,female,0,0,0,0,24.1000,0,0',
        '4,0,1,0,0,female,0,0,0,0,412.0500,0,0',
        '5,1,3,0,0,female,0,0,0,0,14.9250,0,0',
        '6,1,2,0,0,male,0,0,0,0,53.35,0,0',
        '7,0,2,0,0,female,0,0,0,0,122.10,0,0',
        '8,0,3,0,0,male,0,0,0,0,105.424,0,0',
        '9,1,1,0,0,male,0,0,0,0,33.924250,0,0',
        '10,0,2,0,0,female,0,0,0,0,52.142,0,0',
    ]
    price = (100, 1000)
    assert count_survivors(test_data, price) == [0, 0, 0]
