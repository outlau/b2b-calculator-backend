from kanpai import Kanpai
from lib.test_calculator import calculate_test

request_schema = Kanpai.Object({
    'annual_usage': (Kanpai.Number()).required(),
    'orientation': (Kanpai.String().anyof(choices=('west', 'east'))).required(),
})


def main(request):
    request_input = request.args.to_dict()
    validation_result = request_schema.validate(request_input)
    if not validation_result['success']:
        return validation_result['error'], 400

    res = calculate_test(annual_usage=request_input['annual_usage'], orientation=request_input['orientation'])

    return res, 200
