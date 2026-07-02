from models import SearchRequest


class SearchService:
    """
    Отвечает за поиск товаров.

    Пока возвращает тестовые данные.
    Позже здесь появятся DNS, Ozon и Яндекс Маркет.
    """

    def search(self, request: SearchRequest):

        print(f"\n🔍 Searching for: {request.product}")

        if request.max_price:
            print(f"💰 Max price: {request.max_price}")

        if request.shop:
            print(f"🏪 Shop: {request.shop}")

        return []