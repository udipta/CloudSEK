import ast

from results.models import Results


def populate_answers(result_id):
    """
    This function takes the Results object as input and populates the relevant answers with its numbers
    """
    try:
        result = Results.objects.get(id=result_id)
        print(result.__dict__)
        result.answer = ast.literal_eval(result.number1) + ast.literal_eval(result.number2)
        result.save()
        print(result.__dict__)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
