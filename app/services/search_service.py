from models import Product, SearchRequest


class SearchService:

    def search(self, request: SearchRequest) -> list[Product]:

        print()
        print("========== SEARCH ==========")
        print(f"Product : {request.product}")
        print(f"MaxPrice: {request.max_price}")
        print(f"Shop    : {request.shop}")
        print("============================")
        print()

        products = [
            Product(
                title="RTX 5070 MSI Gaming X",
                price=54990,
                shop="DNS",
                url="https://dns-shop.ru"
            ),
            Product(
                title="RTX 5070 Gigabyte Windforce",
                price=55990,
                shop="Ozon",
                url="https://ozon.ru"
            )
        ]

        if request.max_price:

            products = [
                product
                for product in products
                if product.price <= request.max_price
            ]

        return products