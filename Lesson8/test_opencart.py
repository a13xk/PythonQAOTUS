def test_main_page(browser, opencart_base_url):
    browser.get(opencart_base_url)
    footer = browser.find_element_by_tag_name(name="footer")
    assert "OpenCart" in footer.text
#
