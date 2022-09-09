# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Agustin Guardo
# All rights reserved.
#
from connect.eaas.extension import (
    CustomEventResponse,
    Extension,
    ProcessingResponse,
    ProductActionResponse,
    ScheduledExecutionResponse,
    ValidationResponse,
)

import requests
import json

class Weather_projectExtension(Extension):

    def approve_asset_request(self, request, template_id):
        self.logger.info(f'request_id={request["id"]} - template_id={template_id}')
        self.client.requests[request['id']]('approve').post(
            {
                'template_id': template_id,
            }
        )
        self.logger.info(f"Approved request {request['id']}")

    def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request from company {request['asset']['tiers']['customer']['name']}")
        company = request['asset']['tiers']['customer']['name']
        self.logger.info(
            f"Received event for request {request['id']} in status {request['status']}"
        )

        if request['status'] == 'pending':
            for param in request['asset']['params']:
                if param['id'] == 'unitofmeasure':
                    unitofmeasure = param['value']
            citieslimit = 0
            for item in request['asset']['items']:
                if item['mpn'] == 'citieslimit':
                    citieslimit = item['quantity']
            newCompany = {
                'name': company,
                'unitofmeasure': unitofmeasure,
                'citieslimit': citieslimit
            }
            session = requests.Session()
            session.headers.update({'content-type': 'application/json', 'x-provider-token': 'osamwd'})
            vendorDataResponse = session.post('http://myweatherdemo.learn-cloudblue.com/api/company/',
                                              data=json.dumps(newCompany))
            self.logger.info(
                f"Received vendor response as: {vendorDataResponse.content}"
            )
            vendorData = vendorDataResponse.json()
            self.logger.info(
                f"Received event for request id {vendorData['token']} with username {vendorData['username']} and password {vendorData['password']}"
            )

            self.client.requests[request['id']].update(
                {
                    "asset": {
                        "params": [
                            {
                                "id": "id",
                                "value": vendorData['id']
                            },
                            {
                                "id": "password",
                                "value": vendorData['password']
                            },
                            {
                                "id": "username",
                                "value": vendorData['username']
                            }
                        ]
                    }
                }
            )
            self.logger.info("Updating fulfillment parameters as follows:"
                             f"name to {company}, unitofmeasure to {unitofmeasure} and citieslimit to {citieslimit}")
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            self.approve_asset_request(request, template_id)

        return ProcessingResponse.done()

    def process_asset_change_request(self, request):
        self.logger.info(
            f"Received event for request {request['id']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            for item in request['asset']['items']:
                if (item['mpn'] == 'citieslimit'):
                    citieslimit = item['quantity']
            if (citieslimit == 0):
                # reason = 'it is not allowed to set 0 for the citieslimit'
                reason = {
                    'it is not allowed to set 0 for the citieslimit'
                }
                session = requests.Session()
                session.headers.update({'content-type': 'application/json',
                                        'ApiKey SU-254-269': 'dab15888afb1009f015e93eb5d6d95fd51c8b5f5'})
                session.post('https://api.sandbox.connect.cloudblue.com/public/v1/requests/' + request["id"] + '/fail',
                             data=json.dumps(reason))

            for param in request['asset']['params']:
                if (param['id'] == 'id'):
                    companyid = param['value']
            self.logger.info(
                f"The company id is: {companyid}"
            )
            limit = {
                'citieslimit': citieslimit
            }
            self.logger.info(
                f"The new limit is: {limit}"
            )
            session = requests.Session()
            session.headers.update({'content-type': 'application/json', 'x-provider-token': 'osamwd'})
            vendorResponse = session.put('http://myweatherdemo.learn-cloudblue.com/api/company/' + companyid,
                                         data=json.dumps(limit))
            self.logger.info(
                f"Received vendor response as: {vendorResponse.content}"
            )

            vendorData = vendorResponse.json()

            vendorDataInt = int(vendorData['citieslimit'])
            citiesLimitInt = int(citieslimit)
            if (vendorDataInt == citiesLimitInt):
                template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
                self.approve_asset_request(request, template_id)
        return ProcessingResponse.done()

    def process_asset_suspend_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_resume_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request):
        self.logger.info(
            f"Received event for request {request['id']} "
            f"in status {request['status']}"
        )
        if request['status'] == 'pending':
            for param in request['asset']['params']:
                if (param['id'] == 'id'):
                    companyid = param['value']
            self.logger.info(
                f"The company id is: {companyid}"
            )
            company = {
            }
            self.logger.info(
                f"The company to delete is: {company}"
            )
            template_id = self.config['ASSET_REQUEST_APPROVE_TEMPLATE_ID']
            self.approve_asset_request(request, template_id)
            session = requests.Session()
            session.headers.update({'content-type': 'application/json', 'x-provider-token': 'osamwd'})
            vendorResponse = session.delete('http://myweatherdemo.learn-cloudblue.com/api/company/' + companyid,
                                            data=json.dumps(company))
        return ProcessingResponse.done()


    def process_asset_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_tier_config_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def validate_tier_config_setup_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def validate_tier_config_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def execute_product_action(self, request):
        self.logger.info(f"Obtained product custom action with following data: {request}")
        return ProductActionResponse.done()

    def process_product_custom_event(self, request):
        self.logger.info(f"Obtained custom event with following data: {request}")
        return CustomEventResponse.done()

    def process_usage_file(self, request):  # pragma: no cover
        self.logger.info(
            f"Received event for usage file  {request['id']}, type {request['type']} "
            f"in status {request['status']}",
        )
        return ProcessingResponse.done()

    def process_tier_account_update_request(self, request):  # pragma: no cover
        self.logger.info(
            f"Received event for tier account request  {request['id']}, type {request['type']} "
            f"in status {request['status']}",
        )
        return ProcessingResponse.done()

    def execute_scheduled_processing(self, schedule):  # pragma: no cover
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()
