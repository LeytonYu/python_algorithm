import json


def str_to_json(value):
    if value and not isinstance(value, list):
        try:
            tp = json.loads(value)
            return [tp] if isinstance(tp, int) else tp
        except:
            try:
                return json.loads(value.replace("'", '"'))
            except:
                return []
    elif value and isinstance(value, list):
        return value
    else:
        return []