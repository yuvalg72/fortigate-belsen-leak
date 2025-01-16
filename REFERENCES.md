# References and Additional Resources

## Official Advisories
- [Fortinet PSIRT Advisory](https://www.fortinet.com/blog/psirt-blogs/update-regarding-cve-2022-40684) - Official vulnerability disclosure
- [NIST NVD Entry](https://nvd.nist.gov/vuln/detail/CVE-2022-40684)

## Technical Analysis
- CVE-2022-40684 is an authentication bypass vulnerability in FortiOS, FortiProxy, and FortiSwitchManager
- Affected versions:
  - FortiOS: 7.2.0 through 7.2.1, 7.0.0 through 7.0.6
  - FortiProxy: 7.2.0, 7.0.0 through 7.0.6
  - FortiSwitchManager: 7.2.0, 7.0.0

## Timeline
- October 2022: Initial vulnerability discovery and exploitation
- January 2025: Public release of configurations from affected devices

## Mitigation Steps
1. Update to patched versions:
   - FortiOS 7.2.2 or above
   - FortiOS 7.0.7 or above
   - FortiProxy 7.2.1 or above
   - FortiProxy 7.0.7 or above
   - FortiSwitchManager 7.2.1 or above
   - FortiSwitchManager 7.0.1 or above

2. Additional Security Measures:
   - Review and update admin credentials
   - Audit firewall configurations
   - Monitor for unauthorized access
   - Enable logging and monitoring
