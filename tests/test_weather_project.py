# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Agustin Guardo
# All rights reserved.
#

from connect_ext.extension import Weather_projectExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'


def test_process_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_change_request(request)
    assert result.status == 'success'


def test_process_asset_suspend_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_suspend_request(request)
    assert result.status == 'success'


def test_process_asset_resume_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_resume_request(request)
    assert result.status == 'success'


def test_process_asset_cancel_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_cancel_request(request)
    assert result.status == 'success'


def test_process_asset_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_asset_adjustment_request(request)
    assert result.status == 'success'


def test_validate_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_process_tier_config_setup_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_tier_config_setup_request(request)
    assert result.status == 'success'


def test_process_tier_config_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_tier_config_change_request(request)
    assert result.status == 'success'


def test_process_tier_config_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_tier_config_adjustment_request(request)
    assert result.status == 'success'


def test_validate_tier_config_setup_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.validate_tier_config_setup_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_tier_config_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.validate_tier_config_change_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_process_product_action(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.execute_product_action(request)
    assert result.status == 'success'
    assert result.http_status == 200
    assert result.headers is None
    assert result.body is None


def test_process_product_custom_event(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_product_custom_event(request)
    assert result.status == 'success'
    assert result.http_status == 200
    assert result.headers is None
    assert result.body is None


def test_process_usage_file(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'status': 'status'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_usage_file(request)
    assert result.status == 'success'


def test_process_tier_account_update_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'status': 'status'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.process_tier_account_update_request(request)
    assert result.status == 'success'


def test_execute_scheduled_processing(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = Weather_projectExtension(client, logger, config)
    result = ext.execute_scheduled_processing(request)
    assert result.status == 'success'
