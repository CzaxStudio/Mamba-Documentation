# Mamba Security Documentation

[![Python Version](https://img.shields.io/pypi/pyversions/mamba-security)](https://pypi.org/project/mamba-security/)
[![PyPI version](https://badge.fury.io/py/mamba-security.svg)](https://badge.fury.io/py/mamba-security)
[![License](https://img.shields.io/github/license/CzaxStudio/Mamba)](https://github.com/CzaxStudio/Mamba/blob/main/LICENSE)

Welcome to the official Mamba Security documentation. This repository contains everything you need to master OSINT with Mamba.

## What is Mamba?

Mamba is a powerful, production-ready OSINT (Open Source Intelligence) library for Python. It provides simple, unified interfaces for:
- Email intelligence and breach checking
- Domain reconnaissance (WHOIS, DNS, subdomains)
- Username search across multiple platforms
- Phone number validation
- IP geolocation and reputation

## Quick Install

```bash
pip install mamba-security
```

## Example
```python

from mamba import MambaClient, EmailReputation

with MambaClient() as client:
    email = EmailReputation(client)
    result = email.validate_format("user@example.com")
    print(result.summary())

```
## Structure
```
MambaDocumentation/
├── 01_email_osint              # Email validation and breach checking
├── 02_domain_osint             # WHOIS, DNS, subdomain enumeration
├── 03_username_osint           # Social media username search
├── 04_phone_osint              # Phone number validation
├── 05_ip_osint                 # IP geolocation and reputation
├── 06_advanced                 # Caching, batch processing, rate limiting
├── 07_cli_usage                # Command line interface examples
└── 08_real_world               # Production-ready scripts
```

## Verify
```python
python -c "from mamba import MambaClient; print('Mamba installed successfully!')"
```
## Get Started

Hello Investigators. This script will help you to get started in Mamba.
```python


---

## File 3: `01_getting_started/first_script.py`

```python
#!/usr/bin/env python3
"""
Mamba First Script - Your First OSINT Investigation
"""

from mamba import MambaClient
from mamba import EmailReputation, DomainIntel
from mamba.utils import ResultFormatter

def main():
    print("=" * 60)
    print("Mamba OSINT - First Investigation")
    print("=" * 60)
    
    # Create client with context manager (auto-closes connection)
    with MambaClient() as client:
        
        # 1. Email Investigation
        print("\n1. EMAIL INVESTIGATION")
        print("-" * 40)
        email = EmailReputation(client)
        
        result = email.validate_format("security@example.com")
        print(f"Email: security@example.com")
        print(f"  Valid format: {result.data['valid_format']}")
        print(f"  Has MX records: {result.data['has_mx_records']}")
        print(f"  Domain: {result.data['domain']}")
        
        # 2. Domain Investigation
        print("\n2. DOMAIN INVESTIGATION")
        print("-" * 40)
        domain = DomainIntel(client)
        
        result = domain.dns_records("google.com")
        print(f"Domain: google.com")
        print(f"  DNS record types found: {result.data['total_record_types']}")
        
        if 'A' in result.data['records'] and result.data['records']['A']:
            print(f"  IP Address: {result.data['records']['A'][0]}")
        
        # 3. Result Formatting
        print("\n3. RESULT FORMATTING")
        print("-" * 40)
        print(f"Summary: {result.summary()}")
        print(f"JSON: {result.to_json()[:100]}...")
    
    print("\n" + "=" * 60)
    print("Investigation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

## FOR MORE SCRIPTS GO ABOVE TO THE FILES.

