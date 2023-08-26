# GPT Prompt: Write 2 line description of the book "Drive: The Surprising Truth About What Motivates Us". Please use some very uncommonly used words.
EBOOKS = [
        {
        "id": "ebook_1",
        "title": "Pricing Money: A Beginner's Guide to Money, Bonds, Futures and Swaps",
        "description": 'Available for free at: http://www.jdawiseman.com/books/pricing-money/Pricing_Money_JDAWiseman.html. "Pricing Money" delves into the abstruse realm of financial instruments, demystifying the alchemy of bonds, futures, and swaps for neophytes. An indispensable compendium for those eager to decode the esoteric lexicon of monetary machinations.',
        "author": "J. D. A. Wiseman (Author)",
        "cost_of_goods_sold": "74.00 CHF",
        "price": "90.00 CHF",
        "gtin": "978-0471487005",
        # https://www.amazon.com/Pricing-Money-Beginners-Guide-Futures/dp/0471487007
    },
    {
        "id": "ebook_2",
        "title": "Drive: The Surprising Truth About What Motivates Us",
        "description": 'In "Drive," Pink elucidates the enigmatic mechanisms of human motivation, debunking traditional reward systems and proffering the intrinsic trinity: autonomy, mastery, and purpose. A perspicacious tome on the psychodynamics of human propulsion.',
        "author": "Daniel H. Pink",
        "cost_of_goods_sold": "13.99 CHF",
        "price": "20.00 CHF",
        "gtin": "978-1594488849"
        # https://www.goodreads.com/book/show/6452796-drive
        # https://www.amazon.com/gp/product/B004P1JDJO
    },
    {
        "id": "ebook_3",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "description": "Douglas Adams presents a whimsical odyssey through the cosmos, replete with bathrobes and sentient appliances. A scintillating tour de force into the interstellar absurd, where Vogons declaim poetry and answers are worth a mere 42.",
        "author": "Douglas Adams",
        "cost_of_goods_sold": "6.36 CHF",
        "price": "10.00 CHF",
        "gtin": "978-0345391803",
        # https://www.amazon.com/Hitchhikers-Guide-Galaxy-Douglas-Adams/dp/0345391802 
    },
    {
        "id": "ebook_4",
        "title": "Radical Candor: Be a Kick-Ass Boss Without Losing Your Humanity",
        "description": '"Radical Candor" by Kim Scott promulgates the ethos of juxtaposing unvarnished feedback with profound empathy, forging leadership par excellence. A sagacious blueprint for melding solicitude with veracious communication in the modern workspace.',
        "author": "Kim Scott",
        "cost_of_goods_sold": "11.33 CHF",
        "price": "16.00 CHF",
        "gtin": "978-1250103505",
        # https://www.amazon.com/Radical-Candor-Kick-Ass-Without-Humanity/dp/1250103509
    },
    {
        "id": "ebook_5",
        "title": "Managing Humans: Biting and Humorous Tales of a Software Engineering Manager",
        "description": '"Managing Humans" by Michael Lopp unveils the arcane intricacies of the tech leadership labyrinth, replete with vignettes of capricious personalities and office quiddities. A perspicacious manual for navigating the often turbid waters of engineering leadership with sagacity.',
        "author": "Michael Lopp",
        "cost_of_goods_sold": "15 CHF",  # ???
        "price": "20.00 CHF",
        "gtin": "978-1430243144",
        # https://www.amazon.com/Managing-Humans-Humorous-Software-Engineering/dp/1430243147
    },        
    {
        "id": "ebook_6",
        "title": "Never Split the Difference: Negotiating As If Your Life Depended On It",
        "description": '"Never Split the Difference" by Chris Voss, a former FBI negotiator, proffers trenchant strategies gleaned from high-stakes hostage situations, recalibrated for quotidian disputes. This magnum opus elucidates the art of parley, where yielding an inch could mean ceding a mile.',
        "author": "Chris Voss",
        "cost_of_goods_sold": "9.69 CHF",
        "price": "15.00 CHF",
        "gtin": "978-0062407801",
        # https://www.amazon.com/Never-Split-Difference-Negotiating-Depended/dp/0062407805
    },
        {
        "id": "ebook_7",
        "title": "How to Win Friends & Influence People",
        "description": '"How to Win Friends and Influence People" by Dale Carnegie is a magisterial treatise on the nuances of human rapport, imparting time-tested stratagems for engendering goodwill and evoking influence. This seminal work demystifies the alchemy of efficacious interpersonal dynamics in both personal and professional realms.',
        "author": "Dale Carnegie",
        "cost_of_goods_sold": "10.30 CHF",
        "price": "15.00 CHF",
        "gtin": "978-0671027032",
        # https://www.amazon.com/How-Win-Friends-Influence-People/dp/0671027034
    },
    {
        "id": "ebook_8",
        "title": '"Cooking for Geeks" melds the empirical rigor of science with the artistry of culinary creation, inviting the cerebrally-inclined to dissect and revel in the gastronomic process. A veritable smorgasbord for those with a predilection for both algorithms and appetizers.',
        "description": "Cooking for Geeks: Real Science, Great Hacks, and Good Food",
        "author": "Jeff Potter",
        "cost_of_goods_sold": "24.73 CHF",
        "price": "32.00 CHF",
        "gtin": "978-0596805883",
        # https://www.amazon.com/Cooking-Geeks-Science-Great-Hacks/dp/0596805888
    },
    {
        "id": "ebook_9",
        "title": "Harry Potter and the Methods of Rationality",
        "description": "Available for free at: https://hpmor.com/. 'Harry Potter and the Methods of Rationality' by Eliezer Yudkowsky is a fecund reimagining of Rowling's universe, where young Potter, raised by scientists, employs logic and scientific principles in his magical endeavors. A perspicacious exploration of the Wizarding World through the prism of systematic inquiry and critical thought.",
        "author": "Eliezer Yudkowsky",
        "cost_of_goods_sold": "1000 CHF",
        "price": "1300 CHF",
        "gtin": "978-1936661657",
        # https://www.wikiwand.com/en/Harry_Potter_and_the_Methods_of_Rationality
    },
]

# image: gtin + ".jpg"
# availability: in_stock
# condition: new
# google_product_category: Media > Books > E-books
# product_type: E-books
# auto_pricing_min_price: = cogs