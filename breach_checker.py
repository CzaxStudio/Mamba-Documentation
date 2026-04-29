#!/usr/bin/env python3
"""
Breach Checker - Check if emails appear in data breaches
"""

from mamba import MambaClient, EmailReputation
from datetime import datetime

def check_breaches(email_list):
    """Check multiple emails for data breaches"""
    
    results = []
    
    with MambaClient() as client:
        email = EmailReputation(client)
        
        for email_address in email_list:
            print(f"\n🔍 Checking: {email_address}")
            print("-" * 40)
            
            result = email.check_breach(email_address)
            
            if result.success:
                if result.data['found_in_breaches']:
                    print(f"    ALERT: Found in {result.data['breach_count']} breaches!")
                    if result.data['details']:
                        print(f"  Details: {result.data['details'][:2]}")
                else:
                    print(f"   Clean - Not found in known breaches")
            else:
                print(f"   Error: {result.error}")
            
            results.append(result)
    
    return results

def generate_report(results, filename=None):
    """Generate breach check report"""
    
    if not filename:
        filename = f"breach_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, 'w') as f:
        f.write("=" * 60 + "\n")
        f.write("MAMBA BREACH CHECK REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        
        breached = [r for r in results if r.success and r.data.get('found_in_breaches')]
        
        if breached:
            f.write(f"  COMPROMISED EMAILS ({len(breached)})\n\n")
            for r in breached:
                f.write(f"  • {r.query}: {r.data['breach_count']} breach(es)\n")
        else:
            f.write("✓ No compromised emails found\n")
    
    print(f"\n Report saved to {filename}")

def main():
    emails_to_check = [
        "test@example.com",
        "user@gmail.com",
        "admin@company.com",
        "security@hotmail.com"
    ]
    
    print("=" * 60)
    print("Mamba - Email Breach Checker")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    results = check_breaches(emails_to_check)
    generate_report(results)
    
    print("\n Breach check complete!")

if __name__ == "__main__":
    main()
