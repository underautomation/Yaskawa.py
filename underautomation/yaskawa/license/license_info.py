import typing
from underautomation.yaskawa.license.license_state import LicenseState
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..",  'lib', 'UnderAutomation.Yaskawa.dll')))
from UnderAutomation.Yaskawa.License import LicenseInfo as license_info

class LicenseInfo:
	def __init__(self, licenseIdentifier: str, licenseKey: str, _internal = 0):
		if(_internal == 0):
			self._instance = license_info(licenseIdentifier, licenseKey)
		else:
			self._instance = _internal
	def __repr__(self):
		return self._instance.ToString()
	@property
	def license_key(self) -> str:
		return self._instance.LicenseKey
	@license_key.setter
	def license_key(self, value: str):
		self._instance.LicenseKey = value
	@property
	def product(self) -> str:
		return self._instance.Product
	@product.setter
	def product(self, value: str):
		self._instance.Product = value
	@property
	def evaluation_days_left(self) -> typing.Any:
		return self._instance.EvaluationDaysLeft
	@evaluation_days_left.setter
	def evaluation_days_left(self, value: typing.Any):
		self._instance.EvaluationDaysLeft = value
	@property
	def evaluation_start_date(self) -> typing.Any:
		return self._instance.EvaluationStartDate
	@evaluation_start_date.setter
	def evaluation_start_date(self, value: typing.Any):
		self._instance.EvaluationStartDate = value
	@property
	def licensee(self) -> str:
		return self._instance.Licensee
	@licensee.setter
	def licensee(self, value: str):
		self._instance.Licensee = value
	@property
	def trial_period_expiration_date(self) -> typing.Any:
		return self._instance.TrialPeriodExpirationDate
	@trial_period_expiration_date.setter
	def trial_period_expiration_date(self, value: typing.Any):
		self._instance.TrialPeriodExpirationDate = value
	@property
	def state(self) -> LicenseState:
		return LicenseState(self._instance.State)
	@property
	def product_release_date(self) -> typing.Any:
		return self._instance.ProductReleaseDate
	@product_release_date.setter
	def product_release_date(self, value: typing.Any):
		self._instance.ProductReleaseDate = value
	@property
	def maintenance_years(self) -> int:
		return self._instance.MaintenanceYears
	@maintenance_years.setter
	def maintenance_years(self, value: int):
		self._instance.MaintenanceYears = value
	@property
	def license_issued_date(self) -> typing.Any:
		return self._instance.LicenseIssuedDate
	@license_issued_date.setter
	def license_issued_date(self, value: typing.Any):
		self._instance.LicenseIssuedDate = value
	@property
	def maintenance_expiration_date(self) -> typing.Any:
		return self._instance.MaintenanceExpirationDate
	@maintenance_expiration_date.setter
	def maintenance_expiration_date(self, value: typing.Any):
		self._instance.MaintenanceExpirationDate = value
