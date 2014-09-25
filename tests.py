import os

from dmidecode import parse_dmi


def test_bios():
    output = """
Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
	Vendor: Dell Inc.
	Version: A04
	Release Date: 09/11/2010
	Address: 0xF0000
	Runtime Size: 64 kB
	ROM Size: 8192 kB
	Characteristics:
		PCI is supported
		PNP is supported
		APM is supported
		BIOS is upgradeable
		BIOS shadowing is allowed
		ESCD support is available
		Boot from CD is supported
		Selectable boot is supported
		EDD is supported
		Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
		3.5"/720 kB floppy services are supported (int 13h)
		Print screen service is supported (int 5h)
		8042 keyboard services are supported (int 9h)
		Serial services are supported (int 14h)
		Printer services are supported (int 17h)
		ACPI is supported
		USB legacy is supported
		BIOS boot specification is supported
		Function key-initiated network boot is supported
		Targeted content distribution is supported
	BIOS Revision: 0.0
"""
    assert parse_dmi(output)[0] == (0,  {
            '_title': "BIOS Information",
            "Vendor": "Dell Inc.",
            "Version": "A04",
            "Release Date": "09/11/2010",
            "Address": "0xF0000",
            "Runtime Size": "64 kB",
            "ROM Size": "8192 kB",
            "Characteristics": [
		"PCI is supported",
		"PNP is supported",
		"APM is supported",
		"BIOS is upgradeable",
		"BIOS shadowing is allowed",
		"ESCD support is available",
		"Boot from CD is supported",
		"Selectable boot is supported",
		"EDD is supported",
		"Japanese floppy for Toshiba 1.2 MB is supported (int 13h)",
		"3.5\"/720 kB floppy services are supported (int 13h)",
		"Print screen service is supported (int 5h)",
		"8042 keyboard services are supported (int 9h)",
		"Serial services are supported (int 14h)",
		"Printer services are supported (int 17h)",
		"ACPI is supported",
		"USB legacy is supported",
		"BIOS boot specification is supported",
		"Function key-initiated network boot is supported",
		"Targeted content distribution is supported",
                ],
            "BIOS Revision": "0.0",
            })


def test_system():
    output = """
Handle 0x0100, DMI type 1, 27 bytes
System Information
	Manufacturer: Dell Inc.
	Product Name: OptiPlex 980                 
	Version: Not Specified
	Serial Number: 35K213X
	UUID: 4C4C4544-0035-4B10-8032-B3C04F313358
	Wake-up Type: Power Switch
	SKU Number: Not Specified
	Family: Not Specified
"""
    assert parse_dmi(output)[0] == (1, {
            "_title": "System Information",
            "Manufacturer": "Dell Inc.",
            "Product Name": "OptiPlex 980",
            "Version": "Not Specified",
            "Serial Number": "35K213X",
            "UUID": "4C4C4544-0035-4B10-8032-B3C04F313358",
            "Wake-up Type": "Power Switch",
            "SKU Number": "Not Specified",
            "Family": "Not Specified",
            })

