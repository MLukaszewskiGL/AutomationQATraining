
def test_github_invalid_login(github_login_page):
    github_login_page.try_to_login("user", "password")

    assert github_login_page.check_error_message()

