import image
import printify
import uuid
import datetime
import shopify2
import hashtag
import persist
import time

def make_shirts(ideas):
    p = persist.Persist("used_hashtags")
    used_ideas = p.get()

    print(used_ideas)

    if ideas is None:
        ideas = []

    ideas = [elem for elem in ideas if elem not in used_ideas]

    for idea in ideas:
        used_ideas.append(idea)

    p.set(used_ideas)

    # loop through the array
    for idea in ideas:
        print("making t shirt for: " + idea)
        # create image from idea
        img = image.create_text_image(idea, image_width=8000, image_height=6000, font_size=450)

        # save image to disk
        file_path = str(uuid.uuid4()) + ".png"
        img.save(file_path)

        print("created design image")

        # send image to printify
        image_id = printify.upload_image(file_path)

        print("design uploaded to printify")

        # add product to printify
        product = printify.add_product(idea, image_id)
        print("product added to printify")

        # publish product
        printify.publish_existing_product(product["id"])
        print("product sent to shopify")

    # wait 5 seconds for the products to land...
    # time.sleep(5)
    shop = shopify2.shop()
    # collect all the new products from shopify
    new_product_ids = shop.get_newest_product_ids(len(ideas)+3)
    print("Optimizing SEO...")

    # set up SEO
    for new_product_id in new_product_ids:
        shop.set_google_fields_for_t_shirt(new_product_id)
        print("SEO has been set up")



    