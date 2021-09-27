import ast

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Results
from .serializers import ResultsSerializer


# Create your views here.
class ResultsViewset(viewsets.ModelViewSet):
    """
        Viewset to display the answer of Results object.
        **Context**
        :class:`results.models.Results` .

        **Permission** : AllowAny

        :list:
            list of results data for that specific identifier.
    """

    # permission_classes = (IsAuthenticated,)
    serializer_class = ResultsSerializer

    def list(self, request, *args, **kwargs):
        return Response("Hi from test API", status=status.HTTP_200_OK)


class ResultsPushViewset(viewsets.ModelViewSet):
    """
        Viewset to create the Results object.
        **Context**
        :class:`results.models.Results` .

        **Permission** : AllowAny

        :list:
            list of results data for that specific identifier.
    """

    serializer_class = ResultsSerializer

    def list(self, request, *args, **kwargs):
        """
        parameters:
            - name: number1
              required: true
            - name: number2
              required: true
        """

        # Standard check
        if not (self.kwargs.get('number1', '') and self.kwargs.get('number2', '')):
            msg = "Standard input numbers should be digit"
            return Response(msg, status=status.HTTP_406_NOT_ACCEPTABLE)

        number_data = {
            'number1': ast.literal_eval(self.kwargs.get('number1')),
            'number2': ast.literal_eval(self.kwargs.get('number2')),
        }
        serializer = self.get_serializer(data=number_data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

        return Response(status=status.HTTP_404_NOT_FOUND)


class ResultsShowViewset(viewsets.ModelViewSet):
    """
        Viewset to display the answer of Results object.
        **Context**
        :class:`results.models.Results` .

        **Permission** : AllowAny

        :list:
            list of results data for that specific identifier.
    """

    serializer_class = ResultsSerializer

    def list(self, request, *args, **kwargs):
        """
        parameters:
            - name: identifier
              required: true
        """

        # Standard check
        if not self.kwargs.get("identifier", ""):
            msg = "Invalid standard input identifier"
            return Response(msg, status=status.HTTP_406_NOT_ACCEPTABLE)

        results = Results.objects.filter(id=self.kwargs.get("identifier"))
        if results:
            msg = results[0].answer if results[0].answer else "Please wait."
            return Response(msg, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
