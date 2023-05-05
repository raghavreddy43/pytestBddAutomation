import pytest
from src.pom.tests.Testbase import BaseTest


class TestCountryPage(BaseTest):
    # Class automatically manage a tearUp and tearDown

    @pytest.parametrize('username, password', [('admin', 'password')])
    def test_validate_login(self, username, password):
        """
    Given user navigate to RestfulBookerPlatform Home page
    When I click on admin panel link
    When I enter Username and Password
    And I click on login button
    And login successfully
    Then click on logout button
        """
        assert self.home_page.logo_is_displayed() == True

    @pytest.parametrize('username, password', [('admin', 'incorrect1'), ('incorrect2', 'password'), ('incorrect3', 'incorrect4')])
    def test_validate_unsuccessful_login(self, username, password):
        """
    Given user navigate to RestfulBookerPlatform Home page
    When I click on admin panel link
    When I enter Username and Password
    And I click on login button
    Then login should be unsuccessful
        """
        assert self.home_page.invalid_credentails_displayed()
        assert self.home_page.invalid_credentails() == False

    @pytest.parametrize('username, password, room, type, accessible, price, roomdetails', [('admin', 'password', '101', 'Single', 'false', '100', 'WIFI')])
    def test_validate_country_list(self, username, password, room, type, accessible, price, roomdetails):
        """
    Given user navigate to RestfulBookerPlatform Home page
    When I click on admin panel link
    When I enter Username as "<username>" and Password as "<password>"
    When I enter booking details Room, Type, Accessible, Price, RoomDetails
    Then click create button
    Then the room is created and details shown
        """
        assert self.home_page.logo_is_displayed() == True
        self.room_booking(username, password, room, type, accessible, price, roomdetails)
        assert room in self.room_booking()
