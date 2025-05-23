training_data = [
    # Greetings
    # Greetings
("hello", "greeting"),
("hi", "greeting"),
("hi there", "greeting"),
("hey", "greeting"),
("hey there", "greeting"),
("good morning", "greeting"),
("good afternoon", "greeting"),
("good evening", "greeting"),
("greetings", "greeting"),
("how are you?", "greeting"),
("hope you're doing well", "greeting"),

    # Pricing
    ("What are your prices?", "pricing"),
    ("How much is a cake?", "pricing"),
    ("Can I get a price list?", "pricing"),
    ("What is the price of chocolate cake?", "pricing"),
    ("How much does a cheesecake cost?", "pricing"),

    # Purchase
    ("I want to place an order", "purchase"),
    (" i want  order cake", "purchase"),
    (" how i order cake", "purchase"),
    (" how to order cake", "purchase"),


    ("Can I buy some cookies?", "purchase"),
    ("Do you sell cupcakes?", "purchase"),
    ("I want to order a cake for delivery", "purchase"),
    ("Can I reserve a cake for tomorrow?", "purchase"),

    # Location
    ("Where is your shop?", "location"),
    ("Can you tell me your branches?", "location"),
    ("Can you tell me your branche?", "location"),
    ("Do you have any branches in Chennai?", "location"),
    ("Do you have any branche in Chennai?", "location"),
    ("Is there a branch near my home?", "location"),
    ("Do you deliver to Coimbatore?", "location"),
    ("Where can I find your bakery?", "location"),
    ("Do you have a shop in Bangalore?", "location"),
    ("Where are you located?", "location"),
    (" where is your location", "location"),
    ("location", "location"),
    ("branche", "location"),
    ("Can you give me directions to your store?", "location"),

    # Items
    ("What cake do you sell?", "items"),
    ("cake name list", "items"),
    ("cake name", "items"),
    ("Show me your menu", "items"),
    ("menu", "items"),
    ("menu card", "items"),
    ("Do you sell breads and pastries?", "items"),
    ("What are your best-selling items?", "items"),
    ("Do you have eggless options?", "items"),
    ("Which product you have", "items"),

    # Contact
    ("How can I contact you?", "contact"),
    ("contact ", "contact"),
    
    ("i want contact number", "contact"),
    ("What's your phone number?", "contact"),
    ("Give me your contact details", "contact"),
    ("Do you have an email address?", "contact"),
    ("Can I chat with you directly?", "contact"),

    # Order status
    ("Where is my order?", "orderstatus"),
    ("When will my cake arrive?", "orderstatus"),
    ("I want to track my order", "orderstatus"),
    ("Can you check my order status?", "orderstatus"),
    ("Is my order on the way?", "orderstatus"),

    # Support
    ("I need help with my order", "support"),
    ("There's a problem with my delivery", "support"),
    ("I need support", "support"),
    ("My order is delayed", "support"),
    ("The cake I received was damaged", "support"),
    ("I want to cancel my order", "support"),
    ("I have a suggestion", "support"),
    ("Can I give feedback?", "support"),
    ("I want to share my experience", "support"),
    ("How can I leave a review?", "support"),
    ("I want to compliment your service", "support"),
    ("I have a complaint", "support"),
    ("I am not satisfied with my order", "support"),
    ("I want to report an issue", "support"),
    ("My cake was not fresh", "support"),
    ("I received the wrong order", "support"),
    # Purchase (corrected and expanded)


    ("I want to place an order", "purchase"),
    ("I want to order a cake", "purchase"),
      ("how i place a order ", "purchase"),
    ("how to place a order ", "purchase"),
     ("how to order  cake", "purchase"),
    
    ("Can I buy some cookies?", "purchase"),
    ("Do you sell cupcakes?", "purchase"),
    ("I want to order a cake for delivery", "purchase"),
    ("Can I reserve a cake for tomorrow?", "purchase"),
    ("I want to buy a birthday cake", "purchase"),
    ("Can I order pastries?", "purchase"),
    ("I need to place an order for a party", "purchase"),
    ("Can I pre-order a cake?", "purchase"),
    
    # Support (corrected and expanded)
    ("I need help with my order", "support"),
    ("There's a problem with my delivery", "support"),
    ("I need support", "support"),
    ("My order is delayed", "support"),
    ("The cake I received was damaged", "support"),
    ("I want to cancel my order", "support"),
    ("I have a suggestion", "support"),
    ("Can I give feedback?", "support"),
    ("I want to share my experience", "support"),
    ("How can I leave a review?", "support"),
    ("I want to compliment your service", "support"),
    ("I have a complaint", "support"),
    ("I am not satisfied with my order", "support"),
    ("I want to report an issue", "support"),
    ("My cake was not fresh", "support"),
    ("I received the wrong order", "support"),
    ("Can you help me with a refund?", "support"),
    ("I need assistance with my order", "support"),
    ("The delivery was late", "support"),
    ("I want to escalate my issue", "support"),
    # Thank you
    ("Thanks for the help", "thank"),
    ("Thank you", "thank"),
     ("thank you", "thank"),
    ("Thanks a lot!", "thank"),
    ("Much appreciated", "thank"),
    ("Thank you for assisting me", "thank"),

    # Offers
    ("Do you have any offers?", "offers"),
    ("do you have any offer?", "offers"),
    ("any offer?", "offers"),
    ("offer details","offers"),
    ("offers details","offers"),

    ("are there any discounts?", "offers"),

    # Hours
    ("What are your operating hours?", "hours"),
    ("Are you open on weekends?", "hours"),
    ("Are you open on weekend?", "hours"),
     ("open time", "hours"),
    ("open timing", "hours"),
    ("opening time", "hours"),
     ("time", "hours"),
      ("timing", "hours"),


    # Customization
    ("Can I customize my cake?", "customization"),
    ("Do you make themed cakes?", "customization"),
    ("Can I choose the flavor of my cake?", "customization"),
    ("Can I get a cake with my photo?", "customization"),
    ("Do you offer cake customization?", "customization"),
    ("Can I get a cake with my name on it?", "customization"),
    ("Can I get a cake with my name?", "customization"),

    # Order not received
    ("I have not received my order", "ordernotreceived"),
    ("My order is not delivered yet", "ordernotreceived"),
    ("I am waiting for my order", "ordernotreceived"),
    ("I have not received my cake", "ordernotreceived"),
    ("My order is delayed", "ordernotreceived"),
    ("I want to check my order status", "ordernotreceived"),
    ("Can you check my order status?", "ordernotreceived"),
    ("Is my order on the way?", "ordernotreceived"),
    ("Where is my order?", "ordernotreceived"),
    ("When will my cake arrive?", "ordernotreceived"),
    ("I want to track my order", "ordernotreceived"),

    # Response with order ID
    ("its my order id 123456789", "response"),
    ("its my order ID 7418528", "response"),
    ("its my order ID 1234", "response"),
    ("i want to know the status of order 123456", "response"),
    ("order no is 987654", "response"),
    ("my order id is 456321", "response"),
    ("can you track order 852963", "response"),
    ("here is my order 369258", "response"),
    ("order 147258 is delayed", "response"),
    ("741852 is my order id", "response"),
    ("i placed order number 7894561230", "response"),
    ("pls check 258741 order", "response"),
    ("order ID is 369258", "response"),
]



responses = {
    "greeting": "Hello! Welcome to Sweet Treats Bakery. How can I assist you today?",
    
    "pricing": (
        "Here are some cake price details:\n"
        "- Chocolate Truffle Cake: ₹500 (0.5 kg), ₹900 (1 kg)\n"
        "- Red Velvet Cake: ₹550 (0.5 kg), ₹950 (1 kg)\n"
        "- Black Forest Cake: ₹450 (0.5 kg), ₹850 (1 kg)\n"
        "- Butterscotch Delight: ₹480 (0.5 kg), ₹880 (1 kg)\n"
        "- Pineapple Cream Cake: ₹430 (0.5 kg), ₹820 (1 kg)\n"
        "Let me know if you'd like to place an order or need more details!"
    ),

    "purchase": (
        "You can place your order directly through our website, visit any of our branches, or call us at +91-9876543210. "
        "Let us know if you need assistance!"
    ),

    "location": (
        "We have branches in Chennai, Bangalore, and Hyderabad. Let me know if you’d like more details or directions!"
    ),

    "items": (
        "Here’s our menu:\n"
        "- Chocolate Truffle Cake\n"
        "- Red Velvet Cake\n"
        "- Black Forest Cake\n"
        "- Butterscotch Delight\n"
        "- Pineapple Cream Cake\n"
        "- Cheesecakes, Cookies, Pastries, and more!\n"
        "Would you like to know prices or place an order?"
    ),

    "contact": "You can contact us at +91-9876543210 or email us at contact@sweettreats.com.",

    "support": (
        "I’m here to help! Could you share more details about the issue?\n"
        "For urgent assistance, you can also call us at +91-9876543210."
    ),

    "thank": "You're welcome! Have a sweet day! 🍰",

    "offers": (
        "We currently have a 'Buy 1 Get 1 Free' offer on select cookies and cupcakes! "
        "Check our website or visit our store for more details."
    ),

    "hours": "Our bakery operates from 9:00 AM to 9:00 PM, Monday to Sunday.",

    "customization": (
        "Yes, we do offer cake customizations! You can choose flavors, themes, and designs for your cakes. "
        "Let us know your preferences, and we’ll make it happen!"
    ),

    "orderstatus": (
        "To check your order status, please provide your order number or the name under which the order was placed. "
        "You can also call us at +91-9876543210 for immediate assistance."
    ),

    "ordernotreceived": (
        "I’m sorry to hear that you haven’t received your order. Please provide your order number or the name under which the order was placed, and I’ll check the status for you."
    ),

    "response": (
        "Thank you for sharing your order number. Your order is on the way."
    )
}