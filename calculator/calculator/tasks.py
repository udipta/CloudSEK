from celery import shared_task


@shared_task
def populate_answers_task(result_id):
    try:
        print('-'*100)
        print(f'Result Object ID: {result_id}')
        from results.results_populate import populate_answers
        populate_answers(result_id=result_id)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
