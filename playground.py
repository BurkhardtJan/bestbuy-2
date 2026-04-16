import products
import store
import promotions

if __name__=="__main__":
    # setup initial stock of inventory
    mac =  products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250)

    best_buy = store.Store([mac, bose])
    new_store = store.Store([mac, bose, pixel])
    #mac.price = -100         # Should give error
    print(mac)               # Should print `MacBook Air M2, Price: $1450 Quantity:100`
    print(mac > bose)        # Should print True
    print(mac in best_buy)   # Should print True
    print(pixel in best_buy) # Should print False

    print(best_buy)
    double_store = best_buy + new_store
    print(double_store)
    print(best_buy)