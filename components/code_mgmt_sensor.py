"""
This example will show how we manage the latest gitHub release
"""
import logging

from datetime import datetime as dt
from typing import Any, ClassVar, Dict, List, Mapping, Optional, Sequence
from typing_extensions import Self

from google.protobuf.json_format import MessageToDict
from viam.components.component_base import ValueTypes
from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.registry import Registry, ResourceCreatorRegistration
from viam.resource.types import Model, ModelFamily

logger: logging.Logger = getLogger(__name__)


class CodeMgmtSensor(Sensor, Reconfigurable):
    """
    Simple sensor which will deploy and manage applications based on attributes
    found in the configuration.
    """
    MODEL: ClassVar[Model] = Model(ModelFamily('shawns-modules', 'code-mgmt'), 'sensor')

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        """
        create new instance of web sensor

        :param config:
        :param dependencies:
        :return:
        """
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        """
        validate configuration

        :param config:
        :return:
        """

        return []

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> None:
        """
        reconfigure component

        :param config:
        :param dependencies:
        :return:
        """


    async def get_readings(
            self,
            *,
            extra: Optional[Mapping[str, Any]] = None,
            timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Any]:
        """
        :param extra:
        :param timeout:
        :param kwargs:
        :return:
        """

        result = {
            "key": "value"
        }

        return result

    async def do_command(
            self,
            command: Mapping[str, ValueTypes],
            *,
            timeout: Optional[float] = None,
            **kwargs
    ) -> Mapping[str, ValueTypes]:
        """
        not implemented right now

        :param command:
        :param timeout:
        :param kwargs:
        :return:
        """
        pass


"""
Register the new MODEL as well as define how the object is validated 
and created
"""
Registry.register_resource_creator(
    Sensor.SUBTYPE,
    CodeMgmtSensor.MODEL,
    ResourceCreatorRegistration(CodeMgmtSensor.new, CodeMgmtSensor.validate_config)
)