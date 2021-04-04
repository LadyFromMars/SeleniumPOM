import fn.actions as fns
import fn.cmn as fnc


#---------------------------------------------------------------------------------------------
# Test: cart01.py
# Description: Search for item and add it to the cart. Verify price.
#---------------------------------------------------------------------------------------------

description = "Description: Search for item and add it to the cart. Verify price."

    #Start of test
fns.actions.start_test("cart01", description)

    #--Log in
fnc.cmn.login('','')

    #--Verify car badge: 0 items added
fns.actions.verify_text("cart_badge", "", '0', 'Verify car badge shows 0 items added')

    #--Search for an item
textv='chuckit! flying squirrel'
fns.actions.input("search", "", 'y', textv, 'Search for an item chuckit flying squirrel')
fns.actions.click("submit_btn", "", "Click on Search icon", "") #Click on Search icon


#fns.actions.click("test", "", "test exception", "") #fail test, throw exception

    #--Click on item to open it in a new tab
fns.actions.click("data_name", "", "Click on item to open it in a new tab", "")

    #--Verify item price
fns.actions.verify_text("item_price", "", '$7.98', 'Verify item price on cataloge page')

    #--Add to Cart
fns.actions.click("add_to_cart", "", "Add to Cart", "y")

#--Verify message: added to your cart
xpathv="//p[@class='sfw-product-sku__added__label']"
fns.actions.verify_text('', xpathv, 'added to your cart', 'Verify message item added to your cart')

    #--Verify number of items in a card updated to 1
fns.actions.verify_text("cart_badge", "", '1', 'Verify number of items in a card updated to 1')

    #--Click on a cart to open it
fns.actions.click("cart", "", "Click on a cart to open it", "")
fns.actions.click("edit_cart", "", "Click Edit Cart", "y")

    #Verify price in cart item description
fns.actions.verify_text("price_description", "", '$7.99', 'Verify price in cart item description')

    #Verify price in cart subtotal
fns.actions.verify_text("price_cart", "", '$7.99', 'Verify price in cart subtotal')

#fns.actions.screenshot("test")



    #---------------------------
    #End of test
fns.actions.tearDown()
