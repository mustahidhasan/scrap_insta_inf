import json
import traceback

from scrap_insta_inf import get_insta_inf_info
def handler(event, context):
    """
    Takes the event and context as input and sends the event to the scrape function.
    :param event: event is a dictionary that contains information about necessary URLs.
    :param context: Not currently used.
    :return: success or fail.
    """
    events = json.dumps(event)
    service_dict = {
        "get_insta_inf_info": {"func": get_insta_inf_info, "args": ["url", "keyword"]},
    }

    try:
        print(events)
        function = json.loads(events)['function']
        function_data = service_dict[function]
        args = [json.loads(events)[arg] for arg in function_data["args"]]
        function_data["func"](*args, function)
        return {
            'Payload': {'lambda_result': 'success'}
        }

    except Exception as e:
        print(traceback.format_exc())
        return {
            'Payload': {'lambda_result': 'fail'},
            'data': e
        }
