import os
import openprocurement.agreement.cfaua

from logging import getLogger
from pkg_resources import get_distribution
from pyramid.interfaces import IRequest
from openprocurement.api.interfaces import IContentConfigurator

from openprocurement.agreement.cfaua.interfaces\
    import IClosedFrameworkAgreementUA
from openprocurement.agreement.cfaua.models.agreement\
    import Agreement
from openprocurement.agreement.cfaua.adapters.configurator\
    import CFAgreementUAConfigurator

from zope.configuration.xmlconfig import file as ZcmlFile


PKG = get_distribution(__package__)
LOGGER = getLogger(PKG.project_name)


def includeme(config):
    LOGGER.info("Loading cfAgreementUA plugin")
    config.add_agreement_type(Agreement)
    config.registry.registerAdapter(
        CFAgreementUAConfigurator,
        (IClosedFrameworkAgreementUA, IRequest),
        IContentConfigurator
    )
    config.scan('openprocurement.agreement.cfaua.views')

    ZcmlFile(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'configure.zcml'),
        package=openprocurement.agreement.cfaua
    )
