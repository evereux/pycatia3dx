# import pytest
from pycatia3dx.system.license_setting_att import LicenseSettingAtt
from tests.conftest import application


def test_frequency():
    setting_controllers = application.setting_controllers()
    license_setting_attributes: LicenseSettingAtt = setting_controllers.item("CATSysLicenseSettingCtrl")

    assert type(license_setting_attributes.frequency) is float


def test_nodelock_alert():
    setting_controllers = application.setting_controllers()
    license_setting_attributes: LicenseSettingAtt = setting_controllers.item("CATSysLicenseSettingCtrl")

    assert type(license_setting_attributes.nodelock_alert) is int


def test_server_time_out():
    setting_controllers = application.setting_controllers()
    license_setting_attributes: LicenseSettingAtt = setting_controllers.item("CATSysLicenseSettingCtrl")

    assert type(license_setting_attributes.server_time_out) is float


def test_show_license():
    setting_controllers = application.setting_controllers()
    license_setting_attributes: LicenseSettingAtt = setting_controllers.item("CATSysLicenseSettingCtrl")

    assert type(license_setting_attributes.show_license) is bool


# def test_get_frequency_info():

# pass


# def test_get_license():

# pass


# def test_get_license_info():

# pass


def test_get_licenses_list():
    setting_controllers = application.setting_controllers()
    license_setting_attributes: LicenseSettingAtt = setting_controllers.item("CATSysLicenseSettingCtrl")

    assert type(license_setting_attributes.get_licenses_list(5)) is tuple

# def test_get_licenses_list_info():

# pass


# def test_get_nodelock_alert_info():

# pass


# def test_get_server_time_out_info():

# pass


# def test_get_show_license_info():

# pass


# def test_set_frequency_lock():

# pass


# def test_set_license():

# pass


# def test_set_license_lock():

# pass


# def test_set_licenses_list_lock():

# pass


# def test_set_nodelock_alert_lock():

# pass


# def test_set_server_time_out_lock():

# pass


# def test_set_show_license_lock():

# pass
