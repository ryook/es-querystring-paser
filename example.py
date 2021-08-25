from typing import Text
from es_query_string_parser import EsQueryStringParser

text = "(aa AND bb)"

parsed_text = EsQueryStringParser().validate(text)
print(parsed_text)
