import shopify
import json
import credentials

class shop:
    def __init__(self):
        # Set up the Shopify API session
        # session = shopify.Session(shop_url, access_token)

        shopify.Session.setup(api_key=credentials.shopify_api_key, secret=credentials.shopify_api_secret)
        self.session = shopify.Session(credentials.shopify_shop_url, credentials.shopify_api_version, credentials.shopify_access_token)
        shopify.ShopifyResource.activate_session(self.session)

    def get_newest_product_ids(self, product_count):
        # Fetch all products
        products = shopify.Product.find(limit=product_count, order="created_at DESC")

        # extract product ids
        product_ids = [product.id for product in products]

        print(product_ids)

        return product_ids

    def set_google_fields_for_t_shirt(self, product_id):
        """
        Sets Google fields for a Shopify product, specifically for a t shirt

        product_id: the ID of the product to update.
        """
        # Find the product with the specified ID
        product = shopify.Product.find(product_id, session=self.session)

        # Set the Google fields for the product

        metafield = shopify.Metafield({
                'key': 'google_product_category',
                'value': "212",
                'type': 'number_integer',
                'namespace': 'mm-google-shopping',
            }
        )
        product.add_metafield(metafield)
        product.save()

        metafield = shopify.Metafield({
                'key': 'age_group',
                'value': "adult",
                'type': 'single_line_text_field',
                'namespace': 'mm-google-shopping',
            }
        )

        product.add_metafield(metafield)
        product.save()

        metafield = shopify.Metafield({
                'key': 'gender',
                'value': "unisex",
                'type': 'single_line_text_field',
                'namespace': 'mm-google-shopping',
            }
        )
        product.add_metafield(metafield)

        # Save the updated product

        product.save()
