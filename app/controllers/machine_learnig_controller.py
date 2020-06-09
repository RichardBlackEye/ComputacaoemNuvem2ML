import connexion
import six

from app.models.machine_learning import MachineLearning  # noqa: E501
from app import util


def post_ml_job(body):  # noqa: E501
    """Post a ML Job.

     # noqa: E501

    :param body: Post a ML Job.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = MachineLearning.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
