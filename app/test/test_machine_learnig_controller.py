# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.machine_learning import MachineLearning  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMachineLearnigController(BaseTestCase):
    """MachineLearnigController integration test stubs"""

    def test_post_ml_job(self):
        """Test case for post_ml_job

        Post a ML Job.
        """
        body = MachineLearning()
        response = self.client.open(
            '/v1/projects/cloudcomputworlddevelopment/regions/us-central1/jobs:submit//machine_learning',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
