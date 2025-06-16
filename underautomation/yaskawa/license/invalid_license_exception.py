import typing
from underautomation.yaskawa.license.license_info import LicenseInfo
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.License import InvalidLicenseException as invalid_license_exception

class InvalidLicenseException:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = invalid_license_exception()
		else:
			self._instance = _internal
	@property
	def license_info(self) -> LicenseInfo:
		return LicenseInfo(None, None, self._instance.LicenseInfo)
	@license_info.setter
	def license_info(self, value: LicenseInfo):
		self._instance.LicenseInfo = value
