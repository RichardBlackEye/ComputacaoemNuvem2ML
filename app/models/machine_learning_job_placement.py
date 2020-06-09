# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MachineLearningJobPlacement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cluster_name: str=None):  # noqa: E501
        """MachineLearningJobPlacement - a model defined in Swagger

        :param cluster_name: The cluster_name of this MachineLearningJobPlacement.  # noqa: E501
        :type cluster_name: str
        """
        self.swagger_types = {
            'cluster_name': str
        }

        self.attribute_map = {
            'cluster_name': 'clusterName'
        }

        self._cluster_name = cluster_name

    @classmethod
    def from_dict(cls, dikt) -> 'MachineLearningJobPlacement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MachineLearning_job_placement of this MachineLearningJobPlacement.  # noqa: E501
        :rtype: MachineLearningJobPlacement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cluster_name(self) -> str:
        """Gets the cluster_name of this MachineLearningJobPlacement.


        :return: The cluster_name of this MachineLearningJobPlacement.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name: str):
        """Sets the cluster_name of this MachineLearningJobPlacement.


        :param cluster_name: The cluster_name of this MachineLearningJobPlacement.
        :type cluster_name: str
        """

        self._cluster_name = cluster_name