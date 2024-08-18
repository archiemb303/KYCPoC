import os
import yaml
import logging
import json
import jsonschema
from pathlib import Path

logger = logging.getLogger(__name__)


def yaml_parser(yml):
    """Function for parsing Yaml File functionality."""
    data = {}  # assign
    with open(yml) as f:
        try:
            data = yaml.safe_load(f)
            logger.info(data)
        except yaml.YAMLError as exc:
            logger.info(exc)
    return data


def schema_validation(data, path):
    """Function for validating Json Schema functionality."""
    schema = load(path)
    v = jsonschema.Draft4Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    for error in errors:
        print(error.message)
        logger.info('json validation failed')
    logger.info('schema validation done')
    # print('schema validation done')


def load(schema_path):
    """
    :param schema_path:
    :return:
    """
    schema = Path(schema_path)

    with schema.open() as f:
        return json.load(f)


def get_cred():
    """
        :param None:
        :return:
        """
    try:
        yml = yaml_parser(os.path.abspath('los_app/apis/karza/getcredentials/credentials/credential.yaml'))
        p = os.path.abspath('los_app/apis/karza/getcredentials/credentials/schema_credentials.json')
        schema_validation(yml, p)
        return yml
    except Exception as ex:
        output_json = dict(zip(['Status', 'Message', 'Payload'],
                                          ["Failure",
                                           f"Unable to fetch credentials: {ex}",
                                           None]))
        return output_json
