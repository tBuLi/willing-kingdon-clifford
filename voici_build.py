"""voici build, with the VoilaConfiguration.resources that voici itself ignores."""

import sys

from voici_core.app import main
from voici_core.exporter import VoiciExporter
from voila.utils import recursive_update

_init_resources = VoiciExporter._init_resources


def init_resources(self, resources):
    resources = _init_resources(self, resources)
    recursive_update(resources, self.voici_configuration.resources or {})
    return resources


VoiciExporter._init_resources = init_resources

if __name__ == "__main__":
    sys.exit(main())
