from enum import Enum


class UserRole(str, Enum):
    StaffRole = "StaffRole"
    AdminRole = "AdminRole"
    PartnerRole = "PartnerRole"
    VendorRole = "VendorRole"
    SuperUserRole = "SuperUserRole"
