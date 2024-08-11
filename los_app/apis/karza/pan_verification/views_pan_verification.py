import datetime
import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from los_app.apis.karza.creds import get_cred

from karza.creds import KarzaKeys

# from workflows.serializers import WorkflowActionsSerializer


class PANAuthentication(APIView):
    def get(self, request):
        """
        This function will return the page with the workflow id attached to the form
        :param request:
        :return:
        """
        context = dict(zip(['workflow_id'], [request.session['workflow_id']]))
        return render(request, 'pan_authentication_form.html', context)

    def post(self, request):
        """
        This function will call the 3rd party api, store the data, and redirect user to workflow details page
        :param request:
        :return:
        """
        input_json = request.data
        output_json = views_pan_authentication_json(request, input_json)
        return Response(output_json)


def views_pan_authentication_json(request, input_params):
    try:
        input_json, output_list = input_params, []
        api_name_var = "Karza PAN Validation"
        endpoint_url_var = "/v2/pan"
        keys_obj = KarzaKeys()

        # For every API Calling style initiate the params accordingly
        third_party_response = dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                                        [api_name_var, endpoint_url_var, None, None, None]))
        timestamp_one = datetime.datetime.now()

        #####################################################################################
        # Call the third party API here
        call_params = dict(zip(["api_endpoint_url", "payload"],
                               [endpoint_url_var, None]))
        call_params['payload'] = dict(zip(["consent", "pan"],
                                          [input_json['pan_yes'], input_json['pan_number']]))
        third_party_call_result = keys_obj.make_api_call(call_params)

        third_party_response['Request'] = third_party_call_result['request_details']
        third_party_response['Response'] = third_party_call_result['response_details']
        #####################################################################################

        timestamp_two = datetime.datetime.now()
        third_party_response['CallTime'] = dict(zip(['timestamp_one', 'timestamp_two','time_diff'],
                                                    [timestamp_one, timestamp_two,
                                                     (timestamp_two-timestamp_one).total_seconds()]))
        output_list.append(third_party_response)

        # Saving the results in the db
        third_party_response['CallDuration'] = third_party_response['CallTime']['time_diff']
        third_party_response['CallTime'] = str(third_party_response['CallTime']['timestamp_one'])
        insertion_params = dict(zip(['workflow_id', 'details'],
                                    [None, json.dumps(third_party_response)]))
        if 'workflow_id' in input_json:
            insertion_params['workflow_id'] = input_json['workflow_id']
            request.session['workflow_id'] = input_json['workflow_id']
        # serialized_workflow_actions = WorkflowActionsSerializer(data=insertion_params)
        # if serialized_workflow_actions.is_valid(raise_exception=True):
        #     serialized_workflow_actions.save()

        # ###########################################################################################
        # ###########################################################################################
        # # For every API Calling style inititate the params accordingly
        # third_party_response = dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
        #                                 ["Karza PAN Validation method 2", "/v2/pan", None, None, None]))
        # timestamp_one = datetime.datetime.now()
        #
        #
        # #####################################################################################
        # # Call the third party API here
        # call_params = dict(zip(["api_endpoint_url", "payload"],
        #                        ["/v2/pan", dict(zip(["consent", "pan"],
        #                                             ["Y", input_json['pan_number']]))]))
        # # third_party_call_result = keys_obj.make_api_call(call_params)
        # third_party_call_result = keys_obj.make_api_call_2(call_params)
        #
        # third_party_response['Request'] = third_party_call_result['request_details']
        # third_party_response['Response'] = third_party_call_result['response_details']
        # #####################################################################################
        #
        # timestamp_two = datetime.datetime.now()
        # third_party_response['CallTime'] = dict(zip(['timestamp_one', 'timestamp_two','time_diff'],
        #                                             [timestamp_one, timestamp_two,
        #                                              (timestamp_two-timestamp_one).total_seconds()]))
        # output_list.append(third_party_response)
        return output_list

    except Exception as ex:
        output_list=[dict(zip(["APIName", "endpoint_url", "Request", "Response", "CallTime"],
                              ["Karza PAN Validation method 1", "/v2/pan", None, f"Exception Encountered: {ex}", None]))]
        return output_list
