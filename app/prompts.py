PARSE_REQUEST_PROMPT = """
Extract structured information from the user's request.

Return JSON with fields:

product: string
max_price: integer | null
shop: string | null

User request:

{request}
"""