Feature: Emag favorite page

    Background:
      Given home: I am a user on emag.ro Home page
      When home: I search after "iPhone 11, 64GB, White"
      When products: I add product to basket "Telefon mobil Apple iPhone 11, 64GB, White"
      When products: I click Vezi detalii cos

    @favorite
    Scenario: Verify favorite btn and url page
      When cart: I click on favorite button
      When cart: I verify cart is empty
      Then cart: I verify empty cart message is displayed
      When cart: I click favorite button
      Then favorite: I verify favorite page url