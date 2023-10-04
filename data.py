# GPT Prompt: Write 2 line description of the book "Drive: The Surprising Truth About What Motivates Us". Please use some very uncommonly used words.
ITEMS = [
    {
        "title": "Pricing Money: A Beginner's Guide to Money, Bonds, Futures and Swaps",
        "description": 'Available for free on: http://www.jdawiseman.com/books/pricing-money/Pricing_Money_JDAWiseman.html. "Pricing Money" delves into the abstruse realm of financial instruments, demystifying the alchemy of bonds, futures, and swaps for neophytes. An indispensable compendium for those eager to decode the esoteric lexicon of monetary machinations.',
        "author": "J. D. A. Wiseman",
        "cost_of_goods_sold": "74.00 CHF",
        "price": "90.00 CHF",
        "price_float": 90.00,
        "gtin": "978-0471487005",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Pricing-Money-Beginners-Guide-Futures/dp/0471487007
    },
    {
        "title": "Harry Potter and the Methods of Rationality",
        "description": 'Available for free on: https://hpmor.com. "Harry Potter and the Methods of Rationality" by Eliezer Yudkowsky is a fecund reimagining of Rowling`s universe, where young Potter, raised by scientists, employs logic and scientific principles in his magical endeavors. A perspicacious exploration of the Wizarding World through the prism of systematic inquiry and critical thought.',
        "author": "Eliezer Yudkowsky",
        "cost_of_goods_sold": "1000 CHF",
        "price": "1300.00 CHF",
        "price_float": 1300.00,
        "gtin": "978-1936661657",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.wikiwand.com/en/Harry_Potter_and_the_Methods_of_Rationality
    },
    {
        "title": "Never Split the Difference: Negotiating As If Your Life Depended On It",
        "description": '"Never Split the Difference" by Chris Voss, a former FBI negotiator, proffers trenchant strategies gleaned from high-stakes hostage situations, recalibrated for quotidian disputes. This magnum opus elucidates the art of parley, where yielding an inch could mean ceding a mile.',
        "author": "Chris Voss",
        "cost_of_goods_sold": "9.69 CHF",
        "price": "15.00 CHF",
        "price_float": 15.00,
        "gtin": "978-0062407801",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Never-Split-Difference-Negotiating-Depended/dp/0062407805
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "description": "Douglas Adams presents a whimsical odyssey through the cosmos, replete with bathrobes and sentient appliances. A scintillating tour de force into the interstellar absurd, where Vogons declaim poetry and answers are worth a mere 42.",
        "author": "Douglas Adams",
        "cost_of_goods_sold": "6.36 CHF",
        "price": "10.00 CHF",
        "price_float": 10.00,
        "gtin": "978-0345391803",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Hitchhikers-Guide-Galaxy-Douglas-Adams/dp/0345391802 
    },
    {
        "title": "Cooking for Geeks: Real Science, Great Hacks, and Good Food",
        "description": '"Cooking for Geeks" melds the empirical rigor of science with the artistry of culinary creation, inviting the cerebrally-inclined to dissect and revel in the gastronomic process. A veritable smorgasbord for those with a predilection for both algorithms and appetizers.',
        "author": "Jeff Potter",
        "cost_of_goods_sold": "24.73 CHF",
        "price": "32.00 CHF",
        "price_float": 32.00,
        "gtin": "978-0596805883",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Cooking-Geeks-Science-Great-Hacks/dp/0596805888
    },
    {
        "title": "Radical Candor: Be a Kick-Ass Boss Without Losing Your Humanity",
        "description": '"Radical Candor" by Kim Scott promulgates the ethos of juxtaposing unvarnished feedback with profound empathy, forging leadership par excellence. A sagacious blueprint for melding solicitude with veracious communication in the modern workspace.',
        "author": "Kim Scott",
        "cost_of_goods_sold": "11.33 CHF",
        "price": "16.00 CHF",
        "price_float": 16.00,
        "gtin": "978-1250103505",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Radical-Candor-Kick-Ass-Without-Humanity/dp/1250103509
    },
    {
        "title": "Managing Humans: Biting and Humorous Tales of a Software Engineering Manager",
        "description": '"Managing Humans" by Michael Lopp unveils the arcane intricacies of the tech leadership labyrinth, replete with vignettes of capricious personalities and office quiddities. A perspicacious manual for navigating the often turbid waters of engineering leadership with sagacity.',
        "author": "Michael Lopp",
        "cost_of_goods_sold": "15 CHF",  # ???
        "price": "20.00 CHF",
        "price_float": 20.00,
        "gtin": "978-1430243144",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/Managing-Humans-Humorous-Software-Engineering/dp/1430243147
    },        
    {
        "title": "How to Win Friends & Influence People",
        "description": '"How to Win Friends and Influence People" by Dale Carnegie is a magisterial treatise on the nuances of human rapport, imparting time-tested stratagems for engendering goodwill and evoking influence. This seminal work demystifies the alchemy of efficacious interpersonal dynamics in both personal and professional realms.',
        "author": "Dale Carnegie",
        "cost_of_goods_sold": "10.30 CHF",
        "price": "15.00 CHF",
        "price_float": 15.00,
        "gtin": "978-0671027032",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034
    },
    {
        "title": "Drive: The Surprising Truth About What Motivates Us",
        "description": 'In "Drive," Pink elucidates the enigmatic mechanisms of human motivation, debunking traditional reward systems and proffering the intrinsic trinity: autonomy, mastery, and purpose. A perspicacious tome on the psychodynamics of human propulsion.',
        "author": "Daniel H. Pink",
        "cost_of_goods_sold": "13.99 CHF",
        "price": "20.00 CHF",
        "price_float": 20.00,
        "gtin": "978-1594488849",
        "google_product_category": "Media > Books",
        "product_type": "Books",
        "shipping_height": "20.5 cm",
        "shipping_length": "12 cm",
        "shipping_width": "5 cm",
        "shipping_weight": "450 g",
        # https://www.goodreads.com/book/show/6452796-drive
        # https://www.amazon.com/gp/product/B004P1JDJO
    },
    {
        "title": "Colorbang Headphones",
        "description": 'A light and elegant design and super sound quality make these over-ear headphones a constant companion. Foldable to save space, and printed with the white Google logo on one earpiece.',
        "author": "Google factory",
        "cost_of_goods_sold": "7.2 CHF",
        "price": "11.05 CHF",
        "price_float": 11.05,
        "brand": "Google",
        "gtin": "50644632143",  # 11 characters seems incorrect
        "google_product_category": " Electronics > Audio > Audio Components > Headphones & Headsets > Headphones",
        "product_type": "Google accessories",
        "shipping_height": "20.5 cm",
        "shipping_length": "10 cm",
        "shipping_width": "4 cm",
        "shipping_weight": "250 g",
    },
    {
        "title": "YouTube Black Quadra Mug",
        "description": "The Quadra mug is a stylish addition to any desktop or kitchen. With it's matte finish and sleek appearance everyone will want one.",
        "author": "Google factory",
        "cost_of_goods_sold": "7.2 CHF",
        "price_float": 7.2,
        "price": "4.2 CHF",
        "brand": "Google",
        "gtin": "721762492383",
        "google_product_category": "Home & Garden > Kitchen & Dining > Tableware > Drinkware > Mugs",
        "product_type": "Google accessories",
        "shipping_height": "20.5 cm",
        "shipping_length": "10 cm",
        "shipping_width": "4 cm",
        "shipping_weight": "250 g",
    }
]
