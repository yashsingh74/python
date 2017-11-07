# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V2beta1ObjectMetricStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'current_value': 'str',
        'metric_name': 'str',
        'target': 'V2beta1CrossVersionObjectReference'
    }

    attribute_map = {
        'current_value': 'currentValue',
        'metric_name': 'metricName',
        'target': 'target'
    }

    def __init__(self, current_value=None, metric_name=None, target=None):
        """
        V2beta1ObjectMetricStatus - a model defined in Swagger
        """

        self._current_value = None
        self._metric_name = None
        self._target = None
        self.discriminator = None

        self.current_value = current_value
        self.metric_name = metric_name
        self.target = target

    @property
    def current_value(self):
        """
        Gets the current_value of this V2beta1ObjectMetricStatus.
        currentValue is the current value of the metric (as a quantity).

        :return: The current_value of this V2beta1ObjectMetricStatus.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """
        Sets the current_value of this V2beta1ObjectMetricStatus.
        currentValue is the current value of the metric (as a quantity).

        :param current_value: The current_value of this V2beta1ObjectMetricStatus.
        :type: str
        """
        if current_value is None:
            raise ValueError("Invalid value for `current_value`, must not be `None`")

        self._current_value = current_value

    @property
    def metric_name(self):
        """
        Gets the metric_name of this V2beta1ObjectMetricStatus.
        metricName is the name of the metric in question.

        :return: The metric_name of this V2beta1ObjectMetricStatus.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this V2beta1ObjectMetricStatus.
        metricName is the name of the metric in question.

        :param metric_name: The metric_name of this V2beta1ObjectMetricStatus.
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")

        self._metric_name = metric_name

    @property
    def target(self):
        """
        Gets the target of this V2beta1ObjectMetricStatus.
        target is the described Kubernetes object.

        :return: The target of this V2beta1ObjectMetricStatus.
        :rtype: V2beta1CrossVersionObjectReference
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this V2beta1ObjectMetricStatus.
        target is the described Kubernetes object.

        :param target: The target of this V2beta1ObjectMetricStatus.
        :type: V2beta1CrossVersionObjectReference
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V2beta1ObjectMetricStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other