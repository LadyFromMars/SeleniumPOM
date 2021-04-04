

xpathvar = {
    "cart_badge" : "//span[@class='sfw-header-nav-cart__badge']",
    "search" : "//input[@id='search-autocomplete']",
    "submit_btn" : "//button[@type='submit']",
    "data_name" : "//article[@data-name='Chuckit! Flying Squirrel Dog Toy, Color Varies, Medium']",
    "item_price" : "//span[@class='ga-eec__price']",
    "add_to_cart" : "//input[@data-qa-id='addToCart']",
    "cart" : "//a[@title='your cart']/ancestor::div[@class='cw-popper']",
    "edit_cart" : "//a[text()=' Edit Cart ']",
    "price_description" : "//div[@class='sfw-cart-item__content']//span[@class='sfw-cart-price']",
    "price_cart" : "//div[@class='sfw-cart__summary']//span[@class='sfw-cart-price']",
    "account" : "//a[@title='your account']",
    "sign_in" : "//input[@value='Sign In']",
    "sign_in_by_text" : "//a[contains(@class, 'cw-btn') and contains(text(), 'Sign In')]",
    "username" : "//input[@name='username']",
    "password" : "//input[@name='password']",
    "test" : "//input[@name='testtest']",

}



def search_for_xpath(locator):
    global xpathv_f
    if locator in xpathvar:
        xpathv_f=xpathvar.get(locator)
    return xpathv_f


def copmplete_xpath(xpathkey, fullxpath):
    global xpathv_f
    if fullxpath =='':
        xpathv_f=search_for_xpath(xpathkey)
    else:
        xpathv_f= fullxpath
    return xpathv_f


        #return xpathv_f

#search_for_xpath("cart_badge")
#copmplete_xpath("cart_badge", "")

#print(xpathv_f)

