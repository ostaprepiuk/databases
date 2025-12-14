from .owner import Owner
from .user import User
from .address import Address
from .contact import Contact
from .smartwatch import Smartwatch, SmartwatchUser # SmartwatchUser - стикувальна M:M
from .telemetry import Telemetry
from .battery_status import BatteryStatus
from .alert_recipients import AlertRecipient
from .alerts import Alert
from .notification import Notification # Нова таблиця
from .users_update_log import UsersUpdateLog # Лог таблиця